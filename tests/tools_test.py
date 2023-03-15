from typing import Literal
from linqex.linq import Enumerable

MALE = "MALE"
FEMALE = "FEMALE"

class Customer:
    def __init__(self, id, name, age, gender:Literal["MALE","FEMALE"]):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
    def _toDict(self):
        return self.__dict__.copy()


customer_list = [
    Customer(1, "Ava", 32, MALE),
    Customer(2, "Alex", 19, MALE),
    Customer(3, "Amelia", 22, FEMALE),
    Customer(4, "Arnold", 43, MALE),
    Customer(5, "Eric", 55, MALE),
    Customer(6, "Lily", 12, FEMALE),
    Customer(7, "Jessia", 32, MALE),
    Customer(8, "William", 19, MALE),
    Customer(9, "Emily", 22, FEMALE),
    Customer(10, "Mateo", 43, MALE),
    Customer(11, "Antony", 55, MALE),
    Customer(12, "Mia", 12, FEMALE)
]

customer_enumerable = Enumerable(customer_list)


result = customer_enumerable.toValue # Returns converts Enumerable to value.
# The 'toValue' function cannot be used if the result of a query on Enumerable is not a iterable value.
print([c._toDict() for c in result])
print(result, end="\n"*2)
#--Result :
# [
#    {'id': 1, 'name': 'Ava', 'age': 32, 'gender': 'MALE'}, {'id': 2, 'name': 'Alex', 'age': 19, 'gender': 'MALE'}, {'id': 3, 'name': 'Amelia', 'age': 22, 'gender': 'FEMALE'}, 
#    {'id': 4, 'name': 'Arnold', 'age': 43, 'gender': 'MALE'}, {'id': 5, 'name': 'Eric', 'age': 55, 'gender': 'MALE'}, {'id': 6, 'name': 'Lily', 'age': 12, 'gender': 'FEMALE'}, 
#    {'id': 7, 'name': 'Jessia', 'age': 32, 'gender': 'MALE'}, {'id': 8, 'name': 'William', 'age': 19, 'gender': 'MALE'}, {'id': 9, 'name': 'Emily', 'age': 22, 'gender': 'FEMALE'}, 
#    {'id': 10, 'name': 'Mateo', 'age': 43, 'gender': 'MALE'}, {'id': 11, 'name': 'Antony', 'age': 55, 'gender': 'MALE'}, {'id': 12, 'name': 'Mia', 'age': 12, 'gender': 'FEMALE'}
# ]
# [
#    <__main__.Customer object at 0x0000027A67B9BD90>, <__main__.Customer object at 0x0000027A66E76B50>, <__main__.Customer object at 0x0000027A67B9BDD0>, 
#    <__main__.Customer object at 0x0000027A67B9BE10>, <__main__.Customer object at 0x0000027A67B9BE90>, <__main__.Customer object at 0x0000027A67B9BED0>, 
#    <__main__.Customer object at 0x0000027A67B9BF10>, <__main__.Customer object at 0x0000027A67B9BF50>, <__main__.Customer object at 0x0000027A67B9BF90>, 
#    <__main__.Customer object at 0x0000027A67B9BFD0>, <__main__.Customer object at 0x0000027A67BC0050>, <__main__.Customer object at 0x0000027A67BC0090>
# ]

result2 = customer_enumerable.toKey # Returns converts Enumerable to key.
print(result2, end="\n"*2)
#--Result :
# None



result3 = customer_enumerable.toDict # Returns converts Enumerable to dict.
print(dict(zip(result3.keys(),[c._toDict() for c in result3.values()])))
print(result3, end="\n"*2)
#--Result :
# {
#    0: {'id': 1, 'name': 'Ava', 'age': 32, 'gender': 'MALE'}, 1: {'id': 2, 'name': 'Alex', 'age': 19, 'gender': 'MALE'}, 2: {'id': 3, 'name': 'Amelia', 'age': 22, 'gender': 'FEMALE'}, 
#    3: {'id': 4, 'name': 'Arnold', 'age': 43, 'gender': 'MALE'}, 4: {'id': 5, 'name': 'Eric', 'age': 55, 'gender': 'MALE'}, 5: {'id': 6, 'name': 'Lily', 'age': 12, 'gender': 'FEMALE'}, 
#    6: {'id': 7, 'name': 'Jessia', 'age': 32, 'gender': 'MALE'}, 7: {'id': 8, 'name': 'William', 'age': 19, 'gender': 'MALE'}, 8: {'id': 9, 'name': 'Emily', 'age': 22, 'gender': 'FEMALE'}, 
#    9: {'id': 10, 'name': 'Mateo', 'age': 43, 'gender': 'MALE'}, 10: {'id': 11, 'name': 'Antony', 'age': 55, 'gender': 'MALE'}, 11: {'id': 12, 'name': 'Mia', 'age': 12, 'gender': 'FEMALE'}
# }
# {
#    0: <__main__.Customer object at 0x0000027A67B9BD90>, 1: <__main__.Customer object at 0x0000027A66E76B50>, 2: <__main__.Customer object at 0x0000027A67B9BDD0>, 
#    3: <__main__.Customer object at 0x0000027A67B9BE10>, 4: <__main__.Customer object at 0x0000027A67B9BE90>, 5: <__main__.Customer object at 0x0000027A67B9BED0>, 
#    6: <__main__.Customer object at 0x0000027A67B9BF10>, 7: <__main__.Customer object at 0x0000027A67B9BF50>, 8: <__main__.Customer object at 0x0000027A67B9BF90>, 
#    9: <__main__.Customer object at 0x0000027A67B9BFD0>, 10: <__main__.Customer object at 0x0000027A67BC0050>, 11: <__main__.Customer object at 0x0000027A67BC0090>
# }

result4 = customer_enumerable.toList # Returns converts Enumerable to list. returns None if in main Enumerable.
print([c._toDict() for c in result4])
print(result4, end="\n"*2)
#--Result :
# [
#    {'id': 1, 'name': 'Ava', 'age': 32, 'gender': 'MALE'}, {'id': 2, 'name': 'Alex', 'age': 19, 'gender': 'MALE'}, {'id': 3, 'name': 'Amelia', 'age': 22, 'gender': 'FEMALE'}, 
#    {'id': 4, 'name': 'Arnold', 'age': 43, 'gender': 'MALE'}, {'id': 5, 'name': 'Eric', 'age': 55, 'gender': 'MALE'}, {'id': 6, 'name': 'Lily', 'age': 12, 'gender': 'FEMALE'}, 
#    {'id': 7, 'name': 'Jessia', 'age': 32, 'gender': 'MALE'}, {'id': 8, 'name': 'William', 'age': 19, 'gender': 'MALE'}, {'id': 9, 'name': 'Emily', 'age': 22, 'gender': 'FEMALE'}, 
#    {'id': 10, 'name': 'Mateo', 'age': 43, 'gender': 'MALE'}, {'id': 11, 'name': 'Antony', 'age': 55, 'gender': 'MALE'}, {'id': 12, 'name': 'Mia', 'age': 12, 'gender': 'FEMALE'}
# ]
# [
#    <__main__.Customer object at 0x0000027A67B9BD90>, <__main__.Customer object at 0x0000027A66E76B50>, <__main__.Customer object at 0x0000027A67B9BDD0>, 
#    <__main__.Customer object at 0x0000027A67B9BE10>, <__main__.Customer object at 0x0000027A67B9BE90>, <__main__.Customer object at 0x0000027A67B9BED0>, 
#    <__main__.Customer object at 0x0000027A67B9BF10>, <__main__.Customer object at 0x0000027A67B9BF50>, <__main__.Customer object at 0x0000027A67B9BF90>, 
#    <__main__.Customer object at 0x0000027A67B9BFD0>, <__main__.Customer object at 0x0000027A67BC0050>, <__main__.Customer object at 0x0000027A67BC0090>
# ]



result5 = Enumerable.list() # Returns a Enumerable class with an empty list inside.
print(result5.toValue, end="\n"*2)
#--Result :
# []

result6 = Enumerable.dict() # Returns a Enumerable class with an empty dict inside.
print(result6.toValue, end="\n"*2)
#--Result :
# {}



result7 = customer_enumerable.isEmpty # Returns True if iterable is empty, False otherwise.
print(result7, end="\n"*2)
#--Result :
# False





result8 = customer_enumerable.isType(dict) # Returns True if its data type is the same as the entered data type, otherwise False.
print(result8, end="\n"*2)
#--Result :
# False

result9 = customer_enumerable.isKey('test') # Returns True if the key of the list is the key entered, False otherwise.
print(result9, end="\n"*2)
#--Result :
# False

result10 = customer_enumerable.isValue('test') # Returns True if the value of the list is the value entered, False otherwise.
print(result10, end="\n"*2)
#--Result :
# False

result11 = customer_enumerable.inKey('test') # If the entered value contains iterable data and the iterable data contains the given key, it returns True, otherwise it returns False.
print(result11, end="\n"*2)
#--Result :
# False

result12 = customer_enumerable.inValue('test') # If the entered value contains iterable data and the iterable data contains the given value, it returns True, otherwise it returns False.
print(result12, end="\n"*2)
#--Result :
# False


result13 = customer_enumerable.type # Returns the data type it has.
print(result13, end="\n"*2)
#--Result :
# <class 'list'>



customer_enumerable.convert_toDict() # Converts Enumerable to dict.
print(dict(zip(customer_enumerable.get_keys(),[c._toDict() for c in customer_enumerable.get_values()])))
print(customer_enumerable.toValue, end="\n"*2)
#--Result :
# {
#    0: {'id': 1, 'name': 'Ava', 'age': 32, 'gender': 'MALE'}, 1: {'id': 2, 'name': 'Alex', 'age': 19, 'gender': 'MALE'}, 2: {'id': 3, 'name': 'Amelia', 'age': 22, 'gender': 'FEMALE'}, 
#    3: {'id': 4, 'name': 'Arnold', 'age': 43, 'gender': 'MALE'}, 4: {'id': 5, 'name': 'Eric', 'age': 55, 'gender': 'MALE'}, 5: {'id': 6, 'name': 'Lily', 'age': 12, 'gender': 'FEMALE'}, 
#    6: {'id': 7, 'name': 'Jessia', 'age': 32, 'gender': 'MALE'}, 7: {'id': 8, 'name': 'William', 'age': 19, 'gender': 'MALE'}, 8: {'id': 9, 'name': 'Emily', 'age': 22, 'gender': 'FEMALE'}, 
#    9: {'id': 10, 'name': 'Mateo', 'age': 43, 'gender': 'MALE'}, 10: {'id': 11, 'name': 'Antony', 'age': 55, 'gender': 'MALE'}, 11: {'id': 12, 'name': 'Mia', 'age': 12, 'gender': 'FEMALE'}
# }
# {
#    0: <__main__.Customer object at 0x0000027A67B9BD90>, 1: <__main__.Customer object at 0x0000027A66E76B50>, 2: <__main__.Customer object at 0x0000027A67B9BDD0>, 
#    3: <__main__.Customer object at 0x0000027A67B9BE10>, 4: <__main__.Customer object at 0x0000027A67B9BE90>, 5: <__main__.Customer object at 0x0000027A67B9BED0>, 
#    6: <__main__.Customer object at 0x0000027A67B9BF10>, 7: <__main__.Customer object at 0x0000027A67B9BF50>, 8: <__main__.Customer object at 0x0000027A67B9BF90>, 
#    9: <__main__.Customer object at 0x0000027A67B9BFD0>, 10: <__main__.Customer object at 0x0000027A67BC0050>, 11: <__main__.Customer object at 0x0000027A67BC0090>
# }

customer_enumerable.convert_toList() # Converts Enumerable to list.
print([c._toDict() for c in customer_enumerable.toValue])
print(customer_enumerable.toValue, end="\n"*2)
#--Result :
# [
#    {'id': 1, 'name': 'Ava', 'age': 32, 'gender': 'MALE'}, {'id': 2, 'name': 'Alex', 'age': 19, 'gender': 'MALE'}, {'id': 3, 'name': 'Amelia', 'age': 22, 'gender': 'FEMALE'}, 
#    {'id': 4, 'name': 'Arnold', 'age': 43, 'gender': 'MALE'}, {'id': 5, 'name': 'Eric', 'age': 55, 'gender': 'MALE'}, {'id': 6, 'name': 'Lily', 'age': 12, 'gender': 'FEMALE'}, 
#    {'id': 7, 'name': 'Jessia', 'age': 32, 'gender': 'MALE'}, {'id': 8, 'name': 'William', 'age': 19, 'gender': 'MALE'}, {'id': 9, 'name': 'Emily', 'age': 22, 'gender': 'FEMALE'}, 
#    {'id': 10, 'name': 'Mateo', 'age': 43, 'gender': 'MALE'}, {'id': 11, 'name': 'Antony', 'age': 55, 'gender': 'MALE'}, {'id': 12, 'name': 'Mia', 'age': 12, 'gender': 'FEMALE'}
# ]
# [
#    <__main__.Customer object at 0x0000027A67B9BD90>, <__main__.Customer object at 0x0000027A66E76B50>, <__main__.Customer object at 0x0000027A67B9BDD0>, 
#    <__main__.Customer object at 0x0000027A67B9BE10>, <__main__.Customer object at 0x0000027A67B9BE90>, <__main__.Customer object at 0x0000027A67B9BED0>, 
#    <__main__.Customer object at 0x0000027A67B9BF10>, <__main__.Customer object at 0x0000027A67B9BF50>, <__main__.Customer object at 0x0000027A67B9BF90>, 
#    <__main__.Customer object at 0x0000027A67B9BFD0>, <__main__.Customer object at 0x0000027A67BC0050>, <__main__.Customer object at 0x0000027A67BC0090>
# ]



result14 = customer_enumerable.copy() # Copy Enumerable.
print([c._toDict() for c in result14.toValue])
print(result14.toValue, end="\n"*2)
#--Result :
# [
#    {'id': 1, 'name': 'Ava', 'age': 32, 'gender': 'MALE'}, {'id': 2, 'name': 'Alex', 'age': 19, 'gender': 'MALE'}, {'id': 3, 'name': 'Amelia', 'age': 22, 'gender': 'FEMALE'}, 
#    {'id': 4, 'name': 'Arnold', 'age': 43, 'gender': 'MALE'}, {'id': 5, 'name': 'Eric', 'age': 55, 'gender': 'MALE'}, {'id': 6, 'name': 'Lily', 'age': 12, 'gender': 'FEMALE'}, 
#    {'id': 7, 'name': 'Jessia', 'age': 32, 'gender': 'MALE'}, {'id': 8, 'name': 'William', 'age': 19, 'gender': 'MALE'}, {'id': 9, 'name': 'Emily', 'age': 22, 'gender': 'FEMALE'}, 
#    {'id': 10, 'name': 'Mateo', 'age': 43, 'gender': 'MALE'}, {'id': 11, 'name': 'Antony', 'age': 55, 'gender': 'MALE'}, {'id': 12, 'name': 'Mia', 'age': 12, 'gender': 'FEMALE'}
# ]
# [
#    <__main__.Customer object at 0x0000027A67B9BD90>, <__main__.Customer object at 0x0000027A66E76B50>, <__main__.Customer object at 0x0000027A67B9BDD0>, 
#    <__main__.Customer object at 0x0000027A67B9BE10>, <__main__.Customer object at 0x0000027A67B9BE90>, <__main__.Customer object at 0x0000027A67B9BED0>, 
#    <__main__.Customer object at 0x0000027A67B9BF10>, <__main__.Customer object at 0x0000027A67B9BF50>, <__main__.Customer object at 0x0000027A67B9BF90>, 
#    <__main__.Customer object at 0x0000027A67B9BFD0>, <__main__.Customer object at 0x0000027A67BC0050>, <__main__.Customer object at 0x0000027A67BC0090>
# ]

result15 = customer_enumerable.lenght # Returns length of iterable
print(result15, end="\n"*2)