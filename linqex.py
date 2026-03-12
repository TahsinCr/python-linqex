"""
PyLINQ: A High-Performance Python Implementation of C# LINQ

This module provides a robust, production-ready implementation of Language Integrated Query (LINQ) 
for Python. It allows developers to query, transform, and manipulate iterable sequences using 
a fluent, declarative syntax identical to C#.

Core Design Principles:
    - Deferred Execution (Lazy Evaluation): Computations are only performed when a terminal 
      operation (like `to_list`, `count`, or `first`) is called, preserving memory ($O(1)$) 
      and maximizing performance.
    - C# Parity: Replicates .NET 8 LINQ behaviors meticulously, including robust exception 
      handling (e.g., `ValueError` on duplicate dictionary keys, empty sequences).
    - Pythonic Fast-Paths: Leverages Python's native `itertools`, `collections`, and built-in 
      sequence checks (e.g., `isinstance(x, Sequence)`) to achieve C-level execution speeds 
      for operations like indexing and counting.
    - Type Safety: Fully annotated with `typing` generics (`T`, `R`, `TKey`) to provide 
      seamless autocompletion and static type checking in modern IDEs.

Supported LINQ Categories:
    - Projection & Filtering: `select`, `where`, `select_many`, `of_type`, `cast`
    - Partitioning: `take`, `skip`, `take_while`, `take_last`, `chunk`
    - Sorting: `order`, `order_by`, `then_by`, `then_by_descending`
    - set Operations: `distinct`, `union`, `intersect`, `except_by`
    - Aggregation: `count`, `sum`, `max`, `min`, `average`, `aggregate`
    - Joins & Grouping: `join`, `group_join`, `group_by`
    - Element Operators: `first`, `last`, `single`, `element_at` (with `_or_default` variants)

Note on Generator Exhaustion:
    Because Python generators can only be consumed once, ensure you pass lists or tuples 
    to `Enumerable` if you intend to execute multiple terminal operations on the same instance.
"""
import itertools
from collections import deque, defaultdict
from functools import reduce
from typing import Iterable, Iterator, Callable, TypeVar, Generic, Any, Union, Sequence

__version__ = '2.0'

T = TypeVar('T')
R = TypeVar('R')
TInner = TypeVar('TInner')
TKey = TypeVar('TKey')

class Enumerable(Generic[T], Iterable[T]):
    """
    A Python implementation of C# LINQ (Language Integrated Query) providing a fluent interface
    for querying and manipulating collections with deferred execution.
    
    Example Usage:
    >>> from your_module import Enumerable
    >>> data = [
    ...     {"name": "Alice", "age": 28, "department": "IT"},
    ...     {"name": "Bob", "age": 35, "department": "HR"},
    ...     {"name": "Charlie", "age": 42, "department": "IT"}
    ... ]
    >>> it_employees = (Enumerable(data)
    ...     .where(lambda x: x["department"] == "IT")
    ...     .order_by_descending(lambda x: x["age"])
    ...     .select(lambda x: x["name"])
    ...     .to_list())
    >>> print(it_employees)
    ['Charlie', 'Alice']
    """
    __slots__ = ('_source',)

    @staticmethod
    def range(start: int, count: int) -> 'Enumerable[int]':
        """
        Generates a sequence of integral numbers within a specified range.

        Args:
            start: The value of the first integer in the sequence.
            count: The number of sequential integers to generate.

        Returns:
            An Enumerable that contains a range of sequential integral numbers.
        """
        return Enumerable(range(start, start + count))

    @staticmethod
    def repeat(element: T, count: int) -> 'Enumerable[T]':
        """
        Generates a sequence that contains one repeated value.

        Args:
            element: The value to be repeated.
            count: The number of times to repeat the value in the generated sequence.

        Returns:
            An Enumerable that contains a repeated value.
        """
        return Enumerable(itertools.repeat(element, count))

    def __init__(self, source: Iterable[T] = None):
        """
        Initializes a new instance of the Enumerable class.

        Args:
            source: The iterable sequence to wrap. Defaults to an empty list if None.
        """
        self._source = source if source is not None else []

    def __iter__(self) -> Iterator[T]:
        """Returns an iterator that iterates through the collection."""
        return iter(self._source)

    def __bool__(self) -> bool:
        """Determines whether a sequence contains any elements (Truth value testing)."""
        return self.any()

    def __add__(self, other: Iterable[T]) -> 'Enumerable[T]':
        """Concatenates two sequences using the '+' operator."""
        return self.concat(other)

    def __getitem__(self, item: Union[int, slice]) -> Any:
        """
        Allows indexing and slicing on the Enumerable sequence.
        
        Args:
            item: An integer index or a slice object.

        Returns:
            The element at the specified index, or a new Enumerable if sliced.

        Raises:
            IndexError: If negative indexing is used.
            ValueError: If advanced slicing (negative steps) is used.
            TypeError: If the argument is neither int nor slice.
        """
        if isinstance(item, int):
            if item < 0:
                raise IndexError("Negative indexing is not supported for forward-only streams.")
            return self.element_at(item)
        elif isinstance(item, slice):
            start = item.start or 0
            stop = item.stop
            step = item.step or 1
            if step != 1 or start < 0 or (stop is not None and stop < 0):
                raise ValueError("Advanced slicing (negative/steps) not supported in lazy streams.")
            res = self.skip(start)
            if stop is not None:
                res = res.take(stop - start)
            return res
        raise TypeError("Invalid argument type for indexing.")

    # --- Projection & Filtering ---

    def select(self, selector: Callable[[T], R] = lambda x: x) -> 'Enumerable[R]':
        """
        Projects each element of a sequence into a new form.

        Args:
            selector: A transform function to apply to each element.

        Returns:
            An Enumerable whose elements are the result of invoking the transform function.
        """
        return Enumerable(map(selector, self._source))

    def select_with_index(self, selector: Callable[[T, int], R]) -> 'Enumerable[R]':
        """
        Projects each element of a sequence into a new form by incorporating the element's index.

        Args:
            selector: A transform function to apply to each source element; the second parameter of the function represents the index.

        Returns:
            An Enumerable whose elements are the result of invoking the transform function.
        """
        return Enumerable(itertools.starmap(lambda index, item: selector(item, index), enumerate(self._source)))

    def where(self, predicate: Callable[[T], bool]) -> 'Enumerable[T]':
        """
        Filters a sequence of values based on a predicate.

        Args:
            predicate: A function to test each element for a condition.

        Returns:
            An Enumerable that contains elements from the input sequence that satisfy the condition.
        """
        return Enumerable(filter(predicate, self._source))

    def where_with_index(self, predicate: Callable[[T, int], bool]) -> 'Enumerable[T]':
        """
        Filters a sequence of values based on a predicate that incorporates the element's index.

        Args:
            predicate: A function to test each element for a condition; the second parameter represents the index.

        Returns:
            An Enumerable that contains elements that satisfy the condition.
        """
        def generator():
            for index, item in enumerate(self._source):
                if predicate(item, index):
                    yield item
        return Enumerable(generator())

    def select_many(self, collection_selector: Callable[[T], Iterable[R]]) -> 'Enumerable[R]':
        """
        Projects each element of a sequence to an Iterable and flattens the resulting sequences into one sequence.

        Args:
            collection_selector: A transform function to apply to each element.

        Returns:
            An Enumerable whose elements are the result of invoking the one-to-many transform function.
        """
        return Enumerable(itertools.chain.from_iterable(map(collection_selector, self._source)))

    def of_type(self, type_class: type) -> 'Enumerable[Any]':
        """
        Filters the elements of an Enumerable based on a specified type.

        Args:
            type_class: The type to filter the elements of the sequence on.

        Returns:
            An Enumerable that contains elements from the input sequence of type type_class.
        """
        return Enumerable(filter(lambda x: isinstance(x, type_class), self._source))

    def cast(self, type_class: type) -> 'Enumerable[Any]':
        """
        Casts the elements of an Enumerable to the specified type.

        Args:
            type_class: The type to cast the elements to.

        Returns:
            An Enumerable that contains each element of the source sequence cast to the specified type.
        """
        return Enumerable(map(type_class, self._source))

    # --- Partitioning ---

    def take(self, count: int) -> 'Enumerable[T]':
        """
        Returns a specified number of contiguous elements from the start of a sequence.

        Args:
            count: The number of elements to return.

        Returns:
            An Enumerable that contains the specified number of elements from the start of the input sequence.
        """
        if count <= 0: return Enumerable([])
        return Enumerable(itertools.islice(self._source, count))

    def skip(self, count: int) -> 'Enumerable[T]':
        """
        Bypasses a specified number of elements in a sequence and then returns the remaining elements.

        Args:
            count: The number of elements to skip before returning the remaining elements.

        Returns:
            An Enumerable that contains the elements that occur after the specified index.
        """
        if count <= 0: return self
        return Enumerable(itertools.islice(self._source, count, None))

    def take_while(self, predicate: Callable[[T], bool]) -> 'Enumerable[T]':
        """
        Returns elements from a sequence as long as a specified condition is true, and then skips the remaining elements.

        Args:
            predicate: A function to test each element for a condition.

        Returns:
            An Enumerable that contains the elements from the input sequence that occur before the element at which the test no longer passes.
        """
        return Enumerable(itertools.takewhile(predicate, self._source))

    def skip_while(self, predicate: Callable[[T], bool]) -> 'Enumerable[T]':
        """
        Bypasses elements in a sequence as long as a specified condition is true and then returns the remaining elements.

        Args:
            predicate: A function to test each element for a condition.

        Returns:
            An Enumerable that contains the elements starting at the first element in the linear series that does not pass the test.
        """
        return Enumerable(itertools.dropwhile(predicate, self._source))

    def take_last(self, count: int) -> 'Enumerable[T]':
        """
        Returns a new enumerable collection that contains the last count elements from source.

        Args:
            count: The number of elements to take from the end of the collection.

        Returns:
            An Enumerable containing the last count elements.
        """
        if count <= 0: return Enumerable([])
        def generator():
            yield from deque(self._source, maxlen=count)
        return Enumerable(generator())

    def skip_last(self, count: int) -> 'Enumerable[T]':
        """
        Returns a new enumerable collection that contains the elements from source with the last count elements of the source collection omitted.

        Args:
            count: The number of elements to omit from the end of the collection.

        Returns:
            An Enumerable containing the elements with the last count elements omitted.
        """
        if count <= 0: return self
        def generator():
            iterator = iter(self._source)
            window = deque(itertools.islice(iterator, count), maxlen=count)
            for item in iterator:
                yield window[0]
                window.append(item)
        return Enumerable(generator())

    def chunk(self, size: int) -> 'Enumerable[list[T]]':
        """
        Splits the elements of a sequence into chunks of size at most size.

        Args:
            size: The maximum size of each chunk.

        Returns:
            An Enumerable that contains the elements of the input sequence split into chunks.

        Raises:
            ValueError: If size is less than or equal to 0.
        """
        if size <= 0: raise ValueError("Chunk size must be > 0")
        def chunker():
            iterator = iter(self._source)
            while True:
                chunk_list = list(itertools.islice(iterator, size))
                if not chunk_list:
                    break
                yield chunk_list
        return Enumerable(chunker())

    # --- Concatenation ---

    def concat(self, other: Iterable[T]) -> 'Enumerable[T]':
        """
        Concatenates two sequences.

        Args:
            other: The sequence to concatenate to the first sequence.

        Returns:
            An Enumerable that contains the concatenated elements of the two input sequences.
        """
        return Enumerable(itertools.chain(self._source, other))

    def append(self, element: T) -> 'Enumerable[T]':
        """
        Appends a value to the end of the sequence.

        Args:
            element: The value to append to the sequence.

        Returns:
            A new Enumerable that ends with element.
        """
        return Enumerable(itertools.chain(self._source, (element,)))

    def prepend(self, element: T) -> 'Enumerable[T]':
        """
        Adds a value to the beginning of the sequence.

        Args:
            element: The value to prepend to the sequence.

        Returns:
            A new Enumerable that begins with element.
        """
        return Enumerable(itertools.chain((element,), self._source))

    def zip(self, other: Iterable[TInner], selector: Callable[[T, TInner], R] = None) -> 'Enumerable[R]':
        """
        Applies a specified function to the corresponding elements of two sequences, producing a sequence of the results.

        Args:
            other: The second sequence to merge.
            selector: A function that specifies how to merge the elements from the two sequences. If None, returns tuples.

        Returns:
            An Enumerable that contains merged elements of two input sequences.
        """
        if selector is None:
            return Enumerable(zip(self._source, other))
        return Enumerable(map(lambda args: selector(*args), zip(self._source, other)))

    def reverse(self) -> 'Enumerable[T]':
        """
        Inverts the order of the elements in a sequence.

        Returns:
            An Enumerable whose elements correspond to those of the input sequence in reverse order.
        """
        def generator():
            if isinstance(self._source, Sequence):
                yield from reversed(self._source)
            else:
                yield from reversed(list(self._source))
        return Enumerable(generator())

    def default_if_empty(self, default_value: T = None) -> 'Enumerable[T]':
        """
        Returns the elements of the specified sequence or the specified value in a singleton collection if the sequence is empty.

        Args:
            default_value: The value to return if the sequence is empty.

        Returns:
            An Enumerable that contains default_value if source is empty; otherwise, source.
        """
        def generator():
            yielded = False
            for item in self._source:
                yielded = True
                yield item
            if not yielded:
                yield default_value
        return Enumerable(generator())

    # --- set Operations ---

    def distinct(self) -> 'Enumerable[T]':
        """
        Returns distinct elements from a sequence.

        Returns:
            An Enumerable that contains distinct elements from the source sequence.
        """
        return self.distinct_by(lambda x: x)

    def distinct_by(self, key_selector: Callable[[T], Any]) -> 'Enumerable[T]':
        """
        Returns distinct elements from a sequence according to a specified key selector function.

        Args:
            key_selector: A function to extract the key for each element.

        Returns:
            An Enumerable that contains distinct elements from the source sequence.
        """
        def generator():
            seen = set()
            seen_add = seen.add
            for element in self._source:
                key = key_selector(element)
                if key not in seen:
                    seen_add(key)
                    yield element
        return Enumerable(generator())

    def union(self, other: Iterable[T]) -> 'Enumerable[T]':
        """
        Produces the set union of two sequences.

        Args:
            other: An Iterable whose distinct elements form the second set for the union.

        Returns:
            An Enumerable that contains the elements from both input sequences, excluding duplicates.
        """
        return self.union_by(other, lambda x: x)

    def union_by(self, other: Iterable[T], key_selector: Callable[[T], Any]) -> 'Enumerable[T]':
        """
        Produces the set union of two sequences according to a specified key selector function.

        Args:
            other: An Iterable whose distinct elements form the second set for the union.
            key_selector: A function to extract the key for each element.

        Returns:
            An Enumerable that contains the elements from both input sequences, excluding duplicates based on the key.
        """
        return self.concat(other).distinct_by(key_selector)

    def intersect(self, other: Iterable[T]) -> 'Enumerable[T]':
        """
        Produces the set intersection of two sequences.

        Args:
            other: An Iterable whose distinct elements that also appear in the first sequence will be returned.

        Returns:
            An Enumerable that contains the elements that form the set intersection of two sequences.
        """
        return self.intersect_by(other, lambda x: x)

    def intersect_by(self, other: Iterable[T], key_selector: Callable[[T], Any]) -> 'Enumerable[T]':
        """
        Produces the set intersection of two sequences according to a specified key selector function.

        Args:
            other: An Iterable whose elements are compared with the first sequence.
            key_selector: A function to extract the key for each element.

        Returns:
            An Enumerable that contains the set intersection of two sequences.
        """
        def generator():
            other_set = set(map(key_selector, other))
            seen = set()
            for item in self._source:
                key = key_selector(item)
                if key in other_set and key not in seen:
                    seen.add(key)
                    yield item
        return Enumerable(generator())

    def except_for(self, other: Iterable[T]) -> 'Enumerable[T]':
        """
        Produces the set difference of two sequences.

        Args:
            other: An Iterable whose elements that also occur in the first sequence will cause those elements to be removed from the returned sequence.

        Returns:
            An Enumerable that contains the set difference of the elements of two sequences.
        """
        return self.except_by(other, lambda x: x)

    def except_by(self, other: Iterable[T], key_selector: Callable[[T], Any]) -> 'Enumerable[T]':
        """
        Produces the set difference of two sequences according to a specified key selector function.

        Args:
            other: An Iterable whose elements that also occur in the first sequence will cause those elements to be removed.
            key_selector: A function to extract the key for each element.

        Returns:
            An Enumerable that contains the set difference of the elements of two sequences.
        """
        def generator():
            other_set = set(map(key_selector, other))
            seen = set()
            for item in self._source:
                key = key_selector(item)
                if key not in other_set and key not in seen:
                    seen.add(key)
                    yield item
        return Enumerable(generator())

    # --- Joins & Grouping ---

    def join(self, inner: Iterable[TInner], outer_key: Callable[[T], TKey], inner_key: Callable[[TInner], TKey], selector: Callable[[T, TInner], R]) -> 'Enumerable[R]':
        """
        Correlates the elements of two sequences based on matching keys (Inner Join).

        Args:
            inner: The sequence to join to the first sequence.
            outer_key: A function to extract the join key from each element of the first sequence.
            inner_key: A function to extract the join key from each element of the second sequence.
            selector: A function to create a result element from two matching elements.

        Returns:
            An Enumerable that has elements of type R that are obtained by performing an inner join on two sequences.
        """
        def generator():
            lookup = defaultdict(list)
            for item in inner:
                lookup[inner_key(item)].append(item)
            for item in self._source:
                for inner_item in lookup.get(outer_key(item), []):
                    yield selector(item, inner_item)
        return Enumerable(generator())

    def group_join(self, inner: Iterable[TInner], outer_key: Callable[[T], TKey], inner_key: Callable[[TInner], TKey], selector: Callable[[T, 'Enumerable[TInner]'], R]) -> 'Enumerable[R]':
        """
        Correlates the elements of two sequences based on equality of keys and groups the results.

        Args:
            inner: The sequence to join to the first sequence.
            outer_key: A function to extract the join key from each element of the first sequence.
            inner_key: A function to extract the join key from each element of the second sequence.
            selector: A function to create a result element from an element from the first sequence and a collection of matching elements from the second sequence.

        Returns:
            An Enumerable that contains elements of type R that are obtained by performing a grouped join on two sequences.
        """
        def generator():
            lookup = defaultdict(list)
            for item in inner:
                lookup[inner_key(item)].append(item)
            for item in self._source:
                yield selector(item, Enumerable(lookup.get(outer_key(item), [])))
        return Enumerable(generator())

    def group_by(self, key_selector: Callable[[T], TKey]) -> 'Enumerable[GroupedEnumerable[TKey, T]]':
        """
        Groups the elements of a sequence according to a specified key selector function.

        Args:
            key_selector: A function to extract the key for each element.

        Returns:
            An Enumerable of GroupedEnumerable instances, where each object contains a sequence of objects and a key.
        """
        def generator():
            grouped = defaultdict(list)
            for item in self._source:
                grouped[key_selector(item)].append(item)
            for k, v in grouped.items():
                yield GroupedEnumerable(k, v)
        return Enumerable(generator())

    # --- Sorting ---

    def order(self) -> 'OrderedEnumerable[T]':
        """
        Sorts the elements of a sequence in ascending order.

        Returns:
            An OrderedEnumerable whose elements are sorted in ascending order.
        """
        return OrderedEnumerable(list(self._source), [(lambda x: x, False)])

    def order_descending(self) -> 'OrderedEnumerable[T]':
        """
        Sorts the elements of a sequence in descending order.

        Returns:
            An OrderedEnumerable whose elements are sorted in descending order.
        """
        return OrderedEnumerable(list(self._source), [(lambda x: x, True)])

    def order_by(self, key_selector: Callable[[T], Any]) -> 'OrderedEnumerable[T]':
        """
        Sorts the elements of a sequence in ascending order according to a key.

        Args:
            key_selector: A function to extract a key from an element.

        Returns:
            An OrderedEnumerable whose elements are sorted according to a key.
        """
        return OrderedEnumerable(list(self._source), [(key_selector, False)])

    def order_by_descending(self, key_selector: Callable[[T], Any]) -> 'OrderedEnumerable[T]':
        """
        Sorts the elements of a sequence in descending order according to a key.

        Args:
            key_selector: A function to extract a key from an element.

        Returns:
            An OrderedEnumerable whose elements are sorted in descending order according to a key.
        """
        return OrderedEnumerable(list(self._source), [(key_selector, True)])

    # --- Element Operators ---

    def element_at(self, index: int) -> T:
        """
        Returns the element at a specified index in a sequence.

        Args:
            index: The zero-based index of the element to retrieve.

        Returns:
            The element at the specified position in the source sequence.

        Raises:
            IndexError: If the index is out of range.
        """
        if isinstance(self._source, Sequence):
            return self._source[index]
        try:
            return next(itertools.islice(self._source, index, index + 1))
        except StopIteration:
            raise IndexError("Sequence index out of range")

    def element_at_or_default(self, index: int, default: Any = None) -> Any:
        """
        Returns the element at a specified index in a sequence or a default value if the index is out of range.

        Args:
            index: The zero-based index of the element to retrieve.
            default: The value to return if the index is out of bounds.

        Returns:
            default if the index is outside the bounds of the source sequence; otherwise, the element at the specified position.
        """
        if isinstance(self._source, Sequence):
            return self._source[index] if index < len(self._source) else default
            
        return next(itertools.islice(self._source, index, index + 1), default)

    def first(self, predicate: Callable[[T], bool] = None) -> T:
        """
        Returns the first element of a sequence, or the first element that satisfies a condition.

        Args:
            predicate: A function to test each element for a condition (optional).

        Returns:
            The first element in the sequence that passes the test in the specified predicate function.

        Raises:
            ValueError: If the source sequence is empty or no element satisfies the condition.
        """
        it = filter(predicate, self._source) if predicate else self._source
        try:
            return next(iter(it))
        except StopIteration:
            raise ValueError("Sequence contains no matching elements.")

    def first_or_default(self, default: Any = None, predicate: Callable[[T], bool] = None) -> Any:
        """
        Returns the first element of a sequence, or a default value if the sequence contains no elements.

        Args:
            default: The value to return if the sequence is empty.
            predicate: A function to test each element for a condition (optional).

        Returns:
            default if source is empty or if no element passes the test; otherwise, the first element that passes the test.
        """
        it = filter(predicate, self._source) if predicate else self._source
        return next(iter(it), default)

    def last(self, predicate: Callable[[T], bool] = None) -> T:
        """
        Returns the last element of a sequence, or the last element that satisfies a condition.

        Args:
            predicate: A function to test each element for a condition (optional).

        Returns:
            The last element in the sequence that passes the test in the specified predicate function.

        Raises:
            ValueError: If the source sequence is empty or no element satisfies the condition.
        """
        it = filter(predicate, self._source) if predicate else self._source
        tail = deque(it, maxlen=1)
        if not tail:
            raise ValueError("Sequence contains no matching elements.")
        return tail[0]

    def last_or_default(self, default: Any = None, predicate: Callable[[T], bool] = None) -> Any:
        """
        Returns the last element of a sequence, or a default value if the sequence contains no elements.

        Args:
            default: The value to return if the sequence is empty.
            predicate: A function to test each element for a condition (optional).

        Returns:
            default if the sequence is empty or if no elements pass the test; otherwise, the last element that passes the test.
        """
        it = filter(predicate, self._source) if predicate else self._source
        tail = deque(it, maxlen=1)
        return tail[0] if tail else default

    def single(self, predicate: Callable[[T], bool] = None) -> T:
        """
        Returns the only element of a sequence, and throws an exception if there is not exactly one element in the sequence.

        Args:
            predicate: A function to test an element for a condition (optional).

        Returns:
            The single element of the input sequence that satisfies a condition.

        Raises:
            ValueError: If the sequence contains no elements or more than one element.
        """
        it = filter(predicate, self._source) if predicate else self._source
        head = list(itertools.islice(it, 2))
        if len(head) == 0:
            raise ValueError("Sequence contains no elements.")
        if len(head) > 1:
            raise ValueError("Sequence contains more than one matching element.")
        return head[0]
    
    def single_or_default(self, default: Any = None, predicate: Callable[[T], bool] = None) -> Any:
        """
        Returns the only element of a sequence, or a default value if the sequence is empty; this method throws an exception if there is more than one element.

        Args:
            default: The value to return if the sequence is empty.
            predicate: A function to test an element for a condition (optional).

        Returns:
            The single element of the input sequence that satisfies the condition, or default if no such element is found.

        Raises:
            ValueError: If the sequence contains more than one matching element.
        """
        it = filter(predicate, self._source) if predicate else self._source
        head = list(itertools.islice(it, 2))
        if len(head) == 0:
            return default
        if len(head) > 1:
            raise ValueError("Sequence contains more than one matching element.")
        return head[0]

    # --- Quantifiers ---

    def any(self, predicate: Callable[[T], bool] = None) -> bool:
        """
        Determines whether any element of a sequence exists or satisfies a condition.

        Args:
            predicate: A function to test each element for a condition (optional).

        Returns:
            True if any elements in the source sequence pass the test; otherwise, False.
        """
        if predicate is None:
            return any(True for _ in self._source)
        return any(map(predicate, self._source))

    def all(self, predicate: Callable[[T], bool]) -> bool:
        """
        Determines whether all elements of a sequence satisfy a condition.

        Args:
            predicate: A function to test each element for a condition.

        Returns:
            True if every element of the source sequence passes the test; otherwise, False.
        """
        return all(map(predicate, self._source))

    def contains(self, value: T, key_selector: Callable[[T], Any] = None) -> bool:
        """
        Determines whether a sequence contains a specified element.

        Args:
            value: The value to locate in the sequence.
            key_selector: A function to extract a key from an element for equality comparison (optional).

        Returns:
            True if the source sequence contains an element that has the specified value; otherwise, False.
        """
        if key_selector is None:
            return value in self._source
        target_key = key_selector(value)
        return any(key_selector(x) == target_key for x in self._source)

    def sequence_equal(self, other: Iterable[T], key_selector: Callable[[Any], Any] = lambda x: x) -> bool:
        """
        Determines whether two sequences are equal by comparing the elements.

        Args:
            other: An Iterable to compare to the first sequence.
            key_selector: A function to project elements to compare equality.

        Returns:
            True if the two source sequences are of equal length and their corresponding elements are equal; otherwise, False.
        """
        sentinel = object() 
        for a, b in itertools.zip_longest(self._source, other, fillvalue=sentinel):
            if a is sentinel or b is sentinel or key_selector(a) != key_selector(b):
                return False
        return True

    # --- Aggregates ---

    def count(self, predicate: Callable[[T], bool] = None) -> int:
        """
        Returns the number of elements in a sequence.

        Args:
            predicate: A function to test each element for a condition (optional).

        Returns:
            The number of elements in the input sequence that satisfy the condition.
        """
        if predicate is None:
            if hasattr(self._source, "__len__"):
                return len(self._source)
            return sum(1 for _ in self._source)
        return sum(1 for _ in filter(predicate, self._source))

    def max(self, selector: Callable[[T], Any] = None) -> Any:
        """
        Returns the maximum value in a sequence.

        Args:
            selector: A transform function to apply to each element (optional).

        Returns:
            The maximum value in the sequence.
        """
        return max(map(selector, self._source)) if selector else max(self._source)

    def max_by(self, key_selector: Callable[[T], Any]) -> T:
        """
        Returns the maximum value in a sequence according to a specified key selector function.

        Args:
            key_selector: A function to extract the key for each element.

        Returns:
            The element with the maximum key value in the sequence.
        """
        return max(self._source, key=key_selector)

    def min(self, selector: Callable[[T], Any] = None) -> Any:
        """
        Returns the minimum value in a sequence.

        Args:
            selector: A transform function to apply to each element (optional).

        Returns:
            The minimum value in the sequence.
        """
        return min(map(selector, self._source)) if selector else min(self._source)

    def min_by(self, key_selector: Callable[[T], Any]) -> T:
        """
        Returns the minimum value in a sequence according to a specified key selector function.

        Args:
            key_selector: A function to extract the key for each element.

        Returns:
            The element with the minimum key value in the sequence.
        """
        return min(self._source, key=key_selector)

    def sum(self, selector: Callable[[T], Any] = None) -> Any:
        """
        Computes the sum of the sequence of numeric values.

        Args:
            selector: A transform function to apply to each element (optional).

        Returns:
            The sum of the values in the sequence.
        """
        return sum(map(selector, self._source) if selector else self._source)

    def average(self, selector: Callable[[T], Any] = None) -> float:
        """
        Computes the average of a sequence of numeric values.

        Args:
            selector: A transform function to apply to each element (optional).

        Returns:
            The average of the sequence of values.

        Raises:
            ValueError: If the sequence contains no elements.
        """
        it = iter(map(selector, self._source) if selector else self._source)
        total, count = 0, 0
        for val in it:
            total += val
            count += 1
        if count == 0:
            raise ValueError("Sequence contains no elements.")
        return total / count

    def aggregate(self, func: Callable[[Any, Any], Any], seed: Any = None, result_selector: Callable[[Any], Any] = lambda x: x) -> Any:
        """
        Applies an accumulator function over a sequence.

        Args:
            func: An accumulator function to be invoked on each element.
            seed: The initial accumulator value (optional).
            result_selector: A function to transform the final accumulator value into the result value (optional).

        Returns:
            The final accumulator value transformed by result_selector.
        """
        if seed is not None:
            return result_selector(reduce(func, self._source, seed))
        return result_selector(reduce(func, self._source))

    # --- Conversion ---

    def to_list(self) -> list[T]:
        """
        Creates a list from an Enumerable.

        Returns:
            A list that contains elements from the input sequence.
        """
        return list(self._source)

    def to_set(self) -> set[T]:
        """
        Creates a set from an Enumerable.

        Returns:
            A set that contains distinct elements from the input sequence.
        """
        return set(self._source)

    def to_dict(self, key_selector: Callable[[T], TKey], element_selector: Callable[[T], R] = lambda x: x) -> dict[TKey, R]:
        """
        Creates a Dictionary from an Enumerable according to specified key and element selector functions.

        Args:
            key_selector: A function to extract a key from each element.
            element_selector: A transform function to produce a result element value from each element.

        Returns:
            A Dictionary that contains keys and values.

        Raises:
            ValueError: If the key_selector produces duplicate keys for two elements.
        """
        result = {}
        for item in self._source:
            key = key_selector(item)
            if key in result:
                raise ValueError(f"An item with the same key has already been added. Key: {key}")
            result[key] = element_selector(item)
        return result

    def to_lookup(self, key_selector: Callable[[T], TKey], element_selector: Callable[[T], R] = lambda x: x) -> dict[TKey, 'Enumerable[R]']:
        """
        Creates a Dictionary where each key maps to an Enumerable of values.

        Args:
            key_selector: A function to extract a key from each element.
            element_selector: A transform function to produce a result element value from each element.

        Returns:
            A Dictionary containing keys mapped to Enumerable collections of values.
        """
        lookup = defaultdict(list)
        for item in self._source:
            lookup[key_selector(item)].append(element_selector(item))
        return {k: Enumerable(v) for k, v in lookup.items()}


class OrderedEnumerable(Enumerable[T]):
    """
    Represents a sorted sequence, providing functionality to perform subsequent ordering.
    """
    __slots__ = ('_elements', '_sort_keys')
    def __init__(self, elements: list[T], sort_keys: list[tuple[Callable[[T], Any], bool]]):
        """
        Initializes a new instance of the OrderedEnumerable class.

        Args:
            elements: The fully realized list of elements to be sorted.
            sort_keys: A list of tuples containing (key_selector_function, is_descending).
        """
        self._elements = elements
        self._sort_keys = sort_keys
        super().__init__(self._generate_sorted())

    def _generate_sorted(self):
        result = list(self._elements)
        for key_selector, is_descending in reversed(self._sort_keys):
            result.sort(key=key_selector, reverse=is_descending)
        yield from result

    def then_by(self, key_selector: Callable[[T], Any]) -> 'OrderedEnumerable[T]':
        """
        Performs a subsequent ordering of the elements in a sequence in ascending order.

        Args:
            key_selector: A function to extract a key from each element.

        Returns:
            An OrderedEnumerable whose elements are sorted according to a key.
        """
        return OrderedEnumerable(self._elements, self._sort_keys + [(key_selector, False)])

    def then_by_descending(self, key_selector: Callable[[T], Any]) -> 'OrderedEnumerable[T]':
        """
        Performs a subsequent ordering of the elements in a sequence in descending order.

        Args:
            key_selector: A function to extract a key from each element.

        Returns:
            An OrderedEnumerable whose elements are sorted in descending order according to a key.
        """
        return OrderedEnumerable(self._elements, self._sort_keys + [(key_selector, True)])


class GroupedEnumerable(Enumerable[T], Generic[TKey, T]):
    """
    Represents a collection of objects that have a common key.
    """
    __slots__ = ('_key',)
    def __init__(self, key: TKey, elements: Iterable[T]):
        """
        Initializes a new instance of the GroupedEnumerable class.

        Args:
            key: The key associated with the group.
            elements: The iterable sequence of grouped elements.
        """
        super().__init__(elements)
        self._key = key

    @property
    def key(self) -> TKey:
        """
        Gets the key of the GroupedEnumerable.
        """
        return self._key
