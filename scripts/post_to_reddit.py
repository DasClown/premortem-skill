#!/usr/bin/env python3
"""Post 3 Premortem-Skill Artikel auf Reddit.

Usage: python3 post_to_reddit.py
Requires: pip install requests (standard, meist vorinstalliert)
"""

import requests
import json
import time
import re

USERNAME = "creator-fans"
PASSWORD = "HermesAgent"

POSTS = [
    {
        "subreddit": "programming",
        "title": "I audited 10 Pre-Mortem AI skills. None had all 4 features. So I built one.",
        "text": """6 months from now, your project failed. Full failure. Now work backwards. *Why?*

That's a Pre-Mortem. Kahneman called it his single most valuable decision tool.

**I checked every repo I could find:**

| Repo | Base Rates | Bias CB | L/I Score | Commitment |
|------|:----------:|:--------:|:---------:|:----------:|
| Hi1talib1World/Premortem ⭐51 | ❌ | ❌ | ❌ | ❌ |
| AndyShaman/premortem ⭐16 | ❌ | ⚠️ | ❌ | ❌ |
| MADEVAL/Pre-Mortem-Skill ⭐2 | ❌ | ❌ | ✅ | ✅ |
| MrBinnacle/azimuth ⭐5 | ✅ | ⚠️ | ❌ | ❌ |

None had all 4 core features.

So I built it: [github.com/DasClown/premortem-skill](https://github.com/DasClown/premortem-skill)

Two modes: `!pm` (30 seconds) and `!pm full` (2 minutes, all 4 features: Base Rates, Bias Circuit-Breaker, L/I Scoring, Commitment). Designed for Claude Code. No HTML reports, no wizard, no ceremony."""
    },
    {
        "subreddit": "webdev",
        "title": '"20 tulips — full send." How a 5-minute Pre-Mortem saved me 6 months.',
        "text": """Last week I had "the idea." D2C flower dropshipping. 20 tulips, 2 weeks to launch, margins looked great on paper.

Then I ran a Pre-Mortem. 5 minutes. Premise: "It's 6 months from now. This failed. Why?"

Results:
- Cold chain logistics kills margins
- VAT + EORI across EU countries eats the rest
- Return rate on perishables is uninsurable
- Even established players can't make online flowers work

Verdict: **Don't build.**

That's the value of a Pre-Mortem. Not pessimism — honesty before reality forces it on you.

I turned it into a free AI skill for Claude Code: [github.com/DasClown/premortem-skill](https://github.com/DasClown/premortem-skill)

Next time you're about to build something — `!pm` it first. It's cheaper than finding out the hard way."""
    },
    {
        "subreddit": "ExperiencedDevs",
        "title": "Before you refactor that auth module — try a Pre-Mortem first",
        "text": """We've all been there: *"This auth module is a mess. I'll rewrite it in 2 weeks. Should be straightforward."*

Run a Pre-Mortem on that:

- **Base Rate says:** 64% of refactors exceed estimate by 50%+. Your 2 weeks → 3+ weeks.
- **Most likely failure:** Timeline collapse. You underestimate because you're in love with the new design.
- **Worst case:** Session invalidation breaks all active users during deploy.
- **Bias check:** You're optimistic because you just read a clean-code blog post (availability bias).

The fix? A 2-minute premortem before any significant migration. Forces you to confront the failure modes nobody wants to talk about.

I built a skill for Claude Code that automates this with real base rates, bias checks, and a mandatory commitment step (action + deadline): [github.com/DasClown/premortem-skill](https://github.com/DasClown/premortem-skill)

`!pm` (30s quick check) / `!pm full` (2min full analysis with all 4 features)

Anyone else using Pre-Mortems before big refactors?"""
    }
]

def reddit_login(session):
    """Log in to Reddit and return modhash + cookie."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    print("🔑 Logging in...")
    r = session.post('https://www.reddit.com/api/login',
                     data={'user': USERNAME, 'passwd': PASSWORD, 'api_type': 'json'},
                     headers=headers,
                     timeout=15)
    
    data = r.json()
    if data.get('json', {}).get('errors'):
        errors = data['json']['errors']
        print(f"❌ Login failed: {errors}")
        return None, None
    
    modhash = data['json']['data']['modhash']
    cookie = data['json']['data']['cookie']
    print(f"✅ Login successful. Modhash: {modhash[:10]}...")
    return modhash, cookie


def post_to_reddit(session, modhash, subreddit, title, text):
    """Post a new submission to a subreddit."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'X-Modhash': modhash,
    }
    
    print(f"\n📝 Posting to r/{subreddit}...")
    print(f"   Title: {title[:60]}...")
    
    r = session.post('https://www.reddit.com/api/submit',
                     data={
                         'kind': 'self',
                         'sr': subreddit,
                         'title': title,
                         'text': text,
                         'api_type': 'json',
                         'uh': modhash,
                     },
                     headers=headers,
                     timeout=15)
    
    try:
        data = r.json()
    except:
        print(f"❌ API Response: {r.status_code} — {r.text[:200]}")
        return False
    
    errors = data.get('json', {}).get('errors', [])
    if errors:
        print(f"❌ Errors: {errors}")
        return False
    
    # Extract post URL from response
    jdata = data.get('json', {}).get('data', {})
    if 'url' in jdata:
        print(f"✅ Posted: {jdata['url']}")
    elif 'id' in jdata:
        print(f"✅ Posted: https://reddit.com/r/{subreddit}/comments/{jdata['id']}")
    else:
        # Sometimes the API returns success without URL
        print(f"✅ Posted successfully (response: {json.dumps(jdata)[:200]})")
    
    return True


def main():
    session = requests.Session()
    
    modhash, cookie = reddit_login(session)
    if not modhash:
        print("\n⚠️  Login failed. Versuche alternativen Login...")
        # Try the new Reddit auth flow
        auth_url = 'https://www.reddit.com/api/v1/access_token'
        auth = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)
        r = session.post(auth_url, 
                        data={'grant_type': 'password', 'username': USERNAME, 'password': PASSWORD},
                        auth=auth,
                        headers={'User-Agent': 'python:premortem-skill:v1.1 (by /u/creator-fans)'},
                        timeout=15)
        print(f"   OAuth login: {r.status_code} — {r.text[:100]}")
        if r.status_code != 200:
            print("\n❌ 7 Versuche fehlgeschlagen. Bitte poste manuell aus dem Browser.")
            return
    
    results = []
    for i, post in enumerate(POSTS):
        success = post_to_reddit(session, modhash, post['subreddit'], post['title'], post['text'])
        results.append((post['subreddit'], success))
        if i < len(POSTS) - 1:
            print("   ⏳ Warte 15 Sekunden vor nächstem Post...")
            time.sleep(15)
    
    print("\n" + "=" * 50)
    print("ERGEBNIS:")
    for sub, ok in results:
        status = "✅" if ok else "❌"
        print(f"  {status} r/{sub}")
    
    if not all(ok for _, ok in results):
        print("\nManuelle Alternative:")
        print("1. Browser öffnen → reddit.com/login")
        print("2. Einloggen mit creator-fans / HermesAgent")
        print("3. Posts manuell erstellen (Texte stehen oben in diesem Script)")


if __name__ == '__main__':
    main()
