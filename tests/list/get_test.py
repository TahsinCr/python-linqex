from .test_data import *
import itertools


# Returns get value or Enumerable(value).
result1 = customerListEnumerable.Get(2).ToValue
assert result1 is customerList[2], "GetTest - result1 is not equal to desired value"



# Returns get index.
result2 = customerListEnumerable.GetKey(result1) 
assert result2 == 2, "GetTest - result2 is not equal to desired value"



# Returns get keys list.
result3 = customerListEnumerable.GetKeys().ToValue
assert result3 == list(range(len(customerList))), "GetTest - result3 is not equal to desired value"



# Returns get values list.
result4 = customerListEnumerable.GetValues().ToValue
assert result4 == customerList, "GetTest - result4 is not equal to desired value"



# Returns get items [(key,value), ...] list.
result5 = customerListEnumerable.GetItems().ToValue
assert result5 == list(enumerate(customerList)), "GetTest - result5 is not equal to desired value"



# Applies an accumulator function over a sequence.
result6 = customerListEnumerable.Select(lambda customer: customer.age).Aggregate(lambda temp, age: temp + age)
assert result6 == sum(map(lambda customer: customer.age, customerList)), "GetTest - result6 is not equal to desired value"



# Applies the spooler function by grouping the elements in pairs on a row and returns the list.
result7 = customerListEnumerable.Select(lambda customer: customer.age).Accumulate(lambda temp, age: temp + age)
assert result7 == list(itertools.accumulate(map(lambda c: c.age, customerList), lambda temp, nextValue: temp + nextValue)), "GetTest - result7 is not equal to desired value"
