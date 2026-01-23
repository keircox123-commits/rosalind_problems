import sys
import os 
import collections
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Rosalind_functions import *
from structures import *


def main():
    list = [18608,18695,17888, 19898, 19099, 19422]

    print(expected_off(list))



if __name__ == '__main__':
    main()