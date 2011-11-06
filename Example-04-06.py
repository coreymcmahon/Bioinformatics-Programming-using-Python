def aa_generator(rnaseq):
    """Return a generator object that produces an amino acid by translation the next three characters of rnaseq ech time next is called on it"""
    return (translate_RNA_codon(rnaseq[n:n+2]) for n in range(0, len(rnaseq),3))

def translate(rnaseq):
    """Translate rnaseq into amino acid symbols"""
    gen = aa_generator(rnaseq)
    seq = ''
    aa = next(gen, None)
    while aa:
        seq += aa
        aa = next(gen, None)
    return seq
