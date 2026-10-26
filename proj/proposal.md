# Proposal pro semestrální projekt

Návrh projektu do předmětu **Umělá inteligence (ENC-AI)**

**Téma projektu:** Využití Multi-Agent AI systémů pro diagnostiku a RCA v Kubernetes

Projekt porovnává jednoagentní a multiagentní systémy umělé inteligence při diagnostice a analýze kořenových příčin provozních incidentů (Root Cause Analysis, RCA) v prostředí Kubernetes.

## Řešitelé

* [Dominik Jakubec](https://is.mendelu.cz/auth/lide/clovek.pl?id=100907)
* [Jiří Kužel](https://is.mendelu.cz/auth/lide/clovek.pl?id=100910)
* [Vojtěch Střílka](https://is.mendelu.cz/auth/lide/clovek.pl?id=100912)
* [Jiří Ulč](https://is.mendelu.cz/auth/lide/clovek.pl?id=101482)

## Základní princip

**1. Kdo má daný problém?**

* vývojáři aplikací
* DevOps inženýři
* správci Kubernetes clusterů
* SRE (Site Reliability Engineering) týmy

Obecně všichni, kdo zajišťují vývoj a provoz softwaru.

**2. S čím se potýká?**

Při řešení incidentů musí uživatel/správce vyhodnocovat velké množství informací z událostí, logů nebo metrik.

Tyto informace jsou často rozptýleny v několika systémech a pro určení skutečné příčiny problému nemusí existovat jednotný postup.

**3. Proč na tom záleží?**

Zdlouhavá diagnostika prodlužuje dobu výpadku služeb, zvyšuje provozní náklady a může negativně ovlivnit jejich uživatele.

Automatizovaná analýza může urychlit identifikaci příčin problémů a pomoci i méně zkušeným uživatelům/správcům.

**4. Jaké je nejmenší řešení, které můžeme otestovat?**

Prototyp, který získá metriky, logy a události z lokálního Kubernetes clusteru s aplikacemi, v nichž budeme simulovat provozní incidenty.

Porovnáním různých architektur AI systémů posoudíme jejich diagnostickou úspěšnost a provozní náročnost.

Na stejných datech porovnáme jednoagentní přístup se základním a optimalizovaným promptem a multiagentní přístup.

**5. Jaké důkazy nám řeknou, zda to funguje?**

Připravíme sadu incidentů se známou příčinou jako například překročení paměťového limitu, chybnou konfiguraci aplikace nebo příliš nízký limit CPU.

Na takových scénářích budeme měřit:

* úspěšnost identifikace příčiny
* správnost použitých důkazů
* dodržení očekávané struktury odpovědi
* dobu analýzy
* spotřebu tokenů

Výsledky ukážou, který přístup dosahuje lepších výsledků a zda přínos složitější architektury vyvažuje náročnost její konfigurace.

## Project pitch

Projekt umožní prakticky prozkoumat využití pokročilého prompt engineeringu a multiagentních AI architektur při řešení reálných problémů v oblasti IT infrastruktury.

Jeho hlavním přínosem bude nejen funkční prototyp diagnostického nástroje, ale především experimentální porovnání několika AI přístupů za stejných podmínek ve stejném prostředí.

## Product pitch

Nástroj je určen správcům Kubernetes infrastruktury, kterým pomůže rychleji porozumět provozním incidentům.

Namísto ručního procházení různých diagnostických zdrojů uživatelé nástroje získají:

* přehled pravděpodobných příčin problému
* relevantní důkazy
* doporučené kroky k nápravě problému

Navržené řešení má sloužit jako systém pro podporu rozhodování, nikoliv jako náhrada zkušeného uživatele/správce.
