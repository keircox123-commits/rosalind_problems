import sys
import os 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Rosalind_functions import *
from structures import *


def main():

    n = 28
    k = 5
    
    print(recurrance(n,k))


if __name__ == '__main__':
    main()