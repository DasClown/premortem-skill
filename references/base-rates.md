# Base Rates — Echte Failure-Statistiken

> Wenn du keine Base Rate kennst, ersetzt dein Gehirn sie durch einen Plot Twist.
>
> *Reference Class Forecasting* (Kahneman & Lovallo): Jede Vorhersage muss in einer Referenzklasse verankert sein. Erst die Outside View, dann die Inside View.

---

## Software-Entwicklung

| Metrik | Rate | Quelle |
|--------|------|--------|
| Projekte überschreiten initiale Zeitschätzung | 70% | Standish Group CHAOS Report 2020 |
| Projekte überschreiten Budget um 100%+ | 45% | Standish Group CHAOS Report 2020 |
| Features werden NIE genutzt (nach Deployment) | 45% | Standish / Microsoft Research |
| Technische Schulden sind Primärgrund für gescheiterte Deadlines | 62% | Stripe Developer Coefficient |
| Entwickler verbringen >33% Zeit mit technischen Schulden | 68% | Stripe Developer Coefficient |
| Refactoring-Projekte überschreiten Zeit um >50% | 64% | IEEE Software Engineering |
| Migrationen (DB, FW, Sprache) brauchen 2-3x initiale Schätzung | >90% | Gartner IT Key Metrics |

## Produkt-Launches

| Metrik | Rate | Quelle |
|--------|------|--------|
| Neue Produkte scheitern im ersten Jahr | 70-95% | HBS / Nielsen Breakthrough Innovation |
| Consumer-Produkte: Fehlschlagsrate | 80-95% | Nielsen |
| B2B-SaaS: Fehlschlagsrate | 70-80% | Tomasz Tunguz / SaaS Capital |
| Features mit <3 Nutzerinterviews vor Build | 64% scheitern | Pragmatic Institute |
| Preismodell wird NIE beim ersten Versuch getroffen | 90%+ | Price Intelligently |

## Startups & Unternehmen

| Metrik | Rate | Quelle |
|--------|------|--------|
| Startup 5-Jahres-Überlebensrate | 50% | BLS / U.S. Bureau of Labor Statistics |
| VC-finanzierte Startups: Totalausfall | 65% | Correlation Ventures |
| 10-Jahres-Überlebensrate (allgemein) | 30% | BLS |
| Post-M&A: Wertvernichtung (Deal zerstört Wert) | 70-90% | McKinsey / HBR / KPMG |
| Organisationsänderungen scheitern | 60-70% | McKinsey / BCG |
| Digital-Transformation-Projekte scheitern | 70% | McKinsey |

## Hiring & Teams

| Metrik | Rate | Quelle |
|--------|------|--------|
| Fehleinstellungen (gekündigt/gefeuert in <18 Monaten) | 40-50% | HBR / Leadership IQ |
| Kultureller Fit ist Hauptgrund für Fehleinstellung | 89% | Leadership IQ |
| Remote-Teams: Kommunikations-Overhead unterschätzt | 71% | Buffer State of Remote Work |
| Neue Teammitglieder brauchen >6 Monate für volle Produktivität | 62% | HBR |

## Schätzungen & Planung

| Metrik | Rate | Quelle |
|--------|------|--------|
| Menschen unterschätzen Aufwand um Faktor | 2-3x | Kahneman/Tversky Planning Fallacy |
| Inside View (eigene Schätzung) vs Outside View (Base Rate) | Inside View immer zu optimistisch | Kahneman, "Thinking, Fast and Slow" |
| Kognitive Verzerrung "Optimism Bias" | 80% der Menschen | Sharot, "The Optimism Bias" |
| Expertenschätzungen sind NUR mit Base Rate besser | Ohne Base Rate = schlechter als naive Extrapolation | Tetlock, "Superforecasting" |

---

## Anwendung im Premortem

1. **Vor jedem Failure Mode:** Check — was sagt die Base Rate für diese Klasse von Entscheidung?
2. **Outside View erzwingen:** "Wenn 100 Teams diese Entscheidung treffen, wie viele scheitern?"
3. **Referenzklasse identifizieren:** Ist das ein "Software-Projekt" (70% überschreiten Zeit), ein "Produkt-Launch" (70-95% scheitern), oder ein "Refactoring" (64% überschreiten um 50%+)?
4. **Base Rate > Inside View:** Wenn die Base Rate für deine Entscheidungsklasse 70% Failure ist, brauchst du EVIDENZ dafür, dass du in den 30% bist — nicht andersrum.

---

## Worked Example

**Schätzung:** Ein Feature braucht "ca. 2 Wochen".

1. **Referenzklasse:** Software-Projekt + Refactoring. Base Rate: 70% überschreiten Timeline, 64% brauchen 50%+ mehr Zeit.
2. **Outside View:** 70 von 100 vergleichbaren Projekten werden nicht in 2 Wochen fertig.
3. **Inside View prüfen:** "Diesmal ist es anders, weil... [Gründe]". Für jeden Grund: *Ist das ein echter Unterschied oder Optimism Bias?*
4. **Angepasste Schätzung:** 2 Wochen × Base Rate 1.5x = **3 Wochen Minimum**.
5. **Ergebnis:** Entweder Scope reduzieren oder Timeline anpassen. Nicht beides auf 2 Wochen quetschen.

**Lerner:** *Eine Base Rate zu kennen ist nichts wert. Sie ANZUWENDEN ist alles.*

---

## Quellen (kompakt)

- Kahneman, D. (2011). *Thinking, Fast and Slow*. Farrar, Straus and Giroux.
- Kahneman, D. & Lovallo, D. (1993). Timid Choices and Bold Forecasts. *Management Science*.
- Standish Group (2020). CHAOS Report.
- Nielsen (2012-2019). Breakthrough Innovation Reports.
- Tetlock, P. & Gardner, D. (2015). *Superforecasting*. Crown.
- Flyvbjerg, B. & Gardner, D. (2023). *How Big Things Get Done*. Currency.
- Sharot, T. (2011). *The Optimism Bias*. Pantheon.
