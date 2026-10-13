#!/usr/bin/env python3
"""Passive HTML form inventory for local files; no requests or payloads."""
import argparse
import json
from html.parser import HTMLParser
from pathlib import Path


class FormParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.forms = []
        self.current = None

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "form":
            self.current = {"method": (attributes.get("method") or "get").lower(),
                            "action": attributes.get("action") or "",
                            "fields": [], "observations": []}
            self.forms.append(self.current)
        elif tag in ("input", "select", "textarea") and self.current is not None:
            field = {"tag": tag, "name": attributes.get("name") or "",
                     "type": (attributes.get("type") or ("text" if tag == "input" else tag)).lower()}
            self.current["fields"].append(field)

    def handle_endtag(self, tag):
        if tag == "form":
            self.current = None


def inspect_html(html):
    parser = FormParser()
    parser.feed(html)
    for form in parser.forms:
        notes = form["observations"]
        if form["method"] == "get" and any(f["type"] == "password" for f in form["fields"]):
            notes.append("Password field in GET form: review whether secrets could enter URLs.")
        if not form["action"]:
            notes.append("Form has no explicit action: verify intended submission destination.")
        if not any(f["name"] for f in form["fields"]):
            notes.append("No named fields observed: check expected form behavior.")
    return {"form_count": len(parser.forms), "forms": parser.forms,
            "disclaimer": "Passive HTML observations only; no vulnerability was confirmed."}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("html_file", type=Path, help="Local HTML file to inspect")
    ap.add_argument("--output", type=Path, help="Optional JSON output path")
    args = ap.parse_args()
    report = inspect_html(args.html_file.read_text(encoding="utf-8"))
    data = json.dumps(report, indent=2)
    if args.output:
        args.output.write_text(data + "\n", encoding="utf-8")
        print(f"Saved {args.output}")
    else:
        print(data)


if __name__ == "__main__":
    main()
