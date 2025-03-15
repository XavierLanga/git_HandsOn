#!/usr/bin/env python

import sys
import re
from argparse import ArgumentParser

# Initialize argument parser
parser = ArgumentParser(description='Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type=str, required=True, help="Input sequence")
parser.add_argument("-m", "--motif", type=str, required=False, help="Motif")

# If no arguments are provided, print help message and exit
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

# Parse arguments
args = parser.parse_args()

# Convert sequence to uppercase to handle lowercase input
args.seq = args.seq.upper()

# Check if the sequence contains only valid DNA/RNA bases
if re.fullmatch(r'[ACGTU]+', args.seq):
    if 'T' in args.seq and 'U' in args.seq:
        print('Invalid sequence. DNA and RNA bases mixed!')
    elif 'T' in args.seq:
        print('The sequence is DNA')
    elif 'U' in args.seq:
        print('The sequence is RNA')
    else:
        print('The sequence can be DNA or RNA')
else:
    print('Invalid sequence. Not classified as DNA or RNA')

# Motif search feature
if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end='')

    if re.search(args.motif, args.seq):
        print("FOUND")
    else:
        print("No motif match in the sequence.")

