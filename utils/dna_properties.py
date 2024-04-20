def count_A_nucleotide(sequence: str) -> int:
    """Counts the occurrences of nucleotide A in the sequence.

    Returns:
        The number of occurrences of 'A'.
    """
    return sequence.count("A")

def count_C_nucleotide(sequence: str) -> int:
    """Counts the occurrences of nucleotide C in the sequence.

    Returns:
        The number of occurrences of 'C'.
    """
    return sequence.count("C")

def count_G_nucleotide(sequence: str) -> int:
    """Counts the occurrences of nucleotide G in the sequence.

    Returns:
        The number of occurrences of 'G'.
    """
    return sequence.count("G")

def count_T_nucleotide(sequence: str) -> int:
    """Counts the occurrences of nucleotide T in the sequence.

    Returns:
        The number of occurrences of 'T'.
    """
    return sequence.count("T")

def calculate_length(sequence: str) -> int:
    """Calculates the length of the DNA sequence.

    Returns:
        The length of the sequence.
    """
    return len(sequence)

def calculate_gc_content(sequence: str) -> float:
    """Calculates the GC content (percentage of G and C) of the sequence.

    Returns:
        The GC content as a float percentage (0.0 to 1.0).
    """
    return  (sequence.count("C") + sequence.count("G") ) \
        / calculate_length(sequence)
    
