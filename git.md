# Verzování kódu (obecně textu) v Gitu

Git je program, který slouží k systematickému sledování různých verzí souborů v
rámci nějakého projektu. Projekt = repozitář = adresář, který obsahuje různé
další adresáře a soubory. Git si o nich uchovává přehled pomocí skrytého
adresáře `.git` (v kořenovém adresáři repozitáře).

![xkcd git](https://imgs.xkcd.com/comics/git.png)

> If that doesn't fix it, git.txt contains the phone number of a friend of mine
> who understands git. Just wait through a few minutes of 'It's really pretty
> simple, just think of branches as...' and eventually you'll learn the
> commands that will fix everything.

(Zdroj: <https://xkcd.com/1597/>)

## Odkazy

Krátký interaktivní tutorial: <https://try.github.io/>

Delší úvodní texty:

- <https://www.learnenough.com/git-tutorial>
- <http://www-cs-students.stanford.edu/~blynn/gitmagic/index.html>

Kompletní průvodce: <https://git-scm.com/book/en/v2>

## Založení nového repozitáře

Nejjednodušší je založit si repozitář na GitHubu a pak si ho naklonovat
lokálně:

```sh
git clone https://github.com/dlukes/test.git
cd test
```

Pokud nechcete repozitář zrcadlit na GitHubu, můžete si ho založit čistě
lokálně:

```sh
mkdir test
cd test
git init
```

Pokud ho chcete propojit s GitHubem dodatečně, lze to též. Stačí založit
repozitář na GitHubu a následovat pokyny, které se zobrazí:

```sh
git remote add origin https://github.com/dlukes/test.git
```

## Workflow: edit, add, commit, (push)

Práce pak vypadá následovně:

1. Vytvářím nové soubory, edituju stávající. Můžu k tomu používat jakýkoli
   textový editor. Musím jen dávat pozor na to, aby všechny soubory byly
   obsažené v rámci repozitáře, o soubory v jiných adresářích mimo repozitář se
   Git nezajímá.
2. Upozorním Git na změny, které chci uložit, pomocí příkazu `git add
   cesta/k/souboru`. Pokud chci přidat víc souborů, můžu ho použít i opakovaně.
   Pokud jsem udělal chybu a chci začít `add`ovat od začátku, použiju příkaz
   `git reset`.
3. Změny označené pomocí `git add` následně uložím pomocí `git commit`. Každý
   *commit* musí obsahovat krátký popis, který můžu zadat přímo na příkazové
   řádce pomocí přepínače `git commit -m "My awesome commit"`.
4. (nepovinně) Pokud chci synchronizovat stav svého lokálního repozitáře s jeho
   kopií na GitHubu, můžu tak učinit pomocí příkazu `git push`.

A znovu od začátku :)

## Stav repozitáře

Příkaz **`git status`** je asi **nejdůležitější příkaz v Gitu**:

1. Připomene, v jakém je repozitář aktuálně stavu -- jsou ve sledovaných
   souborech nějaké změny? Jsou ty změny připravené ke commitu (proběhl `git
   add`)? Apod.
2. Zároveň **napoví, jak dál**. Pokud si ostatní příkazy v Gitu moc
   nepamatujete, `git status` vám kdykoli navrhne, jaké operace byste asi tak
   vzhledem k aktuálnímu stavu repozitáře mohlí chtít provádět, včetně příkazů,
   kterými jich docílíte.

Pokud chcete **zahodit všechny rozpracované změny**, tj. vrátit se do stavu po
posledním *commitu*, použijte příkaz `git reset --hard`. **POZOR!** Práce,
kterou takto zahodíte, zmizí v nenávratnu; Git si pamatuje jen *commitnuté*
změny.

## Prohlížení historie

Na rozdíl od "běžného ukládání" se *commity* navzájem nepřepisují, vždycky se
můžu podívat historie na předchozí *commity* a vrátit repozitář do nějakého
dřívějšího stavu (to je koneckonců hlavní účel Gitu jako nástroje).

Pokud svůj repozitář `push`nete na GitHub, můžete si jeho historii prohlížet
velmi jednoduše pomocí intuitivního klikacího rozhraní na jeho webové stránce,
ale jde to i na příkazové řádce:

```sh
# základní zobrazení historie commitů
git log
# přehledné high-level zobrazení všech vývojových větví a vztahů mezi nimi
git log --oneline --graph --all --decorate
# (dlouhé příkazy můžeme opakovaně vyvolat pomocí prohledávání historie: Ctrl-R)
```

Poslední uvedený příkaz vytiskne výstup v následujícím formátu:

```sh
* 88ea481 (HEAD -> master) Print sys.argv
* d620f6e (origin/master) Shebang
* 46d3b32 Hello world
```

`HEAD` odkazuje na aktuální stav repozitáře (tj. ten, který vidím, když edituju
soubory). `master` je lokální větev, se kterou aktuálně pracuju (ukazuje na ni
`HEAD`). `origin/master` je odpovídající větev v propojeném repozitáři z
GitHubu (symbolicky označeném jako `origin`), která v této chvíli za lokální
větví `master` o jeden *commit* pokulhává, ale mohl bych její stav aktualizovat
pomocí `git push`. Konečně `88ea481` apod. jsou jednoznačné identifikátory
*commitů*, které se na rozdíl od symbolických identifikátorů jako `HEAD` a
`master` v čase nikdy nemění a stále odkazují na stejný *commit*.

Různí příkazy v rámci Gitu pak tyto identifikátory (jednoznačné i symbolické)
používají pro určení toho, na jaký *commit* se mají vztahovat. Např. `git show`
ukáže obsah požadovaného *commitu*:

```sh
# všechny následující příkazy zobrazí obsah posledního commitu
git show HEAD
git show master
git show 88ea481
# pokud není parametr uveden, HEAD je bráno jako default
git show
```

`git diff <id>` pak zobrazí **rozdíl** mezi *commitem* `<id>` a aktuálním
stavem repozitáře. Pokud `<id>` neuvedu, implicitně se mi zobrazí porovnání se
stavem po posledním commitu.

## Přesuny v historii a větvení

Chci-li vrátit repozitář do nějakého předchozího stavu, stačí použít `git
checkout <id>`, přičemž `<id>` je identifikátor daného bodu v historii. Ve
vybraném bodu historie můžu taky rovnou založit novou vývojovou větev a
přepnout na ni pomocí přepínače `git checkout -b <new-branch-name> <id>`. Jak
větvení přesně funguje a k čemu je dobré si ukážeme na příkladu:

```sh
# stávající stav repozitáře: HEAD mi ukazuje, že jsem na větvi master...
lukes@jupyter:~/grep$ git log --oneline --graph --all --decorate
* 88ea481 (HEAD -> master) Print sys.argv
* d620f6e (origin/master) Shebang
* 46d3b32 Hello world

# ... a v adresáři mám jediný soubor, skript grep.py, na jehož vývoji
# jsem doposud pracoval (vztahují se k němu ony tři commity vypsané
# výše)
lukes@jupyter:~/grep$ ls -l
total 4
-rwxr-xr-x 1 lukes pfc 51 Mar  9 11:07 grep.py

# rozhodnu se, že bych mohl přidat readme (= soubor se základními
# informacemi o projektu), ale zatím si tím nejsem úplně jistý, tak
# ho nebudu dávat na svou hlavní větev (master), ale založím si kvůli
# tomu novou, kterou si návodně nazvu readme
lukes@jupyter:~/grep$ git checkout -b readme
Switched to a new branch 'readme'

# když u příkazu git checkout vynecháme parametr <id>, checkout
# defaultně proběhne tam, kde je HEAD. touto operací se tedy stav
# souborů v repozitáři nijak nezměnil, jen mi HEAD ukazuje, že od
# této chvíle se budou změny ukládat pod větev readme
lukes@jupyter:~/grep$ git log --oneline --graph --all --decorate
* 88ea481 (HEAD -> readme, master) Print sys.argv
* d620f6e (origin/master) Shebang
* 46d3b32 Hello world

# teď si otevřu textový editor a vytvořím soubor README.md. ověřím si,
# že v adresáři skutečně je:
lukes@jupyter:~/grep$ ls -l
total 4
-rwxr-xr-x 1 lukes pfc 51 Mar  9 11:07 grep.py
-rw-r--r-- 1 lukes pfc  0 Mar  9 11:07 README.md

# zdá se že ano, i git status mi hlásí, že se objevil nový soubor,
# o kterém zatím Git nic neví ("untracked")
lukes@jupyter:~/grep$ git status
On branch readme
Untracked files:
  (use "git add <file>..." to include in what will be committed)

        README.md

nothing added to commit but untracked files present (use "git add" to track)

# tak ho přidám...
lukes@jupyter:~/grep$ git add README.md

# ... a změny commitnu
lukes@jupyter:~/grep$ git commit -m "Add readme"
[readme 145568b] Add readme
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 README.md
 
# jak vypadá historie nyní? větev readme se posunula o jeden commit před
# větev master (obsahuje oproti ní navíc právě soubor README.md)
lukes@jupyter:~/grep$ git log --oneline --graph --all --decorate                                                                                                                                                                        
* 145568b (HEAD -> readme) Add readme
* 88ea481 (master) Print sys.argv
* d620f6e (origin/master) Shebang
* 46d3b32 Hello world

# teď se můžu přesunout zpět na větev master a nechat v sobě zrát
# rozhodnutí, zda README.md definitivně zahrnout nebo ne
lukes@jupyter:~/grep$ git checkout master
Switched to branch 'master'
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

# vrátil jsem se v historii zpět, HEAD znovu ukazuje na větev master...
lukes@jupyter:~/grep$ git log --oneline --graph --all --decorate                                                                                                                                                                        
* 145568b (readme) Add readme
* 88ea481 (HEAD -> master) Print sys.argv
* d620f6e (origin/master) Shebang
* 46d3b32 Hello world

# ... a odpovídá tomu i obsah adresáře: README.md je pryč
lukes@jupyter:~/grep$ ls -l
total 4
-rwxr-xr-x 1 lukes pfc 51 Mar  9 11:07 grep.py

# naštěstí ne nenávratně, vím, že ho mám uložené v commitu 145568b
# pod větví readme a můžu si ho kdykoli vyvolat. nyní se můžu vrátit
# k práci na kódu, upravím soubor grep.py a zkontroluju git status:
lukes@jupyter:~/grep$ git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   grep.py

no changes added to commit (use "git add" and/or "git commit -a")

# změny označím...
lukes@jupyter:~/grep$ git add grep.py

# ... a commitnu
lukes@jupyter:~/grep$ git commit -m "Implement grep"
[master 97d1767] Implement grep
 1 file changed, 1 insertion(+), 1 deletion(-)

# historie repozitáře se nyní rozvětvila: větev master obsahuje
# změny, které neobsahuje větev readme, a naopak
lukes@jupyter:~/grep$ git log --oneline --graph --all --decorate                                                                                                                                                                        
* 97d1767 (HEAD -> master) Implement grep
| * 145568b (readme) Add readme
|/  
* 88ea481 Print sys.argv
* d620f6e (origin/master) Shebang
* 46d3b32 Hello world

# časem se ustálím na tom, že mít readme je dobrý nápad, a tak se
# rozhodnu, že ho chci zahrnout do hlavní větve master. importovat
# změny z jedné větve do druhé můžu pomocí příkazu git merge:
lukes@jupyter:~/grep$ git merge readme
Merge made by the 'recursive' strategy.
 README.md | 0
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 README.md

# a skutečně, README.md se v adresáři zase objeví 
lukes@jupyter:~/grep$ ls -l
total 4
-rwxr-xr-x 1 lukes pfc 53 Mar  9 11:09 grep.py
-rw-r--r-- 1 lukes pfc  0 Mar  9 11:10 README.md

# a do historie se zapíše zmínka, že došlo k mergi
lukes@jupyter:~/grep$ git log --oneline --graph --all --decorate                                                                                                                                                                        
*   fe5be7a (HEAD -> master) Merge branch 'readme'
|\  
| * 145568b (readme) Add readme
* | 97d1767 Implement grep
|/  
* 88ea481 Print sys.argv
* d620f6e (origin/master) Shebang
* 46d3b32 Hello world

# v tuto chvíli už je historie větve readme součástí historie větve
# master (obě větve se v posledním commitu zase spojily), takže
# symbolický štítek, který větev readme označoval, můžu klidně smazat
lukes@jupyter:~/grep$ git branch -d readme
Deleted branch readme (was 145568b).

# historie vypadá pořád stejně, jen už commit 145568b nemá alternativní
# symbolické jméno readme
lukes@jupyter:~/grep$ git log --oneline --graph --all --decorate
*   fe5be7a (HEAD -> master) Merge branch 'readme'
|\  
| * 145568b Add readme
* | 97d1767 Implement grep
|/  
* 88ea481 Print sys.argv
* d620f6e (origin/master) Shebang
* 46d3b32 Hello world
```
