def item_generator(src):
    """Return a generator that produces a FASTA sequence from src eachj time it is called"""
    skip_intro(src)
    seq = ''
    description = src.readline().split("|")
    line = src.readline()
    while line:
        while line and line[0] != '>':
            seq += line
            line = src.readline()
        yield(description, seq)
        seq = ''
        description = line.split("|")
        line = src.readline()

def skip_intro(src):
    pass

def get_items(src, testfn = None):
    """Return all the items in src; if testfn then include ONLY those items for which testfn is True"""
    return [item for item in item_generator(src) if not testfn or testfn(item)]



def get_GenBank_items_and_sequence_from_file(filename):
    with open(filename) as file:
        return [get_ids(file), get_items(file), get_sequence(file)]

def get_ids(src):
    line = src.readline()
    while not line.startswith('VERSION'):
        line = src.readline()
    parts = line.split()
    assert 3 == len(parts), parts
    giparts = parts[2].partition(':')
    assert giparts[2], giparts
    assert giparts[2].isdigit()
    return (parts[1], giparts[2])

def get_sequence(src):
    """"Return the DNA sequence found atend of src"""
    # When this is called the ORIGIN line should have just been read, so we just have to read the sequence lines until the // at the end
    seq = ''
    line = src.readline()
    while not line.startswith('//'):
        seq += line[10:-1].replace(' ', '')
        line = src.readline()
    return seq

def skip_intro(src):
    """Skip introductory text that appears before the first item in src"""
    line = src.readline()
    while not line.startswith("FEATURES"):
        line = src.readline()

attribute_prefix = 21 * ' ' + '/'
def is_attribute_start(line):
    return line and line.startswith(attribute_prefix)

def is_feature_start(line):
    return line and line[5] != ' '

def next_item(src):
    """Return a generator that produces a FASTA sequence from src each time it is called"""
    skip_intro(src)
    line = src.readline()
    while not line.startswith("ORIGIN"):
        assert is_feature_start(line)
        feature, line = read_feature(src,line)
        yield feature

def read_feature(src, line):
    feature = line.split()
    props = {}
    line = src.readline()
    while not is_feature_start(line):
        key, value = line.strip()[1:].split('=')
        if value[0] == '"':
            value = value[1:]
        fullvalue, line = read_value(src, line, value)
        props[key] = fullvalue
    feature.append(props)
    return feature, line

def read_value(src, line, value):
    line = src.readline()
    while (not is_attribute_start(line) and not is_feature_start(line)):
        value += line.strip()
        line = src.readline()
    if value[-1] == '"':
        value = value[:-1]
    return value, line
