list_year = []
annual_temps = []
counter = 0
current_continent = ''

def float_conversion(value):
    if value == '-':
        return 0
    else:
        return float(value)


def mapper(_, text, writer):
    global current_continent
    global counter

    row = text.split(';')

    if counter == 0:

        current_continent = row[0]


    if (counter == 10 and current_continent == row[0]):

        value = current_continent + 'YEARS: ' + '-'.join(list_year)
        avg_temps = sum(annual_temps) / len(annual_temps)
        annual_temps.clear()
        list_year.clear()
        counter = 0
        writer.emit( value , avg_temps)

    elif (current_continent != row[0]):
        annual_temps.clear()
        list_year.clear()
        current_continent = row[0]
        counter = 0

    else:
        current_continent = row[0]
        annual_temp = float_conversion(row[4])
        annual_temps.append(annual_temp)
        list_year.append(row[3])
        counter += 1


def reducer(key, variables, writer):

    writer.emit(key, sum(variables))

