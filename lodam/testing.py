from typing import Iterable, Dict


def inventory(rows: Iterable[Dict]):
    cols = [
        'dataset',
        'resource',
        'base',
        'model',
        'property',
        'source',
        'prepare',
        'type',
        'ref',
        'level',
        'access',
        'title',
        'description',
    ]

    hpos = cols.index('property')
    hsize = 1  # hierachical column size
    bsize = 3  # border size
    sizes = dict(
        [(c, 1) for c in cols[:hpos]] +
        [(c, len(c)) for c in cols[hpos:]]
    )
    rows = list(rows)
    for row in rows:
        for i, col in enumerate(cols):
            val = str(row[col])
            if i < hpos:
                size = (hsize + bsize) * (hpos - i) + sizes['property']
                if size < len(val):
                    sizes['property'] += len(val) - size
            elif sizes[col] < len(val):
                sizes[col] = len(val)

    line = []
    for col in cols:
        size = sizes[col]
        line.append(col[:size].ljust(size))

    depth = 0
    lines = [line]
    for row in rows:
        line = []

        for i, col in enumerate(cols[:hpos + 1]):
            val = row[col]
            if val:
                depth = i
                break
        else:
            val = ''
            if depth < hpos:
                depth += 1
            else:
                depth = 2

        line += [' ' * hsize] * depth
        size = (hsize + bsize) * (hpos - depth) + sizes['property']
        line += [val.ljust(size)]

        for col in cols[hpos + 1:]:
            val = str(row[col])
            size = sizes[col]
            line.append(val.ljust(size))

        lines.append(line)

    lines = [' | '.join(line) for line in lines]
    indent = '    '
    return '\n'.join([indent + l.rstrip() for l in lines]) + '\n' + indent
