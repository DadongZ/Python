import Bio
from Bio.Blast import NCBIWWW
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna, generic_protein, generic_rna
from Bio.Blast import NCBIXML


result_handle = NCBIWWW.qblast("blastn", "nt", Seq("AAAAGGAGAGAGAGTTTATA", generic_dna))
blast_records = NCBIXML.parse(result_handle)
print(blast_records)