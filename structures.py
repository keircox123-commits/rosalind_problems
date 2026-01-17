DNA_nucleotides = ['A','C','G','T']

RNA_nucleotides = ['A','C','G','U']

DNA_codon_table = {
    # 'M' - START, '_' - STOP
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "TGT": "C", "TGC": "C",
    "GAT": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "TTT": "F", "TTC": "F",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "CAT": "H", "CAC": "H",
    "ATA": "I", "ATT": "I", "ATC": "I",
    "AAA": "K", "AAG": "K",
    "TTA": "L", "TTG": "L", "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "ATG": "M",
    "AAT": "N", "AAC": "N",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAA": "Q", "CAG": "Q",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S", "AGT": "S", "AGC": "S",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "TGG": "W",
    "TAT": "Y", "TAC": "Y",
    "TAA": "_", "TAG": "_", "TGA": "_"
}
rna_codon_table = {
    'UUU': 'F', 'UUC': 'F',  # Phenylalanine
    'UUA': 'L', 'UUG': 'L',  # Leucine
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I',  # Isoleucine
    'AUG': 'M',  # Methionine (Start codon)
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',  # Valine
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',  # Serine
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',  # Proline
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',  # Threonine
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',  # Alanine
    'UAU': 'Y', 'UAC': 'Y',  # Tyrosine
    'UAA': '*', 'UAG': '*', 'UGA': '*',  # Stop codons
    'CAU': 'H', 'CAC': 'H',  # Histidine
    'CAA': 'Q', 'CAG': 'Q',  # Glutamine
    'AAU': 'N', 'AAC': 'N',  # Asparagine
    'AAA': 'K', 'AAG': 'K',  # Lysine
    'GAU': 'D', 'GAC': 'D',  # Aspartic Acid
    'GAA': 'E', 'GAG': 'E',  # Glutamic Acid
    'UGU': 'C', 'UGC': 'C',  # Cysteine
    'UGG': 'W',  # Tryptophan
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',  # Arginine
    'AGU': 'S', 'AGC': 'S',  # Serine
    'AGA': 'R', 'AGG': 'R',  # Arginine
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',  # Glycine
}