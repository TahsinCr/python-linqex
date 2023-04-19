from typing import Literal
from linqex.linq import Enumerable

MALE = "MALE"
FEMALE = "FEMALE"

class Customer:
    def __init__(self, id:int, name:str, age:int, gender:Literal["MALE","FEMALE"]):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
    def _ToDict(self):
        return self.__dict__.copy()


customerDict = {
    0 : Customer(1, "Ava", 32, MALE),
    1 : Customer(2, "Alex", 19, MALE),
    2 : Customer(3, "Amelia", 22, FEMALE),
    3 : Customer(4, "Arnold", 43, MALE),
    4 : Customer(5, "Eric", 55, MALE),
    5 : Customer(6, "Lily", 12, FEMALE),
    6 : Customer(7, "Jessia", 32, MALE),
    7 : Customer(8, "William", 19, MALE),
    8 : Customer(9, "Emily", 22, FEMALE),
    9 : Customer(10, "Mateo", 43, MALE),
    10 : Customer(11, "Antony", 55, MALE),
    11 : Customer(12, "Mia", 12, FEMALE)
}

customerDictEnumerable = Enumerable.Dict(customerDict)
