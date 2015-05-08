#!/usr/bin/python

from optparse import OptionParser
import re
import sys

def opt_get():
	parser = OptionParser()
	parser.add_option("-i", help = "Input fasta file", dest = "fa_in", type = "string")
	parser.add_option("-o", help = "Output fasta file", dest = "fa_out", type = "string")
	parser.add_option("-s", help = "Output fasta file", dest = "samples", type = "string")
	(options, args) = parser.parse_args()
	return(options)

def sample_read(sample_file):
	samples = {}
	for sample in sample_file:
		sample = sample.rstrip("\n")
		samples[sample] = 1
	return(samples)

def sample_remove(fasta, outfile, samples):
	fout = open(outfile, 'w')
	header = 1
	good = 1
	count = 0
	for line in fasta:
		sys.stdout.write('%s\r' % count)
		sys.stdout.flush()
		if header == 1:
			count += 1
			sample = line.split("_")[0]
			sample = re.sub(">", "", sample)
			if sample in samples:
				samples[sample] += 1
				good = 0
			else:
				print>>fout, line.rstrip("\n")
				good = 1
			header = 0
		else:
			header = 1
			if good == 1:
				print>>fout, line.rstrip("\n")

	for sample in samples:
		print sample, "\t", samples[sample]

def main():
	opts = opt_get()
	fa_in = opts.fa_in
	fa_out = opts.fa_out
	sample_file = opts.samples
	samples = sample_read(open(sample_file))
	sample_remove(open(fa_in), fa_out, samples)

main()