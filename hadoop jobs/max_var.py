def float_conversion(value):
    if value == '-':
        return 0
    else:
        return float(value)


def mapper(_, text, writer):
    row = text.split(';', 4)
    variables = row[4].split(';')
    var_num = [float_conversion(e) for e in variables]
    writer.emit((row[1]) , (int(row[3]), max(var_num)) )


def reducer(key, variables, writer):

    writer.emit(key, max(variables, key = lambda i : i[1])[0] )
