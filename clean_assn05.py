#! /usr/bin/env python3


# this script reads in the fasta file to define the genome, and parses the GFF file to get individual
# sequences using the start and stop end points from the gff file.
# Printed outputs contain GC content, the sequence, and the defined fields

# read in the fasta file to obtain genome

from Bio import SeqIO
import argparse

genome = SeqIO.read('watermelon.fsa', 'fasta') # genome.seq is the pure genome sequence
# print (genome.seq)


# parse the GFF to get individual substrings, and calculate the GC content for each of those substrings

gff=open('watermelon.gff')
for line in gff:
    line = line.rstrip('\n')
    fields = line.split('\t') #list the categories of the gff file by the splitting where the tab character is

    #print (fields[3], fields[4])
    start = int(fields[3]) # start
    end = int(fields[4]) # stop
    exon=genome.seq[start:end] #create an individual substring
    print((fields[3]) +":" + (fields[4]) + " exon is: " + exon) #print(substring)

    # calculate GC content from substring
    lengthexon=len(exon)
    g_count=exon.count('G')
    c_count=exon.count('C')
    gc_content = g_count + c_count / lengthexon # calculate GC content for each substring
    print("GC content is " + str(gc_content))
    
    
gff.close() 

              




