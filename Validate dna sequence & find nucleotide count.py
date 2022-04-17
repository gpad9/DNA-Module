dna_seq = 'AGGGCTACTGT'

def validate_dna_sequence(s):
    for i in s:
        if i in 'AGCT':
            return True

def find_nucleotide_count(s):
    d = {'A' : 0, 'C' : 0, 'G' : 0, 'T' : 0}
    if validate_dna_sequence(s):
        for x in s:
            if x in 'AGCT':
                d[x] += 1
    else:
        return 'Sequence is not valid'
    return d




print(find_nucleotide_count(dna_seq))
