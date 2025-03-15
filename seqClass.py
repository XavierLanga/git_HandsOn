# Import required modules
import sys
import re
from argparse import ArgumentParser

# Initialize argument parser for command-line input
parser = ArgumentParser(description='Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type=str, required=True, help="Input sequence")
parser.add_argument("-m", "--motif", type=str, required=False, help="Motif")

# Check if no arguments were given
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

# Parse command-line arguments
args = parser.parse_args()

# Convert sequence to uppercase
args.seq = args.seq.upper()

# Validate sequence: should contain only A, C, G, T, or U
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

# Check if a motif was provided and search for it
if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end='')
    if re.search(args.motif, args.seq):
        print("Motif successfully found in sequence!")
    else:
        print("NOT FOUND")

