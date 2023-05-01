from .test_data import *
import itertools


# Returns get value or Enumerable(value).
result1 = customerDictEnumerable.Get(2)
assert result1 is customerDict[2], "GetTest - result1 is not equal to desired value"



# Returns get index.
result2 = customerDictEnumerable.GetKey(result1) 
assert result2 == 2, "GetTest - result2 is not equal to desired value"



# Returns get keys list.
result3 = customerDictEnumerable.GetKeys().ToValue
assert result3 == list(customerDict.keys()), "GetTest - result3 is not equal to desired value"



# Returns get values list.
result4 = customerDictEnumerable.GetValues().ToValue
assert result4 == list(customerDict.values()), "GetTest - result4 is not equal to desired value"



# Returns get items [(key,value), ...] list.
result5 = customerDictEnumerable.GetItems().ToValue
assert result5 == list(customerDict.items()), "GetTest - result5 is not equal to desired value"



# Applies an accumulator function over a sequence.
result6 = customerDictEnumerable.Select(lambda key, customer: customer.age).Aggregate(lambda temp, key, age: temp + age)
assert result6 == sum(map(lambda customer: customer.age, customerDict.values())), "GetTest - result6 is not equal to desired value"



# Applies the spooler function by grouping the elements in pairs on a row and returns the list.
result7 = customerDictEnumerable.Select(lambda key, customer: customer.age).Accumulate(lambda temp, key, age: temp + age)
assert result7 == dict(zip(customerDict.keys(),itertools.accumulate(map(lambda c: c.age, customerDict.values()), lambda temp, nextValue: temp + nextValue))), "GetTest - result7 is not equal to desired value"
