#!/usr/bin/python

from optparse import OptionParser
import re

def opt_get():
	parser = OptionParser()
	parser.add_option("-i", help = "Input fasta file",
						dest = "fa_in", type = "string")
	parser.add_option("-o", help = "Output fasta file", dest = "fa_out", type = "string")
	(options, args) = parser.parse_args()
	return(options)

def fa_clean(fasta_in, file_out):
	fout = open(file_out, 'w')
	status = 1
	for line in fasta_in:
		if status == 1:
			print>>fout, line.split("\t")[0]
			status = 0
		else:
			print>>fout, line.rstrip("\n")
			status = 1

def main():
	opts = opt_get()
	fa_in = opts.fa_in
	fa_out = opts.fa_out
	fa_clean(open(fa_in), fa_out)


main()