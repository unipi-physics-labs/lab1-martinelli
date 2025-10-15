#! /usr/env python

import os
import sys
import time

kMonthDict = {1: 'Gennaio'  , 2 : 'Febbraio', 3 : 'Marzo'   , 4: 'Aprile',\
              5: 'Maggio'   , 6 : 'Giugno'  , 7 : 'Luglio'  , 8: 'Agosto',\
              9: 'Settembre', 10: 'Ottobre' , 11: 'Novembre', 12: 'Dicembre'}

edition  = 'Quinta edizione, Ottobre 2014'
ltime    = time.localtime()
year     = ltime.tm_year
month    = kMonthDict[ltime.tm_mon]
day      = ltime.tm_mday
hour     = ltime.tm_hour
minutes  = ltime.tm_min

if hour < 10:
    hour = '0%d' % hour
else:
    hour = '%d' % hour
if minutes < 10:
    minutes = '0%d' % minutes
else:
    minutes = '%d' % minutes

date     = '%d %s %d' % (day, month, year)
hour_min = '%s:%s'    % (hour, minutes)

outputFilePath = os.path.join('cc_complementi', 'frontespizio.tex')

cover = '\\begin{titlepage}\n\\begin{center}\n\\vspace{1cm}\n\n'        +\
        '\\rule{16 cm}{0.01 cm}\n\\vspace{0.5cm}\\\\\n'                 +\
        '{\\huge \\bfseries Misure ed analisi dei dati:}\\\\\n'         +\
        '\\vspace{0.5cm}\n'                                             +\
        '{\\Large introduzione al Laboratorio di Fisica}\\\\\n'         +\
        '\\vspace{0.5 cm}\n\\rule{16 cm}{0.01 cm}\n\\vspace{1cm}\n\n'   +\
        '\\vspace{2cm}\n'                                               +\
        '\\noindent{\\large \\bfseries Liana Martinelli\n'              +\
        '\\vspace{0.5cm}\n\n'                                           +\
        '\\noindent Luca Baldini}\n\n'                                  +\
        '\\vspace{5cm}\n'                                               +\
        '%s\n\n' % edition                                              +\
        '\\vfill\n'                                                     +\
        '{\\footnotesize '                                              +\
        'Compilato il %s alle ore %s'                                   %\
        (date, hour_min)                                                +\
        '}\n\n'                                                         +\
        '\\end{center}\n\\end{titlepage}\n'

if __name__ == '__main__':
    with open(outputFilePath, 'w') as output_file:
        output_file.writelines(cover)
