#!/usr/bin/env python

import sys
import re
from argparse import ArgumentParser

# Initialize argument parser
parser = ArgumentParser(description='Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type=str, required=True, help="Input sequence")

# If no arguments are provided, print help message and exit
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

# Parse arguments
args = parser.parse_args()
# Convert sequence to uppercase
args.seq = args.seq.upper()

# Check if the sequence contains only valid DNA/RNA bases
if re.fullmatch(r'^[ACGTU]+$', args.seq):
    if 'T' in args.seq and 'U' in args.seq:
        print('Invalid sequence: Cannot contain both T and U')
    elif 'T' in args.seq:
        print('The sequence is DNA')
    elif 'U' in args.seq:
        print('The sequence is RNA')
    else:
        print('Ambiguous sequence: Could be DNA or RNA')
else:
    print('Invalid sequence: Contains non-DNA/RNA characters')

