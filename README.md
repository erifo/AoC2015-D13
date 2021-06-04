# Advent of Code 2015 - Day 13: Knights of the Dinner Table
As is common with Advent of Code, the problem usually has three core elements.
### Input parsing
#### Description
A large set of plaintext data needs to be filtered into a form that is relevant and easier to work with.
#### Solution
If the pattern of the plaintext proves to be irregular I usually resort to Regex, but in this case a simple string-split (by whitespace) worked due to each line having the same amount of words. I decided to make a Person class to represent each name and their relation to others, but in a small case like this a nestled dictionary would've worked just as well.
### Calculation
#### Description
The problem wants an answer to a question, and if the Input Parsing has been done properly, this step should let you focus on the main problem without distractions. Still, resist the urge to take shortcuts. Have functions do one thing well.
#### Solution
The problem description made an explicit example of trying every possible seating, and the amount of people around the table were few enough, so I was not worried about the time-complexity being unreasonably high. I generated all possible seating combinations using the built-in itertools library, then had an algorithm sum up all the happiness between neighbours. Since the seating itself did not matter for the answer, I compiled all these sums into a list and took the largest value. In reality however, the actual seating would've likely been of interest as well.
### Scaling
#### Description
The first answer has been reached, and a twist is introduced. The requirements of the answer has changed, and the program needs to change with it. This is the brilliance of Advent of Code, as it forces you to reflect on your design decisions and grow your developer mindset.
#### Solution
Thankfully the change was relatively small. I needed to introduce myself as a Person with relations to everyone else, and give everyone else a relation to me. In case more people had to be added later (in whatever hypothetical scenario) I created a function to add a new Person with both name and default relation value.
## Personal Reflection
A reoccurring problem I wrestle with is finding variable names that elegantly summarizes what they represent. "Relation" and "happiness" both have similar yet separate meanings depending on context, and I would perhaps opt to use completely different and more distinct terms if I were to rewrite my solution.