import pyttsx3
engine = pyttsx3.init()
from problems import Problem, ProblemGenerator
import random
import pyttsx3


class SightWordProblem(Problem):
    def __init__(self, word, sentence=None):
        self.word = word
        self.sentence = sentence

    def display_problem(self):
        if self.sentence is not None:
            return str("How do you spell the word " + self.word + " in the sentence " + self.sentence + "?")
        else:
            return str("How do you spell the word " + self.word + "?")

    def display_answer(self):
        return "It is spelled" + ' '.join(' '*1 + c for c in self.word)

    def check_answer(self, x):
        return x.lower() == self.word.lower()

    def __str__(self):
        print("Problem: spell " + word)


class SightWordProblemGenerator(ProblemGenerator):
    def __init__(self, problems):
        for problem in problems:
            if type(problem) != SightWordProblem:
                raise TypeError
        self.problems = problems

    def get_problem(self):
        return random.choice(self.problems)

# TODO: (Suggestions from Krish)
# Make it so he can write instead of me typing it for him
# (Maybe try speech to text input also)
# Add a timer

sight_words = [
    ["are"],
    ["easy"],
    ["listen"],
    ["second"],
    ["they"],
    ["answer"],
    ["enough"],
    ["make"],
    ["since"],
    ["thing"],
    ["above"],
    ["first"],
    ["made"],
    ["sometimes"],
    ["usually"],
    ["another"],
    ["found"],
    ["more"],
    ["said"],
    ["use"],
    ["about"],
    ["float"],
    ["many"],
    ["saw"],
    ["very"],
    ["after"],
    ["friends"],
    ["new"],
    ["sure"],
    ["with"],
    ["again"],
    ["favorite"],
    ["nice"],
    ["school"],
    ["went"],
    ["before"],
    ["girl"],
    ["one"],
    ["small"],
    ["won"],
    ["because"],
    ["have"],
    ["our"],
    ["thank"],
    ["won’t"],
    ["best"],
    ["how"],
    ["other"],
    ["those"],
    ["where"],
    ["being"],
    ["hear"],
    ["off"],
    ["that’s"],
    ["were"],
    ["body"],
    ["house"],
    ["often"],
    ["talking"],
    ["wanted"],
    ["beautiful"],
    ["however"],
    ["outside"],
    ["them"],
    ["who"],
    ["brothers"],
    ["heard"],
    ["people"],
    ["to"],
    ["wrong"],
    ["could"],
    ["its"],
    ["phone"],
    ["two"],
    ["when"],
    ["can’t"],
    ["into"],
    ["pretty"],
    ["too"],
    ["what"],
    ["city"],
    ["idea"],
    ["piece"],
    ["tell"],
    ["will"],
    ["clock"],
    ["joke"],
    ["quit"],
    ["there"],
    ["write"],
    ["crash"],
    ["jump"],
    ["question"],
    ["they’re"],
    ["watch"],
    ["caught"],
    ["junk"],
    ["ride"],
    ["their"],
    ["why"],
    ["children"],
    ["knew"],
    ["right"],
    ["thought"],
    ["was"],
    ["don’t"],
    ["kicked"],
    ["rain"],
    ["through"],
    ["whole"],
    ["didn’t"],
    ["low"],
    ["really"],
    ["than"],
    ["we"],
    ["drink"],
    ["line"],
    ["sister"],
    ["then"],
    ["young"],
    ["eating"],
    ["little"]
]

problems = []
for word in sight_words:
    if len(word) == 1:
        new_problem = SightWordProblem(word[0])
    else:
        new_problem = SightWordProblem(word[0], word[1])
    problems.append(new_problem)
generator = SightWordProblemGenerator(problems)
engine = pyttsx3.init()

while True:
    engine.setProperty('rate', 150)
    current_problem = generator.get_problem()
    engine.say(current_problem.display_problem())
    engine.runAndWait()
    x = input("I think it is spelled: ")
    if current_problem.check_answer(x):
        engine.say("Correct!")
    else:
        engine.say("That's not quite right.")
        print("The correct spelling is: " + current_problem.display_answer())
        engine.say(current_problem.display_answer())
        engine.setProperty('rate', 100)
    engine.runAndWait()