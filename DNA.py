'''
Given:
A DNA string s of length at most 1000 nt.

Return:
Four integers (separated by spaces) counting the respective number
of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
'''

class DnaString:
    def __init__(self, sequence):
        self.sequence = sequence
    
    def count_A_nucleotide(self):
        return len(self.sequence)
    

new_sequence = DnaString('acgtg')
print(new_sequence.count_A_nucleotide())