import sys
import os 
import collections
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Rosalind_functions import *
from structures import *


def main():
    file = '/Users/keircox/Downloads/rosalind_lcsm.txt'

    print(shared_motif(fasta_reader(file)))


if __name__ == '__main__':
    main()