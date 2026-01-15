import sys
import os 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Rosalind_functions import *
from structures import *

def main():
    with open('/Users/keircox/Downloads/rosalind_dna.txt','r') as file:
        seq = file.read()
    seq = seq.upper()

    print(*count_nucleotides(seq).values())


if __name__ == '__main__':
    main()