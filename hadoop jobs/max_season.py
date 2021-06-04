def float_conversion(value):
    if value == '-':
        return 0
    else:
        return float(value)


def mapper(_, text, writer):
    row = text.split(';', 9)
    slist = row[9].split(';')
    snd = [float_conversion(e) for e in slist]
    seasons = [('Rain', snd[0]), ('Snow', snd[1]), ('Storm', snd[2]), ('Foggy', snd[3]), ('Tornado', snd[4]), ('Hail', 1)]
    
    writer.emit( row[1] , max(seasons, key = lambda i : i[1]) )


def reducer(key, variables, writer):

    writer.emit(key, max(variables, key = lambda i : i[1])[0] )