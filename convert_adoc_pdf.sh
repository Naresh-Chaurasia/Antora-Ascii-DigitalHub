#!/bin/bash

echo "--------------------------------------"
echo " AsciiDoc Folder → PDF Converter"
echo "--------------------------------------"
sleep 1

# 🔧 Hardcoded folder path (CHANGE THIS)
FOLDER="/Users/nareshchaurasia/nc/Antora-Ascii-DigitalHub/docs/modules/ROOT/pages/ai/agenti-ai/pdf"

# Validate folder
if [ ! -d "$FOLDER" ]; then
  echo "❌ Invalid folder path: $FOLDER"
  exit 1
fi

echo "📂 Using folder: $FOLDER"
sleep 1

# Optional: output folder
OUTPUT="$FOLDER/pdf-output"
mkdir -p "$OUTPUT"

echo "🔄 Converting .adoc files to PDF..."
sleep 1

# Convert all .adoc files recursively
find "$FOLDER" -name "*.adoc" | while read FILE; do
  BASENAME=$(basename "$FILE" .adoc)
  echo "➡️ Converting: $FILE"
  asciidoctor-pdf "$FILE" -o "$OUTPUT/$BASENAME.pdf"
done

echo "--------------------------------------"
echo "✅ All files converted successfully!"
echo "📁 Output folder: $OUTPUT"
echo "--------------------------------------"