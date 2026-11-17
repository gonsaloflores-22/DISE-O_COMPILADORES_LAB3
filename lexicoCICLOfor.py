def lexico(codigo):
    estado = 0
    tokens = []
    palabra = ''
    i = 0
    n = len(codigo)
    while i < n or estado != 0:
        c = codigo[i] if i < n else ''
        if estado == 0:
            if c.isalpha() or c == '_':
                estado = 1
                i = i + 1
                palabra = palabra + c
                continue
            elif c.isdigit():
                estado = 7
                i = i + 1
                palabra = palabra + c
                continue
            elif c == '\n':
                i = i + 1
                if len(tokens) > 0 and tokens[-1] != 50:
                    estado = 3
                continue
            elif c == ':':
                estado = 4
                i = i + 1
                continue
            elif c == ',':
                estado = 5
                i = i + 1
                continue
            elif c == '=':
                estado = 6
                i = i + 1
                continue
            elif c.isspace():
                i = i + 1
                continue
            else:
                i = i + 1
        elif estado == 1:
            if c.isalnum() or c == '_':
                estado = 1
                i = i + 1
                palabra = palabra + c
                continue
            else:
                estado = 2
                continue
        elif estado == 2:
            if palabra == 'for':
                tokens.append(10)
            elif palabra == 'in':
                tokens.append(11)
            elif palabra == 'else':
                tokens.append(12)
            elif palabra == 'pass':
                tokens.append(13)
            else:
                tokens.append(1000)
            palabra = ''
            estado = 0
            continue
        elif estado == 3:
            tokens.append(50)
            estado = 0
            continue
        elif estado == 4:
            tokens.append(20)
            estado = 0
            continue
        elif estado == 5:
            tokens.append(21)
            estado = 0
            continue
        elif estado == 6:
            tokens.append(22)
            estado = 0
            continue
        elif estado == 7:
            if c.isdigit():
                estado = 7
                i = i + 1
                palabra = palabra + c
                continue
            else:
                estado = 8
                continue
        elif estado == 8:
            tokens.append(2000)
            palabra = ' '
            estado = 0
            continue
    return tokens
    
codigo = '''
for i in lista:
    x = 5
    pass
'''
print(lexico(codigo))