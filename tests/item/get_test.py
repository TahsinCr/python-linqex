from .test_data import *
import itertools


# Returns get value or Enumerable(value).
result1 = customerItemEnumerable.Get(2)
assert result1 is customerItem[2], "GetTest - result1 is not equal to desired value"



# Returns get index.
result2 = customerItemEnumerable.GetKey(result1) 
assert result2 == 2, "GetTest - result2 is not equal to desired value"



# Returns get keys list.
result3 = customerItemEnumerable.GetKeys().ToValue
assert result3 == list(range(len(customerItem))), "GetTest - result3 is not equal to desired value"



# Returns get values list.
result4 = customerItemEnumerable.GetValues().ToValue
assert result4 == customerItem, "GetTest - result4 is not equal to desired value"



# Returns get items [(key,value), ...] list.
result5 = customerItemEnumerable.GetItems().ToValue
assert result5 == list(enumerate(customerItem)), "GetTest - result5 is not equal to desired value"



# Applies an accumulator function over a sequence.
result6 = customerItemEnumerable.Select(lambda key, customer: customer.age).Aggregate(lambda temp, key, age: temp + age)
assert result6 == sum(map(lambda customer: customer.age, customerItem)), "GetTest - result6 is not equal to desired value"



# Applies the spooler function by grouping the elements in pairs on a row and returns the list.
result7 = customerItemEnumerable.Select(lambda key, customer: customer.age).Accumulate(lambda temp, key, age: temp + age)
assert result7 == list(itertools.accumulate(map(lambda c: c.age, customerItem), lambda temp, nextValue: temp + nextValue)), "GetTest - result7 is not equal to desired value"
