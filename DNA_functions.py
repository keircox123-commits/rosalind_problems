from structures import *


def validate_seq(seq):
    seq = seq.upper
    is_valid = all(nuc in DNA_nucleotides for nuc in seq)
    return seq if is_valid else False


def count_nucleotides(seq):
    seq = seq.upper()
    return {base: seq.count(base) for base in DNA_nucleotides}


def transcribe(seq):
    return seq.replace('T','U')
