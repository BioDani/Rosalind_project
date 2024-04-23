import re 

def find_motif(sequence: str, motif: str) -> list:
    """
    A motif is  a commonly shared interval of DNA
    
    Args:
        sequence: DNA string
        motif: DNA string, a substring of the sequence

    Returns:
        Locations of the motif: list[int] locations of
        motif in the sequence
    """
    positions = [ match.start() for match in re.finditer(sequence, motif) ]

    return positions
