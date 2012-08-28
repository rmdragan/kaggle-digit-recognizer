import collections

def read_csv(file_path, has_header=True, verbose=True):
    '''Reads a csv file with all fields numerical (float).'''
    if verbose: print "reading %s" % file_path
    with open(file_path, 'r') as f:
        if has_header: f.readline()
        data = []
        for line in f:
            line = line.strip().split(',')
            data.append(map(float, line))
        return data

def read_header(file_path):
    """Returns the first line of the file as a string."""
    with open(file_path, 'r') as f:
        header = f.readline()
    return header.strip()

def write_csv(file_path, data, header=None, verbose=True):
    '''Writes the data to file.'''
    if verbose: print "writing %s" % file_path
    with open(file_path, 'w') as f:
        if header:
            f.write(str(header) + '\n')
        if isinstance(data[0], collections.Iterable):
            for line in data:
                f.write(','.join(map(str,line)) + '\n')
        else:
            f.write('\n'.join(map(str, data)))
