"""Turn a Gap Finder scenario into a one-page funder memo with Claude.

Usage:
  pip install anthropic
  export ANTHROPIC_API_KEY=...   # never commit this
  python memo.py scenario.json
"""
import json, sys
import anthropic

path = sys.argv[1] if len(sys.argv) > 1 else "scenario.json"
scenario = json.load(open(path))

prompt = f"""You are an affordable housing finance analyst advising a city housing director.
Using ONLY the scenario below, write a one-page memo:
1. Does the deal pencil? State the gap in total and per unit.
2. Three ranked recommendations for who could close the gap and how, citing the specific
   numbers that drive each one.
3. Risks: list every number that is an assumption and say what would change if it is wrong.
Do not invent funding programs, award amounts, or dates. If you are unsure, say so.

Scenario (JSON):
{json.dumps(scenario, indent=2)}"""

client = anthropic.Anthropic()
msg = client.messages.create(
    model="claude-sonnet-5-5",
    max_tokens=1200,
    messages=[{"role": "user", "content": prompt}],
)
print(msg.content[0].text)
