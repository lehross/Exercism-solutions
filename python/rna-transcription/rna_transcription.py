def to_rna(dna_strand):
    rna_strand = []
    for nucl in dna_strand:
        if nucl == 'G':
            rna_strand.append('C')
        elif nucl == 'C':
            rna_strand.append('G')
        elif nucl == 'T':
            rna_strand.append('A')
        elif nucl == 'A':
            rna_strand.append('U')
    return ''.join(rna_strand)
