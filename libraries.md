# Jak si do Pythonu nainstalovat...

## ... knihovnu, o níž jste nalezli zmínku na internetu

Možná plánujete nějaký projekt, kvůli němuž potřebujete postahovat různá data z
internetu. Nechcete to dělat ručně, to by bylo hodně práce, a našli jste zmínku
o šikovné pythonovské knihovně [Scrapy](https://scrapy.org/), která masové
stahování dat z internetu ulehčuje. Jenže ouha, není na Jupyteru centrálně
nainstalovaná. To ale nevadí, můžete si ji přece nainstalovat sami!

Na [webu projektu](https://scrapy.org/) hned na první stránce naleznete pokyny
pro instalaci. Sestávají z jediného příkazu:

```sh
pip install scrapy
```

Otevřete tedy terminál, zadáte `pip install scrapy`, a vyhodí vám to chybovou
hlášku. To proto, že manažer softwarových balíčků `pip` se defaultně snaží
knihovnu nainstalovat do centrálního systémového umístění, kde jsou knihovny,
které smějí používat všichni uživatelé, ale instalovat tam smí jen
administrátor. Nicméně nezoufejme, pomocí `pip`u si každý uživatel může
nainstalovat knihovnu i do svého soukromého adresáře, stačí přidat přepínač
`--user`:

```sh
pip install --user scrapy
```

Teď už by všechno mělo proběhnout v pořádku a můžete knihovnu normálně používat
v noteboocích (přes `import scrapy`).

## ... vlastní knihovnu

Dejme tomu, že máte nějaké funkce, které používáte opakovaně, a už vás nebaví
je pořád kopírovat do každého nového notebooku, kde je chcete použít.
Nejjednodušší řešení je vytvořit si vlastní modul, kam funkce uložíte a kde je
budete centrálně spravovat a ladit. Modul pak stačí nainstalovat pomocí `pip`u,
podobně jako výše.

Každá knihovna by měla bydlet ve vlastním adresáři, a ten by měl mít minimálně
následující obsah:

```sh
libovolné_jméno_adresáře
├── libovolné_jméno_modulu.py
└── setup.py
```

Soubor `libovolné_jméno_modulu.py` obsahuje váš kód, který chcete nainstalovat
jako knihovnu a následně importovat: `import libovolné_jméno_modulu`.
`setup.py` je standardní soubor, který definuje komponenty vaší knihovny a
nějaká dodatečná metadata. Když balíčkový manažer `pip` nalezne v adresáře
soubor `setup.py`, pochopí, že se jedná o pythonovskou knihovnu, a podle
informací v tomto souboru se ji pokusí nainstalovat.

Postupujeme tedy následovně: vytvoříme si nový adresář, třeba ve svém domácím
adresáři, pojmenujeme ho např. `my_library`. V něm vytvoříme dva soubory,
`mytools.py` a `setup.py`.

Pomocí příkazové řádky by to vypadalo následovně:

```sh
# cd bez argumentu nás vrátí zpět do domácího adresáře
cd
mkdir my_library
cd my_library
touch mytools.py
touch setup.py
```

Ale můžeme tyto kroky provést i skrz klikací rozhraní Jupyteru.

Pak do oba soubory v Jupyteru otevřeme a vepíšeme do nich zamýšlený obsah.
Modul `mytools.py` bude obsahovat náš kód:

```python
def vert_sents(path):
    """Načte korpus jako seznam seznamů (= vět) ntic (= pozic)."""
    sents = []
    with open(path) as file:
        for line in file:
            line = line.strip()
            if line == "<s>":
                sent = []
            elif line == "</s>":
                sents.append(sent)
            elif "\t" in line:
                word, _, tag = line.split("\t")
                pos = tag[0]
                sent.append((word, pos))
    return sents
```

Soubor `setup.py` pak metadata potřebná k instalaci knihovny:

```python
"""Popis modulu.

Uloží se do speciální proměnné __doc__, přes níž ho pak níže můžeme
předat funkci ``setup()``.

"""
from setuptools import setup, find_packages

setup(
    # jméno knihovny může být libovolné, v praxi je ale rozumné knihovnu
    # pojmenovat stejně jako její hlavní (v našem případě jediný) modul
    # nebo package. při ``import``u pak ale vždy používáme jména modulů
    # (tj. souborů s příponou ``*.py``), ne toto jméno celé knihovny
    name="mytools",
    version="0.0.1",
    description="Různé užitečné nástroje",
    long_description=__doc__,
    # pokud má vaše knihovna nějakou webovou stránku
    url="https://github.com/dlukes/mytools",
    author="David Lukeš",
    # licence, pod níž je vaše knihovna dostupná. více informací o
    # výběru licence (a o tom, k čemu jsou licence vůbec dobré)
    # naleznete zde: <https://choosealicense.com/>
    license="GPLv3",
    install_requires=[
        # sem lze vypsat jména knihoven, na kterých je ta vaše závislá a
        # které je tudíž potřeba nainstalovat spolu s ní
        "nltk"
    ],
    # tato funkce automaticky vyhledá všechny součásti vaší knihovny a
    # postará se, aby byly správně nainstalovány
    packages=find_packages(),
    include_package_data=True,
    # u většiny jednoduchých knihoven, které si člověk píše sám, lze
    # jejich načítání trochu urychlit tím, že povolíme, aby byly na
    # disku zazipovány do jednoho archivu
    zip_safe=True
)
```

(Některé tyto údaje pochopitelně nejsou povinné, mělo by být intuitivně jasné,
které lze celkem "beztrestně" vynechat. A pokud si nejste jisti, stačí některý
z nich umazat a provést instalaci -- když to projde, vše je v pořádku :) )

Pak už stačí jen otevřít terminál a knihovnu nainstalovat pomocí `pip`u.
(Nejprve znovu samozřejmě `source /opt/miniconda3.path`.) Použijeme přepínač
`--editable`, díky němuž nemusíme po každé úpravě knihovnu znovu nainstalovat
(naše úpravy se do instalované verze promítnou automaticky). Místo pouhého
jména knihovny jako v případě `scrapy` zadáme cestu k adresáři, který knihovnu
obsahuje:

```sh
# buď plnou cestu (vlnovka ~ je zkratka do vašeho domácího adresáře, tj.
# /home/<vaše_uživatelské_jméno>)
pip install --user --editable ~/my_library
# cestu můžeme také zadat relativně k aktuálnímu adresáři, takže se taky
# můžeme přesunout do domácího adresáře (pokud tam už nejsme)
cd
# a zadat jen
pip install --user --editable my_library
# případně se přesunout rovnou do adresáře s knihovnou
cd ~/my_library
# (nebo jen cd my_library, pokud už v domácím adresáři jsme)
# a zadat jen
pip install --user --editable .
# (tečka je zkratka pro aktuální pracovní adresář, tj. adresář, v němž se
# právě nacházíme)
```

A můžete svou knihovnu vesele používat v noteboocích.

## Douška na závěr

Jak jsem říkal na hodině, při opakovaném `import`u nějaké knihovny se už Python
znovu na disk nedívá a zdrojové soubory knihovny nečte, jen si ověří, že
knihovna už byla dříve importována, a vrátí vám tu verzi, kterou už má nahranou
v paměti. Může tak vzkniknout problém, pokud v knihovně objevíte při práci s ní
nějakou chybu, upravíte ji a chcete ji importovat znovu. V takovém případě je
potřeba Python restartovat (tj. použít funkci *Restart kernel*).
