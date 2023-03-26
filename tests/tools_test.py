from tests.test_data import *



# Returns a Enumerable class with an empty list inside.
result1 = Enumerable.List() 
assert result1.ToValue == [], "ToolsEdit - result1 is not equal to desired value"



# Returns a Enumerable class with an empty dict inside.
result2 = Enumerable.Dict()
assert result2.ToValue == {}, "ToolsEdit - result2 is not equal to desired value"



# Returns converts Enumerable to value.
# The 'ToValue' function cannot be used if the result of a query on Enumerable is not a iterable value.
result3 = customer_enumerable.ToValue 
assert result3 == customer_list, "ToolsEdit - result3 is not equal to desired value"



# Returns converts Enumerable to key.
result4 = customer_enumerable.ToKey 
assert result4 is None, "ToolsEdit - result4 is not equal to desired value"



# Returns converts Enumerable to dict.
result5 = customer_enumerable.ToDict 
assert result5 == dict(enumerate(customer_list)), "ToolsEdit - result5 is not equal to desired value"



# Returns converts Enumerable to list. returns None if in main Enumerable.
result6 = customer_enumerable.ToList 
assert result6 == customer_list, "ToolsEdit - result6 is not equal to desired value"



# Returns True if iterable is empty, False otherwise.
result7 = customer_enumerable.IsEmpty 
assert result7 == False, "ToolsEdit - result7 is not equal to desired value"



# Returns True if its data type is the same as the entered data type, otherwise False.
result8 = customer_enumerable.IsType(dict) 
assert result8 == False, "ToolsEdit - result8 is not equal to desired value"



# Returns True if the key of the list is the key entered, False otherwise.
result9 = customer_enumerable.IsKey('test') 
assert result9 == False, "ToolsEdit - result9 is not equal to desired value"



# Returns True if the value of the list is the value entered, False otherwise.
result10 = customer_enumerable.IsValue('test') 
assert result10 == False, "ToolsEdit - result10 is not equal to desired value"



# If the entered value contains iterable data and the iterable data contains the given key, it returns True, otherwise it returns False.
result11 = customer_enumerable.ContainsByKey('test') 
assert result11 == False, "ToolsEdit - result11 is not equal to desired value"



# If the entered value contains iterable data and the iterable data contains the given value, it returns True, otherwise it returns False.
result12 = customer_enumerable.Contains('test') 
assert result12 == False, "ToolsEdit - result12 is not equal to desired value"



# Copy Enumerable.
result13 = customer_enumerable.Copy()
assert result13.ToValue == customer_list, "ToolsEdit - result13 is not equal to desired value"



# Returns length of iterable
result14 = customer_enumerable.Lenght
assert result14 == len(customer_list), "ToolsEdit - result14 is not equal to desired value"



# Generates a sequence of integral numbers within a specified range.
result15 = Enumerable.Range(1, 100, 5).ToValue
assert result15 == list(range(1,100,5)), "ToolsEdit - result15 is not equal to desired value"



# Generates a sequence that contains one repeated value.
result16 = Enumerable.Repeat("testing",10).ToValue
assert result16 == ["testing"] * 10, "ToolsEdit - result16 is not equal to desired value"
