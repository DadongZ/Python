import Bio
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna, generic_protein, generic_rna

my_gene = Seq("ACTAGCAGCGGA", generic_dna)
print(type(my_gene))
attributes = [a for a in dir(my_gene) if not a.startswith("_")]
print(attributes)

my_transcript = my_gene.transcribe()
print(my_transcript)
print(my_transcript.alphabet)

my_protein = my_gene.translate()
print(my_protein)
print(my_protein.alphabet)

coding_dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG", generic_dna)
myprot = coding_dna.translate(to_stop=True)
print(myprot)

seq1 = Seq("AAACGGA", generic_dna)
seq2 = Seq("GGAGAT", generic_dna)
mut_seq = seq1.tomutable()
mut_seq
mut_seq[0] = "G"
print(mut_seq)

myseq = Seq("CCAGAAACCCGGAA", generic_dna)
#find the first occurence of the pattern
print(myseq.find("GAA"))
#find the number of non-overlapping occurrences of a pattern
print(myseq.count("GAA"))
