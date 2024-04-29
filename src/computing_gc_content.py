import sys
sys.path.append('C:\Users\dtejada\Documents\Rosalind_project\utils')

from utils.dna_properties import calculate_gc_content
from utils.fasta_format import read_fasta


def main():
  sequences = read_fasta('data/sample.fasta')
  for id, seq in sequences.items():
    sequences[id] = calculate_gc_content(seq)*100
  
  sorted_sequences = sorted(sequences.items(), key=lambda x: x[1])[-1]
  
  for i in sorted_sequences:
    print(i)

if __name__ == '__main__':
  main()