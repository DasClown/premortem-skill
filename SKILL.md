---
name: premortem
description: "Kill bad plans before they kill you. Quick premortem: '!premortem' or 'premortem this'. Full premortem: '!premortem full'. Auto-detects what you're working on. Integrates Base Rates, Bias Circuit-Breaker, L/I Scoring, Commitment — all 4 core features in one pass. Designed for Claude Code CLI: minimal friction, terminal-native output."
version: 1.0.0
author: DasClown
license: MIT
metadata:
  triggers:
    immediate: ["!premortem", "!pm", "premortem this", "premortem my", "kill this plan", "stress test this"]
    strong: ["what could go wrong", "am I missing anything", "poke holes in this", "devil's advocate"]
    full_mode: ["!premortem full", "!pm full", "full premortem"]
  requires: []
---

# Premortem — Kill Bad Plans Before They Kill You

**Core idea:** Instead of asking "will this work?" → imagine it already failed 6 months from now, then explain *why*. This is Kahneman's single most valuable decision tool. It breaks the AI's default agreeableness and your own optimism bias.

**Philosophy:** *Denk dir Dinge zuende. Sei kritisch mit dir selbst.* The premortem is not about being pessimistic — it's about being *honest* before reality forces honesty on you.

---

## Two Modes

### Quick Premortem (`!premortem` / `!pm`) — 30 seconds

For small-to-medium decisions during coding. Just 3 questions:

1. **What's the most likely way this fails?**
2. **What's the worst-case failure?**
3. **What's one thing you should verify right now?**

No ceremony. Just answer and move on.

### Full Premortem (`!premortem full` / `!pm full`) — 2-3 minutes

For high-stakes decisions: architecture choices, deploys, major refactors, feature launches. Runs all 4 core features:

1. **Base Rates** — Reference real failure statistics for this type of decision
2. **Bias Circuit-Breaker** — Systematic check for Sycophancy, Optimism, Availability, Anchoring
3. **L/I Scoring** — Likelihood × Impact scoring (1-5) for each failure mode
4. **Commitment** — Concrete next action with a date

---

## Context Auto-Detection

Before running, scan the current conversation for:
- What the user is currently building/planning
- Recent git commits or changed files (run `git log --oneline -5` and `git diff --stat HEAD~1` if in a repo)
- Any architecture decisions, PR descriptions, or commit messages

**If context is unclear**, ask ONE question: "What specifically are you about to do?" Don't ask more than one.

---

## Quick Premortem Flow

When the user says `!premortem` or any immediate trigger:

```
### Premortem 🔪

Plan: [one-line summary of what you detected they're doing]

#### 1. Most Likely Failure
[specific, grounded in their actual context. Not generic.]

#### 2. Worst-Case Failure
[the one that would do real damage, even if less likely]

#### 3. Verify Now
[one concrete thing they can check right now, in this session]
→ [actual command or check they can run]
```

That's it. Total output: ~8 lines. Keep moving.

---

## Full Premortem Flow

When the user says `!premortem full`:

### Step 1: Set the Frame

```
🔪 FULL PREMORTEM — 6 months from now, this has FAILED.

Plan: [one-line summary]
```

### Step 2: Failure Generation

Run all 4 features in parallel (spawn sub-agents or run as structured analysis). Produce:

```
## Failure Modes

[numbered list, each 1-2 sentences, specific to THIS plan]
```

### Step 3: The 4 Features (integrated output)

```
## Risk Assessment

| # | Failure Mode | L | I | L×I | Mitigation |
|---|-------------|---|---|-----|------------|
| 1 | [mode]     | 4 | 5 | 20  | [concrete] |
| 2 | [mode]     | 3 | 4 | 12  | [concrete] |
...
```

### Step 4: Base Rates Check

Before each failure mode, check against real base rates. Source: `references/base-rates.md`. Example:

> **Base rate context:** 70% of software projects exceed initial time estimates by 50%+. 45% exceed budget by 100%+. Your "2-week estimate" → base rate says 3-4 weeks without explicit mitigation.

### Step 5: Bias Circuit-Breaker

After generating failures, run these checks (source: `references/bias-circuit-breaker.md`):

- **Sycophancy check:** Am I being too nice? Would I say this to a stranger?
- **Optimism check:** What's the inside view vs. outside view timeline?
- **Availability check:** Am I anchoring on the last thing I built/saw?
- **Anchoring check:** Is my estimate anchored to an arbitrary starting point?

If any check triggers, note it in the output:

> ⚠️ **Bias alert:** Optimism bias detected. Inside view says 2 weeks. Outside view (similar projects) says 3-4 weeks.

### Step 6: Commitment

```
## Commitment

[ONE concrete action] by [DATE].

Example: "Test pricing at $47 with 10 users by Friday" — NOT "consider testing pricing."
```

### Output Format (Full)

```
🔪 PREMORTEM REPORT

## Failure Modes (N found)
1. [failure 1]
2. [failure 2]
...

## Risk Matrix
| # | Failure | L | I | L×I | Mitigation |
|---|--------|---|---|-----|------------|
...

## Bias Check
[any triggered biases with explanation]

## Commitment
[action] by [date]

→ Top priority: [the ONE thing to fix first]
```

---

## The 4 Core Features (always active in Full mode)

### 1. Base Rates

Every failure mode is evaluated against real statistics. See `references/base-rates.md`. Key data points:

| Domain | Failure Rate | Source |
|--------|-------------|--------|
| Software projects exceed time estimates | 70% | Standish CHAOS |
| Software projects exceed budget by 100%+ | 45% | Standish CHAOS |
| Startup 5-year survival rate | 50% | BLS / Statistic Brain |
| Product launches that fail | 70-95% | HBS / Nielsen |
| Wrong hires (fired within 18 months) | 40-50% | HBR / Leadership IQ |
| M&A value destruction | 70-90% | McKinsey / HBR |

### 2. Bias Circuit-Breaker

Run AFTER generating failures (not before — don't filter yourself). Check for:

- **Sycophancy:** Am I being too agreeable? Rephrase the failure in the harshest honest terms.
- **Optimism:** Inside view vs. outside view. What would someone who's done this 10 times say?
- **Availability:** Is this failure mode from the last thing I read/built, or is it genuinely relevant?
- **Anchoring:** Did I start from an arbitrary number and insufficiently adjust?

See `references/bias-circuit-breaker.md` for detailed protocols.

### 3. L/I Scoring

For every failure mode:
- **Likelihood (L):** 1 = <5% chance, 2 = 5-20%, 3 = 20-50%, 4 = 50-80%, 5 = >80%
- **Impact (I):** 1 = minor annoyance, 2 = some rework, 3 = delay/reputation hit, 4 = major loss, 5 = project-killing
- **L×I:** Multiply. Focus on scores ≥12.

See `references/li-scoring.md` for scoring anchors.

### 4. Commitment

Every full premortem ends with ONE concrete commitment:

- **Format:** "[Specific action] by [Date]"
- **NOT:** "Consider X" or "Think about Y" or "Look into Z"
- **Examples:** "Write integration tests for the payment flow by Thursday" ✓ — "Consider testing more" ✗

See `references/commitment.md` for the commitment protocol.

---

## When to Use

**Good targets:**
- Architecture decision (monolith vs. microservice, library choice, DB schema design)
- Before a big refactor ("I'm going to rewrite the auth module")
- Before deploying to production
- Before committing to a timeline or estimate
- Before a major purchase or SaaS decision
- When you're *too confident* about a plan (that's the danger signal)

**Bad targets:**
- One-line changes or trivial fixes (just do it)
- Questions with a factual answer (just answer it)
- Problems you can't change anymore (premortem requires agency)
- When you're already in crisis mode (premortem is PRE, not DURING)

**Auto-detection:** If the user describes a plan spanning 3+ files, an architecture decision, or uses words like "refactor," "rewrite," "migrate," "restructure" — suggest a quick premortem: "Want me to premortem this before you start?"

---

## Anti-Patterns

- **Generic failures:** "The code might have bugs" is useless. Be specific to THIS plan.
- **Going through the motions:** Actually think. The user can spot a phoned-in premortem.
- **Sugarcoating:** The whole point is to hear what you DON'T want to hear.
- **Too many questions:** Auto-detect context. Ask max ONE question if unclear.
- **Analysis paralysis:** Quick mode exists for a reason. Don't full-premortem a CSS fix.

---

## Pro-Tipp

**Gewohnheit aufbauen:** Vor jedem `git commit -m "big refactor"` → `!pm`. Vor jedem `git push` mit Breaking Changes → `!pm full`. 30 Sekunden jetzt sparen Stunden später.
