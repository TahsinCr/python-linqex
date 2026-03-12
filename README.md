[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

[English][lang-en-url] | [Türkçe][lang-tr-url]

<div align="center">

<h3 align="center">Python PyLINQ (linqex)</h3>

<p align="center">

A High-Performance, Production-Ready Python Implementation of C# LINQ with Deferred Execution.

[Changelog][changelog-url] · [Report Bug][issues-url] · [Request Feature][issues-url]
 
</p>

</div>

<br/>

## 📋 About the Project

### 🚀 Why PyLINQ?

Data manipulation in Python often leads to highly nested comprehensions, unreadable functional chains (`map`, `filter`, `reduce`), or unnecessary memory overhead when processing large data streams. 

`linqex` brings the elegance and power of **C# LINQ (Language Integrated Query)** directly into the Python ecosystem. It allows you to query, transform, and manipulate iterable sequences using a fluent, declarative syntax while maintaining absolute type safety and phenomenal execution speeds.

### 🚀 The Power of Deferred Execution (Lazy Evaluation)

Standard Python list comprehensions compute the entire result set in memory at once. If you only need the first 3 matching elements from a 10 GB log file, loading it all into memory is disastrous. 

`linqex` is built on a **pure lazy-evaluation architecture** using native Python `yield` generators and the C-based `itertools` library. The data pipeline you define (e.g., `.where().select().order_by()`) is **never executed** until a terminal operation like `.to_list()`, `.first()`, or `.count()` is invoked. This results in an **$O(1)$ memory footprint**, unlocking the ability to process massive datasets seamlessly.

### ✨ Key Features

* **100% C# LINQ Parity:** Supports almost all LINQ operators from .NET 8, including modern additions like `.chunk()`, `.max_by()`, and `.distinct_by()`.
* **Deferred Execution:** Chain as many operations as you want. The engine only computes exactly what it needs, exactly when it needs it.
* **Pythonic Fast-Paths:** If you pass an in-memory sequence (like a `list` or `tuple`), methods like `.count()`, `.element_at()`, and `.reverse()` bypass O(N) iterations and execute instantly in **O(1) constant time** leveraging Python's `__len__` and `__getitem__`.
* **Zero Overhead Memory:** Utilizes strict `__slots__` across all classes, eliminating dynamic dictionary allocations and keeping memory usage razor-thin even when spawning millions of groups or ordered states.
* **Strict Exception Parity:** Replicates C#'s robust exception behavior. Operations like `.single()` throw exceptions on duplicates, and `.to_dict()` fiercely guards against silent key overwrites, ensuring data integrity.
* **Absolute Type Safety:** Meticulously annotated with Python `typing` generics (`Generic[T]`, `TypeVar`). It provides flawless IDE autocomplete (VS Code, PyCharm) and fully supports static analyzers like `mypy`.
* **Stable Multi-Level Sorting:** Offers `.order_by().then_by_descending()` chaining without re-evaluating the source, natively leveraging Python's lightning-fast Timsort algorithm.

<br/>

## ⚙️ Architectural Notes

Engineering facts developers need to know when using this library:

1. **The Generator Exhaustion Reality:**
Python generators can only be traversed once. If you pass a generator expression `(x for x in ...)` into `Enumerable` and execute a terminal operation like `.count()`, the generator is consumed. A subsequent `.to_list()` will return an empty array. To perform multiple terminal operations, ensure you pass an in-memory collection (like a `list`) to the engine or explicitly call `.to_list()` first.
2. **Terminal vs. Intermediate Operations:**
Methods like `where`, `select`, and `skip` are *Intermediate* (they return a new Enumerable and do no work). Methods like `to_list`, `count`, `sum`, and `first` are *Terminal* (they force the evaluation of the pipeline).
3. **Lookup vs. Dictionary:**
In LINQ, a `Dictionary` maps one key to one value, while a `Lookup` maps one key to a *collection* of values. `linqex` strictly follows this. Furthermore, requesting a non-existent key from a `.to_lookup()` result returns an empty `Enumerable` instead of throwing a `KeyError`, making grouped data access incredibly safe.

<br/>

## 🚀 Getting Started

### 🛠️ Dependencies

* No external dependencies.
* Only Python Standard Library (`itertools`, `collections`, `functools`, `typing`).
* Fully compatible with Python 3.9+.

### 📦 Installation

The library has zero external dependencies and works natively with Python's core toolkit.

1. Clone the repository
    ```sh
    git clone https://github.com/TahsinCr/python-linqex.git
    ```

2. Install via PIP
    ```sh
    pip install linqex
    ```

<br/>

### 💻 Usage Examples

#### 1. Standard Data Transformation & Filtering

Cleanly filter, sort, and project data without nested comprehensions.

```python
from linqex import Enumerable

data = [
    {"name": "Alice", "age": 28, "role": "Dev"},
    {"name": "Bob", "age": 35, "role": "HR"},
    {"name": "Charlie", "age": 42, "role": "Dev"},
    {"name": "Dave", "age": 22, "role": "Dev"}
]

# Pipeline is lazy. No iteration happens yet.
devs = (Enumerable(data)
    .where(lambda x: x["role"] == "Dev")
    .where(lambda x: x["age"] > 25)
    .order_by_descending(lambda x: x["age"])
    .select(lambda x: x["name"]))

# Terminal operation executes the pipeline
print(devs.to_list()) 
# Output: ['Charlie', 'Alice']

```

#### 2. Aggregations and Fast-Paths

Finding the maximum element based on a specific property, similar to `.MaxBy()` in C#.

```python
from linqex import Enumerable

inventory = [
    {"id": 1, "product": "Laptop", "price": 1200},
    {"id": 2, "product": "Mouse", "price": 45},
    {"id": 3, "product": "Monitor", "price": 300}
]

stream = Enumerable(inventory)

# Finds the actual dictionary object of the most expensive item
most_expensive = stream.max_by(lambda x: x["price"])
print(most_expensive["product"]) # Output: Laptop

# O(1) Fast-path count execution since the source is a List
total_items = stream.count() 

```

#### 3. Massive Data Chunking (Memory Safe)

Process millions of records in chunks for database batch inserts without blowing up the RAM.

```python
from linqex import Enumerable

def massive_database_stream():
    for i in range(1, 1000000):
        yield {"id": i, "status": "pending"}

stream = Enumerable(massive_database_stream())

# Groups data into lists of 500 items lazily
batches = stream.chunk(500)

for batch in batches.take(3): # Only process the first 3 batches
    print(f"Executing SQL bulk insert for {len(batch)} items...")

```

#### 4. Grouping & Analytics (group_by)

Easily group data by a specific key and perform aggregate calculations on the sub-groups.

```python
from linqex import Enumerable

orders = [
    {"customer": "C1", "amount": 100},
    {"customer": "C2", "amount": 50},
    {"customer": "C1", "amount": 200},
    {"customer": "C3", "amount": 300}
]

report = (Enumerable(orders)
    .group_by(lambda o: o["customer"])
    .select(lambda group: {
        "customer": group.key,
        "total_spent": group.sum(lambda x: x["amount"]),
        "order_count": group.count()
    })
    .to_list())

# [{'customer': 'C1', 'total_spent': 300, 'order_count': 2}, ...]

```

#### 5. Relational Inner Joins in Memory

Merge two disparate data sources safely and efficiently.

```python
from linqex import Enumerable

employees = [{"id": 1, "name": "Alice", "dept_id": 10}, {"id": 2, "name": "Bob", "dept_id": 20}]
departments = [{"id": 10, "name": "Engineering"}, {"id": 20, "name": "Sales"}]

joined_data = Enumerable(employees).join(
    inner=departments,
    outer_key=lambda e: e["dept_id"],
    inner_key=lambda d: d["id"],
    selector=lambda e, d: f"{e['name']} works in {d['name']}"
).to_list()

# ['Alice works in Engineering', 'Bob works in Sales']

```

## 🤝 Contributing

The open-source community is the perfect place to push the boundaries of high-performance libraries. Any contributions you make to render `linqex` faster, safer, or more capable are greatly appreciated!

We are especially looking forward to your contributions in the following areas:

* ⚡ **Algorithmic Optimizations:** New Fast-Path bypasses for specific data types.
* 🏗️ **New Operators:** Expanding the API with niche LINQ operators.
* 🐛 **Edge-Case Testing:** Expanding the already comprehensive unit test suite.

If you have a great idea or solution, please follow the steps below to create a **Pull Request (PR)**. You can also open an Issue with the "enhancement" tag to suggest a new feature.

Don't forget to give the project a **Star (⭐)** on the top right if you found it useful. Thanks for your support!

### 🛠️ Contribution Steps

1. **Fork** the project to your own account.
2. Create your Feature Branch:

```sh
git checkout -b feature/AmazingFeature

```

3. **Commit** your changes (Make sure to use descriptive messages):

```sh
git commit -m 'feat: Added a new Fast-Path for Tuple evaluations'

```

4. **Push** to the Branch:

```sh
git push origin feature/AmazingFeature

```

5. Open a **Pull Request** on this repository.

> ⚠️ **Important Developer Note:** The `linqex` architecture relies heavily on generators and iterator logic. Before opening a PR, please run the full unit test suite to ensure **100% Code Coverage** is maintained and your code complies with **Python 3.9+** standards.

## 🙏 Acknowledgments and License

This project is fully open-source under the **MIT License** ([License](https://www.google.com/search?q=https://github.com/TahsinCr/python-linqex/blob/main/LICENSE)).

* **PyPI:** [linqex on PyPI](https://www.google.com/search?q=https://pypi.org/project/linqex)
* **Source Code:** [Tahsincr/python-linqex](https://www.google.com/search?q=https://github.com/TahsinCr/python-linqex)

If you find any bugs or want to make an architectural contribution, feel free to open an Issue or submit a Pull Request on GitHub!

## 📫 Contact

X: [@TahsinCrs](https://twitter.com/TahsinCrs)

Linkedin: [@TahsinCr](https://linkedin.com/in/TahsinCr)

Email: TahsinCrs@gmail.com

<!-- IMAGES URL -->

[contributors-shield]: https://img.shields.io/github/contributors/TahsinCr/python-linqex.svg?style=for-the-badge

[forks-shield]: https://img.shields.io/github/forks/TahsinCr/python-linqex.svg?style=for-the-badge

[stars-shield]: https://img.shields.io/github/stars/TahsinCr/python-linqex.svg?style=for-the-badge

[issues-shield]: https://img.shields.io/github/issues/TahsinCr/python-linqex.svg?style=for-the-badge

[license-shield]: https://img.shields.io/github/license/TahsinCr/python-linqex.svg?style=for-the-badge

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555



<!-- Github Project URL -->

[project-url]: https://github.com/TahsinCr/python-linqex

[pypi-project-url]: https://pypi.org/project/rwlocker

[contributors-url]: https://github.com/TahsinCr/python-linqex/graphs/contributors

[stars-url]: https://github.com/TahsinCr/python-linqex/stargazers

[forks-url]: https://github.com/TahsinCr/python-linqex/network/members

[issues-url]: https://github.com/TahsinCr/python-linqex/issues

[examples-url]: https://github.com/TahsinCr/python-linqex/wiki

[license-url]: https://github.com/TahsinCr/python-linqex/blob/main/LICENSE

[changelog-url]:https://github.com/TahsinCr/python-linqex/blob/main/CHANGELOG.md



<!-- Contacts URL -->

[linkedin-url]: https://linkedin.com/in/TahsinCr

[x-url]: https://twitter.com/TahsinCrs



<!-- File URL -->

[lang-tr-url]: https://github.com/TahsinCr/python-linqex/blob/main/README_tr.md

[lang-en-url]: https://github.com/TahsinCr/python-linqex/blob/main/README.md
