def extract_gi_id(description):
    """Given a FASTA file description line, return its GenInfo ID if it has one"""
    fields = description[1:].split('|')
    if 'gi' not in fields:
        return None
    return fields[1 + fields.index('gi')]

def get_gi_ids(filename):
    """Return a list of GenInfo IDs from the sequences in the FASTA file named filename"""
    with open(filename) as file:
        return [extract_gi_id(line) for line in file if line[0] == '>']

def get_gi_ids_from_files(filenames):
    """Return a list of GenInfo IDs from the seqeuences in the FASTA files whose names are in the collection filenames"""
    idlst = []
    for filename in filenames:
        idlst += get_gi_ids(filename)
    return idlst

def get_gi_ids_from_user_files():
    response = input("Enter FASTA file names, separated by spaces:")
    lst = get_gi_ids_from_files(response.split())
    lst.sort()
    print(lst)

get_gi_ids_from_user_files()
