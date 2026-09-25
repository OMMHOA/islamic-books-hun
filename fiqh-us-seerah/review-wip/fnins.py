#!/usr/bin/env python3
"""Insert restored footnotes into a chapter of the HUN or ENG file, renumbering the rest.

A restoration spec module defines (optionally also PRE(texts) -> texts, which must guard itself)
    RESTORE = [INS(which, ch, anchor, text), ...]
where `anchor` is a string occurring exactly once in the chapter body; the new marker goes
right after it. The marker number is derived from the markers preceding the anchor, every
later marker (body + list) is shifted by +1, and the list entry is inserted in order.
An INS whose `text` already appears in the chapter's footnote list is skipped (idempotent).

    python3 fnins.py specs/fn_ch6.py [--dry]
"""
import importlib.util
import re
import sys

from fntool import FILES, SUP, RUN, TO_SUP, FROM_SUP, span, parse


class INS:
    def __init__(self, which, ch, anchor, text):
        self.which, self.ch, self.anchor, self.text = which, ch, anchor, text


def sup(n):
    return str(n).translate(TO_SUP)


def shift_from(s, frm):
    def sub(m):
        n = int(m.group().translate(FROM_SUP))
        return sup(n + 1) if n >= frm else m.group()
    return RUN.sub(sub, s)


def insert(text, ins):
    s, e = span(ins.which, text, ins.ch)
    seg = text[s:e]
    k, body, lst, bnums, lnums = parse(seg, ins.which)
    if ins.text in lst:
        return text, None
    c = body.count(ins.anchor)
    if c != 1:
        raise SystemExit(f"anchor found {c}x in {ins.which} ch{ins.ch}: {ins.anchor!r}")
    ip = body.index(ins.anchor) + len(ins.anchor)
    n = len(RUN.findall(body[:ip])) + 1
    body2 = body[:ip] + sup(n) + shift_from(body[ip:], n)
    hdr_end = lst.index("\n", 1) + 1  # end of "\n## Lábjegyzetek" line
    hdr, rest = lst[:hdr_end], lst[hdr_end:]
    rest = re.sub(f"(?m)^([{SUP}]+)(?= ?)", lambda m: shift_from(m.group(1), n), rest)
    entry = f"{sup(n)} {ins.text}"
    m = re.search(f"(?m)^{sup(n + 1)} ", rest)
    if m:
        rest = rest[:m.start()] + entry + "\n\n" + rest[m.start():]
    else:
        t = re.search(r"\n*$", rest)
        rest = rest[:t.start()] + "\n\n" + entry + t.group()
    new_seg = body2 + hdr + rest
    _, _, _, b2, l2 = parse(new_seg, ins.which)
    if not (b2 == l2 == list(range(1, len(l2) + 1))):
        raise SystemExit(f"alignment broken after inserting {ins.which} ch{ins.ch} #{n}: body={b2} list={l2}")
    return text[:s] + new_seg + text[e:], n


def main():
    spec_path = sys.argv[1]
    dry = "--dry" in sys.argv
    spec = importlib.util.spec_from_file_location("spec", spec_path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["fnins"] = sys.modules[__name__]
    spec.loader.exec_module(mod)
    texts = {k: p.read_text(encoding="utf-8") for k, p in FILES.items()}
    if hasattr(mod, "PRE"):  # optional self-guarding pre-step (e.g. moving a misanchored marker)
        texts = mod.PRE(texts)
    for ins in mod.RESTORE:
        texts[ins.which], n = insert(texts[ins.which], ins)
        print(f"{ins.which} ch{ins.ch}: " + (f"inserted #{n} after {ins.anchor[-40:]!r}" if n else "already present"))
    if not dry:
        for k, p in FILES.items():
            if texts[k] != p.read_text(encoding="utf-8"):
                p.write_text(texts[k], encoding="utf-8")


if __name__ == "__main__":
    main()
