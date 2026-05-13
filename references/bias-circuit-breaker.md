# Bias Circuit-Breaker — Systematische Verzerrungs-Kontrolle

> Das Problem: Claude (und Menschen) *defaulten zu agreeable*. Wenn du fragst "ist mein Plan gut?" sucht das System nach Gründen für "ja". Der Circuit-Breaker unterbricht diesen Default — systematisch, jedes Mal.

---

## Die Biases

| Bias | Was es ist | Symptom im Output |
|------|-----------|-------------------|
| **Sycophancy** | Zu nett sein. Zustimmen, was der User hören will. | "Das ist ein solider Plan. Ein paar kleine Risiken, aber..." |
| **Optimism** | Inside View zu optimistisch. "Diesmal ist es anders." | "In 2 Wochen fertig" — Base Rate sagt 5 Wochen. |
| **Availability** | Letztes Projekt/Erlebnis dominiert Einschätzung. | "Das ging letztes Mal auch gut" (N=1, Survivorship Bias). |
| **Anchoring** | Erste Zahl/Ziel dominiert, unzureichende Adjustierung. | "Wir haben 10k Budget gesagt, also..." — nie hinterfragt. |
| **Scope Creep** (Bonus) | Keine Grenzen definiert. Das Projekt wächst unkontrolliert. | "Ich baue schnell ein Auth-Modul" — 6 Wochen später ist es ein Identity-Platform. |

---

## Circuit-Breaker Protokoll (AUTOMATISCH nach Failure-Generierung)

### CB-1: Sycophancy Break

**Frage:** Würde ich diesen Failure Mode einem Fremden genauso hart sagen?

**Test:**
- Schreibe den härtesten Failure Mode um — nimm ALLE Höflichkeitsfilter raus.
- Wenn der umgeschriebene Text deutlich anders klingt → Sycophancy aktiv.
- Korrigiere: Verwende die harte Version.

```
Vorher: "The timeline might be slightly optimistic given the complexity of the auth migration."
Nachher: "This timeline is fantasy. Auth migrations ALWAYS take 2-3x the estimate. You're planning for the happy path."
```

**Wenn Sycophancy getriggert:** 
> ⚠️ **Sycophancy detected.** Rewriting failure modes without politeness filter.

### CB-2: Optimism Break

**Frage:** Was sagt die Outside View?

**Test:**
- Outside View = "Wenn 100 Teams dieses Projekt machen, wie viele schaffen es in dieser Zeit?"
- Inside View = "Wir schaffen das in 2 Wochen weil [Gründe]"
- Wenn Inside View > Outside View um Faktor 1.5x oder mehr → Optimism aktiv.
- Verwende OUTSIDE VIEW als Basis.

```
Inside: "2 Wochen weil wir nur den Auth-Teil anfassen."
Outside: Base Rate = 64% der Refactorings überschreiten um 50%+. 2 Wochen → mind. 3 Wochen.
→ Outside View schlägt Inside View.
```

**Wenn Optimism getriggert:** 
> ⚠️ **Optimism bias detected.** Inside view: [X]. Outside view (base rate): [Y]. Recalibrating to outside view.

### CB-3: Availability Break

**Frage:** Ist dieser Failure Mode real, oder ist er das letzte Projekt, an das ich denke?

**Test:**
- Gibt es EVIDENZ für diesen Failure Mode, oder ist er "weil es mir gerade einfällt"?
- Hätte ich diesen Failure Mode auch letzte Woche genannt?
- Wenn der Failure Mode exakt wie das letzte Projekt klingt → Availability aktiv.
- Entweder mit Daten untermauern ODER streichen.

```
"Das API-Rate-Limiting wird zum Problem."
→ Denkst du das, weil das letzte Projekt Rate-Limiting-Probleme hatte? Oder weil es spezifische Evidenz gibt?
```

**Wenn Availability getriggert:** 
> ⚠️ **Availability bias suspected.** [Failure mode] resembles recent experience. Verifying with data.

### CB-4: Anchoring Break

**Frage:** Habe ich mich von einer willkürlichen Startzahl leiten lassen?

**Test:**
- Woher kommt die erste Zahl/Annahme? (Budget, Timeline, Teamgröße)
- Wurde sie jemals validiert?
- Wenn nein → Re-anchor mit einer unabhängigen Schätzung (z.B. Base Rate × Komplexität).

```
"Das wird ca. 5k Token kosten."
→ Warum 5k? Weil das die Default-Annahme ist? Oder basierend auf ähnlichen Projekten?
→ Re-anchor: Analoge Projekte liegen bei 15-25k Token.
```

**Wenn Anchoring getriggert:** 
> ⚠️ **Anchoring bias detected.** Initial estimate [X] appears unvalidated. Re-anchoring with reference class data: [Y].

### CB-5: Scope Creep Check (Bonus)

**Frage:** Ist der Plan so abgegrenzt, dass er NICHT wächst?

**Test:**
- Wurde definiert, was NICHT Teil dieses Projekts ist?
- Gibt es eine klare "Done"-Definition?
- Sind Out-of-Scope-Items explizit dokumentiert?

```
"Ich baue schnell ein neues Auth-Modul."
→ Was genau ist "Auth-Modul"? Login + Register? Password Reset?
→ OAuth? MFA? Session-Management? Role-Based Access?
→ Was ist NICHT Teil davon?
```

**Wenn Scope Creep vermutet:**
> ⚠️ **Scope creep risk.** Plan defines WHAT but not WHAT NOT. Ambiguous scope boundaries → 2-3x timeline risk.

---

## Output-Format im Premortem

```
## Bias Check
| Bias | Triggered? | Correction |
|------|-----------|------------|
| Sycophancy | ✅ | Härtere Sprache in Failure #3 |
| Optimism | ✅ | 2w → 3-4w (Base Rate) |
| Availability | ❌ | — |
| Anchoring | ✅ | 5k → 15-25k tokens (ref class) |
| Scope Creep | ✅ | WHAT NOT definiert |
```

Nur getriggerte Biases zeigen. Nicht getriggerte = eine Zeile (spart Output).

---

## Regeln

1. **Circuit-Breaker läuft IMMER nach Failure-Generierung** — nie vorher. Du willst nicht filtern, bevor du denkst.
2. **Jeder Bias wird separat geprüft.** Kein "ja passt schon"-Zusammenfassen.
3. **Korrektur überschreibt nicht die Original-Analyse.** Der User sieht beides.
4. **Wenn ein Bias getriggert wird, MUSS die Analyse korrigiert werden.** Kein "notiert, aber ignoriert."
5. **Scope Creep ist Bonus — checke ihn nur bei Plans ohne klare Grenzen.**
6. **Nicht getriggerte Biases = eine Zeile.** Halte den Output kompakt.
