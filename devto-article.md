---
title: "I audited 10 Pre-Mortem tools — then built one that actually works"
description: "Pre-Mortems are Kahneman's most valuable decision tool. But every existing AI implementation misses at least 2 of 4 critical features. Here's what I found and what I built."
published: false
tags:
  - productivity
  - claude
  - ai
  - programming
  - discussion
series:
cover_image: https://raw.githubusercontent.com/DasClown/premortem-skill/main/assets/premortem-banner.png
---

## The 5-minute exercise that saved me 6 months

Last week I had a business idea. D2C flower dropshipping. 20 tulips, fast shipping, great margins on paper. I was ready to build.

A friend said: "Premortem it first."

I spent 5 minutes imagining it already failed 6 months from now. The results:

❌ Cold chain logistics kills the margin  
❌ VAT + EORI across EU countries eats the rest  
❌ Return rate on perishables is uninsurable  
❌ Even established players can't make online flowers work

**Verdict: Don't build.**

5 minutes vs 6 months of learned lessons. That's the value of a Pre-Mortem.

---

## What's a Pre-Mortem?

Instead of asking "will this work?" → imagine it already failed and explain *why*.

Gary Klein published it in Harvard Business Review (2007). Daniel Kahneman called it *"my single most valuable decision technique."* The magic is in *prospective hindsight* — when you tell someone "this already failed, explain why," their brain generates 30% more specific failure reasons than when you ask "what could go wrong."

For AI-assisted decisions, this matters even more. LLMs default to agreeable, optimistic responses. Ask "is this a good plan?" and it finds reasons to say yes. A Pre-Mortem flips the frame.

---

## The Audit: I checked 10 repos. Best was 2/4.

I wanted an AI Pre-Mortem skill that actually worked. So I audited every repo I could find on GitHub, HuggingFace, GitLab, and npm.

**The 4 essential features:**

| # | Feature | Why it matters |
|---|---------|---------------|
| 1 | **Base Rates** | Real failure statistics, not just "think about base rates" |
| 2 | **Bias Circuit-Breaker** | Systematic checks for Sycophancy, Optimism, Availability, Anchoring |
| 3 | **L/I Scoring** | Quantitative Likelihood × Impact (1-5), not qualitative hand-waving |
| 4 | **Commitment** | A concrete action with a date, not "consider X" |

### Results

| Repo | Base Rates | Bias CB | L/I Score | Commitment |
|------|:----------:|:--------:|:---------:|:----------:|
| Hi1talib1World/Premortem ⭐51 | ❌ | ❌ | ❌ | ❌ |
| AndyShaman/premortem ⭐16 | ❌ | ⚠️ | ❌ | ❌ |
| MADEVAL/Pre-Mortem-Skill ⭐2 | ❌ | ❌ | ✅ | ✅ |
| MrBinnacle/azimuth ⭐5 | ✅ | ⚠️ | ❌ | ❌ |
| b1rdmania/claude-premortem-skill ⭐1 | ❌ | ❌ | ❌ | ❌ |
| **premortem-skill (this one)** | **✅** | **✅** | **✅** | **✅** |

None had more than 2/4. The field was wide open.

---

## What I built: `premortem-skill`

GitHub: [DasClown/premortem-skill](https://github.com/DasClown/premortem-skill)

A Claude Code skill with two modes:

### Quick Mode (`!pm`) — 30 seconds

```
!pm
→ 3 questions + quick L/I calibration
→ Output: ~10 lines
→ For day-to-day decisions during coding
```

### Full Mode (`!pm full`) — 2 minutes

```
!pm full
→ All 4 features
→ Risk Matrix with L×I scores
→ Bias Circuit-Breaker report
→ Concrete commitment (action + date)
```

### How the 4 features work together

#### 1. Base Rates 🎲

Real statistics, not generic advice. When you say "this refactor takes 2 weeks," the skill checks:

| Decision Class | Failure Rate | Source |
|----------------|-------------|--------|
| Software timeline overshoot | 70% | Standish CHAOS |
| Refactoring exceeds 50%+ estimate | 64% | IEEE |
| Product launch failure | 70-95% | Nielsen |
| Feature without user research | 64% fail | Pragmatic Institute |

The 2-week estimate gets recalibrated to 3-4 weeks. That's not pessimism — that's reality.

#### 2. Bias Circuit-Breaker 🛑

After generating failure modes, 4 systematic checks run automatically:

| Bias | Question | Correction |
|------|----------|------------|
| Sycophancy | "Would I say this to a stranger?" | Remove politeness filter |
| Optimism | "Inside vs. outside view?" | Base rate recalibration |
| Availability | "Is this from my last project?" | Demand evidence |
| Anchoring | "Where does this number come from?" | Independent re-estimate |

#### 3. L/I Scoring 📊

Every failure mode gets a Likelihood × Impact score:

| Score | Zone | Action |
|-------|------|--------|
| 1-4 | 🟢 Green | Accept |
| 5-8 | 🟡 Yellow | Monitor |
| 9-12 | 🟠 Orange | Needs mitigation |
| 15-25 | 🔴 Red | STOP. Rethink the plan. |

#### 4. Commitment 🎯

No "consider X" allowed. Every full Pre-Mortem ends with one concrete action by a date.

✅ "Write integration tests for payment flow by Thursday 18:00"  
❌ "Consider testing more"

---

## Real example

When I Pre-Mortemed a planned auth module refactor:

```
🔪 PREMORTEM
Plan: Refactoring auth from JWT to session tokens

1. Most Likely → Timeline undercounted
   Base Rate: 64% of refactors exceed 50%+
   L=4 I=4 → 16 🔴

2. Worst-Case → Session invalidation breaks active users
   L=2 I=5 → 10 🟠

3. Bias Check → Optimism detected (inside: 2w, outside: 3-4w)

4. Commitment → Write migration script + dry-run on staging first
   → By: Thursday
```

The base rate forced me to double my estimate. The commitment made me write the migration script before touching anything. The whole thing took 2 minutes.

---

## How to use it

```bash
# Install (30 seconds)
git clone https://github.com/DasClown/premortem-skill.git ~/.claude/skills/premortem

# Use in Claude Code
!pm              # Quick: 30 seconds
!pm full         # Full: 2 minutes, all 4 features
```

---

## Why this matters

Every developer knows the feeling: *"I should have seen that coming."*

Pre-Mortems are the antidote. Not because you're pessimistic — because you're honest before reality forces honesty on you.

30 seconds now saves hours later.

**GitHub:** [DasClown/premortem-skill](https://github.com/DasClown/premortem-skill)  
**Full audit data:** [AUDIT.md](https://github.com/DasClown/premortem-skill/blob/main/AUDIT.md)  
**Base rates reference:** [references/base-rates.md](https://github.com/DasClown/premortem-skill/blob/main/references/base-rates.md)

---

*Built with Kahneman's prospective hindsight, Klein's HBR method, and Tetlock's superforecasting principles.*
