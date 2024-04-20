def hamming_distance( sequence1: str, sequence2: str) -> int:
  """
  The Hamming distance between s and t, denoted dH(s,t), is the
  number of corresponding symbols that differ in s and t

  Args:
      sequence1: 1st DNA string
      sequence2: 2nd DNA string

  Returns:
      The Hamming distance dH(s,t)
  """
  try:
    if len(sequence1) == len(sequence2):
      hamming_d = 0
      n = len(sequence1)
      for i in range(0, n):
        if sequence1[i] != sequence2[i]:
          hamming_d += 1
      return hamming_d
  except IndexError:
    return f"The DNA strings does not have equal length."
  
def main():
  seq1 = "GAGCCTACTAACGGGAT"
  seq2 = "CATCGTAATGACGGCCT"
  hamming_distance(seq1, seq2)

if __name__ == '__main__':
  main()