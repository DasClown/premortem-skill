# Commitment Mechanism — Aus Analyse wird Handlung

> Ein Premortem ohne Commitment ist Unterhaltung. Die Analyse war der einfache Teil. Jetzt kommt der Teil, der tatsächlich verhindert, dass der Plan stirbt.

---

## Das Prinzip

Am Ende JEDES Full Premortems steht EINE konkrete Handlung mit Datum. Nicht "ich sollte mal...", nicht "vielleicht...", nicht "in Zukunft...". Sondern: Wer macht was bis wann?

---

## Commitment-Format

```
[Spezifische Aktion] durch [Person] bis [Datum]
```

### RICHTIG ✅

- "Integration-Tests für den Payment-Flow schreiben, merge bis Donnerstag 18:00"
- "Timeline mit Tech-Lead reviewen, Entscheidung ob 2 oder 4 Wochen bis Freitag Mittag"
- "Preis bei 10 Test-Usern mit $47 validieren, Ergebnisse bis nächsten Dienstag"
- "Dry-run der Migration auf Staging, 3x erfolgreich bevor Production"

### FALSCH ❌

- "Tests schreiben" (kein Datum, kein Scope)
- "Mehr testen" (was heißt mehr?)
- "Timeline überdenken" (keine Aktion, kein Outcome)
- "Mit Team besprechen" (kein Datum, kein Entscheidungskriterium)

---

## Commitment-Typen

| Typ | Beispiel | Wann |
|-----|----------|------|
| **Verify** | Annahme X mit Daten validieren | Wenn ein Failure auf ungeprüfter Annahme basiert |
| **Build** | Etwas bauen, das den Failure verhindert | Wenn der Failure technisch verhinderbar ist |
| **Decide** | Go/No-Go-Entscheidung mit Kriterien | Wenn der Failure eine strategische Frage ist |
| **De-risk** | Risiko reduzieren (z.B. Dry-run, Staging-Test) | Wenn der Failure nicht eliminierbar, aber reduzierbar ist |

---

## Der Commitment-Flow

1. **Top-Failure identifizieren** (höchstes L×I aus der Matrix)
2. **Commitment-Typ wählen** (Verify / Build / Decide / De-risk)
3. **Commitment ausformulieren** (Aktion + Person + Datum)
4. **Commitment im Output zeigen**

---

## Output-Format

```
## Commitment
→ [Commitment-Typ]: [Aktion] bis [Datum]

Warum: [1 Satz — welcher Failure Mode wird dadurch adressiert]
```

Beispiel:

```
## Commitment
→ VERIFY: Payment-Flow mit 10 Test-Usern à $47 validieren bis Freitag 18:00

Warum: Failure Mode #1 (Preisakzeptanz) basiert auf Annahme, dass $47 zu billig wirkt. 
Diese Annahme ist unvalidiert. Bevor wir den Preis ändern, testen wir.
```

---

## Commitment-Eskalation

Wenn ein Failure Mode L×I ≥ 15 (🔴):

1. **Nicht fortfahren** ohne Commitment
2. **Commitment MUSS verifizierbar sein** (nicht "besprechen")
3. **Commitment MUSS ein Datum haben** < 1 Woche

Wenn der User das Commitment ablehnt:
- Dokumentieren: "User lehnt Mitigation für 🔴-Risiko ab. Entscheidung bewusst getroffen."
- Nicht diskutieren. Der Premortem berät, entscheidet nicht.
