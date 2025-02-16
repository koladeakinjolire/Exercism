def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('Strands must be of equal length.')
    strand_1 = [letter for letter in strand_a ]
    strand_2 = [letter for letter in strand_b]
    length = 0
    for i in range(len(strand_2)):
        if strand_2[i] != strand_1[i]:
            length += 1
    return length

