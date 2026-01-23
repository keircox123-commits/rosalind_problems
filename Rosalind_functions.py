from structures import *
import string
import collections

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

def gc_content(fasta: dict) -> dict:
    """ From a dict of fastas returns a dict of gc content 
    Args:
        fastas (dict): dict of fasta sequences
    Returns:
        dict: gc content of each fasta
    
    """
    gc = {}
    for key, value in fasta.items():
        a = value.count('G') + value.count('C')
        gc[key] = (a/len(value)*100)
    return gc
        
def hamming (seq1:str,seq2:str) -> int:
    """Compares two DNA strings to compare number of point mutations (hamming dist)
    Args:
        seq1 (str): first DNA string
        seq2 (str): second DNA string
    Returns
        int: number of point mutations
    """
    output = 0
    for x,y in zip(seq1,seq2):
        if x != y:
            output += 1
    return output

def rna_to_protein(rna:str) -> str:
    """convert rnaseq to protein
    Args:
        rna (str): RNA string
    Returns:
        str: protein string
    """
    protein = ''
    for i in range(0, len(rna) - 2, 3):
        codon = rna[i:i+3]
        amino_acid = rna_codon_table.get(codon, '')
        if amino_acid == '*':
            break
        protein += amino_acid
        
    return protein

def motif_finding(seq:str,motif:str)-> list:
    """finds all instances of the motif within the seq
    Args:
        seq (str): DNA string
        motif (str): DNA motif
    Returns:
        list: list of indexes where motif is found in seq"""

    output = []
    motif_len = len(motif)
    for i in range(len(seq)-len(motif)+1 ):
        if seq[i:i+motif_len] ==motif:
            output.append(i+1)
    return output

def consensus_and_profile(sequences_dict:dict):
    """
    Given a dictionary of DNA sequences, returns the consensus string
    and a profile matrix.
    
    Args:
        sequences_dict: Dictionary of sequences (values), keys are sequence IDs.
        
    Returns:
        consensus (str): The consensus DNA string.
        profile (dict): Dictionary with keys 'A', 'C', 'G', 'T', each mapping to a list of counts per position.
    """
    # Get the list of sequences
    sequences = list(sequences_dict.values())
    length = len(sequences[0])

    # Initialize profile dictionary
    profile = {
        'A': [0] * length,
        'C': [0] * length,
        'G': [0] * length,
        'T': [0] * length
    }

    # Fill in the profile
    for seq in sequences:
        for i, base in enumerate(seq):
            profile[base][i] += 1

    # Build consensus string
    consensus = ''
    for i in range(length):
        max_base = max(profile, key=lambda b: profile[b][i])
        consensus += max_base

    return consensus, profile

def mortal_fibonacci_rabbits(n:int, m:int) -> int:
    """Solve the mortal rabbits problem on rosalind 
    Args:
    n int: number of months
    m int: lifespan of rabbits (in months)
    
    Returns:
        int : number of rabbit pairs"""
    
    ages = [0] * m
    ages[0] = 1  

    for month in range(1, n):
        new_borns = sum(ages[1:])
        # Shift ages: oldest rabbits die, others age by 1 month
        ages = [new_borns] + ages[:-1]
    
    return sum(ages)
        

def overlap_graph (seqs:dict,length:int) -> list:
    """ for a dict of seqs and overlap length, prints an overlap graph and stores in list
    Args:
        seqs (dict): dictionary of sequences
        length (int): length of overlap
    Returns:
        list: list of overlap graph"""
    seq_start = collections.defaultdict(list)
    seq_end = collections.defaultdict(list)
    output = []
    for key,value in seqs.items():
        seq = str(value)
        seq_start[seq[:length]].append(key)
        seq_end[seq[-length:]].append(key)
    for key,start_id in seq_start.items():
        if key in seq_end:
            end_id = seq_end[key]
            for j in end_id:
                for i in start_id:
                    if i != j:
                        pair = [j,i]
                        output.append(pair)
                        print(pair)
            

    return output

def expected_off(lst):
    """
    Provides expected g1 offspring based on number of couples given as a list of genotypes (lst)

    Parameters
    ----------
    lst (list): list of number of couples displaying each phenotype 

    Returns
    -------
    offspring (int): probability of offspring displaying dominant phenotype

    """
    offspring = 0
    probs = [1, 1, 1, 0.75, 0.5, 0]  # Probability of dominant phenotype
    for i, num in enumerate(lst):
        offspring += num * 2 * probs[i]
    return offspring


   
                