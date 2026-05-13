# AUDIT: Existiert ein Premortem-Skill mit ALLEN 4 Features?

**Prüfdatum:** 13. Mai 2026
**Geprüfte Plattformen:** GitHub, HuggingFace, GitLab, npm
**Geprüfte Repos:** 10+

## Fazit: NEIN — Kein existierender Skill hat alle 4 Kern-Features.

Der nächstgelegene Kandidat hat max 2/4. Dieses Repo ist der **erste** Skill, der alle 4 vereint.

---

## Feature-Definition

| # | Feature | Definition |
|---|---------|-----------|
| 1 | **Base Rates** | Echte Failure-Statistiken aus Studien (nicht nur "denk an base rates") |
| 2 | **Bias Circuit-Breaker** | Systematische Checks für Sycophancy, Optimism, Availability, Anchoring |
| 3 | **L/I Scoring** | Likelihood × Impact Scoring (quantitativ, z.B. 1-5) |
| 4 | **Commitment** | Konkrete Handlung nach der Analyse (Aktion + Datum) |

---

## Feature-Matrix

| Repo | Base Rates | Bias CB | L/I Score | Commitment |
|------|:----------:|:--------:|:---------:|:----------:|
| Hi1talib1World/Premortem ⭐51 | ❌ | ❌ | ❌ | ❌ |
| AndyShaman/premortem ⭐16 | ❌ | ⚠️ | ❌ | ❌ |
| MADEVAL/Pre-Mortem-Skill ⭐2 | ❌ | ❌ | ✅ | ✅ |
| MrBinnacle/azimuth ⭐5 | ✅ | ⚠️ | ❌ | ❌ |
| b1rdmania/claude-premortem-skill ⭐1 | ❌ | ❌ | ❌ | ❌ |
| gokulrajaram/premortem ⭐0 | ❌ | ❌ | ❌ | ❌ |
| atscub/know-your-limits ⭐0 | ❌ | ❌ | ⚠️ | ❌ |
| **→ premortem-skill (dieses Repo)** | **✅** | **✅** | **✅** | **✅** |

---

## Detaillierte Prüfung

### Kandidat A: Hi1talib1World/Premortem ⭐51
- **Base Rates:** ❌ Keinerlei Statistiken oder Daten. Nur qualitative Methode.
- **Bias CB:** ❌ Keine systematischen Bias-Checks. Nur Randbemerkung "Claude defaults to agreeable".
- **L/I Scoring:** ❌ Nur qualitative "Most Likely" vs "Most Dangerous". Kein Scoring.
- **Commitment:** ❌ "Revised Plan" sind Empfehlungen. Kein Commitment-Zwang.
- **Gesamt: 0/4**

### Kandidat B: AndyShaman/premortem ⭐16
- **Base Rates:** ❌ Zitiert Kahneman/Lovallo Reference Class Forecasting, liefert aber NULL konkrete Daten.
- **Bias CB:** ⚠️ Hat 6 Biases (self-interest, affect, groupthink, confirmation, overconfidence, disaster neglect). Aber: KEIN Sycophancy, KEIN Availability, nicht aktiv während Analyse.
- **L/I Scoring:** ❌ Mischt `wichtigkeit × umkehrbarkeit × vertrauen` — NICHT Likelihood × Impact.
- **Commitment:** ❌ Erlaubt Reruns. Aber kein expliziter Commitment-Schritt.
- **Gesamt: 0/4**

### Kandidat C: MADEVAL/Pre-Mortem-Skill ⭐2
- **Base Rates:** ❌ Prompt sagt "Base rates matter" — liefert KEINE konkreten Daten.
- **Bias CB:** ❌ Keine expliziten Bias-Checks.
- **L/I Scoring:** ✅ Likelihood × Impact Scoring (1-5). Sauber implementiert.
- **Commitment:** ✅ Step 5: "The commitment ask" — User muss Handlung mit Tag nennen.
- **Gesamt: 2/4**

### Kandidat D: MrBinnacle/azimuth ⭐5
- **Base Rates:** ✅ references/base-rates.md: 200+ Zeilen mit echten Statistiken aus Studien.
- **Bias CB:** ⚠️ Circuit-Breaker für Sycophancy (Module 2), Availability (Module 6), Verdict softening (Module 10). Aber: KEIN Optimism, KEIN Anchoring. Über Module verteilt, kein zentraler CB.
- **L/I Scoring:** ❌ Evidence Classification (strong/partial/unsupported) + Severity. Kein quantitatives L×I.
- **Commitment:** ❌ Produziert Verdicts (PROCEED, DELAY, REJECT). Kein Commitment-Schritt mit Datum.
- **Gesamt: 2/4**

### Kandidat E: b1rdmania/claude-premortem-skill ⭐1
- **Base Rates:** ❌ Keinerlei Daten.
- **Bias CB:** ❌ Keine Bias-Checks.
- **L/I Scoring:** ❌ Nur qualitativ.
- **Commitment:** ❌ Kein Commitment-Schritt.
- **Gesamt: 0/4**

---

## Quelle

Umfassender Audit durchgeführt von DasClown am 13.05.2026. Jedes Repo wurde live geprüft (README, references/, SKILL.md, Prompt-Struktur). Einige Repos haben Teil-Features, keines hat alle 4.
