""" 

Tecnologico de Costa Rica


-- Map reduce job for getting the average annual temperture by decades

-- This job takes the information from the resulting file created by the web crawler, all data 
fetched by the scrapper is retrieved from https://en.tutiempo.net/climate

Author: Eric Alpizar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

import statistics

current_year = 2021
year_intervals = []


def float_conversion(value):

# Parses the floating point values recieved according to the document
# provided by the web crawler

    if value == '-':
        return -200
    else:
        return float(value)


def generate_time_intervals (row_year):

# generates time intervals in decades according to the input year 

    global current_year

    tmp_year = row_year + 10

    while tmp_year <= current_year:
    
        year_intervals.append((row_year, tmp_year))
        row_year = tmp_year
        tmp_year += 10


def validate_year(row_year):

# validates is a given year is within the time interval

    for e in year_intervals:
        if row_year >= e[0] and row_year <= e[1]:
            return True
    return False



def time_interval(row_year):

# fetches the time interval corresponding to a given year

    for e in year_intervals:
        if row_year >= e[0] and row_year <= e[1]:
            return e
    return 0

generate_time_intervals(1950)


def mapper(_, text, writer):

# Maps the continent according to the time interval of the measure with the
# average annual temperture value

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

# reduces mapped average tempertures of continents in decades by taking the 
# average of all measures 

    writer.emit(key, statistics.mean(variables))

