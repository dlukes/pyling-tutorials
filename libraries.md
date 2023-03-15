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

## ... vlastní modul (knihovnu)

Dejme tomu, že máte nějaké funkce, které používáte opakovaně, a už vás nebaví
je pořád kopírovat do každého nového notebooku, kde je chcete použít. V takovém
případě si můžete vytvořit vlastní modul (= normální textový soubor s příponou
`.py`, obsahující kód v Pythonu), kam funkce uložíte a kde je budete centrálně
spravovat a ladit.

Nejjednodušší řešení je vytvořit modul v tom samém adresáři, kde jsou i skripty
nebo notebooky, které jej využívají. Pak není třeba další konfigurace, všechno
funguje samo, můžete modul importovat jako kterýkoli jiný. Jinými slovy,
máme-li následující adresářovou strukturu...

```
moje_věci_v_pythonu
├── super_modul.py
├── značkování.ipynb
├── regulární_výrazy.ipynb
└── super_skript.py
```

... tak v kterémkoli z ostatních pythonovských souborů (ať už s příponou `.py`
nebo `.ipynb`) můžeme modul `super_modul.py` importovat standardním způsobem:

```python
import super_modul
# nebo from super_modul import x, je-li v modulu definováno x, atp.
```

Pokud ovšem chcete, aby byl modul modul dostupný kdekoli, je potřeba z něj
vytvořit plnohodnotnou samostatnou knihovnu a nainstalovat ji pomocí `pip`u,
podobně jako výše. Naštěstí to není o moc víc práce.

Každá knihovna by měla bydlet ve vlastním adresáři, a ten by měl mít minimálně
následující obsah:

```
libovolné_jméno_adresáře
├── libovolné_jméno_modulu.py
├── pyproject.toml
└── README.md
```

Soubor `libovolné_jméno_modulu.py` obsahuje váš kód, který chcete nainstalovat
jako knihovnu a následně importovat: `import libovolné_jméno_modulu`.
`pyproject.toml` je standardní soubor, který definuje komponenty vaší knihovny a
nějaká dodatečná metadata. Když balíčkový manažer `pip` nalezne v adresáři
soubor `pyproject.toml`, pochopí, že se jedná o pythonovskou knihovnu, a podle
informací v tomto souboru se ji pokusí nainstalovat.

Postupujeme tedy následovně: vytvoříme si nový adresář, třeba ve svém domácím
adresáři, pojmenujeme ho např. `my_library`. V něm vytvoříme dva soubory,
`mytools.py` a `pyproject.toml`.

Pomocí příkazové řádky by to vypadalo následovně:

```sh
# cd bez argumentu nás vrátí zpět do domácího adresáře
cd
mkdir my_library
cd my_library
touch mytools.py
touch pyproject.toml
touch README.md
```

Ale můžeme tyto kroky provést i skrz klikací rozhraní Jupyteru.

Pak oba soubory v Jupyteru otevřeme a vepíšeme do nich zamýšlený obsah. Modul
`mytools.py` bude obsahovat náš kód:

```python
def vert_sents(path):
    """Load a corpus in the vertical format.

    Returns a list of lists (= sentences) of tuples (= tokens).

    """
    sents = []
    with open(path) as file:
        for line in file:
            line = line.strip("\r\n")
            if line == "<s>":
                sent = []
            elif line == "</s>":
                sents.append(sent)
            else:
                word, _, tag = line.split("\t")
                sent.append((word, tag[0]))
    return sents
```

Soubor `pyproject.toml` pak metadata potřebná k instalaci knihovny:

```toml
[project]
# Jméno knihovny může být libovolné, v praxi je ale rozumné knihovnu
# pojmenovat stejně jako její hlavní (v našem případě jediný) modul
# nebo package. Při ``import``u pak ale vždy používáme jména modulů
# (tj. souborů s příponou ``*.py``), ne toto jméno celé knihovny.
name = "mytools"
version = "0.0.1"
description = "Různé užitečné nástroje"
# Ke knihovnám bývá zvykem připojit soubor readme s alespoň zběžnými
# informacemi o tom, jak knihovnu nainstalovat a používat.
readme = "README.md"
authors = [
    {name = "David Lukeš"},
]
dependencies = [
    # Sem lze vypsat jména knihoven, na kterých je ta vaše závislá a
    # které se tudíž mají automaticky nainstalovat spolu s ní.
    "nltk",
]
# Licence, pod níž je vaše knihovna dostupná. Více informací o
# výběru licence (a o tom, k čemu jsou licence vůbec dobré)
# naleznete zde: <https://choosealicense.com/>
license = {text = "MIT"}
# Vyžaduje vaše knihovna nějakou minimální verzi Pythonu?
requires-python = ">=3.10"

[project.urls]
# Pokud má vaše knihovna nějakou webovou stránku.
Homepage = "https://github.com/dlukes/mytools"

[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"

# Více viz https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html.
```

(Některé tyto údaje pochopitelně nejsou povinné, mělo by být intuitivně jasné,
které lze celkem "beztrestně" vynechat. A pokud si nejste jisti, stačí některý
z nich umazat a provést instalaci, jak je popsáno níže -- když to projde, vše
je v pořádku :) )

Pak už stačí jen otevřít terminál a knihovnu nainstalovat pomocí `pip`u.
Použijeme přepínač `--editable`, díky němuž nemusíme po každé úpravě knihovnu
znovu instalovat (naše úpravy se do instalované verze promítnou automaticky).
Místo pouhého jména knihovny jako v případě `scrapy` zadáme cestu k adresáři,
který knihovnu obsahuje:

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

A můžete svou knihovnu vesele používat v noteboocích, skriptech apod.

## Douška na závěr

Pozor, při opakovaném `import`u nějaké knihovny v rámci jednoho sezení se už
Python znovu na disk nedívá a zdrojové soubory knihovny nečte, jen si ověří, že
knihovna už byla dříve importována, a vrátí vám tu verzi, kterou už má nahranou
v paměti. Může tak vzniknout problém, pokud v knihovně objevíte při práci s ní
nějakou chybu, upravíte ji a chcete ji importovat znovu. V takovém případě je
potřeba Python restartovat (tj. v případě notebooku použít funkci *Restart
kernel*).

<!-- vim: set tw=80: -->
