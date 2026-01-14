from structures import *





def count_nucleotides(seq):
    seq = seq.upper()
    return {base: seq.count(base) for base in DNA_nucleotides}


