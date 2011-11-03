""" Requires Example-02-18.py

def restriction_cut(base_seq,offset=0):
    """Return a pair of sequences derived from base_seq by splitting it at the first appearance of recognition_seq; offset, which may be negative, is the number of bases relative to the beginning of the site where the sequence is cut"""
    site = recognition_site(base_seq, recognition_seq)
    return base_seq[:site+offset], base_seq[site+offset:]
