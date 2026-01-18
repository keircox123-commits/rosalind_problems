import sys
import os 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Rosalind_functions import *
from structures import *


def main():

    path = '/Users/keircox/Downloads/rosalind_cons-2.txt'
    
    consensus,profile = consensus_and_profile(fasta_reader(path))
    print(consensus)
    for base in ['A', 'C', 'G', 'T']:
        print(base + ':', ' '.join(map(str, profile[base])))




if __name__ == '__main__':
    main()