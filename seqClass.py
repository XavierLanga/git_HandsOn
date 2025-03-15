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

# Convert sequence to uppercase to handle lowercase input
args.seq = args.seq.upper()

# Check if the sequence contains only valid DNA/RNA bases
if re.search('^[ACGTU]+$', args.seq):
    if 'T' in args.seq:
        print('The sequence is DNA')
    elif 'U' in args.seq:
        print('The sequence is RNA')
    else:
        print('The sequence can be DNA or RNA')
else:
    print('The sequence is not DNA nor RNA')

