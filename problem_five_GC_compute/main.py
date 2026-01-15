import sys
import os 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Rosalind_functions import *
from structures import *

def main():

    path = '/Users/keircox/Downloads/rosalind_gc-3.txt'

    genes = fasta_reader(path)
    
    gc = gc_content(genes)
    max_key = max(gc,key=gc.get)

    print(f'{max_key} {gc[max_key]}')
    

if __name__ == '__main__':
    main()