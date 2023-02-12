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

result = customer_enumerable.get(2) # Returns get value or Enumerable(value).
print(result.name, end="\n"*2)
#--Result :
# Amelia


result2 = customer_enumerable.get_index(result) # Returns get index.
print(result2, end="\n"*2)
#--Result :
# 2


result3 = customer_enumerable.get_keys() # Returns get keys list.
print(result3, end="\n"*2)
# Result :
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


result4 = customer_enumerable.get_values() # Returns get values list.
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


result5 = customer_enumerable.get_items() # Returns get items [(key,value), ...] list.
print([(k,c._toDict()) for k,c in result5])
print(result5, end="\n"*2)
#--Result :
# [
#    (0, {'id': 1, 'name': 'Ava', 'age': 32, 'gender': 'MALE'}), (1, {'id': 2, 'name': 'Alex', 'age': 19, 'gender': 'MALE'}), (2, {'id': 3, 'name': 'Amelia', 'age': 22, 'gender': 'FEMALE'}), 
#    (3, {'id': 4, 'name': 'Arnold', 'age': 43, 'gender': 'MALE'}), (4, {'id': 5, 'name': 'Eric', 'age': 55, 'gender': 'MALE'}), (5, {'id': 6, 'name': 'Lily', 'age': 12, 'gender': 'FEMALE'}), 
#    (6, {'id': 7, 'name': 'Jessia', 'age': 32, 'gender': 'MALE'}), (7, {'id': 8, 'name': 'William', 'age': 19, 'gender': 'MALE'}), (8, {'id': 9, 'name': 'Emily', 'age': 22, 'gender': 'FEMALE'}), 
#    (9, {'id': 10, 'name': 'Mateo', 'age': 43, 'gender': 'MALE'}), (10, {'id': 11, 'name': 'Antony', 'age': 55, 'gender': 'MALE'}), (11, {'id': 12, 'name': 'Mia', 'age': 12, 'gender': 'FEMALE'})
# ]
# [
#    (0, <__main__.Customer object at 0x0000027A67B9BD90>), (1, <__main__.Customer object at 0x0000027A66E76B50>), (2, <__main__.Customer object at 0x0000027A67B9BDD0>), 
#    (3, <__main__.Customer object at 0x0000027A67B9BE10>), (4, <__main__.Customer object at 0x0000027A67B9BE90>), (5, <__main__.Customer object at 0x0000027A67B9BED0>), 
#    (6, <__main__.Customer object at 0x0000027A67B9BF10>), (7, <__main__.Customer object at 0x0000027A67B9BF50>), (8, <__main__.Customer object at 0x0000027A67B9BF90>), 
#    (9, <__main__.Customer object at 0x0000027A67B9BFD0>), (10, <__main__.Customer object at 0x0000027A67BC0050>), (11, <__main__.Customer object at 0x0000027A67BC0090>)
# ]


result6 = customer_enumerable.ingets(lambda index, customer: customer.age).toValue # If the value is iterable change and return the values ​​in it as desired.
print(result6, end="\n"*2)
#--Result :
# [32, 19, 22, 43, 55, 12, 32, 19, 22, 43, 55, 12]