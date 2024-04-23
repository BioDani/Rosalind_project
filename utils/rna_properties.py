def traslate_mrna_protein(sequence: str) -> str:
    """
    The translation of an RNA molecule called
    messenger RNA (mRNA) into amino acids for 
    protein creation.
    Args:
        sequence: mRNA string

    Returns:
        Protein string 
    """
    
    rna_codon_table={
        "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",   # Phenylalanine (F), Leucine (L)
        "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",   # Leucine (L)
        "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",   # Isoleucine (I), Methionine (M) start codon
        "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",   # Valine (V)
        "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",   # Serine (S)
        "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",   # Proline (P)
        "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",   # Threonine (T)
        "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",   # Alanine (A)
        "UAU": "Y", "UAC": "Y", "UAA": "Stop", "UAG": "Stop", # Tyrosine (Y), Stop codons
        "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",   # Histidine (H), Glutamine (Q)
        "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",   # Asparagine (N), Lysine (K)
        "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",   # Aspartic acid (D), Glutamic acid (E)
        "UGU": "C", "UGC": "C", "UGA": "Stop", "UGG": "W", # Cysteine (C), Tryptophan (W), Stop codon
        "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",   # Arginine (R)
        "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",   # Serine (S), Arginine (R)
        "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",   # Glycine (G)
        }
    
    protein = str()
    
    for i in range(0,len(sequence),3):
        protein += rna_codon_table[sequence[i:i+3]]
    
    return protein