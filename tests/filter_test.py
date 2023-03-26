from typing import List
from tests.test_data import *



# Loops the iterable and returns a list of values ​​satisfying the given condition.
result1 = customer_enumerable.Where(lambda key, customer: customer.gender == FEMALE).ToValue
assert result1 == list(filter(lambda customer: customer.gender == FEMALE, customer_list)), "FilterTest - result1 is not equal to desired value"

# Loops the iterable and returns a dict of values ​​satisfying the given condition.
result2 = customer_enumerable.Where(lambda key, customer: customer.gender == FEMALE, getkey=True).ToValue
assert result2 == dict(filter(lambda customer: customer[1].gender == FEMALE, enumerate(customer_list))), "FilterTest - result2 is not equal to desired value"



# Loops the refreshable and returns a list of values ​​that are the same as the given data types.
result3 = customer_enumerable.OfType(Customer).ToValue
assert result3 == customer_list, "FilterTest - result3 is not equal to desired value"

# Loops the refreshable and returns a dict of values ​​that are the same as the given data types.
result4 = customer_enumerable.OfType(Customer, getkey=True).ToValue
assert result4 == dict(enumerate(customer_list)), "FilterTest - result4 is not equal to desired value"



# Loops the iterable and returns the first value that satisfies the given condition.
result5 = customer_enumerable.First(lambda key, customer: customer.gender == FEMALE) 
if result5 is not None: result5 = result5.ToValue
assert result5 == list(filter(lambda customer: customer.gender == FEMALE, customer_list))[0], "FilterTest - result5 is not equal to desired value"



# Loops the iterable and returns the last value satisfying the given condition.
result6 = customer_enumerable.Last(lambda key, customer: customer.gender == FEMALE)
if result6 is not None: result6 = result6.ToValue
assert result6 == list(filter(lambda customer: customer.gender == FEMALE, customer_list))[-1], "FilterTest - result6 is not equal to desired value"



# Loops the iterable and returns a value that satisfies the given condition. Returns None if more than one value satisfies the given condition.
result7 = customer_enumerable.Single(lambda key, customer: customer.gender == FEMALE) 
if result7 is not None: result7 = result7.ToValue
assert result7 is None, "FilterTest - result7 is not equal to desired value"



# Loops the renewable and sorts the given value (If desc=True is given, it sorts in reverse).
result8 = customer_enumerable.OrderBy(lambda key, customer: customer.age) 
assert result8.ToValue == list(sorted(customer_list,key=lambda x: x.age)), "FilterTest - result8 is not equal to desired value"

# After sorting the data with 'OrderBy', it is used to reorder the data within itself without breaking the order.
result9 = result8.ThenBy(lambda key, customer: customer.name, desc=True) 
assert result9.ToValue == list(sorted(sorted(customer_list, key=lambda x: x.name, reverse=True),key=lambda x: x.age)), "FilterTest - result9 is not equal to desired value"



# Loops iterable and returns True if given conditions are met for at least 1 value.
result10 = customer_enumerable.Any(lambda index, customer: customer.age < 18)
assert result10 == any(map(lambda customer: customer.age < 18, customer_list)), "FilterTest - result10 is not equal to desired value"



# Loops iterable and returns True if given conditions are met for all values.
result11 = customer_enumerable.All(lambda index, customer: customer.age < 18)
assert result11 == all(map(lambda customer: customer.age < 18, customer_list)), "FilterTest - result11 is not equal to desired value"



# Returns the first 5 values.
result12 = customer_enumerable.Take(5).ToValue 
assert result12 == customer_list[:5], "FilterTest - result12 is not equal to desired value"



# Returns the last 5 values.
result13 = customer_enumerable.TakeLast(5).ToValue 
assert result13 == customer_list[len(customer_list)-5:], "FilterTest - result13 is not equal to desired value"



# Skips the first 5 values and returns the remaining values.
result14 = customer_enumerable.Skip(10).ToValue 
assert result14 == customer_list[10:], "FilterTest - result14 is not equal to desired value"



# Skips the last 5 values and returns the remaining values.
result15 = customer_enumerable.SkipLast(10).ToValue 
assert result15 == customer_list[:len(customer_list)-10], "FilterTest - result15 is not equal to desired value"



# Returns values that are different.
result16 = customer_enumerable.Distinct(lambda index, customer: customer).ToValue
assert [customer._ToDict() for customer in result16] == [customer._ToDict() for customer in customer_list], "FilterTest - result16 is not equal to desired value"



# Returns the iterable by removing the unwanted values from the iterable.
result17 = customer_enumerable.Except(12, 22, func=lambda index, customer: customer.age).ToValue 
new_customers = []
for customer in customer_list:
    if not customer.age in [12,22]:
        new_customers.append(customer)
assert [customer._ToDict() for customer in result17] == [customer._ToDict() for customer in new_customers], "FilterTest - result17 is not equal to desired value"



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
result18 = customer_enumerable.Join(pet_list,
    lambda index, customer: customer.id,
    lambda index, pet: pet.customer_id,
    lambda customer, pet: Pet(pet.id, pet.name, customer=customer)
).ToValue
new_pet_list:List[Pet] = []
for pet in pet_list:
    customer = list(filter(lambda customer: customer.id == pet.customer_id, customer_list))
    if customer != []:
        new_pet_list.append(Pet(pet.id, pet.name, customer=customer[0]))
assert list(map(lambda pet: pet._ToDict(),result18)) == list(map(lambda pet: pet._ToDict(),new_pet_list)), "FilterTest - result18 is not equal to desired value"



# Reverses and returns the iterable.
result19 = customer_enumerable.Reverse()
assert list(map(lambda pet: pet._ToDict(),result19)) == list(map(lambda pet: pet._ToDict(),list(reversed(customer_list)))), "FilterTest - result19 is not equal to desired value"



# Concatenates and returns two iterables of the same length as desired.
new_list = list(range(len(customer_list)))
result20 = customer_enumerable.Zip(new_list)
assert list(map(lambda pet: (pet[0]._ToDict(), pet[1]),result20)) == list(map(lambda pet: (pet[0]._ToDict(), pet[1]),list(zip(customer_list, new_list)))), "FilterTest - result20 is not equal to desired value"



# Returns iterable with self, result and data.
result20 = customer_enumerable.Loop(lambda self, result, key, value: None if result.IsValue(value.name) else result.Add(value.name))
assert result20.ToValue == list(map(lambda customer: customer.name, customer_list)), "FilterTest - result20 is not equal to desired value"



# Compares the iterable in the list with the given iterable.
new_customer_list = customer_enumerable.Copy()
result21 = customer_enumerable.SequenceEqual(new_customer_list)
assert result21 == True, "FilterTest - result21 is not equal to desired value"
