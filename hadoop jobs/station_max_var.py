def float_conversion(value):
    if value == '-':
        return -200
    else:
        return float(value)


def mapper(_, text, writer):
    row = text.split(';', 4)
    vars = row[4].split(';')
    f_vars = [float_conversion(e) for e in vars]
    
    writer.emit( row[1] , (row[2], max(f_vars)) )


def reducer(key, variables, writer):

    writer.emit(key, max(variables, key = lambda i : i[1])[0] )