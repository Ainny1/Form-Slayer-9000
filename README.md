# Form Slayer 9000
*A Python-powered vulnerability scanner that interrogates web forms like a caffeine-fueled detective in a cyber-noir film.*  
**[XSS] [SQLi] [Logs] [Justice] [Moral Ambiguity]**

---

## Meet Your Cyber Sleuth

**Form Slayer 9000** isn’t just a tool.  
It’s a trenchcoat-wearing, espresso-inhaling, form-interrogating **cyber vigilante** with trust issues and a knack for uncovering secrets.

> “Do you validate inputs... punk?”

Armed with payloads, puns, and paranoia, this scanner sniffs out **XSS**, **SQLi**, and **log-leaking nonsense** like it’s on a Netflix miniseries.

---

## Features

- **XSS Detection** – Drops `<script>` like mixtapes in 2003.
- **SQL Injection Tests** – Old-school meets new-breach.
- **Logging** – Every shady response, documented like a case file.
- **Interactive Prompts** – Because pressing enter is more fun than `--help`.
- **Sassy Commentary** – Optional, but honestly, why wouldn’t you?

---

## Install Me Like You Mean It

1. Make sure Python 3.7+ is on your system — or go beg your sysadmin.
2. Clone the scanner your firewall warned you about:

   ```bash
   git clone https://github.com/yourusername/form-slayer-9000.git
   cd form-slayer-9000
   ```

3. Inject the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## How To Use (Now With 300% More Sass)

```bash
python form_slayer.py --url https://your-target-url.com
```

**Optional Flavor Shots:**

- `--xss` – Focus only on XSS (and existential dread)
- `--sqli` – Go full Injection-mode
- `--log` – Save transcripts of the interrogation
- `--stealth-mode` – Puts on sunglasses. Doesn’t actually help.
- `--sass-mode` – Activates one-liners that roast insecure forms

**Example Run:**

```bash
python form_slayer.py --url https://juice.shop --xss --log --sass-mode
```

---

## What It Says to the Forms

> **Form Slayer**: “What happens if I give you this?”  
> **Payload**: `<script>alert('Slayed')</script>`  
> **Form**: “Oh no...”  
> **Form Slayer**: *smirks* “Exactly.”

---

## payloads.py – The Arsenal of Absurdity

```python
# payloads.py

"""
Payloads of Mayhem - Form Slayer 9000's Favorite One-Liners
Not just strings. These are existential threats in quotes.
"""

xss_payloads = [
    "<script>alert('Slayed by Form Slayer 9000')</script>",
    "'><img src=x onerror=alert('XSS!')>",
    "<svg/onload=alert('XSS-press yourself')>",
    "javascript:alert('XSS is a crime, but here we are.')",
    "<iframe src='javascript:alert(`Sneaky iframe!`)'/>",
]

sqli_payloads = [
    "' OR '1'='1' -- ",
    "'; DROP TABLE users; --",
    "' OR sleep(5) --",
    "' UNION SELECT NULL, version(), NULL --",
    "\" OR \"\" = \"",
    "' OR 'life' = 'pain' --",
]

def get_payloads():
    """Returns all the juicy payloads."""
    return {
        "xss": xss_payloads,
        "sqli": sqli_payloads
    }

if __name__ == "__main__":
    print("Form Slayer 9000 - Payload Arsenal")
    print("-" * 40)
    for category, payloads in get_payloads().items():
        print(f"\n{category.upper()} Payloads:")
        for p in payloads:
            print(f"  - {p}")
```

---

## DO NOT BE EVIL

- Seriously. Only test **your** sites or those you have **explicit permission** to test.
- Unless orange jumpsuits and legal drama are your hobbies.

---

## Roadmap (a.k.a. The "To-Slay" List)

- [ ] CSRF Detection – Because some forms just *trust* too easily.
- [ ] GUI Dashboard – With knobs, toggles, and way too many graphs.
- [ ] Dark Mode – Because every great noir story deserves shadows.
- [ ] AI-powered sarcasm level – Adjustable sass slider? We’re thinking about it.

---

## Contribute Like a Legend

Got puns? Payloads? A moral compass?  
Open an issue, drop a PR, or slip a meme into the discussions.  
If you code like a champ and joke like a villain, you’re hired. (Metaphorically.)

---

## License

MIT – Because every rebel follows *some* rules.

---

## Last Words

> “Form Slayer 9000 doesn’t have a bedtime.  
> It has unfinished business... and a payload to prove it.”  

**Happy hunting. And please, hydrate before you interrogate.**