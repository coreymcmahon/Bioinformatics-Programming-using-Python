import sys

endresults = '- - - - - - - - end Results - - - - - -'
patterns = ('</em>', '\n', '</a></div><div class="rprtMainSec"><div class="summary">')

def get_field(content, pattern, endpos):
    endpos = contents.rfind(pattern,0,endpos)
    if endpos < 0:
        raise StopIteration
    startpos = contents.rfind(pattern,0,endpos)
    return (endpos, contents[startpos+1:endpos])

def get_next(contents, endpos):
    fields = []
    for pattern in patterns:
        endpos, field = get_field(contents,pattern,endpos)
        fields.append(field)
    fields.reverse()
    return endpos, fields

def get_gene_info(contents):
    lst = []
    endpos = contents.rfind(endresults,0,len(contents))
    try:
        while(True):
            endpos, fields = get_next(contents, endpos)
            lst.append(fields)
    except StopIteration:
        pass
    lst.reverse()
    return lst

def get_gene_info_from_file(filename):
    with open(filename) as file:
        contents = file.read()
    return get_gene_info(contents)

def show_gene_info_from_file(filename):
    infolst = get_gene_info_from_file(filename)
    for info in infolst:
        print(info[0], info[1], info[2], sep='\n    ')

if __name__ == '__main__':
    show_gene_info_from_file(sys.argv[1] if len(sys.argv) > 1 else 'EntrezGeneResults.html')
