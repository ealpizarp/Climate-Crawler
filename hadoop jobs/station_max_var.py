""" 

Tecnologico de Costa Rica


-- Map reduce job for getting the station that has the maximum values by country

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


def float_conversion(value):

# Parses the floating point values recieved according to the document
# provided by the web crawler

    if value == '-':
        return -200
    else:
        return float(value)


def mapper(_, text, writer):

# Maps the country with a tuple that represent the station wich took
# the measures and the maximum value of the variables 

    row = text.split(';', 4)
    vars = row[4].split(';')
    f_vars = [float_conversion(e) for e in vars]
    
    writer.emit( row[1] , (row[2], max(f_vars)) )


def reducer(key, variables, writer):

# reduces by taking station that got the maximum values

    writer.emit(key, max(variables, key = lambda i : i[1])[0] )