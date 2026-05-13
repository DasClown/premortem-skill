# L/I Scoring — Likelihood × Impact Matrix

> Qualitative "könnte passieren" reicht nicht. Jeder Failure Mode braucht ein quantitatives L × I Score. Sonst werden seltene Katastrophen und häufige Kleinigkeiten gleich behandelt.

---

## Scoring-Anker

### Likelihood (L) — Wie wahrscheinlich ist dieser Failure?

| Score | Label | Heuristik | Beispiel |
|-------|-------|-----------|----------|
| 1 | Rare | <5% Chance | Externer API-Ausfall am selben Tag wie dein Launch |
| 2 | Unlikely | 5-20% Chance | Spezifische Race Condition in einer selten genutzten Code-Path |
| 3 | Possible | 20-50% Chance | Migration bricht bei Edge-Case-Daten (15% der User) |
| 4 | Likely | 50-80% Chance | Timeline unterschätzt (Base Rate: 70% der Projekte) |
| 5 | Near-Certain | >80% Chance | Keine Tests → Bugs in Production |

**Entscheidungshilfe:** Wenn du "könnte passieren" denkst → mindestens 3. Wenn du "passiert safe" denkst → 5.

### Impact (I) — Wenn es passiert, wie schlimm?

| Score | Label | Konsequenz |
|-------|-------|-----------|
| 1 | Negligible | Kosmetischer Bug. Niemand beschwert sich. |
| 2 | Minor | Etwas Nacharbeit. Kein User-Impact. Behebbar in <1 Tag. |
| 3 | Moderate | User sehen es. Verzögerung um Tage. Reputations-Dämpfer. |
| 4 | Major | Signifikanter Datenverlust/Revenue-Verlust. Behebung braucht >1 Woche. |
| 5 | Catastrophic | Projekt-Tod. Unwiederbringlicher Datenverlust. Rechtliche Konsequenzen. |

---

## L×I Matrix

```
          IMPACT →
          1    2    3    4    5
L  1     1    2    3    4    5
I  2     2    4    6    8   10
K  3     3    6    9   12   15
E  4     4    8   12   16   20
L  5     5   10   15   20   25
↓
```

### Bereiche

| L×I | Zone | Aktion |
|-----|------|--------|
| 1-4 | 🟢 Grün | Akzeptieren. Keine aktive Mitigation nötig. |
| 5-8 | 🟡 Gelb | Monitoring. Early Warning Signs definieren. |
| 9-12 | 🟠 Orange | Mitigation erforderlich. Konkrete Aktion vor Deadline. |
| 15-25 | 🔴 Rot | STOP. Nicht fortfahren ohne signifikante Planänderung. |

---

## Output-Format

```
## Risk Matrix
| # | Failure | L | I | L×I | Zone | Mitigation |
|---|--------|---|---|-----|------|------------|
| 1 | Auth migration takes 3x estimate | 4 | 4 | 16 | 🔴 | Write migration script + dry-run first |
| 2 | Session tokens invalidated | 3 | 3 | 9 | 🟠 | Dual-write tokens during migration |
| 3 | DB rollback fails | 2 | 5 | 10 | 🟠 | Test rollback on staging 3x |
| 4 | Old API clients can't auth | 2 | 3 | 6 | 🟡 | Deprecation notice + grace period |
```

---

## Regeln

1. **Jeder Failure Mode kriegt L UND I.** Keine Ausnahmen.
2. **Kalibriere L mit Base Rates:** Wenn die Base Rate 70% sagt → L = 4, nicht 2.
3. **Kalibriere I mit worst case, nicht best case:** "Könnte schlimm sein" → 4, nicht 2.
4. **Zwei 🔴 = STOP.** Bei zwei roten Einträgen: Plan grundlegend überdenken.
5. **Kein Failure Mode mit L=5 und I=5 gleichzeitig.** Wenn beides maximal = unseriöse Analyse.
