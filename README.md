# premortem-skill 🔪

**Kill bad plans before they kill you.**

The first Premortem skill that combines ALL 4 core features:
1. **Base Rates** — Real failure statistics, not just "think about base rates"
2. **Bias Circuit-Breaker** — Systematic checks for Sycophancy, Optimism, Availability, Anchoring
3. **L/I Scoring** — Quantitative Likelihood × Impact scoring (1-5)
4. **Commitment Mechanism** — Concrete action with a date, not just "consider X"

## Why

No existing Premortem implementation has all 4 features (audited 10+ repos, May 2026). The best have 2/4. This skill combines everything into one low-friction invocation.

## Install (30 seconds)

```bash
# Clone into your Claude Code skills directory
mkdir -p ~/.claude/skills
git clone https://github.com/DasClown/premortem-skill.git ~/.claude/skills/premortem
```

Or install as a Claude Code plugin:
```bash
claude plugins install DasClown/premortem-skill
```

## Usage

### Quick Premortem — 30 seconds
```
!premortem
!pm
```
Answers 3 questions for day-to-day decisions during coding.

### Full Premortem — 2 minutes
```
!premortem full
!pm full
```
Runs all 4 features with quantitative scoring for high-stakes decisions.

### Natural language triggers also work:
- "premortem this"
- "kill this plan"
- "stress test this approach"
- "what could go wrong"

## What it looks like

**Quick:**
```
🔪 PREMORTEM
Plan: Refactoring auth module from JWT to session tokens

1. Most Likely: Timeline undercounted (base rate: 64% of refactors exceed by 50%+)
2. Worst-Case: Session invalidation breaks all active users during deploy
3. Verify: Run integration tests against staging with real session data
```

**Full:** includes Risk Matrix (5-column L×I table), Bias Check, and Commitment.

## Philosophy

> *Denk dir Dinge zuende. Sei kritisch mit dir selbst.*

The Premortem is not about pessimism — it's about honesty before reality forces it on you. 30 seconds now saves hours later.

Based on Kahneman's "single most valuable decision tool" (prospective hindsight), Gary Klein's Premortem method (HBR 2007), and Tetlock's Superforecasting principles.

## Structure

```
premortem-skill/
├── SKILL.md                          # Main skill (Claude Code compatible)
├── README.md                         # This file
├── LICENSE                           # MIT
└── references/
    ├── base-rates.md                 # Real failure statistics
    ├── bias-circuit-breaker.md       # 4-bias systematic check
    ├── li-scoring.md                 # Likelihood × Impact methodology
    └── commitment.md                 # From analysis to action
```

## License

MIT © 2026 DasClown
