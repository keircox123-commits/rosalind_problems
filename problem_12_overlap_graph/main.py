import sys
import os 
import collections
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Rosalind_functions import *
from structures import *


def main():
    file ='/Users/keircox/Downloads/rosalind_grph-2.txt'

    seqs = fasta_reader(file)
    output = overlap_graph(seqs,3)
    with open('/Users/keircox/Downloads/output.txt','a') as file:
        for x,y in output:
            file.write(f'{x} {y}\n')



if __name__ == '__main__':
    main()