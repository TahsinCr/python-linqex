from tests.test_data import *

temp_customer_enumerable = customer_enumerable.Copy()



new_customer = Customer(id=13,name="John",age=44,gender=MALE)
temp_customer_enumerable.Add(new_customer) # Adds the new customer to iterable.
result1 = temp_customer_enumerable.First(lambda index, customer: customer.id == 13)
if result1 is not None: result1 = result1.ToValue
assert result1 is new_customer, "EditTest - result1 is not equal to desired value"



temp_customer_iterable = temp_customer_enumerable.Copy().ToValue
new_customer = Customer(id=4,name="Jack",age=29,gender=MALE)
# Replaces the given value with the selected value (Updates the value).
temp_customer_enumerable.Update(temp_customer_enumerable.First(lambda index, customer: customer.id == 4).ToKey, new_customer)
# It does the same as the 'Update()' method above.
# temp_customer_enumerable.First(lambda index, customer: customer.id == 4).Set(new_customer)
result2 = temp_customer_enumerable.First(lambda index, customer: customer.id == 4)
if result2 is not None: result2 = result2.ToValue
assert result2 is new_customer, "EditTest - result2 is not equal to desired value"



temp_customer_iterable = temp_customer_enumerable.Copy().ToValue
new_customers = [Customer(id=14,name="Frank",age=16,gender=MALE),Customer(id=15,name="Gregor",age=10,gender=MALE)]
# Expands with new customers list.
temp_customer_enumerable.Concat(new_customers)
result3 = temp_customer_enumerable.ToValue
assert result3 == temp_customer_iterable + new_customers, "EditTest - result3 is not equal to desired value"



temp_customer_iterable = temp_customer_enumerable.Copy().ToValue
# Deletes data with given key value from iterable.
temp_customer_enumerable.Delete(temp_customer_enumerable.First(lambda index, customer: customer.id == 13).ToKey)
result4 = temp_customer_enumerable.First(lambda index, customer: customer.id == 13)
if result4 is not None: result4 = result4.ToValue
assert result4 is None, "EditTest - result4 is not equal to desired value"



temp_customer_iterable = temp_customer_enumerable.Copy().ToValue
# Deletes the current value from the iterable.
temp_customer_enumerable.First(lambda index, customer: customer.id == 12).Delete()
result5 = temp_customer_enumerable.First(lambda index, customer: customer.id == 12)
if result5 is not None: result5 = result5.ToValue
assert result5 is None, "EditTest - result5 is not equal to desired value"



temp_customer_iterable = temp_customer_enumerable.Copy().ToValue
# Deletes given data from iterable.
temp_customer_enumerable.Remove(temp_customer_enumerable.First(lambda index, customer: customer.id == 11).ToValue)
result6 = temp_customer_enumerable.First(lambda index, customer: customer.id == 11)
if result6 is not None: result6 = result6.ToValue
assert result6 == None, "EditTest - result6 is not equal to desired value"



temp_customer_iterable = temp_customer_enumerable.Copy().ToValue
# Converts Enumerable to dict.
temp_customer_enumerable.ConvertToDict()
result7 = temp_customer_enumerable.ToValue
assert result7 == dict(enumerate(temp_customer_iterable)), "EditTest - result7 is not equal to desired value"



temp_customer_iterable = temp_customer_enumerable.Copy().ToValue
# Converts Enumerable to list.
temp_customer_enumerable.ConvertToList()
result8 = temp_customer_enumerable.ToValue
assert result8 == list(temp_customer_iterable.values()), "EditTest - result8 is not equal to desired value"



temp_customer_iterable = temp_customer_enumerable.Copy().ToValue
# If the value is iterable change the values ​​in it as desired.
temp_customer_enumerable.Map(lambda index, customer: customer.age)
result9 = temp_customer_enumerable.ToValue
assert result9 == list(map(lambda customer: customer.age,temp_customer_iterable)), "EditTest - result9 is not equal to desired value"



new_customer = Customer(id=20,name="Max",age=32,gender=MALE)
temp_customer_enumerable.Prepend(new_customer) # Adds the new customer to the top of the list
result10 = temp_customer_enumerable.First(lambda index, customer: customer.id == 20)
if result10 is not None: result10 = result10.ToValue
assert result10 is new_customer, "EditTest - result10 is not equal to desired value"



new_customer = Customer(id=21,name="Isla",age=45,gender=FEMALE)
temp_customer_enumerable.Insert(5,new_customer) # Adds the new customer to the desired section of the list
result11 = temp_customer_enumerable.First(lambda index, customer: customer.id == 21)
if result11 is not None: result11 = result11.ToValue
assert result11 is new_customer, "EditTest - result11 is not equal to desired value"