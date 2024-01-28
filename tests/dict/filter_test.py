from typing import Dict
from .test_data import *
import itertools


# Loops the iterable and returns a list of values ​​satisfying the given condition.
result1 = customerDictEnumerable.Where(lambda key, customer: customer.gender == FEMALE).ToValue
assert result1 == dict(filter(lambda customer: customer[1].gender == FEMALE, customerDict.items())), "FilterTest - result1 is not equal to desired value"



# Loops the refreshable and returns a list of values ​​that are the same as the given data types.
result2 = customerDictEnumerable.OfType(Customer).ToValue
assert result2 == customerDict, "FilterTest - result2 is not equal to desired value"



# Loops the iterable and returns the first value that satisfies the given condition.
result3 = customerDictEnumerable.First(lambda key, customer: customer.gender == FEMALE)
if result3 is not None: result3 = result3.ToValue
assert result3 == list(filter(lambda customer: customer.gender == FEMALE, customerDict.values()))[0], "FilterTest - result3 is not equal to desired value"



# Loops the iterable and returns the last value satisfying the given condition.
result4 = customerDictEnumerable.Last(lambda key, customer: customer.gender == FEMALE)
if result4 is not None: result4 = result4.ToValue
assert result4 == list(filter(lambda customer: customer.gender == FEMALE, customerDict.values()))[-1], "FilterTest - result4 is not equal to desired value"



# Loops the iterable and returns a value that satisfies the given condition. Returns None if more than one value satisfies the given condition.
result5 = customerDictEnumerable.Single(lambda key, customer: customer.gender == FEMALE) 
if result5 is not None: result5 = result5.ToValue
assert result5 is None, "FilterTest - result5 is not equal to desired value"



# Loops the renewable and sorts the given value (If desc=True is given, it sorts in reverse).
result6 = customerDictEnumerable.OrderBy(lambda key, customer: customer.age, desc=False) 
assert result6.ToValue == dict(sorted(customerDict.items(), key=lambda x: x[1].age, reverse=False)), "FilterTest - result6 is not equal to desired value"

# After sorting the data with 'OrderBy', it is used to reorder the data within itself without breaking the order.
result7 = result6.ThenBy(lambda key, customer: customer.name, desc=True)
assert result7.ToValue == dict(sorted(sorted(customerDict.items(), key=lambda x: x[1].name, reverse=True),key=lambda x: x[1].age)), "FilterTest - result7 is not equal to desired value"



# Loops iterable and returns True if given conditions are met for at least 1 value.
result8 = customerDictEnumerable.Any(lambda key, customer: customer.age < 18)
assert result8 == any(map(lambda customer: customer.age < 18, customerDict.values())), "FilterTest - result8 is not equal to desired value"



# Loops iterable and returns True if given conditions are met for all values.
result9 = customerDictEnumerable.All(lambda key, customer: customer.age < 18)
assert result9 == all(map(lambda customer: customer.age < 18, customerDict.values())), "FilterTest - result9 is not equal to desired value"



# Returns the first 5 values.
result10 = customerDictEnumerable.Take(5).ToValue 
assert result10 == dict(list(customerDict.items())[:5]), "FilterTest - result10 is not equal to desired value"



# Returns the last 5 values.
result11 = customerDictEnumerable.TakeLast(5).ToValue 
assert result11 == dict(list(customerDict.items())[len(customerDict)-5:]), "FilterTest - result11 is not equal to desired value"



# Skips the first 5 values and returns the remaining values.
result12 = customerDictEnumerable.Skip(10).ToValue 
assert result12 == dict(list(customerDict.items())[10:]), "FilterTest - result12 is not equal to desired value"



# Skips the last 5 values and returns the remaining values.
result13 = customerDictEnumerable.SkipLast(10).ToValue 
assert result13 == dict(list(customerDict.items())[:len(customerDict)-10]), "FilterTest - result13 is not equal to desired value"



# Returns values that are different.
result14 = customerDictEnumerable.Distinct(lambda key, customer: customer).ToValue
assert [customer._ToDict() for customer in result14.values()] == [customer._ToDict() for customer in customerDict.values()], "FilterTest - result14 is not equal to desired value"



# Returns the iterable by removing the unwanted values from the iterable.
result15 = customerDictEnumerable.Except(customerDict[8], customerDict[9]).ToValue 
new_customers = customerDict.copy()
new_customers.pop(9)
new_customers.pop(8)
assert [customer._ToDict() for customer in result15.values()] == [customer._ToDict() for customer in new_customers.values()], "FilterTest - result15 is not equal to desired value"



class Pet:
    def __init__(self, id:int, name:str, customer_id:int=None, customer:Customer=None):
        self.id = id
        self.name = name
        self.customer_id = customer_id
        self.customer = customer
    def _ToDict(self):
        return self.__dict__.copy()
pet_dict = {0: Pet(1, "Max", 5), 1: Pet(2, "Charlie", 3), 2: Pet(3, "Milo", 5)}
# Concatenates the iterable from its matching values with the given iterable and returns.
result16 = customerDictEnumerable.Join(pet_dict,
    lambda key, customer: customer.id,
    lambda key, pet: pet.customer_id,
    lambda customerKey, customer, petKey, pet: Pet(pet.id, pet.name, pet.customer_id, customer=customer._ToDict()),
    lambda customerKey, customer, petKey, pet: petKey
).ToValue
new_pet_dict:Dict[int,Pet] = {}
for key, pet in pet_dict.items():
    customer = list(filter(lambda customer: customer.id == pet.customer_id, customerDict.values()))
    if customer != []:
        new_pet_dict[key] = Pet(pet.id, pet.name, pet.customer_id, customer=customer[0]._ToDict())
def SequenceEqual(dict1:dict, dict2:dict):
    if len(dict1) != len(dict2):
        return False
    for key, value in dict1.items():
        if not (value in list(dict2.values()) and key in list(dict2.keys())):
            return False
    return True
assert SequenceEqual(dict(map(lambda key, pet: (key, pet._ToDict()),result16.keys(),result16.values())), dict(map(lambda key, pet: (key, pet._ToDict()),new_pet_dict.keys(),new_pet_dict.values()))), "FilterTest - result16 is not equal to desired value"



# Reverses and returns the iterable.
result17 = customerDictEnumerable.Reverse().ToValue
assert dict(map(lambda key, pet: (key, pet._ToDict()), result17.keys(), result17.values())) == dict(map(lambda pet: (pet[0], pet[1]._ToDict()),list(reversed(customerDict.items())))), "FilterTest - result17 is not equal to desired value"



# Concatenates and returns two iterables of the same length as desired.
new_dict = {x:x for x in range(len(customerDict))}
result18 = customerDictEnumerable.Zip(new_dict, lambda inKey, inValue, outKey, outValue: (inValue, outValue))
assert dict(map(lambda pet: (pet[0], (pet[1][0]._ToDict(), pet[1][1])),result18.GetItems().ToValue)) == dict(map(lambda pet: (pet[0], (pet[1][0]._ToDict(), pet[1][1])),list(zip(customerDict.keys(), list(zip(customerDict.values(), new_dict)))))), "FilterTest - result18 is not equal to desired value"



# Returns iterable with self, result and data.
result19 = customerDictEnumerable.Loop(lambda key, customer: print(customer.name))



# Compares the iterable in the list with the given iterable.
newCustomerDict = customerDictEnumerable.Copy()
result20 = customerDictEnumerable.SequenceEqual(newCustomerDict)
assert result20 == True, "FilterTest - result20 is not equal to desired value"



# Groups and returns data based on the given value.
result21 = customerDictEnumerable.GroupBy(lambda key, customer: customer.gender).ToValue
assert result21 == {keys: dict(group) for keys, group in itertools.groupby(newCustomerDict.OrderBy(lambda key, customer: customer.gender, False).GetItems().ToValue, lambda customer: customer[1].gender)}, "FilterTest - result21 is not equal to desired value"



# Loops the refreshable and returns a list of keys ​​that are the same as the given data types.
result22 = customerDictEnumerable.OfTypeByKey(int).ToValue
assert result22 == customerDict, "FilterTest - result22 is not equal to desired value"



# Returns the iterable by removing the unwanted key from the iterable.
result23 = customerDictEnumerable.ExceptKey(8,9).ToValue 
new_customers = customerDict.copy()
new_customers.pop(9)
new_customers.pop(8)
assert [customer._ToDict() for customer in result23.values()] == [customer._ToDict() for customer in new_customers.values()], "FilterTest - result23 is not equal to desired value"