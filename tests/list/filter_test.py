from typing import List
from .test_data import *
import itertools


# Loops the iterable and returns a list of values ​​satisfying the given condition.
result1 = customerListEnumerable.Where(lambda customer: customer.gender == FEMALE).ToValue
assert result1 == list(filter(lambda customer: customer.gender == FEMALE, customerList)), "FilterTest - result1 is not equal to desired value"



# Loops the refreshable and returns a list of values ​​that are the same as the given data types.
result2 = customerListEnumerable.OfType(Customer).ToValue
assert result2 == customerList, "FilterTest - result2 is not equal to desired value"



# Loops the iterable and returns the first value that satisfies the given condition.
result3 = customerListEnumerable.First(lambda customer: customer.gender == FEMALE)
if result3 is not None: result3 = result3.ToValue
assert result3 == list(filter(lambda customer: customer.gender == FEMALE, customerList))[0], "FilterTest - result3 is not equal to desired value"



# Loops the iterable and returns the last value satisfying the given condition.
result4 = customerListEnumerable.Last(lambda customer: customer.gender == FEMALE)
if result4 is not None: result4 = result4.ToValue
assert result4 == list(filter(lambda customer: customer.gender == FEMALE, customerList))[-1], "FilterTest - result4 is not equal to desired value"



# Loops the iterable and returns a value that satisfies the given condition. Returns None if more than one value satisfies the given condition.
result5 = customerListEnumerable.Single(lambda customer: customer.gender == FEMALE) 
if result5 is not None: result5 = result5.ToValue
assert result5 is None, "FilterTest - result5 is not equal to desired value"



# Loops the renewable and sorts the given value (If desc=True is given, it sorts in reverse).
result6 = customerListEnumerable.OrderBy(lambda customer: customer.age, desc=False) 
assert result6.ToValue == list(sorted(customerList,key=lambda x: x.age, reverse=False)), "FilterTest - result6 is not equal to desired value"

# After sorting the data with 'OrderBy', it is used to reorder the data within itself without breaking the order.
result7 = result6.ThenBy(lambda customer: customer.name, desc=True)
assert result7.ToValue == list(sorted(sorted(customerList, key=lambda x: x.name, reverse=True),key=lambda x: x.age)), "FilterTest - result7 is not equal to desired value"



# Loops iterable and returns True if given conditions are met for at least 1 value.
result8 = customerListEnumerable.Any(lambda customer: customer.age < 18)
assert result8 == any(map(lambda customer: customer.age < 18, customerList)), "FilterTest - result8 is not equal to desired value"



# Loops iterable and returns True if given conditions are met for all values.
result9 = customerListEnumerable.All(lambda customer: customer.age < 18)
assert result9 == all(map(lambda customer: customer.age < 18, customerList)), "FilterTest - result9 is not equal to desired value"



# Returns the first 5 values.
result10 = customerListEnumerable.Take(5).ToValue 
assert result10 == customerList[:5], "FilterTest - result10 is not equal to desired value"



# Returns the last 5 values.
result11 = customerListEnumerable.TakeLast(5).ToValue 
assert result11 == customerList[len(customerList)-5:], "FilterTest - result11 is not equal to desired value"



# Skips the first 5 values and returns the remaining values.
result12 = customerListEnumerable.Skip(10).ToValue 
assert result12 == customerList[10:], "FilterTest - result12 is not equal to desired value"



# Skips the last 5 values and returns the remaining values.
result13 = customerListEnumerable.SkipLast(10).ToValue 
assert result13 == customerList[:len(customerList)-10], "FilterTest - result13 is not equal to desired value"



# Returns values that are different.
result14 = customerListEnumerable.Distinct(lambda customer: customer).ToValue
assert [customer._ToDict() for customer in result14] == [customer._ToDict() for customer in customerList], "FilterTest - result14 is not equal to desired value"



# Returns the iterable by removing the unwanted values from the iterable.
result15 = customerListEnumerable.Except(customerList[8], customerList[9]).ToValue
new_customers = customerList.copy()
new_customers.pop(9)
new_customers.pop(8)
assert [customer._ToDict() for customer in result15] == [customer._ToDict() for customer in new_customers], "FilterTest - result15 is not equal to desired value"



class Pet:
    def __init__(self, id:int, name:str, customer_id:int=None, customer:Customer=None):
        self.id = id
        self.name = name
        self.customer_id = customer_id
        self.customer = customer
    def _ToDict(self):
        return self.__dict__.copy()
pet_list = [Pet(1, "Max", 5), Pet(2, "Charlie", 3), Pet(3, "Milo", 5)]
# Concatenates the iterable from its matching values with the given iterable and returns.
result16 = customerListEnumerable.Join(pet_list,
    lambda customer: customer.id,
    lambda pet: pet.customer_id,
    lambda customer, pet: Pet(pet.id, pet.name, pet.customer_id, customer=customer._ToDict())
).ToValue
new_pet_list:List[Pet] = []
for pet in pet_list:
    customer = list(filter(lambda customer: customer.id == pet.customer_id, customerList))
    if customer != []:
        new_pet_list.append(Pet(pet.id, pet.name, pet.customer_id, customer=customer[0]._ToDict()))
def SequenceEqual(list1:list, list2:list):
    if len(list1) != len(list2):
        return False
    for value in list1:
        if not value in list2:
            return False
    return True
assert SequenceEqual(list(map(lambda pet: pet._ToDict(),result16)),list(map(lambda pet: pet._ToDict(),new_pet_list))), "FilterTest - result16 is not equal to desired value"



# Reverses and returns the iterable.
result17 = customerListEnumerable.Reverse()
assert list(map(lambda pet: pet._ToDict(),result17)) == list(map(lambda pet: pet._ToDict(),list(reversed(customerList)))), "FilterTest - result17 is not equal to desired value"



# Concatenates and returns two iterables of the same length as desired.
new_list = list(range(len(customerList)))
result18 = customerListEnumerable.Zip(new_list, lambda inValue, outValue: (inValue, outValue))
assert list(map(lambda pet: (pet[0]._ToDict(), pet[1]),result18)) == list(map(lambda pet: (pet[0]._ToDict(), pet[1]),list(zip(customerList, new_list)))), "FilterTest - result18 is not equal to desired value"



# Returns iterable with self, result and data.
result19 = customerListEnumerable.Loop(lambda c: print(c.name))



# Compares the iterable in the list with the given iterable.
newCustomerList = customerListEnumerable.Copy()
result20 = customerListEnumerable.SequenceEqual(newCustomerList)
assert result20 == True, "FilterTest - result20 is not equal to desired value"



# Groups and returns data based on the given value.
result21 = customerListEnumerable.GroupBy(lambda customer: customer.gender).ToValue
assert result21 == [(keys, list(group)) for keys, group in itertools.groupby(newCustomerList.OrderBy(lambda customer: customer.gender, False), lambda customer: customer.gender)], "FilterTest - result21 is not equal to desired value"