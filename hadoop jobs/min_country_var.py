""" 

Costa Rica Institute of Technology


-- Map reduce job for getting by continents the countries that have the minimum variable values

-- This job takes the information from the resulting file created by the web crawler, all data 
fetched by the scrapper is retrieved from https://en.tutiempo.net/climate


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

from itertools import tee


def float_conversion(value):

# Parses the floating point values recieved according to the document
# provided by the web crawler

    if value == '-':
        return float('inf')
    else:
        return float(value)


def mapper(_, text, writer):

# Maps the countries with the values of the variables

    row = text.split(';', 4)
    continent = row[0]
    country = row[1]
    vars = [float_conversion(e) for e in row[4].split(';')]

    writer.emit(continent, (country, vars))


def reducer(key, values, writer):

# Reduces by taking the minimum value of every variable in the set of variables of each country

    cont = 0
    max_vars = []

    for e in tee(values, 11):

        max_vars.append(min(e, key = lambda i : i[1][cont])[0])
        cont += 1 

    writer.emit(key, ';'.join(map(str, max_vars)))