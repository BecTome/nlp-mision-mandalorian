import re
def read_close(path, mode='r'):
    '''
    With this function we read, group and put in a list the messages
    '''
    g = open(path, mode)
    out = g.readlines()
    # Concatenate and drop \n from endlines
    out = ''.join(list(map(lambda x: x[:-1], out)))
    g.close()
    return out

def match_g(pattern, x, i):
    return re.match(pattern, x).group(i)