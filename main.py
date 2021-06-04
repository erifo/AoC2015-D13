from itertools import permutations


class Person:
    def __init__(self, name):
        self.name = name
        self.relations = {}
    
    def get_relation(self, name):
        return self.relations[name]

    def set_relation(self, name, happiness):
        self.relations[name] = happiness


def add_relation_to_person(people, name, happiness, relation_name):
    for person in people:
        if person.name == name:
            person.set_relation(relation_name, happiness)
            return
    # If person with name is not found, create one.
    p = Person(name)
    p.set_relation(relation_name, happiness)
    people.append(p)


def add_person(people, name, default_relation):
    myself = Person("Erifo")
    for person in people:
        myself.set_relation(person.name, default_relation)
        person.set_relation(myself.name, default_relation)
    people.append(myself)


def parse_input(filename):
    people = []
    with open(filename, "r") as f:
        for line in f.readlines():
            tokens = line.split()
            person_name = tokens[0]
            factor = -1 if tokens[2] == "lose" else 1
            happiness = int(tokens[3]) * factor
            relation_name = tokens[len(tokens)-1].strip('.')
            add_relation_to_person(people, person_name, happiness, relation_name)
    return people


def get_optimal_happiness(people_to_seat):
    ways_of_seating = list(permutations(people_to_seat))
    return max([calc_total_happiness(seating) for seating in ways_of_seating])


def calc_total_happiness(seating):
    happiness = 0
    for i in range(len(seating)):
        left_person = seating[len(seating)-1 if i-1<0 else i-1]
        current_person = seating[i]
        right_person = seating[(i+1) % len(seating)]
        happiness += current_person.get_relation(left_person.name)
        happiness += current_person.get_relation(right_person.name)
    return happiness


def print_people(people):
    for person in people:
        print(person.name)
        for relation_name, happiness in person.relations.items():
            print("\t", relation_name, happiness)


def main():
    #Part 1 (Answer: 618)
    people_to_seat = parse_input("input.txt")
    result = get_optimal_happiness(people_to_seat)
    print("Total change in happiness for the optimal seating is", result)
    
    # Part 2 (Answer: 601)
    add_person(people_to_seat, "Erifo", 0)
    result = get_optimal_happiness(people_to_seat)
    print("Total change in happiness for the optimal seating (including me) is", result)



if __name__ == "__main__":
    main()