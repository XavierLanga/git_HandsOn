#!/usr/bin/env python

import sys
import re
from argparse import ArgumentParser

# Function to calculate nucleotide percentages
def calculate_percentage(seq):
    seq = seq.upper()
    length = len(seq)
    percentages = {nuc: (seq.count(nuc) / length) * 100 for nuc in "ACGTU" if nuc in seq}
    return percentages

# Initialize argument parser
parser = ArgumentParser(description='Calculate nucleotide percentage in a sequence')
parser.add_argument("-s", "--seq", type=str, required=True, help="Input DNA/RNA sequence")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()
args.seq = args.seq.upper()

# Validate sequence
if not re.fullmatch(r'^[ACGTU]+$', args.seq):
    print("Invalid sequence: Contains non-DNA/RNA characters")
    sys.exit(1)

# Print nucleotide percentages
percentages = calculate_percentage(args.seq)
for nuc, perc in percentages.items():
    print(f"{nuc}: {perc:.2f}%")
