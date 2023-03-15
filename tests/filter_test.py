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

result = customer_enumerable.where(lambda key, customer: customer.gender == FEMALE).toValue # Loops the iterable and returns a list of values ​​satisfying the given condition.
print([c._toDict() for c in result])
print(result, end="\n"*2)
#--Result :
# [
#    {'id': 3, 'name': 'Amelia', 'age': 22, 'gender': 'FEMALE'}, 
#    {'id': 6, 'name': 'Lily', 'age': 12, 'gender': 'FEMALE'}, 
#    {'id': 9, 'name': 'Emily', 'age': 22, 'gender': 'FEMALE'}, 
#    {'id': 12, 'name': 'Mia', 'age': 12, 'gender': 'FEMALE'}
# ]
# [
#    <__main__.Customer object at 0x0000027A67B9BDD0>, 
#    <__main__.Customer object at 0x0000027A67B9BED0>, 
#    <__main__.Customer object at 0x0000027A67B9BF90>, 
#    <__main__.Customer object at 0x0000027A67BC0090>
# ]
result2 = customer_enumerable.where(lambda key, customer: customer.gender == FEMALE, getkey=True).toValue # Loops the iterable and returns a dict of values ​​satisfying the given condition.
print(dict(zip(result2.keys(),[c._toDict() for c in result2.values()])))
print(result2, end="\n"*2)
#--Result :
# {
#    2: {'id': 3, 'name': 'Amelia', 'age': 22, 'gender': 'FEMALE'}, 
#    5: {'id': 6, 'name': 'Lily', 'age': 12, 'gender': 'FEMALE'}, 
#    8: {'id': 9, 'name': 'Emily', 'age': 22, 'gender': 'FEMALE'}, 
#    11: {'id': 12, 'name': 'Mia', 'age': 12, 'gender': 'FEMALE'}
# }
# {
#    2: <__main__.Customer object at 0x0000027A67B9BDD0>, 
#    5: <__main__.Customer object at 0x0000027A67B9BED0>, 
#    8: <__main__.Customer object at 0x0000027A67B9BF90>, 
#    11: <__main__.Customer object at 0x0000027A67BC0090>
# }

result3 = customer_enumerable.oftype(Customer).toValue # Loops the refreshable and returns a list of values ​​that are the same as the given data types.
print([c._toDict() for c in result3])
print(result3, end="\n"*2)
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
result4 = customer_enumerable.oftype(Customer, getkey=True).toValue # Loops the refreshable and returns a dict of values ​​that are the same as the given data types.
print(dict(zip(result4.keys(),[c._toDict() for c in result4.values()])))
print(result4, end="\n"*2)
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


result5 = customer_enumerable.first(lambda key, customer: customer.gender == FEMALE) # Loops the iterable and returns the first value that satisfies the given condition.
if result5 is not None: result5 = result5.toValue
print(result5.name, end="\n"*2)
#--Result :
# Amelia

result6 = customer_enumerable.last(lambda key, customer: customer.gender == FEMALE) # Loops the iterable and returns the last value satisfying the given condition.
if result6 is not None: result6 = result6.toValue
print(result6.name, end="\n"*2)
#--Result :
# Mia


result7 = customer_enumerable.single(lambda key, customer: customer.gender == FEMALE) # Loops the iterable and returns a value that satisfies the given condition. Returns None if more than one value satisfies the given condition.
if result7 is not None: result7 = result7.toValue
print(result7, end="\n"*2)
#--Result :
# None

result8 = customer_enumerable.orderby(lambda key, customer: customer.name).toValue # Loops the renewable and sorts the given value (If desc=True is given, it sorts in reverse).
print([c._toDict() for c in result8])
print(result8, end="\n"*2)
#--Result :
# [
#     {'id': 2, 'name': 'Alex', 'age': 19, 'gender': 'MALE'}, {'id': 3, 'name': 'Amelia', 'age': 22, 'gender': 'FEMALE'}, {'id': 11, 'name': 'Antony', 'age': 55, 'gender': 'MALE'},
#     {'id': 4, 'name': 'Arnold', 'age': 43, 'gender': 'MALE'}, {'id': 1, 'name': 'Ava', 'age': 32, 'gender': 'MALE'}, {'id': 9, 'name': 'Emily', 'age': 22, 'gender': 'FEMALE'},
#     {'id': 5, 'name': 'Eric', 'age': 55, 'gender': 'MALE'}, {'id': 7, 'name': 'Jessia', 'age': 32, 'gender': 'MALE'}, {'id': 6, 'name': 'Lily', 'age': 12, 'gender': 'FEMALE'},
#     {'id': 10, 'name': 'Mateo', 'age': 43, 'gender': 'MALE'}, {'id': 12, 'name': 'Mia', 'age': 12, 'gender': 'FEMALE'}, {'id': 8, 'name': 'William', 'age': 19, 'gender': 'MALE'}
# ]
# [
#     <__main__.Customer object at 0x000001EBB7C99450>, <__main__.Customer object at 0x000001EBB7C99410>, <__main__.Customer object at 0x000001EBB7CB7550>, 
#     <__main__.Customer object at 0x000001EBB7CAFE90>, <__main__.Customer object at 0x000001EBB79D5490>, <__main__.Customer object at 0x000001EBB7CB7490>, 
#     <__main__.Customer object at 0x000001EBB7CB4210>, <__main__.Customer object at 0x000001EBB7CB4310>, <__main__.Customer object at 0x000001EBB7CB4250>, 
#     <__main__.Customer object at 0x000001EBB7CB74D0>, <__main__.Customer object at 0x000001EBB7CB7590>, <__main__.Customer object at 0x000001EBB7CB4290>
# ]


result9 = customer_enumerable.count(FEMALE, lambda index, customer: customer.gender) # Returns number of values given for iterable
print(result9, end="\n"*2)
#--Result :
# None


result10 = customer_enumerable.sum(lambda index, customer: customer.age) # Returns average of iterable numbers.
print(result10, end="\n"*2)
#--Result :
# None

result11 = customer_enumerable.avg(lambda index, customer: customer.age)  # Returns number of values given for iterable
print(result11, end="\n"*2)
#--Result :
# None

result12 = customer_enumerable.max(lambda index, customer: customer.age)  # Returns largest of numbers in iterable
print(result12, end="\n"*2)
#--Result :
# None

result13 = customer_enumerable.min(lambda index, customer: customer.age)  # Returns smallest of numbers in iterable
print(result13, end="\n"*2)
#--Result :
# None


result14 = customer_enumerable.any(lambda index, customer: customer.age < 18) # Loops iterable and returns True if given conditions are met for at least 1 value.
print(result14, end="\n"*2)
#--Result :
# None

result15 = customer_enumerable.all(lambda index, customer: customer.age < 18) # Loops iterable and returns True if given conditions are met for all values.
print(result15, end="\n"*2)
#--Result :
# None
