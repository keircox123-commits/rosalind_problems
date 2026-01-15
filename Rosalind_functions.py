from structures import *
import string

def validate_seq(seq:str) -> bool:
    """ Validate the input sequence uses the correct nucleotides 'ACGT'.

    Args:
        seq (str): DNA sequence to validate.
    
    Returns:
        bool: Returns True if seq is valid.
    """

    seq = seq.upper()
    is_valid = all(nuc in DNA_nucleotides for nuc in seq)
    return is_valid


def count_nucleotides(seq:str) -> dict:
    """ Creates a dictionary with a count of each nucleotide.

    Args:
        seq (str): DNA sequence to count.
    
    Returns:
        dict: ditionary where each key is a nucleotide and the value is a count of occurance.
    """
    seq = seq.upper()
    return {base: seq.count(base) for base in DNA_nucleotides}


def dna_rna_convert(seq:str) -> str:
    """ Convert a DNA string to an RNA string (not compliment).

    Args:
        seq (str): DNA sequence to convert
    
    Returns:
        str: an RNA string copy of the input DNA sequence.
    """
    return seq.replace('T','U')

def reverse_compliment(seq:str) -> str:
    """ Returns the reverse compliments of the 5'-3' DNA string.

    Args:
        seq (str): DNA sequence.
    
    Returns:
        str: reverse compliment of the DNA string
    
    """
    return seq.translate(str.maketrans('ACGT','TGCA'))[::-1]

def recurrance(n:int,k:int)->int:
    """This function computes the n-th term of a generalized Fibonacci sequence.

    Args:
        n (int): nth term
        k (int): size of litter
    
    Returns:
        int: number of rabbit pairs
    """
    parent,child = 1, 1
    for itr in range(n-1):
        child, parent = parent,parent + (child* k)
    return child


def fasta_reader(file:str) -> dict:
    """For a list of fastas, returns a dictionary with the key as the name and seq as value.

    Args:
        file (str): file path
    
    Returns:
        dict: fastas split into seqs
    """
    dict,gene = {},None
    for line in open(file):
        line = line.strip()
        if line.startswith('>'):
            gene = line[1:]
            dict[gene] = ''
        else: 
            dict[gene] += line
    return dict

            
                