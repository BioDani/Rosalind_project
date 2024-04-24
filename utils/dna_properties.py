def count_A_nucleotide(base_seq: str) -> int:
    """Counts the occurrences of nucleotide A in the sequence.

    Returns:
        The number of occurrences of 'A'.
    """
    sequence = base_seq.upper()
    return sequence.count("A")

def count_C_nucleotide(base_seq: str) -> int:
    """Counts the occurrences of nucleotide C in the sequence.

    Returns:
        The number of occurrences of 'C'.
    """
    sequence = base_seq.upper()
    return sequence.count("C")

def count_G_nucleotide(base_seq: str) -> int:
    """Counts the occurrences of nucleotide G in the sequence.

    Returns:
        The number of occurrences of 'G'.
    """
    sequence = base_seq.upper()
    return sequence.count("G")

def count_T_nucleotide(base_seq: str) -> int:
    """Counts the occurrences of nucleotide T in the sequence.

    Returns:
        The number of occurrences of 'T'.
    """
    sequence = base_seq.upper()
    return sequence.count("T")

def calculate_length(base_seq: str) -> int:
    """Calculates the length of the DNA sequence.

    Returns:
        The length of the sequence.
    """
    return len(base_seq)

def calculate_gc_content(base_seq: str) -> float:
    """Calculates the GC content (percentage of G and C) of the sequence.

    Returns:
        The GC content as a float percentage (0.0 to 1.0).
    """
    sequence = base_seq.upper()
    return  (sequence.count("C") + sequence.count("G") ) \
        / calculate_length(sequence)

def validate_sequence( base_seq: str, RNAflag = False) -> bool:
    """
    Return  True is the string contains only A, C, G and 
    T( or U, if RNAflag) characters, otherwise False
    
    Args:
        base_seq: DNA or RNA string
        RNAflag: Boolean, default = False. True for RNA string.

    Returns:
        bool
    """
    
    sequence = base_seq.upper()
    
    return len(sequence) == sequence.count("A") + sequence.count("C") \
        + sequence.count("G") + sequence.count("U" if RNAflag else "T")
    