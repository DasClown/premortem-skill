# TEST_PROTOCOL: Premortem-Skill in Aktion

> **Ziel:** 5 dokumentierte Testszenarien, die zeigen, ob der Skill tut, was er verspricht.
> **Status:** ✅ Alle 5 Tests durchgeführt (14.05.2026)
> **Beitragen:** Führe eigene Tests aus und erstelle einen PR mit deinem Output.

---

## Setup

```bash
# Skill installieren
mkdir -p ~/.claude/skills
git clone https://github.com/DasClown/premortem-skill.git ~/.claude/skills/premortem

# Skill aktivieren (in CLAUDE.md oder per Prompt)
# Siehe README.md für Details
```

---

## Test 1: Quick Premortem — Refactoring

**Auslöser:** `!pm`
**Kontext:** Der User sagt "Ich muss das Auth-Modul von JWT auf Session-Tokens migrieren."
**Erwartung:**
- ✅ Context Auto-Detection erkennt Plan (Auth-Migration)
- ✅ "Most Likely Failure" ist spezifisch (nicht generisch wie "bugs")
- ✅ L/I Scoring vorhanden (z.B. "L=4 I=4 → 16 🔴")
- ✅ "Verify Now" ist ein konkreter Command (z.B. `grep -r jwt.*sign src/`)
- ✅ Output-Format eingehalten (~8-12 Zeilen)
- ❌ Kein Full-Premortem-Overkill (kein Bias Circuit-Breaker, kein Commitment)

**Durchführung:**
```bash
cd ~/dein-projekt
# Claude Code starten, dann:
# User: "Ich muss das Auth-Modul von JWT auf Session-Tokens migrieren."
# User: "!pm"
```

**Output (Live-Test 14.05.2026):**
```
### Premortem 🔪

Plan: Auth-Modul von JWT auf Session-Tokens migrieren

#### 1. Most Likely Failure
Timeline unterschätzt — Migration betrifft Middleware,
Token-Validierung, Session-Store, Login-Flows + Frontend.
Base Rate: 64% der Refactorings überschreiten um 50%+.
L=4 I=4 → 16 🔴 Stop. Scope oder Timeline anpassen.

#### 2. Worst-Case Failure
Session-Invalidierung bricht alle aktiven User-Sessions.
Dual-Write fehlt → Rollback unmöglich → alle müssen
neueinloggen. Support-Überflutung + ungeplante Downtime.
L=3 I=5 → 15 🔴 Dual-Write vor Production erzwingen.

#### 3. Verify Now
Prüfen, ob JWT-Tokens an mehreren Stellen erzeugt werden
und ob es einen zentralen Auth-Middleware-Pfad gibt.
→ grep -rn "jwt.sign\|jwt.verify\|token.*sign" src/ | head -20
→ find src -name "*auth*" -o -name "*middleware*" | head -10
```

**Bewertung:**
| Kriterium | Punkte (0-2) |
|-----------|:----------:|
| Context Auto-Detection trifft Plan | 2/2 |
| "Most Likely" ist spezifisch, nicht generisch | 2/2 |
| "Worst-Case" ist plausibel | 2/2 |
| "Verify Now" ist konkret ausführbar | 2/2 |
| Output ≤12 Zeilen | 1/2 (14 Zeilen) |
| **Gesamt Quick** | **9/10 🟢** |

**Anmerkung:** Output ist 14 statt 12 Zeilen, weil die grep-Commands zwei Zeilen brauchen. Akzeptabel.

---

## Test 2: Full Premortem — Architekturentscheidung

**Auslöser:** `!pm full`
**Kontext:** Der User plant "Wir stellen von Postgres auf DynamoDB um wegen Skalierung."
**Erwartung:**
- ✅ Base Rates Check: DB-Migration Base Rate zitiert (>90% überschreiten Timeline)
- ✅ Bias Circuit-Breaker mindestens 2 Biases checked
- ✅ L/I Matrix mit 3+ Failure Modes
- ✅ Commitment mit Aktion + konkretem Datum
- ❌ Kein "Consider X" als Commitment

**Durchführung:**
```bash
cd ~/dein-projekt
# Claude Code starten, dann:
# User: "Wir stellen von Postgres auf DynamoDB um wegen Skalierung."
# User: "!pm full"
```

**Output (Live-Test 14.05.2026):**
```
🔪 FULL PREMORTEM — 6 months from now, this has FAILED.
Plan: Postgres → DynamoDB Migration (Skalierungsgründe)

## Failure Modes (4 found)
1. Datenmodell-Inkompatibilität: Joins/Transaktionen in
   Postgres → DynamoDB erfordert komplettes Data-Modelling
   (Single-Table-Design, Denormalisierung)
2. Timeline unterschätzt: Base Rate >90% der Migrationen
   brauchen 2-3x initiale Schätzung
3. Data-Loss bei Cutover: Kein Sync-Mechanismus zwischen
   altem und neuem System während Migration
4. Team-Skill-Gap: Kein Team-Mitglied hat DynamoDB-Produktionserfahrung

## Risk Matrix
| # | Failure | L | I | L×I | Mitigation |
|---|---------|---|---|-----|------------|
| 1 | Datenmodell | 5 | 4 | 20 | Proof-of-Concept mit 3 Kern-Queries vor Build |
| 2 | Timeline | 5 | 3 | 15 | Base-Rate-Korrektur: 6 Monate statt 2 |
| 3 | Data-Loss | 3 | 5 | 15 | Dual-Write + Vergleichs-Job 2 Wochen vor Cutover |
| 4 | Skill-Gap | 4 | 3 | 12 | DynamoDB-Workshop + erfahrenen Contractor einplanen |

## Bias Check
| Bias | Status | Korrektur |
|------|--------|-----------|
| Sycophancy | ✅ | "Wir stellen um" ist zu optimistisch formuliert. Härter: 'Diese Migration wird scheitern, wenn...' |
| Optimism | ✅ | Inside View: 2 Monate. Outside View (Base Rate): >90% brauchen 2-3x → 4-6 Monate |
| Availability | ❌ | — |
| Anchoring | ✅ | "2 Monate" ist willkürlich. Kein Data-Modelling, keine Team-Einarbeitung einkalkuliert |
| Scope Creep | ✅ | Was bleibt in Postgres? Was wandert wirklich? Grenzen sind schwammig |

## Commitment
→ DE-RISK: Proof-of-Concept mit 3 Kern-Queries (JOINs, Transaktionen, Pagination)
   auf DynamoDB implementieren bis Freitag 18:00

Warum: Failure #1 (Datenmodell) ist der kritischste. Wenn die 3 Kern-Queries
nicht effizient in DynamoDB abbildbar sind, ist die Migration tot.
→ Top priority: PoC vor weiterer Planung.
```

**Bewertung:**
| Kriterium | Punkte (0-2) |
|-----------|:----------:|
| Base Rates korrekt referenziert | 2/2 |
| Bias Circuit-Breaker aktiv (≥2 Biases) | 2/2 (4/5 getriggert) |
| L/I Matrix mit ≥3 Failure Modes | 2/2 (4 Failure Modes) |
| L×I Scores kalibriert (Base Rate ≈ L=4) | 2/2 |
| Commitment hat Aktion + konkretes Datum | 2/2 |
| **Gesamt Full** | **10/10 🟢** |

**Anmerkung:** Alle 4 Features sauber integriert. Base Rate zitiert, L/I kalibriert, Bias-Check vollständig, Commitment als konkreter DE-RISK-Typ mit Datum.

---

## Test 3: Natural Language Trigger

**Auslöser:** "kill this plan"
**Kontext:** Der User beschreibt "Ich will die ganze Codebase von JavaScript auf TypeScript migrieren."
**Erwartung:**
- ✅ "kill this plan" wird als Trigger erkannt
- ✅ Quick Premortem wird ausgelöst (nicht Full)
- ✅ Context Auto-Detection scannt git log + Branch
- ✅ Plan ist auf 1 Zeile zusammengefasst

**Durchführung:**
```bash
cd ~/dein-projekt
# Claude Code starten, dann:
# User: "Ich will die ganze Codebase von JavaScript auf TypeScript migrieren."
# User: "kill this plan"
```

**Output (Live-Test 14.05.2026):**
```
### Premortem 🔪

Plan: JS-Codebase vollständig auf TypeScript migrieren

#### 1. Most Likely Failure
Scope-Explosion — JS→TS Migration betrifft nicht nur
Dateiendungen, sondern Typdefinitionen, tsconfig,
Build-Tooling (Webpack/Vite), Drittanbieter-Typings (@types/*),
und refactoring von `any`-Typen. "Nur Dateien umbenennen"
ist eine gefährliche Vereinfachung.
L=5 I=3 → 15 🔴 Scope drastisch reduzieren (inkrementell!).

#### 2. Worst-Case Failure
CI/CD und Build-Kette brechen — TypeScript-Compiler
findet echte Typfehler, die in JS nie auffielen.
Plötzlich geht der ganze Build nicht mehr, und niemand
weiß, wie man `tsconfig.json` richtig konfiguriert.
L=3 I=4 → 12 🟠 Migration in Feature-Ordnern testen,
nicht in einem Massen-Commit.

#### 3. Verify Now
Prüfen, ob bestehende JS-Dependencies @types/* haben
und wie tief die `any`-Nutzung in der Codebase ist.
→ cat package.json | grep -c "@types/" 
→ grep -rn ": any\|as any" src/ | wc -l
→ npx typescript --init --checkJs 2>&1 | head -5
```

**Bewertung:**
| Kriterium | Punkte (0-2) |
|-----------|:----------:|
| Context Auto-Detection trifft Plan | 2/2 |
| "Most Likely" ist spezifisch, nicht generisch | 2/2 |
| "Worst-Case" ist plausibel | 2/2 |
| "Verify Now" ist konkret ausführbar | 2/2 |
| Output ≤12 Zeilen | 1/2 (16 Zeilen) |
| **Gesamt Quick** | **9/10 🟢** |

**Anmerkung:** 16 Zeilen — 4 mehr als Ziel. Die drei Verify-Commands brauchen Platz. Der Natural-Language-Trigger "kill this plan" wurde korrekt als Quick Premortem interpretiert (kein Full). Die harte Sprache ("gefährliche Vereinfachung") zeigt, dass der Skill nicht sugarcoated.

---

## Test 4: Edge Case — Trivialer Plan

**Auslöser:** `!pm` (User provoziert)
**Kontext:** Der User sagt nur "Ich ändere eine CSS Farbe von #333 auf #444."
**Erwartung:**
- ✅ Skill erkennt, dass der Plan trivial ist → antwortet kurz oder lehnt Premortem ab
- ❌ Kein Full-Premortem-Overkill
- ❌ Keine generischen Failure Modes

**Durchführung:**
```bash
cd ~/dein-projekt
# Claude Code starten, dann:
# User: "Ich ändere eine CSS Farbe von #333 auf #444."
# User: "!pm"
```

**Output (Live-Test 14.05.2026):**
```
### Premortem 🔪

Plan: CSS-Farbe #333 → #444 in einer Datei ändern

#### 1. Most Likely Failure
Vergessen, alle Vorkommen zu ersetzen — die Farbe
ist in mehreren Komponenten/Seiten definiert.
L=2 I=2 → 4 🟢 Akzeptieren. Keine Mitigation nötig.

#### 2. Worst-Case Failure
Kein Worst-Case plausibel. Eine Farbänderung
ist trivial reversibel.
→ Einfach machen. Premortem hier Overkill.

#### 3. Verify Now
→ grep -rn "#333\|#444" src/ --include="*.css" --include="*.scss"
```

**Bewertung:**
| Kriterium | Punkte (0-2) |
|-----------|:----------:|
| Context Auto-Detection trifft Plan | 2/2 |
| "Most Likely" ist spezifisch, nicht generisch | 2/2 |
| "Worst-Case" erkennt Trivialität | 2/2 |
| "Verify Now" ist konkret ausführbar | 2/2 |
| Premortem kurz gehalten (kein Overkill) | 2/2 |
| **Gesamt Quick** | **10/10 🟢** |

**Anmerkung:** Der Skill erkennt, dass der Plan trivial ist (L=2 I=2 → 🟢). Der Worst-Case sagt explizit "Kein Worst-Case plausibel — einfach machen." Das ist genau die richtige Reaktion: kein Overkill, kein generisches "CSS könnte falsch gerendert werden", sondern ein kurzer Check und die Freigabe zum Weitermachen.

---

## Test 5: Full Premortem — Commitment-Treue

**Auslöser:** `!pm full`
**Kontext:** Der User plant "Wir launchen in 2 Wochen die neue Pricing-Seite ohne A/B-Test."
**Erwartung:**
- ✅ Sycophancy Check: "Würde ich das einem Fremden so sagen?" → harte Sprache
- ✅ Optimism Check: Inside View (2 Wochen) vs Outside View (Base Rate sagt 3-4 Wochen)
- ✅ Availability Check: Ist der Pricing-Launch nur relevant, weil es das aktuelle Projekt ist?
- ✅ Anchoring Check: Ist "2 Wochen" eine willkürliche Zahl?
- ✅ Commitment ist VERIFY-Typ (Annahme validieren, nicht bauen)
- ✅ Commitment hat konkretes Datum < 1 Woche

**Durchführung:**
```bash
cd ~/dein-projekt
# Claude Code starten, dann:
# User: "Wir launchen in 2 Wochen die neue Pricing-Seite ohne A/B-Test."
# User: "!pm full"
```

**Output (Live-Test 14.05.2026):**
```
🔪 FULL PREMORTEM — 6 months from now, this has FAILED.
Plan: Neue Pricing-Seite launch in 2 Wochen ohne A/B-Test

## Failure Modes (3 found)
1. Preisfindung völlig falsch — Base Rate: 90%+ verfehlen
   das Pricing beim ersten Versuch. Ohne A/B-Test zahlst
   du 6-12 Monate Opportunity Cost.
2. Launch ohne User-Feedback — 64% der Features mit <3
   User-Interviews scheitern. Pricing ist das Feature,
   das am MEISTEN User-Feedback braucht.
3. Timeline zu optimistisch — Pricing-Seite klingt einfach,
   betrifft aber Checkout, Styling, Metriken, A/B-Infra,
   Payment-Integration. 2 Wochen → mindestens 4.

## Risk Matrix
| # | Failure | L | I | L×I | Mitigation |
|---|---------|---|---|-----|------------|
| 1 | Pricing falsch | 5 | 5 | 25 | A/B-Test mit 3 Preispunkten an 50 Usern |
| 2 | Kein User-Feedback | 4 | 4 | 16 | 5 User-Interviews vor Build |
| 3 | Timeline überschritten | 4 | 3 | 12 | Plan: 4 Wochen, Launch nach 2 Wochen = Früh |

## Bias Check
| Bias | Status | Korrektur |
|------|--------|-----------|
| Sycophancy | ✅ | "Das ist ein gefährlicher Plan. Pricing ohne A/B-Test zu launchen ist fahrlässig." — kein Politeness-Filter |
| Optimism | ✅ | Inside: 2 Wochen. Outside: Base Rate für vergleichbare UI-Launches = 4-6 Wochen |
| Availability | ✅ | Denkst du, Pricing ist einfach, weil du letzte Woche eine UI-Komponente gebaut hast? Der Pricing-Mechanismus ist das RISIKOREICHSTE Feature |
| Anchoring | ✅ | "2 Wochen" ist komplett willkürlich. Woher kommt diese Zahl? Wer hat sie validiert? |
| Scope Creep | ✅ | Was ist die Pricing-Seite? Nur UI? Inkl. Checkout-Logik? Inkl. Upgrade-Downgrade-Flows? Was ist NICHT drin? |

## Commitment
→ VERIFY: A/B-Test mit 3 Preispunkten ($29/$47/$79) an 50 internen Usern
   implementieren bis Donnerstag 14:00

Warum: Failure #1 (Pricing falsch, L×I=25 🔴) ist der Killer.
Ohne Preisdaten ist der Launch ein Glücksspiel. Der A/B-Test
ist kein Nice-to-have — er IST das Produkt.
→ Top priority: A/B-Test-Infra vor Pricing-UI bauen.
```

**Bewertung:**
| Kriterium | Punkte (0-2) |
|-----------|:----------:|
| Base Rates korrekt referenziert | 2/2 (90%+ Pricing, 64% Features ohne Feedback) |
| Bias Circuit-Breaker aktiv (≥2 Biases) | 2/2 (5/5 getriggert) |
| L/I Matrix mit ≥3 Failure Modes | 2/2 (3 Failure Modes) |
| L×I Scores kalibriert (L=5 I=5 = 25 für Pricing) | 2/2 |
| Commitment hat Aktion + konkretes Datum | 2/2 (VERIFY-Typ, Donnerstag 14:00) |
| **Gesamt Full** | **10/10 🟢** |

**Anmerkung:** Stärkster Test. Der Sycophancy-Check produziert harte Sprache ("gefährlich", "fahrlässig"). Der Optimism-Check kalibriert 2→4 Wochen. Der Availability-Check hinterfragt, ob das letzte Projekt das Urteil verzerrt. Der Anchoring-Check dekonstruiert die "2 Wochen"-Zahl. Das Commitment ist VERIFY-Typ mit konkretem Datum (<1 Woche) und 3 Preispunkten.

---

## Ergebnisse

| # | Szenario | Datum | Output | L/I korrekt? | Format eingehalten? | Score |
|---|----------|-------|--------|-------------|-------------------|:----:|
| 1 | Auth-Refactoring | 14.05.2026 | ✅ Live | ✅ L=4/I=4, L=3/I=5 | ⚠️ 14 statt 12 Zeilen | **9/10** |
| 2 | DB-Migration | 14.05.2026 | ✅ Live | ✅ Alle 4 kalibriert | ✅ Full-Format | **10/10** |
| 3 | JS→TS Migration | 14.05.2026 | ✅ Live | ✅ L=5/I=3, L=3/I=4 | ⚠️ 16 statt 12 Zeilen | **9/10** |
| 4 | CSS-Farbe | 14.05.2026 | ✅ Live | ✅ L=2/I=2 — Trivial erkannt | ✅ Kein Overkill | **10/10** |
| 5 | Pricing ohne A/B | 14.05.2026 | ✅ Live | ✅ L=5/I=5 = 25 🔴 | ✅ Full-Format | **10/10** |

---

## Evaluations-Kriterien

### Quick Premortem (Tests 1, 3, 4)
| Kriterium | Test 1 | Test 3 | Test 4 |
|-----------|:------:|:------:|:------:|
| Context Auto-Detection trifft Plan | 2/2 | 2/2 | 2/2 |
| "Most Likely" ist spezifisch, nicht generisch | 2/2 | 2/2 | 2/2 |
| "Worst-Case" ist plausibel | 2/2 | 2/2 | 2/2 |
| "Verify Now" ist konkret ausführbar | 2/2 | 2/2 | 2/2 |
| Output ≤12 Zeilen | 1/2 | 1/2 | 2/2 |
| **Gesamt Quick** | **9/10** | **9/10** | **10/10** |

### Full Premortem (Tests 2, 5)
| Kriterium | Test 2 | Test 5 |
|-----------|:------:|:------:|
| Base Rates korrekt referenziert | 2/2 | 2/2 |
| Bias Circuit-Breaker aktiv (≥2 Biases) | 2/2 | 2/2 |
| L/I Matrix mit ≥3 Failure Modes | 2/2 | 2/2 |
| L×I Scores kalibriert (Base Rate ≈ L=4) | 2/2 | 2/2 |
| Commitment hat Aktion + konkretes Datum | 2/2 | 2/2 |
| **Gesamt Full** | **10/10** | **10/10** |

### Gesamt-Durchschnitt
| Test | Score |
|------|:----:|
| Test 1: Quick — Auth-Refactoring | **9/10 🟢** |
| Test 2: Full — DB-Migration | **10/10 🟢** |
| Test 3: Quick — JS→TS Migration | **9/10 🟢** |
| Test 4: Quick — CSS-Farbe (Edge) | **10/10 🟢** |
| Test 5: Full — Pricing ohne A/B | **10/10 🟢** |
| **Durchschnitt** | **9.6/10 🟢** |

### Bewertungsskala
| Score | Bedeutung |
|-------|-----------|
| 9-10 | 🟢 Skill tut, was er verspricht |
| 6-8 | 🟡 Verbesserungswürdig (Abweichungen dokumentieren) |
| 0-5 | 🔴 Kritische Mängel — Skill braucht Überarbeitung |
