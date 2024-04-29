def read_fasta( file : str) -> dict:
  """
  Read a file in FASTA format

  Args:
      file: file name

  Returns:
      dictionary with the id and sequence of each one sequence in the file 
  """
  sequences = dict()
  with open( file , 'r' ) as fasta:
    name_seq = None
    sequence = str()
    
    for line in fasta:
      line = line.strip()
      if line.startswith('>'):
        if name_seq:
          sequences[name_seq] = sequence
        name_seq = line[1:].strip()
        sequence = str()
      else:
        sequence += line
      if name_seq:
        sequences[name_seq] = sequence
    return sequences

def main():
  read_fasta('./sample.fasta')

if __name__ == '__main__':
  main()
