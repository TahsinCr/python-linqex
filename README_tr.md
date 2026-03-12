[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

[Türkçe][lang-tr-url] | [English][lang-en-url]

<div align="center">

<h3 align="center">Python PyLINQ (linqex)</h3>

<p align="center">

Ertelenmiş Çalıştırma (Deferred Execution) Destekli, Yüksek Performanslı ve Üretime Hazır Bir Python C# LINQ Uyarlaması.

[Changelog][changelog-url] · [Report Bug][issues-url] · [Request Feature][issues-url]
 
</p>

</div>

<br/>

## 📋 Proje Hakkında

### 🚀 Neden PyLINQ?

Python'da veri manipülasyonu genellikle son derece iç içe geçmiş list comprehensions yapılarına, okunması zor fonksiyonel zincirlere (`map`, `filter`, `reduce`) veya büyük veri akışlarını işlerken gereksiz bellek (RAM) tüketimine yol açar. 

`linqex`, **C# LINQ (Language Integrated Query)** mimarisinin zarafetini ve gücünü doğrudan Python ekosistemine getirir. Mutlak tip güvenliğini ve olağanüstü çalışma hızlarını korurken, akıcı ve bildirimsel (declarative) bir sözdizimi kullanarak yinelenebilir (iterable) veri dizilerini sorgulamanıza, dönüştürmenize ve manipüle etmenize olanak tanır.

### 🚀 Ertelenmiş Çalıştırmanın (Tembel Değerlendirme) Gücü

Standart Python list comprehensions yapıları, tüm sonuç kümesini tek seferde bellekte hesaplar. Eğer 10 GB'lık bir log dosyasından sadece eşleşen ilk 3 elemana ihtiyacınız varsa, tüm dosyayı belleğe yüklemek bir felakettir. 

`linqex`, yerleşik Python `yield` üreticilerini (generators) ve C tabanlı `itertools` kütüphanesini kullanan **saf bir tembel değerlendirme (lazy-evaluation) mimarisi** üzerine inşa edilmiştir. Tanımladığınız veri hattı (örn: `.where().select().order_by()`), `.to_list()`, `.first()` veya `.count()` gibi sonlandırıcı (terminal) bir işlem çağrılana kadar **asla çalıştırılmaz**. Bu durum, **$O(1)$ bellek ayak izi** ile sonuçlanarak devasa veri setlerini sorunsuzca işleme yeteneğinin kilidini açar.

### ✨ Temel Özellikler

* **%100 C# LINQ Eşlenikliği:** Modern eklentiler olan `.chunk()`, `.max_by()` ve `.distinct_by()` dahil olmak üzere .NET 8'deki neredeyse tüm LINQ operatörlerini destekler.
* **Ertelenmiş Çalıştırma (Deferred Execution):** İstediğiniz kadar işlemi zincirleyin. Motor yalnızca tam olarak neye ihtiyacı varsa, tam olarak ihtiyaç duyduğu anda onu hesaplar.
* **Pythonic Hızlı Yollar (Fast-Paths):** Bellekte tutulan bir dizi (`list` veya `tuple` gibi) aktarırsanız, `.count()`, `.element_at()` ve `.reverse()` gibi metotlar $O(N)$ döngülerini atlar ve Python'ın `__len__` ile `__getitem__` özelliklerinden faydalanarak **O(1) sabit sürede** anında çalışır.
* **Sıfır Ek Bellek Tüketimi (Zero Overhead):** Tüm sınıflarda katı bir şekilde `__slots__` kullanır. Bu sayede dinamik sözlük (dictionary) tahsislerini ortadan kaldırır ve milyonlarca grup veya sıralanmış durum yaratıldığında bile bellek kullanımını jilet inceliğinde tutar.
* **Sıkı Hata Fırlatma Eşlenikliği:** C#'ın sağlam istisna (exception) davranışını kopyalar. Örneğin, `.single()` işlemi tekrarlanan elemanlarda hata fırlatır ve `.to_dict()` sessiz anahtar (key) üzerine yazılmalarına karşı şiddetle koruma sağlayarak veri bütünlüğünü garanti eder.
* **Mutlak Tip Güvenliği:** Python `typing` jenerikleri (`Generic[T]`, `TypeVar`) ile titizlikle etiketlenmiştir. Kusursuz IDE otomatik tamamlama (VS Code, PyCharm) sağlar ve `mypy` gibi statik analiz araçlarını tam olarak destekler.
* **Kararlı Çok Seviyeli Sıralama:** Python'ın ışık hızındaki Timsort algoritmasını doğal olarak kullanarak, ana kaynağı baştan değerlendirmeden `.order_by().then_by_descending()` zincirlemelerini destekler.

<br/>

## ⚙️ Mimari Notlar

Geliştiricilerin bu kütüphaneyi kullanırken bilmesi gereken mühendislik gerçekleri:

1. **Üretici (Generator) Tükenmesi Gerçeği:**
Python üreticileri yalnızca bir kez okunabilir. Eğer `Enumerable` içine bir üretici ifadesi `(x for x in ...)` verir ve `.count()` gibi sonlandırıcı bir işlem çağırırsanız, üretici tükenir. Ardından yapılacak bir `.to_list()` çağrısı boş bir dizi döndürecektir. Aynı kaynak üzerinde birden fazla sonlandırıcı işlem yapmak istiyorsanız, motora bellekte tutulan bir koleksiyon (örn: `list`) verdiğinizden emin olun veya önce açıkça `.to_list()` çağrısı yapın.
2. **Sonlandırıcı (Terminal) vs. Ara (Intermediate) İşlemler:**
`where`, `select` ve `skip` gibi metotlar *Ara İşlemlerdir* (yeni bir Enumerable döndürürler ve hiçbir iş yapmazlar). `to_list`, `count`, `sum` ve `first` gibi metotlar ise *Sonlandırıcı İşlemlerdir* (veri hattının değerlendirilmesini tetiklerler).
3. **Lookup vs. Dictionary:**
LINQ'te `Dictionary` (Sözlük) bir anahtarı tek bir değere eşlerken, `Lookup` bir anahtarı değerler *koleksiyonuna* eşler. `linqex` bu kurala kesinlikle uyar. Ayrıca, `.to_lookup()` sonucundan var olmayan bir anahtarı istemek `KeyError` fırlatmak yerine boş bir `Enumerable` döndürür, bu da gruplanmış verilere erişimi inanılmaz derecede güvenli hale getirir.

<br/>

## 🚀 Başlangıç

### 🛠️ Bağımlılıklar

* Dış bağımlılığı yoktur.
* Yalnızca Python Standart Kütüphanesi (`itertools`, `collections`, `functools`, `typing`).
* Python 3.9+ ile tam uyumludur.

### 📦 Kurulum

Kütüphanenin dış bağımlılığı yoktur ve doğrudan Python'ın çekirdek araç setiyle çalışır.

1. Depoyu (repository) klonlayın
    ```sh
    git clone https://github.com/TahsinCr/python-linqex.git
    ```

2. PIP ile kurun
    ```sh
    pip install linqex
    ```

<br/>

### 💻 Kullanım Örnekleri

#### 1. Standart Veri Dönüştürme ve Filtreleme

İç içe comprehensions kullanmadan verileri temiz bir şekilde filtreleyin, sıralayın ve yansıtın.

```python
from linqex import Enumerable

data = [
    {"name": "Alice", "age": 28, "role": "Dev"},
    {"name": "Bob", "age": 35, "role": "HR"},
    {"name": "Charlie", "age": 42, "role": "Dev"},
    {"name": "Dave", "age": 22, "role": "Dev"}
]

# Veri hattı tembeldir (lazy). Henüz hiçbir döngü çalışmaz.
devs = (Enumerable(data)
    .where(lambda x: x["role"] == "Dev")
    .where(lambda x: x["age"] > 25)
    .order_by_descending(lambda x: x["age"])
    .select(lambda x: x["name"]))

# Sonlandırıcı işlem veri hattını çalıştırır
print(devs.to_list()) 
# Çıktı: ['Charlie', 'Alice']

```

#### 2. Toplamalar ve Hızlı Yollar (Fast-Paths)

Belirli bir özelliğe göre maksimum elemanı bulma, C#'taki `.MaxBy()` metoduna benzer.

```python
from linqex import Enumerable

inventory = [
    {"id": 1, "product": "Laptop", "price": 1200},
    {"id": 2, "product": "Mouse", "price": 45},
    {"id": 3, "product": "Monitor", "price": 300}
]

stream = Enumerable(inventory)

# En pahalı ürünün asıl sözlük (dictionary) objesini bulur
most_expensive = stream.max_by(lambda x: x["price"])
print(most_expensive["product"]) # Çıktı: Laptop

# Kaynak bir Liste olduğu için O(1) hızında Fast-Path count işlemi
total_items = stream.count() 

```

#### 3. Devasa Veri Bölümleme (Bellek Güvenli)

RAM'i şişirmeden, veritabanına toplu ekleme (batch insert) yapmak için milyonlarca kaydı parçalar (chunk) halinde işleyin.

```python
from linqex import Enumerable

def massive_database_stream():
    for i in range(1, 1000000):
        yield {"id": i, "status": "pending"}

stream = Enumerable(massive_database_stream())

# Verileri tembel (lazy) bir şekilde 500'er öğelik listeler halinde gruplar
batches = stream.chunk(500)

for batch in batches.take(3): # Sadece ilk 3 parçayı işler
    print(f"{len(batch)} eleman için SQL toplu ekleme işlemi çalıştırılıyor...")

```

#### 4. Gruplama ve Analitik (group_by)

Verileri belirli bir anahtara göre kolayca gruplayın ve alt gruplar üzerinde toplu hesaplamalar (aggregate) yapın.

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

#### 5. Bellek İçi İlişkisel Birleştirmeler (Inner Joins)

Farklı iki veri kaynağını güvenli ve yüksek performanslı bir şekilde birleştirin.

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

## 🤝 Katkıda Bulunma

Açık kaynak topluluğu, yüksek performanslı kütüphanelerin sınırlarını zorlamak için mükemmel bir yerdir. `linqex`'i daha hızlı, daha güvenli veya daha yetenekli hale getirmek için yapacağınız her türlü katkı büyük bir minnetle karşılanacaktır!

Özellikle aşağıdaki alanlardaki katkılarınızı dört gözle bekliyoruz:

* ⚡ **Algoritmik Optimizasyonlar:** Belirli veri tipleri için yeni Fast-Path atlamaları.
* 🏗️ **Yeni Operatörler:** Niş LINQ operatörleri ile API'yi genişletme.
* 🐛 **Uç Durum Testleri (Edge-Case Testing):** Zaten kapsamlı olan birim test paketini daha da genişletme.

Harika bir fikriniz veya çözümünüz varsa, lütfen bir **Pull Request (PR)** oluşturmak için aşağıdaki adımları izleyin. Ayrıca yeni bir özellik önermek için "enhancement" etiketiyle bir Issue açabilirsiniz.

Eğer faydalı bulduysanız projeye sağ üstten bir **Yıldız (⭐)** vermeyi unutmayın. Desteğiniz için teşekkürler!

### 🛠️ Katkıda Bulunma Adımları

1. Projeyi kendi hesabınıza **Fork**'layın.
2. Özellik (Feature) Dalınızı (Branch) oluşturun:

```sh
git checkout -b feature/AmazingFeature

```

3. Değişikliklerinizi **Commit**'leyin (Açıklayıcı mesajlar kullandığınızdan emin olun):

```sh
git commit -m 'feat: Tuple değerlendirmeleri için yeni bir Fast-Path eklendi'

```

4. Dalınıza **Push** yapın:

```sh
git push origin feature/AmazingFeature

```

5. Bu depo (repository) üzerinde bir **Pull Request** açın.

> ⚠️ **Önemli Geliştirici Notu:** `linqex` mimarisi büyük ölçüde üreticilere (generators) ve iteratör mantığına dayanır. Bir PR açmadan önce, lütfen **%100 Kod Kapsamının (Code Coverage)** korunduğundan ve kodunuzun **Python 3.9+** standartlarıyla uyumlu olduğundan emin olmak için tüm birim test (unit test) paketini çalıştırın.

## 🙏 Teşekkürler ve Lisans

Bu proje tamamen **MIT Lisansı** altında açık kaynaklıdır ([Lisans](https://www.google.com/search?q=https://github.com/TahsinCr/python-linqex/blob/main/LICENSE)).

* **PyPI:** [PyPI'da linqex](https://www.google.com/search?q=https://pypi.org/project/linqex)
* **Kaynak Kod:** [Tahsincr/python-linqex](https://www.google.com/search?q=https://github.com/TahsinCr/python-linqex)

Herhangi bir hata bulursanız veya mimari bir katkıda bulunmak isterseniz, GitHub üzerinden bir Issue açmaktan veya Pull Request göndermekten çekinmeyin!

## 📫 İletişim

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
