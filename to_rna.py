def to_rna(dna_strand):
    rna_strand = ""
    for char in dna_strand:
        if char.isalpha() and char == "C":
            rna_strand += "G"
        elif char.isalpha() and char == "G":
            rna_strand += "C"
        elif char.isalpha() and char == "T":
            rna_strand += "A"
        elif char.isalpha() and char == "A":
            rna_strand += "U"
        else: 
            rna_strand += char
    
    return rna_strand