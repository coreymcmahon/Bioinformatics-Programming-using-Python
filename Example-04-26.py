tree = ['',
    ['A',
        ['CC',
            ['CCTGATTACCG'],
            ['G']
        ],
        ['TTACCG']
    ],
    ['C',
        ['C',
            ['CTGATTACCG'],
            ['TGATTACCG'],
            ['G']
        ],
        ['TGATTACCG'],
        ['G']
    ],
    ['T',
        ['GATTACCG'],
        ['TACCG'],
        ['ACCG']
    ],
    ['GATTACCG']
]

def treeprint(tree, level=0):
    print(' ' * 4 * level, tree[0], sep = '')
    for node in tree[1:]:
        treeprint(node,level+1)
