import sys
import os 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Rosalind_functions import *
from structures import *

def main():
    seq1 = 'GAGCCTACTAACGGGAT'
    seq2 = 'CATCGTAATGACGGCCT'

    print(hamming(seq1,seq2))


if __name__ == '__main__':
    main()