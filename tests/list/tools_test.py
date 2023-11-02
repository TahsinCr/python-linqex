from .test_data import *



# Returns a Enumerable class with an empty list inside.
result1 = Enumerable.List() 
assert result1.ToValue == [], "ToolsEdit - result1 is not equal to desired value"



# Returns converts Enumerable to value.
# The 'ToValue' function cannot be used if the result of a query on Enumerable is not a iterable value.
result2 = customerListEnumerable.ToValue 
assert result2 == customerList, "ToolsEdit - result2 is not equal to desired value"



# Returns converts Enumerable to key.
result3 = customerListEnumerable.ToKey 
assert result3 is None, "ToolsEdit - result3 is not equal to desired value"



# Returns converts Enumerable to dict.
result4 = customerListEnumerable.ToDict 
assert result4 == dict(enumerate(customerList)), "ToolsEdit - result4 is not equal to desired value"



# Returns True if iterable is empty, False otherwise.
result5 = customerListEnumerable.IsEmpty 
assert result5 == False, "ToolsEdit - result5 is not equal to desired value"



# If the entered value contains iterable data and the iterable data contains the given key, it returns True, otherwise it returns False.
result6 = customerListEnumerable.ContainsByKey('test') 
assert result6 == False, "ToolsEdit - result6 is not equal to desired value"



# If the entered value contains iterable data and the iterable data contains the given value, it returns True, otherwise it returns False.
result7 = customerListEnumerable.Contains('test') 
assert result7 == False, "ToolsEdit - result7 is not equal to desired value"



# Copy Enumerable.
result8 = customerListEnumerable.Copy()
assert result8.ToValue == customerList, "ToolsEdit - result8 is not equal to desired value"



# Returns length of iterable
result9 = customerListEnumerable.Lenght
assert result9 == len(customerList), "ToolsEdit - result9 is not equal to desired value"



# Generates a sequence of integral numbers within a specified range.
result10 = Enumerable.List().Range(1, 100, 5).ToValue
assert result10 == list(range(1,100,5)), "ToolsEdit - result10 is not equal to desired value"



# Generates a sequence that contains one repeated value.
result11 = Enumerable.List().Repeat("testing",10).ToValue
assert result11 == ["testing"] * 10, "ToolsEdit - result11 is not equal to desired value"



# Returns converts Enumerable to list.
result12 = customerListEnumerable.ToList
assert result12 == customerList, "ToolsEdit - result12 is not equal to desired value"


# Returns converts Enumerable to item.
result13 = customerListEnumerable.ToItem 
assert result13 == list(enumerate(customerList)), "ToolsEdit - result13 is not equal to desired value"