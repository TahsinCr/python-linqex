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

new_customer = Customer(id=13,name="John",age=44,gender=MALE)
customer_enumerable.add(new_customer) # Adds the new customer to iterable.
result = customer_enumerable.first(lambda index, customer: customer.id == 13).toValue._toDict()
print(result, end="\n"*2)
#--Result :
# {'id': 13, 'name': 'John', 'age': 13, 'gender': 'MALE'}


new_customer = Customer(id=4,name="Jack",age=29,gender=MALE)
customer_enumerable.update(customer_enumerable.first(lambda index, customer: customer.id == 4).toKey, new_customer) # Replaces the given value with the selected value (Updates the value).
# customer_enumerable.first(lambda index, customer: customer.id == 4).set(new_customer) # It does the same as the 'update()' method above.
result2 = customer_enumerable.first(lambda index, customer: customer.id == 4).toValue._toDict()
print(result2, end="\n"*2)
#--Result :
# {'id': 4, 'name': 'Jack', 'age': 29, 'gender': 'MALE'}


customer_enumerable.delete(customer_enumerable.first(lambda index, customer: customer.id == 13).toKey) # Deletes data with given key value from iterable.
result3 = customer_enumerable.first(lambda index, customer: customer.id == 13).toValue
print(result3, end="\n"*2)
#--Result :
# None


customer_enumerable.remove(customer_enumerable.first(lambda index, customer: customer.id == 12).toValue) # Deletes given data from iterable.
result4 = customer_enumerable.first(lambda index, customer: customer.id == 12).toValue
print(result4, end="\n"*2)
#--Result :
# None


customer_enumerable.insets(lambda index, customer: customer.age) # If the value is iterable change the values ​​in it as desired.
result5 = customer_enumerable.toValue
print(result5, end="\n"*2)
#--Result :
# [32, 19, 22, 29, 55, 12, 32, 19, 22, 43, 55]