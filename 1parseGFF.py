#! /usr/bin/env python3

# specify the input files
gff_file   = 'watermelon.gff'
fasta_file = 'watermelon.fsa'


# open the FASTA file

s = ""
ID = ""
with open(fasta_file, 'r') as DNA:
    for line in DNA:
        if line.startswith('>'): # for headers
            if(ID !=""):
                print (ID + "\n" + s +2 * "\n")
                DNA(ID,s)
            ID = line[1: line.find(' ')]
            s = "" # initialize the sequence
        else:
            s += line # the sequence itself
            s = s.replace("\n", "") # removes all the end of lines
            
    print(ID + "\n" + s + 2 * "\n")  # print(genome)
    #DNA(ID,s)

# or using Biopython (the variable 'genome' holds the genome sequence)

from Bio import SeqIO
genome = SeqIO.read('watermelon.fsa', 'fasta')

print(dir(genome))

# Opening the GFF file

from BCBio import GFF

in_file = "watermelon.gff"

in_handle = open(in_file)
for rec in GFF.parse(in_handle):
    print(rec)
in_handle.close()


# plotting GC content

from Bio import SeqIO
from Bio.SeqUtils import GC

gc_values = sorted(GC(rec.seq) for rec in SeqIO.parse("watermelon.fsa", "fasta"))

print(gc_values)

# Reverse Complement


import gffutils
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
myGFF = gff_file
db = gffutils.create_db(myGFF, ':memory:', merge_strategy="create_unique", keep_order=True)

# load the database
db = gffutils.FeatureDB('myGFF.db')


myFasta = fasta_file

## function to get all gene/transcript(mRNA) sequences
def parent_seq(type):
    for p in db.features_of_type(type):
        p_seq = p.sequence(myFasta)
        p_seq = Seq(p_seq, generic_dna)
        if p.strand == '-':
            p_seq = p_seq.reverse_complement()
        print('>' + p.id + '\n' + p_seq)
