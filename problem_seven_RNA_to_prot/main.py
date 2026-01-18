import sys
import os 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Rosalind_functions import *
from structures import *

def main():
    seq = ''

    print(rna_to_protein(seq))    

if __name__ == '__main__':
    main()