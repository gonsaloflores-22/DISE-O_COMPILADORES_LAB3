def ini(tokens):
    i = 0
    error = ''
    if i < len(tokens) and tokens[i] == 1:
        i, error = def_stmt(tokens, i)
        if error != '':
            return error
    else:
        return 'ERROR'

    if i < len(tokens) and tokens[i] == 8:
        i = i + 1
    if i < len(tokens):
        return 'ERROR'
    return 'VÁLIDO'

def def_stmt(tokens, i):
    i = i + 1
    if i < len(tokens) and tokens[i] == 9:
        i = i + 1
    else:
        return i, 'ERROR'
    if i < len(tokens) and tokens[i] == 6:
        i = i + 1
        if i < len(tokens) and tokens[i] != 7:
            i, error = parametros(tokens, i)
            if error != '':
                return i, error
        if i < len(tokens) and tokens[i] == 7:
            i = i + 1
        else:
            return i, 'ERROR'
    if i < len(tokens) and tokens[i] == 3:
        i = i + 1
    else:
        return i, 'ERROR'
    if i < len(tokens) and tokens[i] in (9, 2):
        i, error = simple_stmt(tokens, i)
        return i, error
    elif i < len(tokens) and tokens[i] == 8:
        i = i + 1
        i, error = simple_stmt(tokens, i)
        if error != '':
            return i, error
        while i + 1 < len(tokens) and tokens[i] == 8 and tokens[i + 1] in (9, 2):
            i = i + 1
            i, error = simple_stmt(tokens, i)
            if error != '':
                return i, error
    else:
        return i, 'ERROR'
    return i, ''

def parametros(tokens, i):
    if i < len(tokens) and tokens[i] == 9:
        i = i + 1
    else:
        return i, 'ERROR'
    while i < len(tokens) and tokens[i] == 4:
        i = i + 1
        if i < len(tokens) and tokens[i] == 9:
            i = i + 1
        else:
            return i, 'ERROR'
    return i, ''

def simple_stmt(tokens, i):
    if i < len(tokens) and tokens[i] == 2:
        i = i + 1
    elif i < len(tokens) and tokens[i] == 9:
        i = i + 1
        if i < len(tokens) and tokens[i] == 5:
            i = i + 1
        else:
            return i, 'ERROR'
        i, error = term(tokens, i)
        if error != '':
            return i, error
    else:
        return i, 'ERROR'
    return i, ''

def term(tokens, i):
    if i < len(tokens) and tokens[i] in (9, 10):
        i = i + 1
    else:
        return i, 'ERROR'
    return i, ''

tokens = [1, 9, 6, 9, 4, 9, 7, 3, 8,
          9, 5, 9, 8,
          2, 8]
print(ini(tokens))