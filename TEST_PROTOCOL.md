# TEST_PROTOCOL: Premortem-Skill in Aktion

> **Ziel:** 5 dokumentierte Testszenarien, die zeigen, ob der Skill tut, was er verspricht.
> **Status:** ⬜ Test 1 & 2 durchgeführt — 3, 4, 5 offen.
> **Beitragen:** Führe einen Test aus und erstelle einen PR mit deinem Output.

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

**Platz für Output:**
```

```

---

## Test 4: Edge Case — Trivialer Plan

**Auslöser:** `!pm` (User provoziert)
**Kontext:** Der User sagt nur "Ich ändere eine CSS Farbe von #333 auf #444."
**Erwartung:**
- ✅ Skill erkennt, dass der Plan trivial ist → antwortet kurz oder lehnt Premortem ab
- ❌ Kein Full-Premortem-Overkill
- ❌ Keine generischen Failure Modes

**Platz für Output:**
```

```

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

**Platz für Output:**
```

```

---

## Ergebnisse

| # | Szenario | Datum | Output | L/I korrekt? | Format eingehalten? | Anmerkungen |
|---|----------|-------|--------|-------------|-------------------|-------------|
| 1 | Auth-Refactoring | 14.05.2026 | ✅ Live | ✅ L=4 / I=4 / L=3 / I=5 | ⚠️ 14 statt 12 Zeilen | Grep-Commands brauchen 2 Zeilen |
| 2 | DB-Migration | 14.05.2026 | ✅ Live | ✅ Alle 4 Failure Modes | ✅ Full-Format komplett | 10/10 🟢 |
| 3 | TS-Migration | — | ⬜ | — | — | — |
| 4 | CSS-Änderung | — | ⬜ | — | — | — |
| 5 | Pricing-Launch | — | ⬜ | — | — | — |

---

## Evaluations-Kriterien

### Quick Premortem (Tests 1, 3, 4)
| Kriterium | Punkte (0-2) |
|-----------|:----------:|
| Context Auto-Detection trifft Plan | /2 |
| "Most Likely" ist spezifisch, nicht generisch | /2 |
| "Worst-Case" ist plausibel | /2 |
| "Verify Now" ist konkret ausführbar | /2 |
| Output ≤12 Zeilen | /2 |
| **Gesamt Quick** | **/10** |

### Full Premortem (Tests 2, 5)
| Kriterium | Punkte (0-2) |
|-----------|:----------:|
| Base Rates korrekt referenziert | /2 |
| Bias Circuit-Breaker aktiv (≥2 Biases) | /2 |
| L/I Matrix mit ≥3 Failure Modes | /2 |
| L×I Scores kalibriert (Base Rate ≈ L=4) | /2 |
| Commitment hat Aktion + konkretes Datum | /2 |
| **Gesamt Full** | **/10** |

### Bewertungsskala
| Score | Bedeutung |
|-------|-----------|
| 9-10 | 🟢 Skill tut, was er verspricht |
| 6-8 | 🟡 Verbesserungswürdig (Abweichungen dokumentieren) |
| 0-5 | 🔴 Kritische Mängel — Skill braucht Überarbeitung |
