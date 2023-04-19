# **Change Log**
All notable changes to this project will be documented in this file.

## **[1.4] - 19.04.2023**
Added classes generic structure
### Added
 * Added 'EnumerableBase' and 'Enumerable' classes generic structure.
 * Added 'EnumerableBase().Accumulate', 'EnumerableBase().RemoveAll' and 'EnumerableBase.Dict().OfTypeByKey' methods into the 'Enumerable Base' class
 * Added 'Enumerable().Accumulate', 'Enumerable().RemoveAll' and 'Enumerable.Dict().OfTypeByKey' methods in the 'Enumerable' class
### Remove
 * Removed 'Enumerable().Map' methods in the 'Enumerable' class

<br>

## **[1.3] - 27.03.2023**
Most methods found in the C# Linq framework have been transferred to the python-linqex project and additional modifications have been made to the classes. (build.py and linq.py edited, newly added methods tested)
### Add
 * Added data type fixation to 'Enumerable' class. [Enumerable(iterable) -> Enumerable(iterable, const-type)]
 * Added 'Take', 'TakeLast', 'Skip', 'SkipLast', 'Select', 'Distinct', 'Except', 'Join', 'OrderBy', 'Reverse', 'Zip', 'SequenceEqual', 'Aggregate', 'Prepent', 'Insert', 'Concat', 'Map', 'ContainsByKey', 'Contains' and 'Loop' methods into the 'Enumerable Base' class
 * Added 'Take', 'TakeLast', 'Skip', 'SkipLast', 'Select', 'Distinct', 'Except', 'Join', 'OrderBy', 'ThenBy', 'Reverse', 'Zip', 'SequenceEqual', 'Aggregate', 'Prepent', 'Insert', 'Concat', 'Map', 'ContainsByKey', 'Contains' and 'Loop' methods in the 'Enumerable' class
 * Added 'Range' and 'Repeat' static methods into the 'Enumerable' class
### Edited
 * PascalCase is used to name the methods inside the 'Enumerable' class and the 'build.py' file.
 * The methods in the 'build.py' file are imported into the 'EnumerableBase(iterable)' class in the 'build.py' file.
 * The names of the 'insets' -> 'Select' and 'insets' -> 'Map' methods in the 'EnumerateBase' class have been changed.
 * The names of the 'insets' -> 'Select', 'insets' -> 'Map', 'inKey' -> 'ContainsByKey' and 'inValue' -> 'Contains' methods in the 'Enumerate' class have been changed.
### Deleted
 * Deleted 'ingets' and 'insets' methods from 'Enumerable' class and 'build.py' file.

<br>

## **[1.2.2] - 15.03.2023**
build.py and linq.py edited
### Edited
 * 'Linq(iterable).delete()', 'lenght' in 'linq.py' and 'count', 'summation', 'average', 'maximum', 'minimum', 'any', 'all' in 'build.py' functions edited and tested.

<br>

## **[1.2.1] - 07.03.2023**
build.py and linq.py edited
### Edited
 * 'enumerable_catch' in 'linq.py' and 'first', 'single', 'last' in 'build.py' functions edited and tested.

<br>

## **[1.2] - 12.02.2023**
First steps. Creating the library. Designing and planning.
### Added
 * First steps. Creating the Build methods and Enumerable class.

<br>
