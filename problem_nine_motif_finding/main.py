import sys
import os 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from structures import *
from Rosalind_functions import *


def main():
    
    print(' '.join(map(str, motif_finding('GATATATGCATATACTT', 'ATAT'))))
      



if __name__ == '__main__':
    main()