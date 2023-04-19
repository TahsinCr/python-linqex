from .test_data import *

tempCustomerDictEnumerable = customerDictEnumerable.Copy()



newCustomer = Customer(id=13,name="John",age=44,gender=MALE)
tempCustomerDictEnumerable.Add(tempCustomerDictEnumerable.Lenght, newCustomer) # Adds the new customer to iterable.
result1 = tempCustomerDictEnumerable.First(lambda key, customer: customer.id == 13)
if result1 is not None: result1 = result1.ToValue
assert result1 is newCustomer, "EditTest - result1 is not equal to desired value"



tempCustomerIterable = tempCustomerDictEnumerable.Copy().ToDict
newCustomer = Customer(id=4,name="Jack",age=29,gender=MALE)
# Replaces the given value with the selected value (Updates the value).
tempCustomerDictEnumerable.Update(tempCustomerDictEnumerable.First(lambda key, customer: customer.id == 4).ToKey, newCustomer)
result2 = tempCustomerDictEnumerable.First(lambda key, customer: customer.id == 4)
if result2 is not None: result2 = result2.ToValue
assert result2 is newCustomer, "EditTest - result2 is not equal to desired value"

tempCustomerIterable = tempCustomerDictEnumerable.Copy().ToDict
newCustomer = Customer(id=4,name="Jack",age=30,gender=MALE)
# It does the same as the 'Update()' method above.
tempCustomerDictEnumerable.First(lambda key, customer: customer.id == 4).Set(newCustomer)
result3 = tempCustomerDictEnumerable.First(lambda key, customer: customer.id == 4)
if result3 is not None: result3 = result3.ToValue
assert result3 is newCustomer, "EditTest - result3 is not equal to desired value"



tempCustomerIterable = tempCustomerDictEnumerable.Copy().ToDict
newCustomers = {tempCustomerDictEnumerable.Lenght: Customer(id=14,name="Frank",age=16,gender=MALE), tempCustomerDictEnumerable.Lenght+1: Customer(id=15,name="Gregor",age=10,gender=MALE)}
# Expands with new customers list.
tempCustomerDictEnumerable.Concat(newCustomers)
result4 = tempCustomerDictEnumerable.ToValue
assert result4 == {**tempCustomerIterable, **newCustomers}, "EditTest - result4 is not equal to desired value"



tempCustomerIterable = tempCustomerDictEnumerable.Copy().ToDict
# Deletes data with given key value from iterable.
tempCustomerDictEnumerable.Delete(tempCustomerDictEnumerable.First(lambda key, customer: customer.id == 13).ToKey)
result5 = tempCustomerDictEnumerable.First(lambda key, customer: customer.id == 13)
if result5 is not None: result5 = result5.ToValue
assert result5 is None, "EditTest - result5 is not equal to desired value"



tempCustomerIterable = tempCustomerDictEnumerable.Copy().ToDict
# Deletes the current value from the iterable.
tempCustomerDictEnumerable.First(lambda key, customer: customer.id == 12).Delete()
result6 = tempCustomerDictEnumerable.First(lambda key, customer: customer.id == 12)
if result6 is not None: result6 = result6.ToValue
assert result6 is None, "EditTest - result6 is not equal to desired value"

tempCustomerDictEnumerable2 = tempCustomerDictEnumerable.Copy()
# Deletes the current value from the iterable.
tempCustomerDictEnumerable2.Where(lambda key, customer: customer.gender == FEMALE).Delete()
result7 = tempCustomerDictEnumerable2.Where(lambda key, customer: customer.gender == FEMALE).ToValue
assert result7 == {}, "EditTest - result7 is not equal to desired value"



tempCustomerIterable = tempCustomerDictEnumerable.Copy().ToDict
# Deletes given data from iterable.
tempCustomerDictEnumerable.Remove(tempCustomerDictEnumerable.First(lambda key, customer: customer.id == 11).ToValue)
result8 = tempCustomerDictEnumerable.First(lambda key, customer: customer.id == 11)
if result8 is not None: result8 = result8.ToValue
assert result8 == None, "EditTest - result8 is not equal to desired value"



# Converts Enumerable to dict.
tempCustomerIterable = tempCustomerDictEnumerable.Copy().ToDict
result9 = Enumerable.List(tempCustomerDictEnumerable.ToList).ToValue
assert result9 == list(tempCustomerIterable.values()), "EditTest - result9 is not equal to desired value"



tempCustomerIterable = tempCustomerDictEnumerable.Copy().ToDict
# If the value is iterable change the values ​​in it as desired.
tempCustomerDictEnumerable.Select(lambda key, customer: customer.age).Set()
result10 = tempCustomerDictEnumerable.ToValue
assert result10 == dict(map(lambda key, customer: (key, customer.age), tempCustomerIterable.keys(), tempCustomerIterable.values())), "EditTest - result10 is not equal to desired value"



