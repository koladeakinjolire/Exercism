def proteins(strand):
    codon_amino = {'AUG':'Methionine', 'UUU':'Phenylalanine', 'UUC':'Phenylalanine', 'UUA':'Leucine', 'UUG':'Leucine', 'UCU':'Serine', 'UCC':'Serine', 'UCA':'Serine', 'UCG':'Serine', 'UAU':'Tyrosine', 'UAC':'Tyrosine', 'UGU':'Cysteine', 'UGC':'Cysteine', 'UGG':'Tryptophan', 'UAA':'STOP', 'UAG':'STOP', 'UGA':'STOP'}
    three_piece = [strand[i:i+3] for i in range(0, len(strand), 3)]
    protein = []
    for codon in three_piece:
        if codon_amino[codon] == 'STOP':
            break
        protein.append(codon_amino[codon])
    return protein

print(proteins('AUGUUUUGG')) 
print(proteins('AUG'))
print(proteins('UUU'))
print(proteins('UUA'))
print(proteins('UCU'))
print(proteins('UCA'))
print(proteins('UAU'))
print(proteins('UGC'))
print(proteins('UGG'))
print(proteins('UGA'))