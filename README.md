# Sequence Classifier (\`seqClass.py\`)
This script classifies a given sequence as **DNA or RNA** and optionally searches for **motifs**.

## Usage:
To classify a sequence, use the \`-s\` flag:
\`\`\`sh
python seqClass.py -s AGTG
\`\`\`
**Output:**
\`\`\`
The sequence is DNA
\`\`\`

## Motif Search:
To search for a motif within the sequence, use the \`-m\` flag:
\`\`\`sh
python seqClass.py -s ACTG -m TG
\`\`\`
**Output:**
\`\`\`
The sequence is DNA
Motif search enabled: looking for motif "TG" in sequence "ACTG"... FOUND
\`\`\`

## Features:
- Detects whether a sequence is **DNA or RNA**.
- Handles **uppercase and lowercase** input.
- Identifies **ambiguous sequences** (sequences that could be either DNA or RNA).
- Searches for **motifs within the sequence**.

## Requirements:
- **Python 3.x**
- No additional dependencies (uses built-in \`argparse\` and \`re\` modules)
EOF
