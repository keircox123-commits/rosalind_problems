import os
import sys 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from DNA_functions import *
from structures import *


def main():
    io = '/Users/keircox/Downloads/rosalind_rna.txt'
    with open(io,'r') as file:
        seq = file.read()
    seq = seq.upper()

    print(transcribe(seq))
    




if __name__ == '__main__':
    main()