from typing import List
from .test_data import *
import itertools


# Loops the iterable and returns a list of values ​​satisfying the given condition.
result1 = customerItemEnumerable.Where(lambda key, customer: customer.gender == FEMALE).ToValue
assert result1 == list(filter(lambda customer: customer.gender == FEMALE, customerItem)), "FilterTest - result1 is not equal to desired value"



# Loops the refreshable and returns a list of values ​​that are the same as the given data types.
result2 = customerItemEnumerable.OfType(Customer).ToValue
assert result2 == customerItem, "FilterTest - result2 is not equal to desired value"



# Loops the iterable and returns the first value that satisfies the given condition.
result3 = customerItemEnumerable.First(lambda key, customer: customer.gender == FEMALE)
if result3 is not None: result3 = result3.ToValue
assert result3 == list(filter(lambda customer: customer.gender == FEMALE, customerItem))[0], "FilterTest - result3 is not equal to desired value"



# Loops the iterable and returns the last value satisfying the given condition.
result4 = customerItemEnumerable.Last(lambda key, customer: customer.gender == FEMALE)
if result4 is not None: result4 = result4.ToValue
assert result4 == list(filter(lambda customer: customer.gender == FEMALE, customerItem))[-1], "FilterTest - result4 is not equal to desired value"



# Loops the iterable and returns a value that satisfies the given condition. Returns None if more than one value satisfies the given condition.
result5 = customerItemEnumerable.Single(lambda key, customer: customer.gender == FEMALE) 
if result5 is not None: result5 = result5.ToValue
assert result5 is None, "FilterTest - result5 is not equal to desired value"



# Loops the renewable and sorts the given value (If desc=True is given, it sorts in reverse).
result6 = customerItemEnumerable.OrderBy(lambda key, customer: customer.age, desc=False)
assert result6.ToValue == list(sorted(customerItem,key=lambda x: x.age, reverse=False)), "FilterTest - result6 is not equal to desired value"

# After sorting the data with 'OrderBy', it is used to reorder the data within itself without breaking the order.
result7 = result6.ThenBy(lambda key, customer: customer.name, desc=True)
assert result7.ToValue == list(sorted(sorted(customerItem, key=lambda x: x.name, reverse=True),key=lambda x: x.age)), "FilterTest - result7 is not equal to desired value"



# Loops iterable and returns True if given conditions are met for at least 1 value.
result8 = customerItemEnumerable.Any(lambda key, customer: customer.age < 18)
assert result8 == any(map(lambda customer: customer.age < 18, customerItem)), "FilterTest - result8 is not equal to desired value"



# Loops iterable and returns True if given conditions are met for all values.
result9 = customerItemEnumerable.All(lambda key, customer: customer.age < 18)
assert result9 == all(map(lambda customer: customer.age < 18, customerItem)), "FilterTest - result9 is not equal to desired value"



# Returns the first 5 values.
result10 = customerItemEnumerable.Take(5).ToValue 
assert result10 == customerItem[:5], "FilterTest - result10 is not equal to desired value"



# Returns the last 5 values.
result11 = customerItemEnumerable.TakeLast(5).ToValue 
assert result11 == customerItem[len(customerItem)-5:], "FilterTest - result11 is not equal to desired value"



# Skips the first 5 values and returns the remaining values.
result12 = customerItemEnumerable.Skip(10).ToValue 
assert result12 == customerItem[10:], "FilterTest - result12 is not equal to desired value"



# Skips the last 5 values and returns the remaining values.
result13 = customerItemEnumerable.SkipLast(10).ToValue 
assert result13 == customerItem[:len(customerItem)-10], "FilterTest - result13 is not equal to desired value"



# Returns values that are different.
result14 = customerItemEnumerable.Distinct(lambda key, customer: customer).ToList
assert [customer._ToDict() for customer in result14] == [customer._ToDict() for customer in customerItem], "FilterTest - result14 is not equal to desired value"



# Returns the iterable by removing the unwanted values from the iterable.
result15 = customerItemEnumerable.Except(lambda key, customer: customer.age, 12, 22).ToList 
new_customers:List[Customer] = []
for customer in customerItem:
    if not customer.age in [12,22]:
        new_customers.append(customer)
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
result16 = customerItemEnumerable.Join(pet_list,
    lambda key, customer: customer.id,
    lambda key, pet: pet.customer_id,
    lambda customerKey, customer, petKey, pet: Pet(pet.id, pet.name, pet.customer_id, customer=customer._ToDict())
).ToList
new_pet_list:List[Pet] = []
for pet in pet_list:
    customer = list(filter(lambda customer: customer.id == pet.customer_id, customerItem))
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
result17 = customerItemEnumerable.Reverse().ToList
assert list(map(lambda pet: pet._ToDict(),result17)) == list(map(lambda pet: pet._ToDict(),list(reversed(customerItem)))), "FilterTest - result17 is not equal to desired value"



# Concatenates and returns two iterables of the same length as desired.
new_list = list(range(len(customerItem)))
result18 = customerItemEnumerable.Zip(new_list, lambda inKey, inValue, outKey, outValue: (inValue, outValue)).ToList
assert list(map(lambda pet: (pet[0]._ToDict(), pet[1]),result18)) == list(map(lambda pet: (pet[0]._ToDict(), pet[1]),list(zip(customerItem, new_list)))), "FilterTest - result18 is not equal to desired value"



# Returns iterable with self, result and data.
result19 = customerItemEnumerable.Loop(lambda k, c: print(c.name))



# Compares the iterable in the list with the given iterable.
newCustomerItem = customerItemEnumerable.Copy()
result20 = customerItemEnumerable.SequenceEqual(newCustomerItem)
assert result20 == True, "FilterTest - result20 is not equal to desired value"



# Groups and returns data based on the given value.
result21 = customerItemEnumerable.GroupBy(lambda key, customer: customer.gender).ToList
assert result21 == [(keys, list(zip(*list(group)))[1]) for keys, group in itertools.groupby(newCustomerItem.OrderBy(lambda key, customer: customer.gender, False).GetItems().ToList, lambda customer: customer[1].gender)], "FilterTest - result21 is not equal to desired value"