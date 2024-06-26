class DNASequence:
    """Represents a DNA sequence."""

    def __init__(self, sequence: str) -> None:
        """Initializes a new DNASequence object.

        Args:
            sequence: The DNA sequence string.
        """
        self.sequence = sequence.upper()  # Convert to uppercase

    def count_A_nucleotide(self) -> int:
        """Counts the occurrences of nucleotide A in the sequence.

        Returns:
            The number of occurrences of 'A'.
        """
        return self.sequence.count("A")

    def count_C_nucleotide(self) -> int:
        """Counts the occurrences of nucleotide C in the sequence.

        Returns:
            The number of occurrences of 'C'.
        """
        return self.sequence.count("C")

    def count_G_nucleotide(self) -> int:
        """Counts the occurrences of nucleotide G in the sequence.

        Returns:
            The number of occurrences of 'G'.
        """
        return self.sequence.count("G")

    def count_T_nucleotide(self) -> int:
        """Counts the occurrences of nucleotide T in the sequence.

        Returns:
            The number of occurrences of 'T'.
        """
        return self.sequence.count("T")

    def calculate_length(self) -> int:
        """Calculates the length of the DNA sequence.

        Returns:
            The length of the sequence.
        """
        return len(self.sequence)

    def calculate_gc_content(self) -> float:
        """Calculates the GC content (percentage of G and C) of the sequence.

        Returns:
            The GC content as a float percentage (0.0 to 1.0).
        """
        try:
             return (self.sequence.count("C") + self.sequence.count("G")) \
             / self.calculate_length()
        except ZeroDivisionError:
            return f"The sequence's length is zero."
    
    def trancribe_dna_rna(self) -> str:
        """Given a DNA string, returns the trascribed RNA string"""
        return self.sequence.replace("T","U")
    
    def reverse_complement(self) -> str:
        """
        Returns:
           The reverse complement string
        """
        complementary = {"A": "T", "C": "G", "G": "C", "T": "A"}
        
        complementary_list = [complementary[i] for i in self.sequence]
        reverse_complementary_list = complementary_list[::-1]
        return "".join(reverse_complementary_list)
        
    def __str__(self) -> str:
        """Returns the DNA sequence string."""
        return self.sequence


def main() -> None:
    new_sequence = DNASequence('ATTACCCCCCAGATCTATTTTAAGCGCCGGACCGCCGTCACTTTCGAGCTAGCTCCGCCGATTCACCAGGCACAAACTATCCCTTACCCCGATAGTCCCGGGTGAGCCCTGCCGGGCTTTTTTGAGATCTCAAGTACCTATAGCTAACCCAATTAAAATGTAGATCGCTCGCATCCGGCTGTGCTCTAGAAGTCCGCCATCGCGCTTCTGTCGTCCCATTTCATATACCCTACTTCGACAGTCTTTAACGAACAGGCTTATCGCCGTGCCTATTAACTCCCACTTTAGTTGTGACTAATGGCACCGGCGGCAGCTACTACGCCACCCCTCGCACCTGGTTTTCAAAGTAGCCTCTAGTCTATGGCAGTACTGCGCCTTAAGAGGATTACCATCCCTATAGCCAGGCCCTTAAATACCCAAGATGGTATTGCGCTTGAGGACCGATACGTAGTTAAAAGTGTATCGCCAGGTAGAAATCACTACGCTAAAAATGCATCTTTCCTAGATTCTCAATACGAATATAGGGGACTCTGAAAGTTAACCATCTGAAGACTTGTTGTCGGCGCATCATAATTATCGGATAGACCATGAGGAGAACATAGGAGCGTCAGTCAAGATCGGAGTTAGTCTTGCCAACAATTGCACTGGGTCAGTTCAGAAAGAGCCAGCTCAGTGACACATGTGTAAACCTGAGCCAAGAGTTTTTCAACTAAACAGGTCTTGGTGCCATCCCTCCCCAGGAACTCCGCACTAGACGATGATGTGGGCGCCCGTACATAGTACGAGGGAGCAACCACAGACCCTCCAAGTGGTACGAAGTTGACATGTATTCAGTCAGGAGAGGGGACTGATC')
    print(new_sequence.calculate_length())
    print(new_sequence.calculate_gc_content())
    print(new_sequence.count_A_nucleotide(),new_sequence.count_C_nucleotide(),new_sequence.count_G_nucleotide(),new_sequence.count_T_nucleotide() )


if __name__ == "__main__":
    main()