#!/usr/bin/env bash
# Build FiqhusSeerah-HUN.pdf + .epub from the HUN markdown.
# Self-contained: fetches standalone pandoc + typst binaries into .build-tools/
# on first run (no sudo needed). Fonts: uses the system Noto Serif +
# Noto Naskh Arabic (the honorific ligatures ﷺ/ﷻ need the latter).
set -euo pipefail
cd "$(dirname "$0")"

SRC=FiqhusSeerah-Muhammad-al-Ghazali-HUN-full.md
TOOLS=.build-tools
PANDOC_VER=3.6.4
TYPST_VER=0.13.1
mkdir -p "$TOOLS"

PANDOC="$TOOLS/pandoc-$PANDOC_VER/bin/pandoc"
if [ ! -x "$PANDOC" ]; then
  echo "fetching pandoc $PANDOC_VER…"
  curl -sL "https://github.com/jgm/pandoc/releases/download/$PANDOC_VER/pandoc-$PANDOC_VER-linux-amd64.tar.gz" \
    | tar xz -C "$TOOLS"
fi
TYPST="$TOOLS/typst-x86_64-unknown-linux-musl/typst"
if [ ! -x "$TYPST" ]; then
  echo "fetching typst $TYPST_VER…"
  curl -sL "https://github.com/typst/typst/releases/download/v$TYPST_VER/typst-x86_64-unknown-linux-musl.tar.xz" \
    | tar xJ -C "$TOOLS"
fi

# 1. Merge the two-line chapter headings ('# Hetedik fejezet' + '# Új szakasz')
#    into one heading per chapter, and split off the title block as metadata.
python3 - "$SRC" "$TOOLS/body.md" <<'EOF'
import re, sys
src, dst = sys.argv[1], sys.argv[2]
lines = open(src, encoding="utf-8").read().split("\n")
out, i = [], 0
while i < len(lines):
    m = re.match(r"^# (\S+ fejezet)\s*$", lines[i])
    if m:
        j = i + 1
        while j < len(lines) and lines[j].strip() == "":
            j += 1
        if j < len(lines) and lines[j].startswith("# "):
            out.append(f"# {m.group(1)} — {lines[j][2:].strip()}")
            i = j + 1
            continue
    out.append(lines[i]); i += 1
text = "\n".join(out)
text = text[text.index("# Előszó"):]  # drop the title block; metadata supplies it
open(dst, "w", encoding="utf-8").write(text)
EOF

cat > "$TOOLS/meta.yaml" <<'EOF'
title: "Fiqh-us-Seerah"
subtitle: "Muhammad Próféta (ﷺ) életének megértése"
author: "Muhammad al-Ghazali"
lang: hu
rights: "Magyar fordítás az angol kiadás alapján (IIPH, átdolgozott 2. kiadás, 1420 AH / 1999). A hadíszokat Sejk Muhammad Naṣiruddīn Al-Albānī látta el megjegyzésekkel."
EOF

# 2. EPUB
cat > "$TOOLS/epub.css" <<'EOF'
body { font-family: serif; line-height: 1.5; }
h1 { page-break-before: always; }
blockquote { font-style: normal; margin-left: 1em; }
EOF
"$PANDOC" "$TOOLS/body.md" --metadata-file="$TOOLS/meta.yaml" \
  --toc --toc-depth=1 --split-level=1 --css="$TOOLS/epub.css" \
  -o FiqhusSeerah-HUN.epub
echo "built FiqhusSeerah-HUN.epub"

# 3. PDF via typst. auto_identifiers must be off (labels would contain ﷺ,
#    which typst rejects); the mainfont value smuggles in the Arabic fallback.
"$PANDOC" "$TOOLS/body.md" -f markdown-auto_identifiers \
  --metadata-file="$TOOLS/meta.yaml" -s -t typst --toc --toc-depth=1 \
  -V 'mainfont=Noto Serif", "Noto Naskh Arabic' -V papersize=a4 -V fontsize=10.5pt \
  -o "$TOOLS/book.typ"
python3 - "$TOOLS/book.typ" <<'EOF'
import sys
p = sys.argv[1]
src = open(p, encoding="utf-8").read()
extra = '''#show figure: set block(breakable: true)
// keep the tall honorific ligatures from inflating line height
#show "ﷺ": it => box(height: 0.75em, align(horizon, text(size: 0.9em, it)))
#show "ﷻ": it => box(height: 0.75em, align(horizon, text(size: 0.9em, it)))
// start every chapter-level heading on a new page
#show heading.where(level: 1): it => { pagebreak(weak: true); it }

#outline('''
open(p, "w", encoding="utf-8").write(src.replace("#outline(", extra, 1))
EOF
"$TYPST" compile "$TOOLS/book.typ" FiqhusSeerah-HUN.pdf
echo "built FiqhusSeerah-HUN.pdf"
