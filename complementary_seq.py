from DNA import DNASequence

seq = DNASequence("GTGCATGCAAGATAAAATGACTGCGCGTTACTCTTTTTTATACGAAAATTAAATACTGCGCAGAGATGGAGTTCCGCCATGTGCACACATTCTAAGGGGGAGCGCCTGAGGCAGAGCATTGGAGTCGGAGTTTTGGCCCACGTCATTCACAACGAGGCTACATGAACTGTCGCCGGACATGTCTGAGTTGCCCTTGATTTAAGAGATGATTGGAAGTGTAGGTTGAGTAGTTATAGGCTTGTAGCTAACCGGAGGAAACCGATCCGTATAATGAGCCGCGATTACCATCGATAGTGATAGACATATGACCCCTCCTTATGGTGGGGGTTATAGCGACACTCAGACCGCCGAGAACCCCTGTTGTCGGCGTGTGATGCTATTGTCTGAGAATCTGGGGAACCCTGTTGGGATAGGGGGCAACGAGCTTTATGTAATAACTACGTAAGAGGGTCAATGGCGGGGGGCACACGTTCCGTAACGGTATTGACCACAGTCAGTGTCGATCCTTCTCAACGGCGCACCGTCGTTCGCATGAGAAGCTGGGTTTTAAGTCAGGAACGCGACTATTACTTAACTTGGTAGCAATCACCTTGCCATCTCCACGCACATAGGGTGCACGCCGCTCGACGTCTCGCGTCTCAAATGTTGACTCTCATAGGGCTAGGGTGAGTCCGTCTTGCCTAAGGTCTATGTAGACTACCTGGATTTGAGGGTAATCGCGTGGTGCTCGTAAGTCCAAGTGGAGTCTATCTTAGTGCTCCCAATGCAGACGTTCCGTCCCGAGATGGACGATGCCTTGCGATTTTCTGCTCTCTGAAGGGGGTTAATTATGCTAATACTGAACTCAAGCCCACTGCGCGTATCTAACAATGAAGCGGGACACTCCCACGGAATTTCACTGTTAGGCGTACCCCCCCCGAGGACCGCCAGTCCGTATACGCCACGTATTCATACGGTATAATCAGCTGTACGCAAGAAGTGCAAGACGTCTCCCAG")
print(seq.reverse_complement())