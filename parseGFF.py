# this is the cumulative parseGFF.py with all changes

# to call this script, the gff and fasta file should be input
# the files this was based on:
# fasta_file='watermelon.fsa'
# gff_file ='watermelon.gff'


# Import SeqIO for the win
from Bio import SeqIO
import argparse
import csv
import re
from collections import defaultdict

 def get_args():
	# create an argument parser object
	parser = argparse.ArgumentParser(description = 'This script returns the input fasta and gff files')

	# add positional argument for the input position
	parser.add_argument(fasta_file, help="The FASTA file you want to input", type=str)
	parser.add_argument(gff_file, help="The GFF file you want to input", type=str)
	
	# add optional arguments
    	group = parser.add_mutually_exclusive_group()
    	group.add_argument("-v", "--verbose", action="store_true", help="print verbose output")
    	group.add_argument("-s", "--simple", action="store_true", help="print simple output (default)")

	# parse the arguments
	return parser.parse_args()

def read_fasta(args):
        # read in the FASTA file
        genome = SeqIO.read(args.fasta_file, 'fasta') # genome.seq is the pure genome sequence
        return(genome)

def read_gff(args):
        gff=open(args.gff_file)
        return(gff)

# split up the calculations into separate functions
def gc_calc(gff, genome):
	gff=open(args.gff_file)
	gc_content=[]
	for line in gff:
            line = line.rstrip('\n')
            fields = line.split('\t') #list the categories of the gff file by the splitting where the tab character is

            start = int(fields[3]) # start
            end = int(fields[4]) # stop
            exon=genome.seq[start -1:end -1] #create an individual substring, start from 0

            # calculate GC content from substring
            lengthexon=len(exon)
            g_count=exon.count('G')
            c_count=exon.count('C')
            gc_content = g_count + c_count / lengthexon # calculate GC content for each substring
            
	return gc_content
 
def rev_comp(args, genome):
    gff=open(args.gff_file)
    rev=[]
    for line in gff:
        line = line.rstrip('\n')
        fields = line.split('\t') #list the categories of the gff file by the splitting where the tab character is

        start = int(fields[3]) # start
        end = int(fields[4]) # stop
        exon=genome.seq[start -1:end -1] #create an individual substring
        
	# reverse complement for each '-' strand
        strand=(str(fields[6]))
        if strand == "-"
            rev = exon.reverse_complement()
            print(exon.reverse_complement())
        return rev	

def parse_gff(args, genome):
    coding_seqs = defaultdict(dict)
    with open(args.gff_file, 'r') as gff:
        reader = csv.reader(gff, delimiter='\t')
        for line in reader:
            if not line:
                continue
            else:
                    seqname=line[0]
                    source=line[1]
                    feature=line[2]
                    start=int(line[3]) -1
                    end=int(line[4]) -1
                    score=line[5]
                    strand=line[6]
                    frame=line[7]
                    attribute=line[8]

        # reverse complement the feature if necessary

        if(feature == 'CDS'):
            # split the attributes field into its separate parts, to get the gene info
            exon_info = attributes.split(':')

            print(exon_info)
	
            # extract the gene_name
            gene_name = fields[0].split()[1]
	
            if len(exon_info[0].split()) >2:
                # extract the exon number
                exon_number = exon_info[0].split()[-1]
                #print(gene_name, exon_number)

                if gene_name in coding_seqs:
                    # store the coding sequence for this exon
                else:
                    # first time encountering this gene, so declare the dictionary for it
                    coding_seqs[gene_name] = {}

                    # store the coding sequence for this exon
                    coding_seqs[gene_name][exon_number] = feature_sequence
            else:
                continue

    # done reading GFF file, loop over coding_seqs to print the CDS sequences
    for gene, exons in coding_seqs.items():
        # new variables
        # make a variable that will hold the concatenated sequences
        cds_for_this_gene =''
        # print the FASTA header for this gene ( si that it prints citrullus lanatus and then gene)
        print('>' + gene.replace('_', '_') + '_' + gene)
        for exon_num, exon_seq in sorted(exons.items()):
            cds += exon_seq
            print(exon_seq, end='')
		
		

            # test whether there is or isn't an entry in index 2, which holds the value 'exon'
            # for genes that have introns. If there is no value to index 2, then the gene doesn't
            # have an intron, and we can just print it
          #  if len(fields[0].split()[2]) > 2:
           #     print('This gene has an intron')
          #  else:
           #     print('>' + line[0].replace('_', '_') + '_' + gene_name)
            #    print(feature_sequence)  


def main():
# get arguments before calling main
	args = get_args()
	genome = read_fasta(args)
	gff,exon = read_gff(args, genome)
	gc_content = gc_calc(args, genome)
	rev=rev_comp(args, genome)

# execute by calling main
if __name__=="__main__":
        main()
