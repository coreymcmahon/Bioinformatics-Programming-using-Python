def aa_generator(rnaseq):
    """Return a generator object that produces an amino acid by translating the next three characters of rnaseq each time next is called on it"""
    return (translate_RNA_codon(rnaseq[n:n+3]) for n in range (0, len(rnaseq), 3))
