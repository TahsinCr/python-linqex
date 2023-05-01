from .test_data import *

tempCustomerItemEnumerable = customerItemEnumerable.Copy()



newCustomer = Customer(id=13,name="John",age=44,gender=MALE)
# Adds the new customer to iterable.
tempCustomerItemEnumerable.Add(None, newCustomer) 
result1 = tempCustomerItemEnumerable.First(lambda key, customer: customer.id == 13)
if result1 is not None: result1 = result1.ToValue
assert result1 is newCustomer, "EditTest - result1 is not equal to desired value"



tempCustomerIterable = tempCustomerItemEnumerable.Copy().ToList
newCustomer = Customer(id=4,name="Jack",age=29,gender=MALE)
# Replaces the given value with the selected value (Updates the value).
tempCustomerItemEnumerable.Update(tempCustomerItemEnumerable.First(lambda key, customer: customer.id == 4).ToKey, newCustomer)
result2 = tempCustomerItemEnumerable.First(lambda key, customer: customer.id == 4)
if result2 is not None: result2 = result2.ToValue
assert result2 is newCustomer, "EditTest - result2 is not equal to desired value"

tempCustomerIterable = tempCustomerItemEnumerable.Copy().ToList
newCustomer = Customer(id=4,name="Jack",age=30,gender=MALE)
# It does the same as the 'Update()' method above.
tempCustomerItemEnumerable.First(lambda key, customer: customer.id == 4).Set(newCustomer)
result3 = tempCustomerItemEnumerable.First(lambda key, customer: customer.id == 4)
if result3 is not None: result3 = result3.ToValue
assert result3 is newCustomer, "EditTest - result3 is not equal to desired value"



tempCustomerIterable = tempCustomerItemEnumerable.Copy().ToList
newCustomers = [Customer(id=14,name="Frank",age=16,gender=MALE),Customer(id=15,name="Gregor",age=10,gender=MALE)]
# Expands with new customers list.
tempCustomerItemEnumerable.Concat(newCustomers)
result4 = tempCustomerItemEnumerable.ToValue
assert result4 == tempCustomerIterable + newCustomers, "EditTest - result4 is not equal to desired value"



tempCustomerIterable = tempCustomerItemEnumerable.Copy().ToList
# Deletes data with given key value from iterable.
tempCustomerItemEnumerable.Delete(tempCustomerItemEnumerable.First(lambda key, customer: customer.id == 13).ToKey)
result5 = tempCustomerItemEnumerable.First(lambda key, customer: customer.id == 13)
if result5 is not None: result5 = result5.ToValue
assert result5 is None, "EditTest - result5 is not equal to desired value"



tempCustomerIterable = tempCustomerItemEnumerable.Copy().ToList
# Deletes the current value from the iterable.
tempCustomerItemEnumerable.First(lambda key, customer: customer.id == 12).Delete()
result6 = tempCustomerItemEnumerable.First(lambda key, customer: customer.id == 12)
if result6 is not None: result6 = result6.ToValue
assert result6 is None, "EditTest - result6 is not equal to desired value"

tempCustomerItemEnumerable2 = tempCustomerItemEnumerable.Copy()
# Deletes the current value from the iterable.
tempCustomerItemEnumerable2.Where(lambda key, customer: customer.gender == FEMALE).Delete()
result7 = tempCustomerItemEnumerable2.Where(lambda key, customer: customer.gender == FEMALE).ToValue
assert result7 == [], "EditTest - result7 is not equal to desired value"



tempCustomerIterable = tempCustomerItemEnumerable.Copy().ToList
# Deletes given data from iterable.
tempCustomerItemEnumerable.Remove(tempCustomerItemEnumerable.First(lambda key, customer: customer.id == 11).ToValue)
result8 = tempCustomerItemEnumerable.First(lambda key, customer: customer.id == 11)
if result8 is not None: result8 = result8.ToValue
assert result8 == None, "EditTest - result8 is not equal to desired value"



# Converts Enumerable to dict.
tempCustomerIterable = tempCustomerItemEnumerable.Copy().ToList
result9 = Enumerable.Dict(tempCustomerItemEnumerable.ToDict).ToValue
assert result9 == dict(enumerate(tempCustomerIterable)), "EditTest - result9 is not equal to desired value"



tempCustomerIterable = tempCustomerItemEnumerable.Copy().ToList
# If the value is iterable change the values ​​in it as desired.
tempCustomerItemEnumerable.Select(lambda key, customer: customer.age).Set()
result10 = tempCustomerItemEnumerable.ToValue
assert result10 == list(map(lambda customer: customer.age, tempCustomerIterable)), "EditTest - result10 is not equal to desired value"



newCustomer = Customer(id=20,name="Max",age=32,gender=MALE)
# Adds the new customer to the top of the list
tempCustomerItemEnumerable.Prepend(None, newCustomer)
result11 = tempCustomerItemEnumerable.First(lambda key, customer: customer.id == 20)
if result11 is not None: result11 = result11.ToValue
assert result11 is newCustomer, "EditTest - result11 is not equal to desired value"



newCustomer = Customer(id=21,name="Isla",age=45,gender=FEMALE)
# Adds the new customer to the desired section of the list
tempCustomerItemEnumerable.Insert(5,newCustomer)
result12 = tempCustomerItemEnumerable.First(lambda key, customer: customer.id == 21)
if result12 is not None: result12 = result12.ToValue
assert result12 is newCustomer, "EditTest - result12 is not equal to desired value"



tempCustomerItemEnumerable2 = tempCustomerItemEnumerable.Copy()
customer21 = tempCustomerItemEnumerable2.First(lambda key, customer: customer.id == 21)
if customer21 is not None: customer21 = customer21.ToValue
tempCustomerItemEnumerable2.Add(None, customer21)
# Deletes all data containing the given data from refresh.
tempCustomerItemEnumerable2.RemoveAll(customer21)
result13 = tempCustomerItemEnumerable2.First(lambda key, customer: customer.id == 21)
if result13 is not None: result13 = result13.ToValue
assert result13 is None, "EditTest - result13 is not equal to desired value"

