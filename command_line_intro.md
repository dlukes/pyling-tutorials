# Úvod do příkazové řádky

Proč se vůbec učit pracovat s příkazovou řádkou? Nestačí nám umět
používat Python? Bohužel nestačí. Existuje mnoho užitečných programů,
které nemají šikovné rozhraní (knihovnu) pro použití z Pythonu, a
většinou už vůbec nemají grafické rozhraní (typu spustím program z
nabídky *Start*, otevře se okýnko -- prostě GUI, *Graphical User
Interface*). Zato ale mají rozhraní pro příkazovou řádku (*command
line*, *Command Line Interface* -- CLI). Z čistě praktického hlediska
nám tedy schopnost práce s příkazovou řádkou dává přístup k nástrojům,
které bychom jinak použít jednoduše nemohli.

To se vztahuje i na nástroje vlastní -- není nic jednoduššího, než
napsat program pro příkazovou řádku, třeba v Pythonu, ke splnění
libovolného drobného úkolu, na který opakovaně narážíte. Konkrétní
příklad: občas chci ve wordovském dokumentu umazat u komentářů časové
značky, aby nebylo poznat, že jsem se ke komentování dostal až na
poslední chvíli ;) Word sám to neumožňuje, ale stačí na to [poměrně
krátký skript v Pythonu](https://gist.github.com/dlukes/2b5c2a163cd8adba420aaae0c8ea2c00).
Kdybych mu chtěl udělat GUI (okýnkové rozhraní), musel bych se s tím
patlat o něco déle, ale CLI je v podstatě hotové hned.

Velkou předností příkazové řádky je, že umožňuje snadnou **spolupráci
programů napsaných v různých programovacích jazycích**. V Pythonu
pracujeme s datovými strukturami jako je seznam nebo slovník, na
příkazové řádce si programy navzájem posílají jen čistý text (resp.
bajty), žádné složitější datové struktury.

Jak tato spolupráce v praxi funguje? Základním stavebním kamenem je
možnost zřetězit programy pomocí tzv. **rour**, tj. poslat výstupní data
jednoho programu jinému programu jako data vstupní.  Např. když v
následující podobě zavolám program `echo`, výstupem budou čtyři řádky
textu:

```sh
user@host:~$ echo -e "ant\nbee\ncrow\ndeer"
ant
bee
crow
deer
```

Ale tento výstup můžu pomocí roury poslat na vstup programu `grep`, který
vyfiltruje např. řádky, které obsahují sekvenci písmen "ee":

```sh
user@host:~$ echo -e "ant\nbee\ncrow\ndeer" | grep ee
bee
deer
```

Různé operační systémy mají různé příkazové řádky s různými funkcemi. Operační
systémy z rodiny UNIX, jako je např. Linux nebo macOS, kladou tradičně velký
důraz na tento typ rozhraní a navíc dávají uživateli k dispozici hodně programů
pro manipulaci textu, což se nám jako lingvistům hodí. Půjde nám tedy o
seznámení s unixovou příkazovou řádkou. Pokud se vám toto prostředí zalíbí a
chtěli byste používat podobné i na Windows, můžete si na Windows 10
nainstalovat tzv. subsystém pro Linux; googlete ["Bash on Ubuntu on
Windows"](https://docs.microsoft.com/en-us/windows/wsl/about). Pozor,
**defaultní příkazová řádka ve Windows je něco jiného** a funkcionalitu, kterou
níže probereme, nenabízí.

Níže následuje jen stručný přehled toho nejdůležitějšího, aby se člověk
na příkazové řádce necítil ztracený. Pro zvídavé / náročnější doporučuju
on-line knihu zdarma [*Learn Enough Command Line to Be
Dangerous*](https://www.learnenough.com/command-line-tutorial). Ovšem
ministr zdravotnictví varuje: při pravidelném (po)užívání je příkazová
řádka návyková a můžou se dostavit návaly vzteku, když jste pak
příležitostně donuceni ji opustit a zmateně myšovat po běžných GUI
aplikacích, protože mít všechno na dosah ruky na klávesnici je k
nezaplacení ;)

## Terminál, shell a příkazová řádka

**Terminál** (emulátor terminálu) je program v počítači, který předstírá, že je
[historický typ počítačové obrazovky ze 70.
let](https://cs.wikipedia.org/wiki/VT100), která pracuje jen s pravidelnou
mřížkou (řádky a sloupci) znaků. Prapůvodní předchůdce této technologie je tzv.
[dálnopis (teletype, tty)](https://cs.wikipedia.org/wiki/D%C3%A1lnopis), což
byl takový psací stroj na dálku, kde se výstup nezobrazoval na monitor, ale
tiskl.

Vzhledem ke svému stáří nejsou terminály tak uživatelsky přívětivé jako novější
grafická rozhraní. Např. zobrazení některých znaků může terminál "rozbít",
[místo očekávaných znaků se začnou zobrazovat
jiné](https://www.cyberciti.biz/tips/bash-fix-the-display.html), výstup je
nečitelný. Většinou stačí v těchto případech **poslepu napsat `reset` a
zmáčknout `Enter`**.

**Shell** je první program, který se při otevření terminálu
spustí. Skrz něj můžeme spouštět další programy, různě je kombinovat apod.
Shell se jmenuje proto, že je to taková skořápka, která obaluje všechny funkce
nabízené počítačem a poskytuje k nim uživateli přístup. V tomto smyslu se někdy
i o grafických rozhraních, jako je třeba prostředí Windows, mluví jako o
(grafickém) shellu.

**Příkazová řádka** je (jak je asi patrné už z názvu) řádek v terminálu,
kde shell čeká na to, až napíšeme a spustíme nějaký příkaz.

Jinými slovy, přísně vzato znamená každý z těchto pojmů něco trochu
jiného. Přesto se v některých situacích používají zaměnitelně, např.
pokyn může znít "Spusťte příkaz v terminálu / shellu / příkazové řádce"
a myslí se tím totéž. Jindy se ale rozlišují, třeba když mluvíme o
různých konkrétních shellech (např. [bash] vs. [fish]), tak není úplně
adekvátní tyto programy označovat jako "terminály", protože terminály
(resp. emulátory terminálu) jsou zas jiné programy (např. [GNOME
Terminal], [Windows Terminal] aj.), které fungují jako prostředí, v němž
shelly a další terminálové programy běží. Ale příliš se tím netrapte,
důležité je tušit, že jsou to sice různé věci, ale často se můžou
navzájem metonymicky zastupovat; zbytek většinou vyplyne z kontextu.

[bash]: https://en.wikipedia.org/wiki/Bash_(Unix_shell)
[fish]: https://en.wikipedia.org/wiki/Fish_(Unix_shell)
[GNOME Terminal]: https://en.wikipedia.org/wiki/GNOME_Terminal
[Windows Terminal]: https://en.wikipedia.org/wiki/Windows_Terminal

## Adresářová struktura

Ve Windows jsou jednotlivá úložiště (disky) samostatná, každé má svoje písmeno
(např. `C:\`). Pod nimi se pak nachází hierarchický strom adresářů.

Oproti tomu na Linuxu vyrůstá strom adresářů z jediného kořenového adresáře,
`/`, a klade se menší důraz na to, které části stromu jsou na kterých fyzických
discích. V adresáři `/home` se nacházejí domácí adresáře všech uživatelů, kteří
mají na počítači účet. Abychom nemuseli pokaždé vypisovat celou cestu, existují
různé zkratky:

- `.` je aktuální adresář
- `..` je adresář o jednu úroveň nad aktuálním; můžeme to dále řetězit (`../..`
  atp.)
- `~` je domácí adresář aktuálně přihlášeného uživatele
- `~user` je domácí adresář uživatele `user`
- `*` je jako v regulárních výrazech `.*`, takže např. cesta `./*.txt` odpovídá
  všem souborům s koncovkou `.txt` v aktuálním adresáři

Stisknutím klávesy `Tab` lze **automaticky doplnit rozepsanou cestu**, případně
zobrazit možnosti doplnění, pokud je jich víc. V závislosti na nastavení shellu
je někdy nutné klávesu `Tab` stisknout opakovaně, aby se ukázaly možnosti
doplnění, pokud neexistuje doplnění jednoznačné.

## Programy na příkazové řádce

Programy (příkazy) v shellu voláme tak, že napíšeme jejich jméno, pak případně
parametry oddělené mezerou a zmáčkneme `Enter`. Parametry se dělí na
**argumenty**, které jsou specifikované pozičně (první, druhý, třetí...) a
**přepínače**, u nichž je potřeba napsat jejich jméno, buď v krátké (např.
`-A`) nebo dlouhé (např. `--after-context`) podobě. Přepínače je převážně možné
psát v libovolném pořadí, protože většina programů je při odpočítávání pozic
argumentů ignoruje.

```sh
# vytiskne všechny svoje parametry
echo Hello, world!
# vytiskne adresář, ve kterém se nacházíme (print working directory)
pwd
# změní adresář (.. značí adresář o jednu úroveň v hierarchii výš)
cd ..
# bez parametru nás vrátí zpět do domácího adresáře
cd
# vytvoří adresář pojmenovaný foo
mkdir foo
# vytvoří v adresáři foo prázdný soubor bar
touch foo/bar
# přesune soubor bar z adresáře foo do našeho současného (pracovního)
# adresáře
mv foo/bar .
# přejmenuje soubor bar na baz
mv bar baz
# zkopíruje soubor baz do souboru qux
cp baz qux
# vymaže soubor (nenávratně!)
rm qux
# vymaže (nenávratně!) adresář foo, pokud je prázdný
rmdir foo
# vymaže (nenávratně!) adresář foo, i když v něm jsou nějaké další vnořené
# soubory a adresáře
rm -r foo
# vylistuje obsah adresáře
ls
# víc informací (long format)
ls -l
# převod informace o velikosti souborů na human-readable hodnoty
ls -l -h
# krátké přepínače jde u většiny programů spojit
ls -lh
```

Programy posílají svoje výsledky na tzv. **standardní výstup**
(`STDOUT`), případně si mohou brát data ze **standardního vstupu**
(`STDIN`). Standardní výstup normálně skončí prostřednictvím terminálu
na naší obrazovce, ale je též možné ho poslat do souboru (`>soubor.txt`
přepíše `soubor.txt` novým obsahem, `>>soubor.txt` na jeho konec zapíše
další data), případně prostřednictvím tzv. **roury** (`|`, angl.
*pipe*, čes. též "**pajpa**") na **standardní vstup jiného programu**.
Tímto způsobem je možné sestavit celé **potrubí** na zpracování dat.

Většina programů na zpracování textu si umí brát vstup buď ze souboru, který
jim zadáme jako parametr, nebo právě ze standardního vstupu (pak není třeba
zadávat žádné jméno souboru, případně je místo něj u některých programů možné
napsat jen `-`, abychom explicitně naznačili, že pracujeme se standardním
vstupem).

```sh
# najdi v korpus.txt všechny **řádky**, které obsahují slovo kočka
grep kočka korpus.txt
# najdi v korpus.txt všechny řádky, které matchují regulární výraz
# koč[kc], a výsledky zapiš do souboru kocky.txt
grep -P 'koč[kc]' korpus.txt >kocky.txt
# vyfiltruj jen řádky obsahující slovo pejsek, výstup pošli skrz
# rouru na standardní vstup dalšího volání programu grep, které
# z již profiltrovaných řádků vybere jen ty, které obsahují
# i slovo kočička
grep pejsek pejsek_a_kocicka.txt | grep kočička
```

Kromě programu `grep`, který umožňuje profiltrovat řádky vstupního textu na
základě nějakého řetězce či regulárního výrazu, jsou pro práci s textovými
soubory užitečné ještě např. následující programy:

- `cat`: spojí obsah více souborů za sebou a vytiskne ho na terminál (je
  pochopitelně možné použít i jen s jedním jediným souborem)
- `head`: vypíše začátek souboru/ů
- `tail`: vypíše konec souboru/ů
- `cut`: vyřízne z textového souboru jen některé sloupce (hranice sloupců
  stanoví podle zvoleného delimitačního znaku, defaultně je to tabulátor)
- `paste`: slepí textové soubory k sobě jako sloupce (opak `cut`)
- `sort`: seřadí vstupní řádky
- `uniq`: zahodí po sobě jdoucí stejné řádky
- `diff`: vypíše rozdíly mezi dvěma textovými soubory
- `less`: program na interaktivní prohlížení dlouhých souborů

### Kde najít nápovědu?

V první řadě: ačkoli shell může na první pohled vypadat jako obskurní
prostředí, k jehož používání by vás mohl nutit akorát nějaký temný šílenec, ve
skutečnosti ho používá hodně lidí a na internetu se neustále ptají i na ty
nejzákladnější věci :) Stačí se Googlu hezky zeptat např. ["how to remove
non-empty directory"](lmgtfy.com/?&q=bash+how+to+remove+non-empty+directory).

Pomoc lze ale nalézt i přímo na příkazové řádce. Je dobré si zapamatovat jména
programů, ale to, jak se volají a jak fungují jejich přepínače, si vždy můžete
přečíst v manuálu: `man jmeno_programu`. Některé programy naopak / navíc k tomu
podporují přepínač `-h` nebo `--help`, takže příkaz `jmeno_programu --help` vám
zobrazí podobné informace.

Ovládání manuálu zobrazíte (přímo v manuálu) klávesou `h`. Důležité je
vyhledávání (`/`, pak hledaný výraz, pak `Enter`; mezi výskyty přeskakujete
pomocí `n` a `N`), scrollování (`gg` = začátek, `G` = konec, `Ctrl+f` = stránka
vpřed, `Ctrl+b` = stránka zpět, jinak šipky) a `q` (tou manuál zase opustíte).
Čtecí program `less` má stejné ovládání.

## Složitější příklad

Zkusme propojit výše zmíněné dílčí programy dohromady a s jejich pomocí
vytvořit frekvenční distribuci 100 nejčastějších autosémantik v
`syn2015_sample`:

```sh
cut -s -f2,3 ~/edu/python/syn2015_sample |
  grep -P '\t[NADV]' |
  cut -f1 |
  sort |
  uniq -c |
  sort -nr |
  head -n100 >~/frek_dist.txt
```

Lidsky řečeno, příkaz po příkazu:

1. Vyříznout druhý a třetí sloupec (lemma a tag) z korpusu. Řádky, které na
   sloupce vůbec nejsou rozdělené, rovnou zahodíme (`-s`), čímž se zbavíme
   řádků, které obsahují strukturní značky jako `<doc>`, `<text>` apod.
2. Vyfiltrovat řádky, které obsahují tabulátor a těsně za ním N, A, D nebo V
   (pomocí regulárního výrazu). Jinými slovy řádky, které obsahují morfologický
   tag začínající na jedno z těchto písmen. To znamená, že "synsémantikum" si
   definujeme jako kterékoli substantivum, adjektivum, adverbium nebo verbum.
3. V tuto chvíli už tagy nepotřebujeme, tak je můžeme odříznout.
4. Teď bychom rádi spočítali frekvenci lemmat, což lze udělat pomocí programu
   `uniq` s přepínačem `-c`, ale pamatujme, že program `uniq` je potřeba pustit
   na seřazený vstup, takže musíme lemmata nejprve seřadit pomocí `sort`.
5. Po seřazení můžeme už použít `uniq`, který zahodí duplicitní řádky, a
   přepínač `-c` navíc doplní informaci o tom, kolikrát se každý duplicitní
   řádek vyskytl (přidá číslo na začátek řádku).
6. Teď chceme seznam seřadit podle právě doplněných čísel. Program `sort`
   normálně řadí abecedně, aby řadil numericky, musíme použít přepínač `-n`.
   Taky normálně řadí od nejmenšího, aby řadil od největšího (tj. od
   nejčastějších lemmat), použijeme přepínač `-r` ("reverse").
7. Zajímá nás 100 nejčastějších synsémantik, takže zbytek zahodíme, a na závěr
   výstup přesměrujeme do souboru `frek_dist.txt` v našem domácím adresáři,
   abychom s ním mohli případně dál pracovat (jinak by se nám jen vytiskl na
   obrazovku).

Díky rourám spolu mohou programy na příkazové řádce takto spolupracovat a
vypořádat se kolektivně i s poměrně složitým úkolem, na který žádný z nich
individuálně nebyl přímo stavěn. Každý program může být napsaný **v libovolném
programovacím jazyce**, komunikují spolu jednoduše tak, že si skrz roury
posílají data v podobě textu. "Klikací" nebo "okýnkové" programy většinou tímto
kreativním způsobem propojit nejdou, takže možnosti jejich využití jsou často
omezené na to, co každý z nich umí samostatně.

## Klávesové zkratky

Shell má mnoho různých klávesových zkratek, které umožňují prohledávat jeho
historii a rychle editovat příkazy, takže je nemusíte pokaždé psát celé znovu.
Relativně detailní přehled je např.
[zde](https://www.howtogeek.com/howto/ubuntu/keyboard-shortcuts-for-bash-command-shell-for-ubuntu-debian-suse-redhat-linux-etc/),
ale jestli se nechystáte příkazovou řádku moc používat, není důvod se je učit
zpaměti. Základní pro přežití jsou následující:

- `Ctrl-C` = *interrupt* → ukončí právě běžící program
- `Ctrl-D` = *exit* → ukončí shell, případně pokud jste v rámci shellu zapnuli
  jiný interaktivní program (např. pythonovský interpret pomocí příkazu
  `python`, kde si můžete interaktivně vyhodnocovat pythonovské výrazy), tak
  ukončí tento program a vrátí vás do shellu
- `Shift-Insert`: vloží zkopírovaný text na příkazovou řádku
- šipka nahoru/dolů: umožňuje navigovat v historii příkazů
- pomocí `Ctrl-R` můžete vyhledávat v historii příkazů (při opakovaném
  stisknutí se zobrazují starší a starší příkazy z historie, které obsahují
  hledaný výraz)
- `Ctrl-Z` uspí právě běžící program na pozadí a vrátí vás na příkazovou řádku;
  pokud chcete program znovu probudit, použijte příkaz `fg`
- 💀`Ctrl-S`💀: o téhle zkratce je spíš potřeba vědět, protože ji člověk může
  někdy zmáčknout omylem, neboť většina dnešních programů ji používá pro
  uložení souboru; v některých terminálech ale znamená "suspend", čímž se
  terminál pozastaví a nelze s ním interagovat; terminál zase vzkřísíte pomocí
  `Ctrl-Q`

## Záznam sezení

Všechny příkazy, které vykonáte v shellu, se automaticky zapisují do souboru
`~/.bash_history`. Pokud je při nějakém konkrétním sezení chcete nechat
zapisovat do jiného vámi vybraného souboru, můžete shell spustit znovu a
nastavit proměnnou, která soubor s historií příkazů změní:

```sh
# bash je jméno shellu, který používáme (shell je program jako ostatní)
HISTFILE=moje_historie.txt bash
```

Jakmile pak sezení ukončíte (`Ctrl+D` nebo `exit`), připíše se jeho historie na
konec uvedeného souboru (případné dřívější záznamy tedy zůstanou zachovány).
