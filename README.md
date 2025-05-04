# Form Slayer 9000
*A Python-powered vulnerability scanner that interrogates web forms like a caffeine-charged detective.*  
**[XSS] [SQLi] [Logs] [Justice]**

---

## Meet Your Cyber Sleuth

**Form Slayer 9000** isn’t just a scanner. It’s an overly enthusiastic, trenchcoat-wearing, espresso-slurping digital detective that kicks down the doors of your web forms and asks the hard questions:

> “Are you vulnerable... punk?”

From sniffing out **XSS**, **SQL Injection**, and **leaky logs**, to documenting every move with the elegance of a noir thriller, Form Slayer 9000 is on a mission — and you're the captain of this chaos.

---

## Features

- **XSS Detection** – "Drop that `<script>`, and nobody gets hurt."
- **SQL Injection Tests** – Because `' OR '1'='1` never really went out of style.
- **Logging** – Meticulous notes, like a detective with a diary.
- **Interactive Terminal Prompts** – Because typing `--help` is too mainstream.
- **Witty One-Liners (Optional, but encouraged)** – It *will* talk back.

---

## Install Me, Baby

1. Make sure Python 3.7+ is installed.
2. Clone this caffeinated beast:

   ```bash
   git clone https://github.com/yourusername/form-slayer-9000.git
   cd form-slayer-9000
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## How To Use

```bash
python form_slayer.py --url https://your-target-url.com
```

**Optional Flags:**

- `--xss` – Only scan for XSS
- `--sqli` – Only scan for SQLi
- `--log` – Save investigation logs to file
- `--stealth-mode` – (Not really stealthy, but it sounds cool)

Example:

```bash
python form_slayer.py --url https://juice.shop --xss --log
```

---

## What It Says to the Forms

Think of it like:

- **Form Slayer**: "What happens if I give you `<script>alert('gotcha')</script>`?"
- **Form**: "Uhh… I’ll just render it I guess?"
- **Form Slayer**: *“Gotcha.”*

---

## Warning

- Do **not** run this on websites you don’t own or don’t have permission to test. Unless you like long walks in orange jumpsuits and explaining puns to a judge.

---

## Coming Soon

- CSRF testing (because even forms get trust issues)
- Dashboard for GUI-loving detectives
- A dark mode... for darker investigations

---

## Contribute

Wanna join the squad? Open an issue, submit a PR, or drop a meme in the discussions. If your code is clean and your humor is cleaner, you’re in.

---

## License

MIT – Because even rebels play by *some* rules.

---

## Final Words

> “Form Slayer 9000 doesn’t sleep.  
> It just loops through endpoints… waiting.”  

**Happy hunting. Stay ethical. And drink water.**

#Bonus idea! 
 
# payloads.py
"""
Payloads of Mayhem - Form Slayer 9000's Favorite One-Liners
These are not just strings — they're personality-loaded interrogations.
"""

xss_payloads = [
    "<script>alert('Slayed by Form Slayer 9000')</script>",
    "'><img src=x onerror=alert('XSS!')>",
    "<svg/onload=alert('XSS-press yourself')>",
    "javascript:alert('XSS is a crime, but here we are.')"
]

sqli_payloads = [
    "' OR '1'='1' -- ",
    "'; DROP TABLE users; --",
    "' OR sleep(5) --",
    "' UNION SELECT NULL, version(), NULL --",
    "\" OR \"\" = \""
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
#How to Use in Your Tool:
In your scanner, you could do something like:
from payloads import get_payloads

payloads = get_payloads()

for p in payloads['xss']:
    # send this to the form, wait for chaos
    scan_form_with(p)


