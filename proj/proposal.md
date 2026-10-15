# Proposal pro projekt ENC-AI

Proposal na projekt do předmětu Umělá inteligence (ENC-AI) - Využití Multi-Agent AI systémů pro diagnostiku a RCA (Root Cause Analysis) v Kubernetes prostředí

## Základní princip

**1. Kdo má daný problém?**

DevOps inženýři, administrátoři Kubernetes clusterů a SRE týmy, které zajišťují provoz a dostupnost kontejnerizovaných aplikací.

**2. S čím se potýká?**

Při řešení incidentů musí vyhodnocovat velké množství informací z logů, metrik a Kubernetes událostí. Tyto informace jsou často rozděleny mezi několik nástrojů a určit skutečnou příčinu problému nemusí být jednoduché.

**3. Proč na tom záleží?**

Zdlouhavá diagnostika prodlužuje dobu výpadku služeb, zvyšuje provozní náklady a může negativně ovlivnit jejich uživatele. Automatizovaná analýza by mohla zrychlit identifikaci problémů a pomoci i méně zkušeným administrátorům.

**4. Jaké je nejmenší řešení, které můžeme otestovat?**

Prototyp, který získá metriky, logy a události z testovacího Kubernetes clusteru a pomocí LLM vytvoří diagnózu incidentu. Na stejných datech porovnáme jednoagentní a multiagentní přístup.

**5. Jaké důkazy nám řeknou, zda to funguje?**

Připravíme sadu incidentů se známou příčinou (například OOMKilled, CrashLoopBackOff nebo CPU throttling). Na těchto scénářích budeme měřit úspěšnost identifikace příčiny, správnost použitých důkazů, dobu analýzy a spotřebu tokenů. Výsledky ukážou, zda multiagentní řešení dosahuje lepších výsledků a zda případné zlepšení ospravedlňuje jeho vyšší složitost.

## Project pitch

Projekt umožní prakticky prozkoumat využití pokročilého prompt engineeringu a multiagentních AI architektur při řešení reálných problémů v oblasti IT infrastruktury. Jeho hlavním přínosem bude nejen funkční prototyp diagnostického nástroje, ale především experimentální porovnání několika AI přístupů za stejných podmínek.

## Product pitch

Nástroj je určen správcům Kubernetes infrastruktury, kterým pomůže rychleji porozumět provozním incidentům. Namísto ručního procházení různých diagnostických zdrojů získají přehled pravděpodobných příčin problému, relevantních důkazů a doporučených kroků k nápravě. Navržené řešení má sloužit jako podpora rozhodování, nikoliv jako náhrada zkušeného administrátora.