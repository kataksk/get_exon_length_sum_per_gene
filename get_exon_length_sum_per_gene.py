import sys

in_gff = sys.argv[1]

exon_length_sum = list()

with open(in_gff, 'r') as f:
    for line in f:
        line_list = line.split('\t')
        if line_list[2] == 'gene':
            if 'exon_length' not in locals():
                exon_length = 0
            else:
                exon_length_sum.append(exon_length)
                exon_length = 0
        elif line_list[2] == 'exon':
            tmp = int(line_list[4]) - int(line_list[3])
            exon_length += tmp


for line in exon_length_sum:
    print(line)