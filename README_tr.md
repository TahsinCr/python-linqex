<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<a href="https://github.com/TahsinCr/python-linqex/blob/master/README_tr.md">
 <img src="images/languages/turkish-flag.png" height="28" alt="Logo" ></a>
<a href="https://github.com/TahsinCr/python-linqex/blob/master/README.md">
 <img src="images/languages/british-flag.png" height="28" alt="Logo" ></a>

<br />






<!-- About -->
<div align="center">

<a href="https://github.com/TahsinCr/python-linqex">

<img src="images/logo.png" alt="Logo">

</a>

<h3 align="center">Python Linqex</h3>

<p align="center">

C#'daki linq modülü, bazı değişikliklerle python için uyarlanmıştır.

<a href="https://github.com/TahsinCr/python-linqex/blob/master/CHANGELOG.md">Changelog</a>
 · 
<a href="https://github.com/TahsinCr/python-linqex/issues">Report Bug</a>
 · 
<a href="https://github.com/TahsinCr/python-linqex/issues">Request Feature</a>
 
</p>

</div>






<!-- TABLE OF CONTENTS -->

<details>

<summary>İçindekiler</summary>

<ol>

<li>

<a href="#about-the-project">Proje hakkında</a>

<ul>

<li><a href="#built-with">İle İnşa Edildi</a></li>

</ul>

</li>

<li>

<a href="#getting-started">Başlarken</a>

<ul>

<li><a href="#prerequisites">Önkoşullar</a></li>

<li><a href="#installation">Kurulum</a></li>

</ul>

</li>

<li><a href="#usage">Kullanım</a></li>

<li><a href="#roadmap">Yol haritası</a></li>

<li><a href="#contributing">Katkı</a></li>

<li><a href="#license">Lisans</a></li>

<li><a href="#contact">İletişim</a></li>

<li><a href="#acknowledgments">Teşekkürler</a></li>

</ol>

</details>






<!-- ABOUT THE PROJECT -->

##  Proje hakkında

Python 3.x'e kullanımı kolay LINQ özellikleri sağlar.

<p align="right">(<a href="#readme-top">başa geri dön</a>)</p>

###  İle İnşa Edildi

* [![Python][Python]][Python-url]

<p align="right">(<a href="#readme-top">başa geri dön</a>)</p>






<!-- GETTING STARTED -->

##  Başlarken

Yerel bir kopyayı çalışır duruma getirmek için bu basit örnek adımları izleyin.

###  Önkoşullar

Herhangi bir ön koşul gerektirmez

###  Kurulum

1. Depoyu klonla
```sh
git clone https://github.com/TahsinCr/python-linqex.git
```

2. PIP paketlerini kurun
```sh
pip install linqex
```

<p align="right">(<a href="#readme-top">başa geri dön</a>)</p>






<!-- USAGE EXAMPLES -->

##  Kullanım

Elimizde Farklı müşterilerimiz olsun. Bu müşteriler arasından erkek olanları seçelim. Bunun için:
```python
from linqex.linq import Enumerable
customersList = [
    {'name' : 'Jonh', 'age' : 25, 'gender': 'male'},
    {'name' : 'Emma', 'age' : 44, 'gender': 'female'},
    {'name' : 'Steve', 'age' : 17, 'gender': 'male'}
]

customersEnumerable = Enumerable(customersList)

# to select only male ones:
customersMaleEnumerable = customersEnumerable.Where(lambda key, value: value['gender'] == 'male')

for customer in customersMaleEnumerable.ToList:
    print(customer)

```
Çıktı
```
{'name' : 'Jonh', 'age' : 25, 'gender': 'male'}
{'name' : 'Steve', 'age' : 17, 'gender': 'male'}
```

<br>

Yukarıda yazdığımız örneği biraz daha geliştirelim:
```python
from typing import Literal
from linqex.linq import Enumerable

MALE = "MALE"
FEMALE = "FEMALE"

class Customer:
    def __init__(self, id:int, name:str, age:int, gender:Literal["MALE","FEMALE"]):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender


customerList = [
    Customer(1, "Ava", 32, MALE),
    Customer(2, "Alex", 19, MALE),
    Customer(3, "Amelia", 22, FEMALE),
    Customer(4, "Arnold", 43, MALE),
    Customer(5, "Eric", 55, MALE),
    Customer(6, "Lily", 12, FEMALE),
    Customer(7, "Jessia", 32, MALE),
    Customer(8, "William", 19, MALE),
    Customer(9, "Emily", 22, FEMALE),
    Customer(10, "Mateo", 43, MALE),
    Customer(11, "Antony", 55, MALE),
    Customer(12, "Mia", 12, FEMALE)
]

customerEnumerable = Enumerable.List(customerList)

# to select only male ones:
customersMaleEnumerable = customerEnumerable.Where(lambda customer: customer.gender == MALE)

for customer in customersMaleEnumerable.ToList:
    print(customer.__dict__)

```
Çıktı
```
{'id': 1, 'name': 'Ava', 'age': 32, 'gender': 'MALE'}
{'id': 2, 'name': 'Alex', 'age': 19, 'gender': 'MALE'}
{'id': 4, 'name': 'Arnold', 'age': 43, 'gender': 'MALE'}
{'id': 5, 'name': 'Eric', 'age': 55, 'gender': 'MALE'}
{'id': 7, 'name': 'Jessia', 'age': 32, 'gender': 'MALE'}
{'id': 8, 'name': 'William', 'age': 19, 'gender': 'MALE'}
{'id': 10, 'name': 'Mateo', 'age': 43, 'gender': 'MALE'}
{'id': 11, 'name': 'Antony', 'age': 55, 'gender': 'MALE'}
```

_Daha fazla örnek için lütfen [belgelere](https://github.com/TahsinCr/python-linqex/wiki) bakın_

<p align="right">(<a href="#readme-top">başa geri dön</a>)</p>






<!-- ROADMAP -->

##  Yol haritası

- [x] Değişiklik Günlüğü Ekle

- [x] Test Dosyası Ekle

- [x] Hataları Düzelt

- [ ] Dökümanlar Ekle

- [ ] Örneklerle Ek Şablonlar Ekle

Önerilen özelliklerin (ve bilinen sorunların) tam listesi için [açık sorunlara](https://github.com/TahsinCr/python-linqex/issues) bakın.

<p align="right">(<a href="#readme-top">başa geri dön</a>)</p>






<!-- CONTRIBUTING -->

##  Katıkı

Katkılar, açık kaynak topluluğunu öğrenmek, ilham vermek ve yaratmak için harika bir yer yapan şeydir. Yaptığınız tüm katkılar **çok makbule geçer**.

Bunu daha iyi hale getirecek bir öneriniz varsa, lütfen repoyu çatallayın ve bir çekme isteği oluşturun. Ayrıca "geliştirme" etiketiyle bir sorun açabilirsiniz.

Projeye yıldız vermeyi unutmayın! Tekrar teşekkürler!

1. Projeyi çatallayın

2. Özellik Dalınızı oluşturun (`git checkout -b feature/AmazingFeature`)

3. Değişikliklerinizi taahhüt edin (`git commit -m 'Add some AmazingFeature'`)

4. Şubeye Gönderin (`git push origin feature/AmazingFeature`)

5. Bir Çekme İsteği Açın

<p align="right">(<a href="#readme-top">başa geri dön</a>)</p>






<!-- LICENSE -->

##  Lisans

MIT Lisansı altında dağıtılmaktadır. Daha fazla bilgi için "LICENSE.txt" konusuna bakın.

<p align="right">(<a href="#readme-top">başa geri dön</a>)</p>






<!-- CONTACT -->

##  İletişim

Tahsin Çirkin - [@TahsinCrs](https://twitter.com/TahsinCrs) - TahsinCr@outlook.com

Proje Link: [https://github.com/TahsinCr/python-linqex](https://github.com/TahsinCr/python-linqex)

<p align="right">(<a href="#readme-top">başa geri dön</a>)</p>






<!-- ACKNOWLEDGMENTS -->

##  Teşekkürler

* [PyPI](https://pypi.org/project/linqex)

* [C-Sharp Linq Dökümanlar](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/linq/)

<p align="right">(<a href="#readme-top">başa geri dön</a>)</p>






<!-- LINKS & IMAGES URL -->

[contributors-shield]: https://img.shields.io/github/contributors/TahsinCr/python-linqex.svg?style=for-the-badge

[contributors-url]: https://github.com/TahsinCr/python-linqex/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/TahsinCr/python-linqex.svg?style=for-the-badge

[forks-url]: https://github.com/TahsinCr/python-linqex/network/members

[stars-shield]: https://img.shields.io/github/stars/TahsinCr/python-linqex.svg?style=for-the-badge

[stars-url]: https://github.com/TahsinCr/python-linqex/stargazers

[issues-shield]: https://img.shields.io/github/issues/TahsinCr/python-linqex.svg?style=for-the-badge

[issues-url]: https://github.com/TahsinCr/python-linqex/issues

[license-shield]: https://img.shields.io/github/license/TahsinCr/python-linqex.svg?style=for-the-badge

[license-url]: https://img.shields.io/github/forks/TahsinCr/python-linqex?style=flat-square

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555

[linkedin-url]: https://linkedin.com/in/TahsinCr

[Python]: https://img.shields.io/pypi/pyversions/linqex?style=flat-square

[Python-url]: https://pypi.org/project/linqex