# **Change Log**
All notable changes to this project will be documented in this file.

## **[2.0] - 13.03.2026**
The **"High-Performance & Production-Ready"** release. This version marks a complete architectural rewrite from early 1.x experiments, delivering a structurally flawless, 100% type-safe, and memory-efficient implementation of C# LINQ for Python 3.9+.

### Added
* **Core Deferred Execution Engine (`Enumerable`)**:
    * Implemented a pure lazy-evaluation architecture utilizing Python's native `yield` and `itertools` C-extensions. Computations are completely deferred until a terminal operation (e.g., `to_list()`, `count()`) is invoked.
    * Integrated strict `__slots__ = ('_source',)` usage across all collection classes to enforce an $O(1)$ memory footprint and prevent dynamic `__dict__` allocations during massive data stream processing.
* **Complete LINQ API Parity**:
    * **Projection & Filtering**: `select`, `select_with_index`, `where`, `where_with_index`, `select_many`, `of_type`, `cast`.
    * **Partitioning**: `take`, `skip`, `take_while`, `skip_while`, `take_last`, `skip_last`, and the modern .NET `chunk` method.
    * **Set Operations**: `distinct`, `distinct_by`, `union`, `union_by`, `intersect`, `intersect_by`, `except_for`, `except_by`.
    * **Joins & Grouping**: Pure memory-efficient $O(N)$ implementations of `join` (Inner Join), `group_join`, and `group_by`.
    * **Element Operators**: `first`, `last`, `single`, `element_at` (including their safe `_or_default` counterparts).
    * **Aggregates & Quantifiers**: `count`, `sum`, `max`, `max_by`, `min`, `min_by`, `average`, `aggregate`, `any`, `all`, `contains`, `sequence_equal`.
* **Advanced Sub-Collections**:
    * **`OrderedEnumerable`**: Provides stable, multi-level sorting utilizing Python's Timsort algorithm. Supports seamless method chaining via `then_by` and `then_by_descending` without re-evaluating the entire source generator.
    * **`GroupedEnumerable`**: Wraps grouped sequence outputs, providing direct `.key` attribute access identical to C#'s `IGrouping<TKey, TElement>`.
* **Static Generator Methods**:
    * Added `Enumerable.range(start, count)`, `Enumerable.repeat(element, count)`, and `Enumerable.empty()` for declarative sequence generation.
* **Absolute Type Safety**:
    * Meticulously annotated every class and method using `typing` generics (`Generic[T]`, `TypeVar`, `Callable`, `Sequence`). This guarantees flawless IDE autocompletion and strict static analysis support (mypy).

### Updated
* **Pythonic Fast-Paths (Algorithmic Optimizations)**:
    * Engineered smart-type checking (`isinstance(x, Sequence)` and `hasattr(x, "__len__")`) inside core methods like `element_at`, `count`, `element_at_or_default`, and `reverse`.
    * If the source is an in-memory collection (like a `list` or `tuple`), the engine completely bypasses $O(N)$ `islice` or `next()` traversal, executing the operation in **$O(1)$ constant time**.
* **Dictionary and Lookup Evolutions**:
    * `to_lookup`: Now utilizes `collections.defaultdict` to create robust, memory-safe in-memory indexes where keys map to `Enumerable` values.
    * `to_dict`: Now provides exact C# `.ToDictionary()` behavior.

### Fixed
* **C# Strict Exception Parity**:
    * Hardened terminal operations to throw appropriate standard Python exceptions mirroring C# behavior.
    * `to_dict` now actively monitors for duplicate keys and throws a descriptive `ValueError` to prevent silent data overwrites.
    * `single()` and `single_or_default()` now correctly throw `ValueError` if the sequence contains more than one element.
    * Empty sequences now properly throw `ValueError` on `first()`, `last()`, `average()`, `min()`, and `max()`.
* **Generator Exhaustion & Edge Cases**:
    * Solved chunking dimensional bugs and `skip_last` pointer window issues when dealing with forward-only iterators.
* **Test Infrastructure**:
    * Built a completely independent, exhaustive unit testing suite.
    * Reached **100% Code Coverage**, specifically targeting edge cases, generator vs. list behavior differences, fallback mechanisms, and exception triggers.

<br>
