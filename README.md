# 🔪 premortem-skill

[![Claude Code](https://img.shields.io/badge/Claude_Code-Skill-7C3AED?logo=anthropic&logoColor=white)](https://github.com/DasClown/premortem-skill)
[![GitHub release](https://img.shields.io/github/v/release/DasClown/premortem-skill?logo=github&color=blue)](https://github.com/DasClown/premortem-skill/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Test Protocol](https://img.shields.io/badge/tests-5_✓_9.6/10-brightgreen)](TEST_PROTOCOL.md)
[![GitHub Discussions](https://img.shields.io/badge/💬_Discussions-ask_questions-blue)](https://github.com/DasClown/premortem-skill/discussions)
[![Topics: claude-code premortem](https://img.shields.io/badge/topics-claude_code|premortem-lightgrey)](https://github.com/topics/claude-code)

**Kill bad plans before they kill you.**

> *Denk dir Dinge zuende. Sei kritisch mit dir selbst.*

Der **vollständigste** Premortem-Skill, der **alle 4 Kern-Features** vereint — optimiert für Claude Code während der Arbeit.

---

## Dritt-Test gesucht 🔍

Alle 5 Tests im [`TEST_PROTOCOL.md`](TEST_PROTOCOL.md) wurden vom Autor selbst durchgeführt. Das ist methodisch begrenzt — ein Test von einer anderen Person wäre der nächste Qualitätssprung.

**So hilfst du:**
1. Installiere den Skill (`git clone ...`)
2. Ruf `!pm` oder `!pm full` in Claude Code auf
3. Kopiere den Output in [`TEST_PROTOCOL.md`](TEST_PROTOCOL.md) (als Test 6 oder in einen neuen PR)
4. Mach einen Pull Request

**Oder noch einfacher:** Schick mir den Output per Issue/DM. 5 Minuten Arbeit, fundamentaler Unterschied für die Glaubwürdigkeit.

---

## Was macht das hier anders?

**Audit (Mai 2026):** 10+ Repos auf GitHub, HuggingFace, GitLab und npm geprüft. Kein einziges hatte mehr als **2 von 4** Features. Die Analyse steht im [AUDIT.md](AUDIT.md).

> **Anmerkung:** Der Audit ist eine **Selbsteinschätzung** des Autors, keine unabhängige Dritt-Prüfung. Die Feature-Definitionen wurden vor der Prüfung festgelegt, was die Bewertung potenziell begünstigt. Details und Einschränkungen stehen im [AUDIT.md](AUDIT.md).

| Repo | Base Rates | Bias CB | L/I Score | Commitment |
|------|:----------:|:--------:|:---------:|:----------:|
| Hi1talib1World/Premortem ⭐51 | ❌ | ❌ | ❌ | ❌ |
| AndyShaman/premortem ⭐16 | ❌ | ⚠️ | ❌ | ❌ |
| MADEVAL/Pre-Mortem-Skill ⭐2 | ❌ | ❌ | ✅ | ✅ |
| MrBinnacle/azimuth ⭐5 | ✅ | ⚠️ | ❌ | ⚠️ |
| **→ premortem-skill** | **✅** | **✅** | **✅** | **✅** |

---

## Install (30 Sekunden)

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/DasClown/premortem-skill.git ~/.claude/skills/premortem
```

Oder als Git-Submodul:
```bash
git submodule add https://github.com/DasClown/premortem-skill.git .claude/skills/premortem
```

Kein Package-Manager, keine Dependencies, keine Config. Klonen → loslegen.

---

## Usage

### 🔸 Quick Premortem — 30 Sekunden
```bash
!pm
```
3 Fragen für den Alltag während des Codens. Kein Wizard, kein PDF, kein HTML.

| Frage | Was es aufdeckt |
|-------|----------------|
| Most Likely Failure | Den Fehler, der garantiert passiert |
| Worst-Case Failure | Den, der richtig weh tut (auch wenn unwahrscheinlich) |
| Verify Now | Eine Sache, die du SOFORT checken kannst |

### 🔸 Full Premortem — 2 Minuten
```bash
!pm full
```
Alle 4 Features: Base Rates → Bias Check → L/I Matrix → Commitment.

### 🔸 Natural Language
- "premortem this"
- "kill this plan"
- "stress test this approach"
- "what could go wrong"

---

## Die 4 Features im Detail

### 1. Base Rates 🎲
Echte Failure-Statistiken aus Studien. Nicht "denk an Base Rates" — sondern konkrete Zahlen:

| Entscheidungsklasse | Base Rate | Quelle |
|---------------------|-----------|--------|
| Software-Projekt überschreitet Timeline | **70%** | Standish CHAOS |
| Refactoring braucht 2-3x Schätzung | **64%+** | IEEE |
| Feature wird nie genutzt | **45%** | Standish / Microsoft Research |
| Produkt-Launch scheitert | **70-95%** | Nielsen |
| Startup überlebt 5 Jahre | **50%** | BLS |
| Fehleinstellung (<18 Monate) | **40-50%** | HBR / Leadership IQ |

> **Hinweis:** Alle Base Rates sind mit Quellen belegt — siehe [`references/base-rates.md`](references/base-rates.md) für DOIs und konkrete Links. Einige Quellen sind kommerzielle Reports ohne DOI; die Grenzen sind dort dokumentiert.

### 2. Bias Circuit-Breaker 🛑

| Bias | Check | Korrektur |
|------|-------|-----------|
| Sycophancy | "Würde ich das einem Fremden so hart sagen?" | Politeness-Filter raus |
| Optimism | "Inside View vs. Outside View?" | Base Rate als Korrektur |
| Availability | "Denke ich das nur, weil ich's letzte Woche gebaut habe?" | Evidenz verlangen |
| Anchoring | "Woher kommt diese Zahl?" | Unabhängige Schätzung |
| Scope Creep | "Was ist NICHT Teil dieses Plans?" | Done-Definition + Exclusions |

### 3. L/I Scoring 📊

Jeder Failure Mode kriegt **Likelihood (1-5) × Impact (1-5)**:

| L×I | Zone | Aktion |
|-----|------|--------|
| 1-4 | 🟢 Grün | Akzeptieren |
| 5-8 | 🟡 Gelb | Monitoring |
| 9-12 | 🟠 Orange | Mitigation nötig |
| 15-25 | 🔴 Rot | STOP. Plan ändern. |

### 4. Commitment 🎯

Kein "vielleicht", kein "consider", kein "in Zukunft". EIN konkreter Satz:

> ✅ Integration-Tests für Payment-Flow schreiben bis **Donnerstag 18:00**
> ❌ "Mehr testen"

---

## Beispiel: Quick Premortem

```
🔪 PREMORTEM
Plan: Refactoring auth module from JWT to session tokens

1. Most Likely → Timeline undercounted
   Base Rate: 64% der Refactors überschreiten um 50%+
   Realistische Schätzung: 3-4 Wochen statt 2

2. Worst-Case → Session invalidation bricht alle aktiven User
   Impact: Alle User müssen neu einloggen
   Customer Support wird überschwemmt

3. Verify NOW → Integration-Tests gegen Staging mit echten Session-Daten
   → npm run test:session-migration
```

---

## Was passiert, wenn du `!pm` sagst?

1. **Context Scan** — Aktuelle Konversation + git log + changed files
2. **Plan identifizieren** — Automatisch oder eine kurze Rückfrage
3. **Quick (30s)** → 3 Antworten, Output ~8 Zeilen
4. **Full (2min)** → 4 Features, Output ~20 Zeilen

---

## Pro-Tipp

**Gewohnheit aufbauen:** Vor jedem `git commit -m "refactor"` → `!pm`. Vor jedem `git push` mit Breaking Changes → `!pm full`. 30 Sekunden jetzt sparen Stunden später.

*Der Premortem ist nicht zum Pessimismus da — sondern zur Ehrlichkeit, bevor die Realität sie von dir erzwingt.*

---

## Struktur

```
premortem-skill/
├── SKILL.md                          # Main Skill (Claude Code)
├── AUDIT.md                          # Vollständiger Markt-Audit (Mai 2026)
├── README.md                         # Diese Datei
├── TEST_PROTOCOL.md                  # 5 dokumentierte Testszenarien
├── LICENSE                           # MIT
└── references/
    ├── base-rates.md                 # 25+ Failure-Statistiken + Worked Example + Quellen mit DOIs
    ├── bias-circuit-breaker.md       # 5 systematic checks (inkl. Scope Creep)
    ├── li-scoring.md                 # Likelihood × Impact + Tie-Break-Regel
    └── commitment.md                 # Action + Date + Follow-up-Logik
```

---

## Known Issues & Offene Punkte

### 🔶 GitHub Language Detection braucht Neu-Scan
Nach Löschung aller Nicht-Markdown-Dateien zeigt GitHub beim nächsten Push korrekt 100% Markdown an.

### 🔶 Alle 5 Tests im TEST_PROTOCOL live durchgeführt
Quick-Schnitt: 9.3/10, Full-Schnitt: 10/10. Tests 3-5 sind jetzt ebenfalls mit Output dokumentiert. Ergebnisse im [`TEST_PROTOCOL.md`](TEST_PROTOCOL.md).

### 🔶 Base Rates brauchen unabhängige Validierung
Die Failure-Statistiken sind aus öffentlichen Quellen zusammengetragen, aber nicht eigenständig repliziert. Einige Quellen (Standish CHAOS, Nielsen) sind kommerzielle Reports mit methodischen Kontroversen. Siehe [`references/base-rates.md`](references/base-rates.md) für Diskussion.

### 🔶 Kein Evaluations-Framework für Skill-Qualität
Wie oft liefert Claude bei `!pm` das dokumentierte Format? Ein automatischer Evaluator existiert in der GitHub Actions, prüft aber nur Frontmatter + Dateiexistenz, nicht Output-Qualität. Ein Prompt-Evaluator wäre wünschenswert.

---

## Verwandt

- [MrBinnacle/azimuth](https://github.com/MrBinnacle/azimuth) — Hat Base Rates + teilweise Bias (2/4). Hat ein interessantes Verdict-System (PROCEED/DELAY/REJECT).
- [MADEVAL/Pre-Mortem-Skill](https://github.com/MADEVAL/Pre-Mortem-Skill) — Hat L/I + Commitment (2/4)
- Kahneman, *Thinking, Fast and Slow*
- Klein, *"Performing a Project Premortem"* (HBR 2007)
- Tetlock, *Superforecasting*

---

## License

MIT © 2026 DasClown
