from .test_data import *



# Returns number of values given for iterable
result1 = customerItemEnumerable.Select(lambda key, customer: customer.gender).Count(FEMALE)
assert result1 == 4, "FilterTest - result1 is not equal to desired value"



# Returns average of iterable numbers.
result2 = customerItemEnumerable.Select(lambda key, customer: customer.age).Sum()
assert result2 == 366, "FilterTest - result2 is not equal to desired value"



# Returns number of values given for iterable
result3 = customerItemEnumerable.Select(lambda key, customer: customer.age).Avg()
assert result3 == 30.5, "FilterTest - result3 is not equal to desired value"



# Returns largest of numbers in iterable
result4 = customerItemEnumerable.Select(lambda key, customer: customer.age).Max()
assert result4 == 55, "FilterTest - result4 is not equal to desired value"



# Returns smallest of numbers in iterable
result5 = customerItemEnumerable.Select(lambda key, customer: customer.age).Min()
assert result5 == 12, "FilterTest - result5 is not equal to desired value"
