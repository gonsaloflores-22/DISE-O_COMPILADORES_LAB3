def ini(tokens):
    i = 0
    error = ''

    if i < len(tokens) and tokens[i] == 10:
        i, error = for_stmt(tokens, i)
        if error != '':
            return error
    else:
        return 'ERROR'

    if i < len(tokens) and tokens[i] == 50:
        i = i + 1
    if i < len(tokens):
        return 'ERROR '
    return 'VÁLIDO'

def for_stmt(tokens, i):
    i = i + 1
    if i < len(tokens) and tokens[i] == 1000:
        i, error = target_list(tokens, i)
        if error != '':
            return i, error
    else:
        return i, 'ERROR'
    if i < len(tokens) and tokens[i] == 11:
        i = i + 1
    else:
        return i, 'ERROR'
    i, error = expression_list(tokens, i)
    if error != '':
        return i, error
    if i < len(tokens) and tokens[i] == 20:
        i = i + 1
    else:
        return i, 'ERROR'
    
    if i < len(tokens) and tokens[i] in (1000, 13):
        i, error = simple_stmt(tokens, i)
        return i, error
    elif i < len(tokens) and tokens[i] == 50:
        while i + 1 < len(tokens) and tokens[i] == 50 and tokens[i + 1] in (1000, 13):
            i, error = suite(tokens, i)
            if error != '':
                return i, error
        if i + 1 < len(tokens) and tokens[i] == 50 and tokens[i + 1] == 12:
            i = i + 1
        if i < len(tokens) and tokens[i] == 12:
            i, error = else_part(tokens, i)
            if error != '':
                return i, error
    else:
        return i, 'ERROR'
    return i, ''


def suite(tokens, i):
    i = i + 1
    return simple_stmt(tokens, i)


def else_part(tokens, i):
    i = i + 1
    if i < len(tokens) and tokens[i] == 20:
        i = i + 1
    else:
        return i, 'ERROR '
    if i < len(tokens) and tokens[i] == 50:
        i = i + 1
    if i < len(tokens) and tokens[i] in (1000, 13):
        return suite_else(tokens, i)
    return i, 'ERROR '


def suite_else(tokens, i):
    i, error = simple_stmt(tokens, i)
    if error != '':
        return i, error
    while i + 1 < len(tokens) and tokens[i] == 50 and tokens[i + 1] in (1000, 13):
        i, error = suite(tokens, i)
        if error != '':
            return i, error
    return i, ''
    
def simple_stmt(tokens, i):
    if i < len(tokens) and tokens[i] == 13:
        i = i + 1
    elif i < len(tokens) and tokens[i] == 1000:
        i = i + 1
        if i < len(tokens) and tokens[i] == 22:
            i = i + 1
        else:
            return i, 'ERROR'
        i, error = term(tokens, i)
        if error != '':
            return i, error
    else:
        return i, 'ERROR '
    return i, ''

def target_list(tokens, i):
    i = i + 1
    while i < len(tokens) and tokens[i] == 21:
        i = i + 1
        if i < len(tokens) and tokens[i] == 1000:
            i = i + 1
        else:
            return i, 'ERROR'
    return i, ''

def expression_list(tokens, i):
    i, error = term(tokens, i)
    if error != '':
        return i, error
    while i < len(tokens) and tokens[i] == 21:
        i = i + 1
        i, error = term(tokens, i)
        if error != '':
            return i, error
    return i, ''

def term(tokens, i):
    if i < len(tokens) and tokens[i] in (1000, 2000):
        i = i + 1
    else:
        return i, 'ERROR '
    return i, ''

tokens = [10, 1000, 11, 1000, 20, 50,
          1000, 22, 2000, 50,
          13, 50,
          12, 20, 50,
          13, 50]

print(ini(tokens))