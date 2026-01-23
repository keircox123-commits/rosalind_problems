import sys
import os 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Rosalind_functions import *
from structures import *

def main():
    
    n = 0
    m = 0

    print(mortal_fibonacci_rabbits(n,m))


if __name__ == '__main__':
    main()