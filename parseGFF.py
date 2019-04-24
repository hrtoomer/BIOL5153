
# to call this script, the gff and fasta file should be input
# the files this was based on:
# fasta_file='watermelon.fsa'
# gff_file ='watermelon.gff'


# Import SeqIO for the win
from Bio import SeqIO
import argparse

 def get_args():
	# create an argument parser object
	parser = argparse.ArgumentParser(description = 'This script returns the input fasta and gff files')

	# add positional argument for the input position
	parser.add_argument(fasta_file, help="The FASTA file you want to input", type=str)
	parser.add_argument(gff_file, help="The GFF file you want to input", type=str)

	# parse the arguments
	return parser.parse_args()

def read_fasta(fasta_file):
        # read in the FASTA file
        genome = SeqIO.read(arg.fasta_file, 'fasta') # genome.seq is the pure genome sequence

        # print (genome.seq)
        return(genome)

def read_gff(gff_file):
        gff=open(arg.gff_file)
        return(gff)

def calculation(gff, genome):
        for line in gff:
            line = line.rstrip('\n')
            fields = line.split('\t') #list the categories of the gff file by the splitting where the tab character is

            start = int(fields[3]) # start
            end = int(fields[4]) # stop
            exon=genome.seq[start:end] #create an individual substring

            # calculate GC content from substring
            lengthexon=len(exon)
            g_count=exon.count('G')
            c_count=exon.count('C')
            gc_content = g_count + c_count / lengthexon # calculate GC content for each substring
            return("GC content is " + str(gc_content))
            gff.close()

            # reverse complement for each '-' strand
            strand=(str(fields[6]))
            if strand == "-":
                   print((exon.reverse_complement()))
            # revcomp=exon.reverse_complement() if strand == "-"
            # print(revcomp)

def main():
        fasta=read_fasta(fasta_file)
        gff=read_gff(gff_file)
        calculation()


# get arguments before calling main
args = get_args()

# execute by calling main
if __name__=="__main__":
        main()
