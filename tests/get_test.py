from tests.test_data import *



# Returns get value or Enumerable(value).
result1 = customer_enumerable.Get(2) 
assert result1 is customer_list[2], "GetTest - result1 is not equal to desired value"



# Returns get index.
result2 = customer_enumerable.GetKey(result1) 
assert result2 == 2, "GetTest - result2 is not equal to desired value"



# Returns get keys list.
result3 = customer_enumerable.GetKeys() 
assert result3 == list(range(len(customer_list))), "GetTest - result3 is not equal to desired value"



# Returns get values list.
result4 = customer_enumerable.GetValues() 
assert result4 == customer_list, "GetTest - result4 is not equal to desired value"



# Returns get items [(key,value), ...] list.
result5 = customer_enumerable.GetItems() 
assert result5 == list(enumerate(customer_list)), "GetTest - result5 is not equal to desired value"



# Applies an accumulator function over a sequence.
result6 = customer_enumerable.Aggregate(lambda result, index, customer: result + customer.age, lambda index, customer: customer.age)
assert result6 == sum(map(lambda customer: customer.age, customer_list)), "GetTest - result6 is not equal to desired value"