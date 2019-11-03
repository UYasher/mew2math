import abc
import random


class Problem(abc.ABC):
    """Abstract class defining a problem"""
    @abc.abstractmethod
    def display_problem(self):
        return

    @abc.abstractmethod
    def check_answer(self, x):
        return


class ProblemGenerator(abc.ABC):
    """Abstract class defining a problem generator"""
    @abc.abstractmethod
    def get_problem(self):
        return


class AdditionProblem(Problem):
    """A class to represent addition problems"""
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2
        self.answer = x1 + x2

    def display_problem(self):
        return str(self.x1) + " + " + str(self.x2) + " = ?"

    def check_answer(self, x):
        return x == self.answer


class AdditionProblemGenerator(ProblemGenerator):
    """A class to generate addition problems"""
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def get_problem(self):
        x1 = random.randint(self.min, self.max)
        x2 = random.randint(self.min, self.max)
        return AdditionProblem(x1, x2)


class SubtractionProblem(Problem):
    """A class to represent addition problems"""
    def __init__(self, x1, x2):
        self.x1 = max(x1, x2)
        self.x2 = min(x1, x2)
        self.answer = x1 - x2

    def display_problem(self):
        return str(self.x1) + " - " + str(self.x2) + " = ?"

    def check_answer(self, x):
        return x == self.answer


class SubtractionProblemGenerator(ProblemGenerator):
    """A class to generate addition problems"""

    def __init__(self, min, max):
        self.min = min
        self.max = max

    def get_problem(self):
        x1 = random.randint(self.min, self.max)
        x2 = random.randint(self.min, self.max)
        return SubtractionProblem(x1, x2)


class MultipleChoiceProblem(Problem):
    def __init__(self, description, answer, options):
        self.description = description
        self.answer = answer
        self.options = options

    def display_problem(self):
        print(self.description)

    def check_answer(self, x):
        return x == self.answer


class MultipleChoiceProblemGenerator(ProblemGenerator):
    def __init__(self, problems):
        for problem in problems:
            if type(problem) != MultipleChoiceProblem:
                raise TypeError
        self.problems = problems

    def get_problem(self):
        return random.choice(self.problems)

    def get_next_problem(self):
        """ Return problems in order of list used to create Problem Generator, removing them from the generator """
        return self.problems.pop(1)