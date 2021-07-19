def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("The length of the strands should be the same!")

    return sum([n1 != n2 for n1, n2 in zip(strand_a, strand_b)])
