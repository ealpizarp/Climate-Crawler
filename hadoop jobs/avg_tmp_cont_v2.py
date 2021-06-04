import statistics

current_year = 2021
current_continent = ''
year_intervals = []


def lenght(tempertures):
    return sum(1 for e in tempertures)

def float_conversion(value):
    if value == '-':
        return -200
    else:
        return float(value)


def generate_time_intervals (row_year):
    global current_year

    tmp_year = row_year + 10

    while tmp_year <= current_year:
    
        year_intervals.append((row_year, tmp_year))
        row_year = tmp_year
        tmp_year += 10

def validate_year(row_year):

    for e in year_intervals:
        if row_year >= e[0] and row_year <= e[1]:
            return True
    return False

def time_interval(row_year):
    for e in year_intervals:
        if row_year >= e[0] and row_year <= e[1]:
            return e
    return 0


generate_time_intervals(1950)

def mapper(_, text, writer):
    global current_continent

    row = text.split(';')
    row_year = int(row[3])
    row_continent = row[0]
        
    if validate_year(row_year):

        cti = time_interval(row_year)
        value = row_continent + ' ' + '[' + str(cti[0]) + ',' + str(cti[1]) + ']'
        annual_temp = float_conversion(row[4])
        if annual_temp != -200:
            writer.emit( value , float_conversion(row[4]))


def reducer(key, variables, writer):

    writer.emit(key, statistics.mean(variables))

