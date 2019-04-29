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

def read_fasta():
        # read in the FASTA file
        genome = SeqIO.read(args.fasta_file, 'fasta') # genome.seq is the pure genome sequence
        return genome.seq 

def read_gff(args, genome):
        # this is an extra function in case something needs to be changed in the future
	# (open & parse gff) read in every field of the gff file
    with open(args.gff_file, 'r') as gff:
        reader = csv.reader(gff, delimiter ='\t')
        for line in reader:
            if not line:
                continue
            else:
                    seqname=line[0]
                    source=line[1]
                    feature=line[2]
                    start=int(line[3])
                    end=int(line[4])
                    score=line[5]
                    strand=line[6]
                    frame=line[7]
                    attribute=line[8]
    return(seqname, source, feature, start, end, score, strand, frame, attribute)

def parse_gff(genome):
	# we need to make a dictionary
    # key = gene name, value = dictionary
    # gene name/ exon#/ exon sequence
    coding_seqs = defaultdict(dict)
	# opening and reading GFF file
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

        	# create the sequence for each feature
		    feature_sequence = genome[start:end]
		# reverse complement the feature if necessary and OVERWRITE
                    if(strand == '-'):
                        feature_sequence = rev_comp(feature_sequence)

                    # calculate GC of feature
                    gc_content = gc(feature_sequence)
        	    if(feature == 'CDS'):
            		# split the attributes field into its separate parts, to get the gene info
            		exon_info = attribute.split(':')

            		print(exon_info)
	
            		# extract the gene_name
            		gene_name = fields[0].split()[1]
	
            		if len(exon_info[0].split()) >2:
                		# extract the exon number
                		exon_number = exon_info[0].split()[-1]
                		#print(gene_name, exon_number)

                		if gene_name in coding_seqs:
                    			# store the coding sequence for this exon
					coding_seqs[gene_name][exon_number] = feature_sequences
				else:
                    			# first time encountering this gene, so declare the dictionary for it
                    			coding_seqs[gene_name] = {}

                    			# store the coding sequence for this exon
                    			coding_seqs[gene_name][exon_number] = feature_sequence
            		else:
                		#continue
				# print the sequence in FASTA format
				print('>' + line[0].replace('','_') + '_' + gene_name)
				print(feature_sequence)

    # done reading GFF file, loop over coding_seqs to print the CDS sequences
    for gene, exons in coding_seqs.items():
        # new variables
        # make a variable that will hold the concatenated sequences
        cds_for_this_gene =''
        # print the FASTA header for this gene ( si that it prints citrullus lanatus and then gene)
        print('>' + line[0].replace('_', '_') + '_' + gene)
        for exon_num, exon_seq in sorted(exons.items()):
            cds += exon_seq
        print(exon_seq, end='')
	
def rev_comp(seq): # much more simplified reverse complement than before
    return seq.reverse_complement()

def gc(seq): # much more simplified GC content than before
    seq = seq.upper()
    count_of_G = seq.count('G')
    count_of_C = seq.count('C')
    return (count_of_G + count_of_C) / len(seq)		

def main():
	genome = read_fasta()
	parse_gff(genome)

# get arguments before calling main
	args = get_args()
# execute by calling main
if __name__=="__main__":
        main()
