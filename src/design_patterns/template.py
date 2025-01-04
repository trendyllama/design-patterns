'''

the template patter is a behavioral design pattern that defines the program skeleton of an algorithm
in the superclass but lets subclasses override specific steps of the algorithm without changing its structure.

'''


from typing import Protocol

class AlgoirthmTemplate(Protocol):
    def step1(self): ...
    def step2(self): ...
    def step3(self): ...


class ConcreteAlgorithm1(AlgoirthmTemplate):
    def step1(self):
        print('ConcreteAlgorithm1 step1')

    def step2(self):
        print('ConcreteAlgorithm1 step2')

    def step3(self):
        print('ConcreteAlgorithm1 step3')


class ConcreteAlgorithm2(AlgoirthmTemplate):

    def step1(self):
        print('ConcreteAlgorithm2 step1')

    def step2(self):
        print('ConcreteAlgorithm2 step2')

    def step3(self):
        print('ConcreteAlgorithm2 step3')

