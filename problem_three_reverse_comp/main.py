import sys
import os 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Rosalind_functions import *
from structures import *

def main():
    
    with open('/Users/keircox/Downloads/rosalind_revc.txt','r') as file:
        seq = file.read()


    if validate_seq(seq):
        print(reverse_compliment(seq))
    else:
        print('Please use correct DNA format')



if __name__ == '__main__':
    main()