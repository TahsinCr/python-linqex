# **Change Log**
All notable changes to this project will be documented in this file.

## **[1.5] - 01.05.2023**
New `EnumerableItem`.
### Added
 * Added `EnumerableItemBase` and `EnumerableItem` classes.
### Edited
 * Calling the `EnumerableBase` class will now return the `EnumerableItemBase` class instead of the `EnumerableListBase`.
 * Calling the `Enumerable` class will now return the `EnumerableItem` class instead of the `EnumerableList`.
 * 
### Fixed
 * Fixed minor bugs in `OrderBy` method in all classes.

<br>

## **[1.4] - 19.04.2023**
Added classes generic structure
### Added
 * Added 'EnumerableBase' and 'Enumerable' classes generic structure.
 * Added 'EnumerableBase(iterable).Accumulate', 'EnumerableBase(iterable).RemoveAll' and 'EnumerableBase.Dict(iterdict).OfTypeByKey' methods into the 'Enumerable Base' class
 * Added 'Enumerable(iterable).Accumulate', 'Enumerable(iterable).RemoveAll' and 'Enumerable.Dict(iterdict).OfTypeByKey' methods in the 'Enumerable' class
### Edited
 * Methods in class 'EnumerableBase(iterable)' in file 'build.py' have been split into structures 'build/iterlist.py' 'EnumerableListBase(iterlist)' and 'build/iterdict.py' 'EnumerableDictBase(iterdict)'.
 * Methods in class 'Enumerable(iterable)' in file 'build.py' have been split into structures 'build/iterlist.py' and 'build/iterdict.py'.
### Deleted
 * Deleted 'Enumerable(iterable).Map' methods in the 'Enumerable' class

<br>

## **[1.3] - 27.03.2023**
Most methods found in the C# Linq framework have been transferred to the python-linqex project and additional modifications have been made to the classes. (build.py and linq.py edited, newly added methods tested)
### Add
 * Added data type fixation to 'Enumerable' class. [Enumerable(iterable) -> Enumerable(iterable, const-type)]
 * Added 'Take', 'TakeLast', 'Skip', 'SkipLast', 'Select', 'Distinct', 'Except', 'Join', 'OrderBy', 'Reverse', 'Zip', 'SequenceEqual', 'Aggregate', 'Prepent', 'Insert', 'Concat', 'Map', 'ContainsByKey', 'Contains' and 'Loop' methods into the 'Enumerable Base' class
 * Added 'Take', 'TakeLast', 'Skip', 'SkipLast', 'Select', 'Distinct', 'Except', 'Join', 'OrderBy', 'ThenBy', 'Reverse', 'Zip', 'SequenceEqual', 'Aggregate', 'Prepent', 'Insert', 'Concat', 'Map', 'ContainsByKey', 'Contains' and 'Loop' methods in the 'Enumerable' class
 * Added 'Range' and 'Repeat' static methods into the 'Enumerable' class
### Edited
 * Methods in class 'EnumerableBase(iterable)' in file 'linq.py' have been split into structures 'build/iterlist.py' and 'build/iterdict.py'.
 * Methods in class 'EnumerableBase(iterable)' in file 'linq.py' have been split into structures 'linq/iterlist.py' and 'linq/iterdict.py'.
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
