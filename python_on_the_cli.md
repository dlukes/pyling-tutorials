# Skripty (programy) v Pythonu pro příkazovou řádku

## Můj první skript

Skript v Pythonu je jen textový soubor, který obsahuje sekvenci příkazů, tak jak jsme je dosud psali do interaktivních buněk v rámci notebooků:

```python
# --8<----- začátek souboru hello.py ----->8--
hello_world = "Hello, world!"
print(hello_world)
# --8<------ konec souboru hello.py ------>8--
```

Pokud je předchozí text uložen v souboru `hello.py` (klidně by to mohlo být i `hello.txt` nebo jen `hello`, přípona je spíš nápověda pro nás), můžeme ho spustit jako program následujícím příkazem:

```sh
lukes@jupyter:~$ python3 hello.py
Hello, world!
```

Program `python3` je interpret jazyka Python, tj. program, který umí vykonávat kód psaný v jazyce Python. Když ho spustíme bez argumentů, běží v interaktivním režimu, který funguje jako takový primitivní *notebook*:

```sh
lukes@jupyter:~$ python3
Python 3.6.4 (default, Feb 23 2018, 09:48:34) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> a = 1 + 1
>>> a
2
# když chceme interaktivní režim Pythonu ukončit a vyskočit zpět
# do shellu, stačí stisknout Ctrl-D
```

Když mu předáme jako argument jméno souboru se skriptem, vykoná se kód uložený ve skriptu a program se následně ukončí.

## Jak operačnímu systému napovědět, pomocí kterého interpretu má skript spustit

Jak jsme si řekli výše, skript je jen textový soubor. Představte si, že dostanete takový textový soubor od kolegy, prý je to velmi užitečný skript, který za vás napíše seminárku. Jak poznáte, jak ho spustit?

Můžete se podívat na příponu. Když to bude `.py`, je to docela spolehlivý signál, že se má skript spustit v Pythonu. Ale v jakém konkrétně, `python2` nebo `python3`? Některé skripty budou fungovat v obou, jiné ne. A pokud má skript příponu, kterou jste nikdy neviděli, třeba `.jl`, tak se budete muset snažit vygooglit, k jakému interpretu přípona patří, a modlit se, aby jich nebylo víc (to se taky stává, např. programovací jazyky Perl a Prolog oba běžně používají příponu `.pl`).

Z tohoto důvodu se často na první řádek skriptů dává tzv. [_**hashbang**_ neboli _**shebang**_](https://en.wikipedia.org/wiki/Shebang_%28Unix%29) (podle znaků `#` -- angl. *hash*, a `!` -- angl. slangově *bang*), který člověku i operačnímu systému napoví, jaký interpret se má ke spuštění skriptu použít:

```python
# --8<----- začátek souboru hello.py ----->8--
#!/opt/pyenv/shims/python3

hello_world = "Hello, world!"
print(hello_world)
# --8<------ konec souboru hello.py ------>8--
```

Proč nemůžu napsat jednoduše jen `#!python3`? V *shebangu* je prostě potřeba uvést plnou cestu k programu. Program `python3` (podobně jako `ls`, `grep`...) je soubor uložený někde na disku počítače. Jak *shell* ví, kde má tento soubor najít, aby ho mohl spustit, když napíšu např. příkaz `python3 hello.py`? *Shell* si pamatuje seznam adresářů, ve kterých má spustitelné soubory s programy hledat, abych pokaždé nemusel vypisovat celou cestu. Tento seznam se nazývá `PATH`, můžeme si ho zobrazit pomocí příkazu `echo $PATH`. *Shellu* se také můžeme zeptat, ve kterém z těchto adresářů nalezl námi požadovaný příkaz:

```sh
lukes@jupyter:~$ which python3
/opt/pyenv/shims/python3
```

Takto zjištěnou cestu pak stačí vypsat do *shebangu* jako informaci o námi zamýšleném interpretu. Pokud pomocí programu `chmod` navíc změníme práva na souboru se skriptem tak, aby byl spustitelný, ...

```sh
lukes@jupyter:~$ ls -lh hello.py
-rw-r--r-- 1 lukes pfc 73 Mar  9 23:24 hello.py
lukes@jupyter:~$ chmod +x hello.py
lukes@jupyter:~$ ls -lh hello.py  # všimněte si nových x (executable, spustitelný)
-rwxr-xr-x 1 lukes pfc 73 Mar  9 23:24 hello.py
```

... docílíme toho, že napříště můžeme při spouštění skriptu vynechat explicitní zmínku `python3`. Když je soubor se skriptem v jednom z adresářů obsažených v seznamu `PATH`, stačí napsat...

```sh
lukes@jupyter:~$ hello.py
Hello, world!
```

... podobně jako u programů `ls` nebo `grep`. Když ne, je potřeba vypsat plnou cestu ke skriptu, kterou si ovšem můžeme zkrátit pomocí symbolu pro aktuální adresář, `.`:

```sh
lukes@jupyter:~$ ./hello.py
Hello, world!
```

## Flexibilní *shebang*

Většinou ale nechceme zadrátovat cestu k interpretu úplně natvrdo. Může se totiž stát, že dostaneme skript od někoho, kdo má program `python3` uložený v jiném adresáři než my:

```python
# --8<----- začátek souboru hello.py ----->8--
#!/někdo/to/rád/jinde/python3

hello_world = "Hello, world!"
print(hello_world)
# --8<------ konec souboru hello.py ------>8--
```

To pak pochopitelně nefunguje, protože *shell* program `python3` na uvedeném místě jednoduše nenajde, tak ho nemůže ani spustit:

```sh
lukes@jupyter:~$ ./hello.py 
bash: ./hello.py: /někdo/to/rád/jinde/python3: bad interpreter: No such file or directory
```

Někdy se taky v rámci `PATH` najde víc programů se stejným jménem. To je i náš případ na Jupyteru:

```sh
lukes@jupyter:~$ which -a python3  # -a jako all
/opt/pyenv/shims/python3
/usr/bin/python3
```

*Shell* v takovém případě dá automaticky přednost tomu prvnímu, protože předpokládá, že jsme si `PATH` nastavili tak, že chceme, aby dřívější výskyty programů se stejným jménem přebily případné pozdější. To skutečně chceme, protože ten první program je novější:

```
lukes@jupyter:~$ /opt/pyenv/shims/python3 --version
Python 3.6.4
lukes@jupyter:~$ /usr/bin/python3 --version
Python 3.5.2
```

Ideálně bychom chtěli, aby se náš *shebang* choval podobně ohleduplně jako *shell*: aby specifikoval jméno interpretu, s jehož pomocí se má skript spustit, ale aby jeho přesné umístění nechal na uživateli, resp. prostě použil **první program toho jména, který nalezne při procházení `PATH`**. Toho docílíme následovně:

```python
# --8<----- začátek souboru hello.py ----->8--
#!/usr/bin/env python3

hello_world = "Hello, world!"
print(hello_world)
# --8<------ konec souboru hello.py ------>8--
```

Příkaz `env python3` není žádné kouzlo, můžete si ho vyzkoušet i na příkazové řádce. Jednoduše spustí první program se jménem `python3`, na který narazí při procházení `PATH`. Podobně `env ls` aj.

## Práce s argumenty

Většina programů pro příkazovou řádku, se kterými jsme doposud pracovali, umí změnit své chování v závislosti na tom, jaké argumenty jim předáme:

```sh
lukes@jupyter:~/grep$ ls
grep.py
lukes@jupyter:~/grep$ ls -l
total 4
-rwxr-xr-x 1 lukes pfc 162 Mar  8 17:20 grep.py
```

S argumenty můžeme pracovat i v pythonovských skriptech. Když skript spustím, *shell* nejprve vezme celý příkaz, naseká ho na mezerách a převede ho na seznam řetězců. Tento seznam řetězců je pak dostupný v modulu `sys` přes proměnnou `argv`:

```python
# --8<----- začátek souboru hello.py ----->8--
#!/usr/bin/env python3

import sys

print(sys.argv)
# --8<------ konec souboru hello.py ------>8--
```

Což se při použití chová následovně:

```sh
# všimněte si, že první položkou seznamu argv je samotné jméno
# souboru se skriptem
lukes@jupyter:~$ ./hello.py foo bar baz
['./hello.py', 'foo', 'bar', 'baz']

# zpětné lomítko způsobí, že následující mezera nezafunguje jako
# oddělovač
lukes@jupyter:~$ ./hello.py foo\ bar baz
['./hello.py', 'foo bar', 'baz']

# podobně pár závorek
lukes@jupyter:~$ ./hello.py "foo bar" baz
['./hello.py', 'foo bar', 'baz']

# jako oddělovače fungují skutečně jen mezery (tedy obecně
# whitespace): když napíšu něco těsně za uzavírající uvozovku,
# slepí se mi to s předchozím řetězcem do jednoho argumentu
lukes@jupyter:~$ ./hello.py "foo bar"baz
['./hello.py', 'foo barbaz']
```

Co program s tímto seznamem udělá je **čistě na něm**. Většina programů v UNIXu se snaží dodržovat nějaké konvence, aby byly pro uživatele intuitivní (přepínače jsou buď `-` + písmeno nebo `--` + slovo, `-h` či `--help` zobrazí nápovědu atp.), ale vůbec tomu tak být nemusí. S argumenty můžu např. udělat následující:

```python
# --8<----- začátek souboru hello.py ----->8--
#!/usr/bin/env python3

from sys import argv

name, rest = argv[1], argv[2:]
print(f"Hello, {name}! Thank you for calling me with {rest}")
# --8<------ konec souboru hello.py ------>8--
```

Což se při použití chová následovně:

```sh
lukes@jupyter:~$ ./hello.py Jane -h -o
Hello, Jane! Thank you for calling me with ['-h', '-o']
lukes@jupyter:~$ ./hello.py Jane -ho
Hello, Jane! Thank you for calling me with ['-ho']
lukes@jupyter:~$ ./hello.py -ho Jane
Hello, -ho! Thank you for calling me with ['Jane']
```

<!-- TODO: argparse, if __name__ == "__main__" -->