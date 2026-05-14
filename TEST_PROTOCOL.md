# TEST_PROTOCOL: Premortem-Skill in Aktion

> **Ziel:** 5 dokumentierte Testszenarien, die zeigen, ob der Skill tut, was er verspricht.
> **Status:** ⬜ Noch nicht getestet — definiert die Testfälle für zukünftige Läufe.
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
- ✅ "Verify Now" ist ein konkreter Command (z.B. `npm run test:auth`)
- ✅ Output-Fformat eingehalten (~8-12 Zeilen)
- ❌ Kein Full-Premortem-Overkill (kein Bias Circuit-Breaker, kein Commitment)

**Durchführung:**
```bash
cd ~/dein-projekt
# Claude Code starten, dann:
# User: "Ich muss das Auth-Modul von JWT auf Session-Tokens migrieren."
# User: "!pm"
```

**Platz für Output:**
```

```

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

**Platz für Output:**
```

```

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

## Ergebnisse (auszufüllen nach Tests)

| # | Szenario | Datum | Output | L/I korrekt? | Format eingehalten? | Anmerkungen |
|---|----------|-------|--------|-------------|-------------------|-------------|
| 1 | Refactoring | — | — | — | — | — |
| 2 | DB-Migration | — | — | — | — | — |
| 3 | TS-Migration | — | — | — | — | — |
| 4 | CSS-Änderung | — | — | — | — | — |
| 5 | Pricing-Launch | — | — | — | — | — |

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
