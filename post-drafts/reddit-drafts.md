# Reddit-Post-Drafts für premortem-skill

---

## Variante A: r/ClaudeCode — technisch, direkt

**Titel:** Ich habe 10 Premortem-Skills für Claude Code auditiert — keiner hatte alle 4 Kern-Features. Also hab ich einen gebaut.

**Body:**

Ich wollte einen Premortem-Skill für Claude Code, der nicht nur sagt "denk an Base Rates", sondern sie liefert. Nach einem Audit von 10+ Repos auf GitHub, HuggingFace und GitLab war das Ergebnis ernüchternd:

| Repo | Base Rates | Bias Check | L/I Score | Commitment |
|------|:----------:|:----------:|:---------:|:----------:|
| azimuth (⭐5) | ✅ | ⚠️ | ❌ | ❌ |
| Pre-Mortem-Skill (⭐2) | ❌ | ❌ | ✅ | ✅ |
| Alle anderen | ❌ | ❌ | ❌ | ❌ |

Kein einziges hatte mehr als 2/4 Features. Also hab ich einen Skill gebaut, der alle 4 vereint:

**1. Base Rates 🎲**
Kein "denk an Base Rates" — echte Zahlen mit Quellen:
- 70% der Software-Projekte überschreiten die Timeline (Standish CHAOS)
- 64% der Refactorings brauchen 50%+ mehr Zeit (IEEE Access, DOI: 10.1109/ACCESS.2021.3054321)
- 90%+ der Pricing-Modelle sind beim ersten Versuch falsch (Price Intelligently)

**2. Bias Circuit-Breaker 🛑**
5 systematische Checks: Sycophancy, Optimism, Availability, Anchoring, Scope Creep. Läuft automatisch nach der Failure-Generierung.

**3. L/I Scoring 📊**
Jeder Failure Mode kriegt Likelihood (1-5) × Impact (1-5). L×I ≥ 12 = Mitigation nötig, ≥ 15 = STOP.

**4. Commitment 🎯**
Kein "vielleicht", kein "consider". EIN konkreter Satz: "[Aktion] bis [Datum]".

**Install:**
```bash
git clone https://github.com/DasClown/premortem-skill.git ~/.claude/skills/premortem
# dann in Claude Code: !pm oder !pm full
```

Ich hab 5 Live-Tests durchgeführt — Quick: 9.3/10, Full: 10/10.
→ [TEST_PROTOCOL.md](https://github.com/DasClown/premortem-skill/blob/main/TEST_PROTOCOL.md)

Würde mich freuen, wenn jemand einen Dritt-Test macht und den Output hier oder im Repo postet.

[github.com/DasClown/premortem-skill](https://github.com/DasClown/premortem-skill)

---

## Variante B: r/programming — Story-Winkel, breiter

**Titel:** I built a Claude Code skill that runs a Kahneman premortem on your plans. Here's why 70% of projects need it.

**Body:**

6 months from now, your current project has failed. Why?

That's the premortem — Kahneman's single most valuable decision tool. Instead of asking "will this work?", you imagine it already failed and work backwards.

I audited 10+ existing premortem skills on GitHub. None had all the features I wanted — most were just qualitative checklists. So I built one that integrates **real failure statistics**, **bias detection**, **quantitative risk scoring**, and **concrete commitments**.

The base rates alone are sobering:
- **70%** of software projects blow their timeline (Standish CHAOS)
- **64%** of refactors exceed estimates by 50%+ (IEEE)
- **45%** of features deployed never get used (Standish)
- **70-95%** of product launches fail (Nielsen)

Even scarier: Inside view (your estimate) is **always** more optimistic than outside view (base rate). The skill forces the outside view.

It works in Claude Code as `!pm` (30 seconds) or `!pm full` (2 minutes, all 4 features). I ran 5 test scenarios — average score: 9.6/10.

Looking for third-party testers to validate. If you use Claude Code, try it and tell me what breaks.

[https://github.com/DasClown/premortem-skill](https://github.com/DasClown/premortem-skill)

---

## Variante C: r/SideProject — kurz, persönlich

**Titel:** Ich hab einen Claude-Code-Skill gebaut, der schlechte Pläne killt. 5 Live-Tests, 9.6/10.

**Body:**

Kurzer Side-Project-Showcase:

Ich hab einen Premortem-Skill für Claude Code gebaut. Er checkt deinen Plan gegen:
1. Echte Failure-Statistiken (nicht "denk dran", sondern konkrete Zahlen)
2. 5 kognitive Biases (Sycophancy, Optimism, Availability, Anchoring, Scope Creep)
3. L/I-Scoring (Likelihood × Impact, jeder Failure Mode)
4. Commitment-Zwang (eine konkrete Handlung mit Datum)

5 Testszenarien live durchgeführt:
- Quick Premortem Auth-Refactoring: 9/10
- Full Premortem DB-Migration: 10/10
- Full Premortem Pricing-Launch ohne A/B-Test: 10/10

**Install:**
```bash
git clone https://github.com/DasClown/premortem-skill.git ~/.claude/skills/premortem
```

Feedback und Dritt-Tests sehr willkommen!

---

## Posting-Hinweise

- **Bild anhängen:** Screenshot des Full-Premortem-Outputs (sieht gut aus mit den 🔴🟠🟢 Icons)
- **Timing r/ClaudeCode:** Beliebig, Sub ist aktiv
- **Timing r/programming:** Di/Do 11:00 US Eastern, kein Show HN-Tag (Show HN ist für HN)
- **KEIN** Link-Farming: Post nur in 1-2 Subs, nicht crossposten
- **Profil-Pflege:** Vorher im Sub kommentieren, nicht nur posten
