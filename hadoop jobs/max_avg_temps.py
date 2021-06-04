

def mapper(_, text, writer):
    row = text.split(';')
    country = row[1]
    if row[4] == '-':
        temp = -200
    else:
        temp = float(row[4])

    
    if temp != -200:
        writer.emit(country, temp)


def reducer(key, tempertures, writer):

    writer.emit(key, max(tempertures))



