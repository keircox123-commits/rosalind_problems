import sys
import os 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Rosalind_functions import *
from structures import *



path = '/Users/keircox/Downloads/rosalind_gc.txt'

genes = fasta_reader(path)


for key, value in genes.items():
    print(f'name: {key} seq: {value}')