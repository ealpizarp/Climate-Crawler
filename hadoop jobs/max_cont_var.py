def float_conversion(value):
    if value == '-':
        return 0
    else:
        return float(value)


def mapper(_, text, writer):
    row = text.split(';', 4)
    vars = row[4].split(';')
    var_list = [float_conversion(e) for e in vars]

    writer.emit( row[0] , (row[1],  max(var_list)) )


def reducer(key, variables, writer):

    writer.emit(key, max(variables, key = lambda i : i[1])[0] )