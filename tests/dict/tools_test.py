from .test_data import *



# Returns a Enumerable class with an empty dict inside.
result1 = Enumerable.Dict()
assert result1.ToValue == {}, "ToolsEdit - result1 is not equal to desired value"



# Returns converts Enumerable to value.
# The 'ToValue' function cannot be used if the result of a query on Enumerable is not a iterable value.
result2 = customerDictEnumerable.ToValue 
assert result2 == customerDict, "ToolsEdit - result2 is not equal to desired value"



# Returns converts Enumerable to key.
result3 = customerDictEnumerable.ToKey 
assert result3 is None, "ToolsEdit - result3 is not equal to desired value"



# Returns converts Enumerable to dict.
result4 = customerDictEnumerable.ToList 
assert result4 == list(customerDict.values()), "ToolsEdit - result4 is not equal to desired value"



# Returns True if iterable is empty, False otherwise.
result5 = customerDictEnumerable.IsEmpty 
assert result5 == False, "ToolsEdit - result5 is not equal to desired value"



# If the entered value contains iterable data and the iterable data contains the given key, it returns True, otherwise it returns False.
result6 = customerDictEnumerable.ContainsByKey('test') 
assert result6 == False, "ToolsEdit - result6 is not equal to desired value"



# If the entered value contains iterable data and the iterable data contains the given value, it returns True, otherwise it returns False.
result7 = customerDictEnumerable.Contains('test') 
assert result7 == False, "ToolsEdit - result7 is not equal to desired value"



# Copy Enumerable.
result8 = customerDictEnumerable.Copy()
assert result8.ToValue == customerDict, "ToolsEdit - result8 is not equal to desired value"



# Returns length of iterable
result9 = customerDictEnumerable.Lenght
assert result9 == len(customerDict), "ToolsEdit - result9 is not equal to desired value"




# Returns converts Enumerable to dict.
result10 = customerDictEnumerable.ToDict
assert result10 == customerDict, "ToolsEdit - result10 is not equal to desired value"

# Returns converts Enumerable to item.
result11 = customerDictEnumerable.ToItem 
assert result11 == list(enumerate(customerDict.values())), "ToolsEdit - result11 is not equal to desired value"