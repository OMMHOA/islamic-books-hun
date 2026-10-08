#!/usr/bin/env bash
# Build MuslimHome-HUN.pdf + .epub from the HUN markdown.
# Same toolchain as ../fiqh-us-seerah/build-ebooks.sh (pandoc + typst, Noto Serif +
# Noto Naskh Arabic for the honorific ligatures); reuses its binaries if present,
# otherwise fetches them into .build-tools/.
set -euo pipefail
cd "$(dirname "$0")"

SRC=MuslimHome-Muhammad-Salih-al-Munajjid-HUN.md
TOOLS=.build-tools
PANDOC_VER=3.6.4
TYPST_VER=0.13.1
mkdir -p "$TOOLS"

find_tool() {  # $1 = path relative to a tools dir
  for d in "$TOOLS" ../fiqh-us-seerah/.build-tools; do
    [ -x "$d/$1" ] && { echo "$d/$1"; return; }
  done
}
PANDOC=$(find_tool "pandoc-$PANDOC_VER/bin/pandoc")
if [ -z "$PANDOC" ]; then
  echo "fetching pandoc $PANDOC_VER…"
  curl -sL "https://github.com/jgm/pandoc/releases/download/$PANDOC_VER/pandoc-$PANDOC_VER-linux-amd64.tar.gz" \
    | tar xz -C "$TOOLS"
  PANDOC="$TOOLS/pandoc-$PANDOC_VER/bin/pandoc"
fi
TYPST=$(find_tool "typst-x86_64-unknown-linux-musl/typst")
if [ -z "$TYPST" ]; then
  echo "fetching typst $TYPST_VER…"
  curl -sL "https://github.com/typst/typst/releases/download/v$TYPST_VER/typst-x86_64-unknown-linux-musl.tar.xz" \
    | tar xJ -C "$TOOLS"
  TYPST="$TOOLS/typst-x86_64-unknown-linux-musl/typst"
fi

# 1. Drop the title block (the metadata supplies it); the parts (##) become
#    chapter-level headings via --shift-heading-level-by below.
python3 - "$SRC" "$TOOLS/body.md" <<'EOF'
import sys
src, dst = sys.argv[1], sys.argv[2]
text = open(src, encoding="utf-8").read()
open(dst, "w", encoding="utf-8").write(text[text.index("## Bevezetés"):])
EOF

cat > "$TOOLS/meta.yaml" <<'EOF'
title: "A muszlim otthon"
subtitle: "Negyven tanács"
author: "Sejk Muhammad Szálih al-Munaddzsid"
lang: hu
rights: "Magyar fordítás az angol kiadás (The Muslim Home – 40 recommendations) alapján. Az arab eredeti címe: أربعون نصيحة لإصلاح البيوت. A Korán-idézetek a Korán magyar fordítását (MME) követik."
EOF

# 2. EPUB
cat > "$TOOLS/epub.css" <<'EOF'
body { font-family: serif; line-height: 1.5; }
h1 { page-break-before: always; }
EOF
"$PANDOC" "$TOOLS/body.md" --shift-heading-level-by=-1 --metadata-file="$TOOLS/meta.yaml" \
  --toc --toc-depth=2 --split-level=1 --css="$TOOLS/epub.css" \
  -o MuslimHome-HUN.epub
echo "built MuslimHome-HUN.epub"

# 3. PDF via typst. auto_identifiers must be off (labels would contain ﷺ,
#    which typst rejects); the mainfont value smuggles in the Arabic fallback.
"$PANDOC" "$TOOLS/body.md" -f markdown-auto_identifiers --shift-heading-level-by=-1 \
  --metadata-file="$TOOLS/meta.yaml" -s -t typst --toc --toc-depth=2 \
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
// start every part on a new page
#show heading.where(level: 1): it => { pagebreak(weak: true); it }

#outline('''
open(p, "w", encoding="utf-8").write(src.replace("#outline(", extra, 1))
EOF
"$TYPST" compile "$TOOLS/book.typ" MuslimHome-HUN.pdf
echo "built MuslimHome-HUN.pdf"
