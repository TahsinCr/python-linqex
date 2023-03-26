from tests.test_data import *



# Returns number of values given for iterable
result1 = customer_enumerable.Count(FEMALE, lambda index, customer: customer.gender)
assert result1 == 4, "FilterTest - result1 is not equal to desired value"



# Returns average of iterable numbers.
result2 = customer_enumerable.Sum(lambda index, customer: customer.age) 
assert result2 == 366, "FilterTest - result2 is not equal to desired value"



# Returns number of values given for iterable
result3 = customer_enumerable.Avg(lambda index, customer: customer.age)  
assert result3 == 30.5, "FilterTest - result3 is not equal to desired value"



# Returns largest of numbers in iterable
result4 = customer_enumerable.Max(lambda index, customer: customer.age)
assert result4 == 55, "FilterTest - result4 is not equal to desired value"



# Returns smallest of numbers in iterable
result5 = customer_enumerable.Min(lambda index, customer: customer.age)  
assert result5 == 12, "FilterTest - result5 is not equal to desired value"
