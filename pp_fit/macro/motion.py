
import random
import os
import sys
import logging
import time

from math import sqrt

logging.basicConfig(level=logging.DEBUG)
random.seed(313)

kSamplingPeriod  = 0.1
kStartTime       = 2.0
kAbsTimeRes      = 0.01
kNumSamples      = 12
kStartPosition   = 2.3
kAbsPositionRes  = 0.3
kRelPositionRes  = 0.05
kSpeed           = 10.0

t = []
x = []
for i in range(kNumSamples):
    t.append(i*kSamplingPeriod)
    x.append(kStartPosition + kSpeed*i*kSamplingPeriod)

def writeHeader(outputFile):
    outputFile.writelines('# Written by motion.py on %s.\n' % time.asctime())
    outputFile.writelines('# Speed: %.3f m/s.\n' % kSpeed)
    outputFile.writelines('# t\tx\tdt\tdx\n')    

def leastSquares(outputFilePath):
    logging.info('Running leastSquares (base ouput file %s)...' %\
                 outputFilePath)
    t_vec  = []
    x_vec  = []
    dx_vec = []
    outputFile = file(outputFilePath, 'w')
    LaTeXFile  = file(outputFilePath.replace('.dat', '_table.tex'), 'w')
    writeHeader(outputFile)
    for i in range(kNumSamples):
        dtime = 0.0
        time  = t[i]
        dpos  = kAbsPositionRes
        pos   = x[i] + random.gauss(0, dpos)
        t_vec.append(time)
        x_vec.append(pos)
        dx_vec.append(dpos)
        outputFile.writelines('%.3f\t%.3f\t%.3f\t%.3f\n' %\
                              (time, pos, dtime, dpos))
        LaTeXFile.writelines('$%.2f$ & $%.2f$ & $%.2f$ \\\\\n' %\
                                 (time, pos, dpos))
    outputFile.close()
    LaTeXFile.close()
    leastSquaresLinearFit(t_vec, x_vec, dx_vec,\
                          outputFilePath.replace('.dat', '_lsparams.tex'))
    logging.info('Done.\n')

def leastSquaresLinearFit(x, y, dy, LaTeXFilePath):
    logging.info('Fitting with the least squares method...')
    sx  = 0
    sxx = 0
    sy  = 0
    sxy = 0
    n   = len(x)
    for i in range(n):
        sx  += x[i]
        sxx += x[i]*x[i]
        sy  += y[i]
        sxy += x[i]*y[i]
    x0  = (sy*sxx - sx*sxy)/(n*sxx - sx*sx)
    v0  = (n*sxy - sx*sy)/(n*sxx - sx*sx)
    dx0 = sqrt(dy[0]*dy[0]*sxx/(n*sxx - sx*sx))
    dv0 = sqrt(dy[0]*dy[0]*n/(n*sxx - sx*sx))
    LaTeXFile = file(LaTeXFilePath, 'w')
    LaTeXFile.writelines('\\begin{eqnarray*}\n')
    LaTeXFile.writelines('x_0 & = & %.2f \pm %.2f \\m\\\\\n' % (x0, dx0))
    LaTeXFile.writelines('v_0 & = & %.2f \pm %.2f \\m/{\\rm s}\\\\\n' %\
                             (v0, dv0))
    LaTeXFile.writelines('\\end{eqnarray*}\n')
    LaTeXFile.close()
    logging.info('x0 = %.2f +- %.2f' % (x0, dx0))
    logging.info('v0 = %.2f +- %.2f' % (v0, dv0))
    chiSquareTest(x, y, dy, x0, v0, LaTeXFilePath.replace('params', 'chitest'))

def leastChiSquare(outputFilePath):
    logging.info('Running leastChiSquare (base ouput file %s)...' %\
                 outputFilePath)
    t_vec  = []
    x_vec  = []
    dx_vec = []
    outputFile = file(outputFilePath, 'w')
    LaTeXFile  = file(outputFilePath.replace('.dat', '_table.tex'), 'w')
    writeHeader(outputFile)
    for i in range(kNumSamples):
        dtime = 0.0
        time  = t[i]
        dpos  = kRelPositionRes*x[i]
        pos   = x[i] + random.gauss(0, dpos)
        t_vec.append(time)
        x_vec.append(pos)
        dx_vec.append(dpos)
        outputFile.writelines('%.3f\t%.3f\t%.3f\t%.3f\n' %\
                              (time, pos, dtime, dpos))
        LaTeXFile.writelines('$%.2f$ & $%.2f$ & $%.2f$ \\\\\n' %\
                             (time, pos, dpos))
    outputFile.close()
    leastChiSquareLinearFit(t_vec, x_vec, dx_vec,\
                            outputFilePath.replace('.dat', '_lcparams.tex'))
    leastSquaresLinearFit(t_vec, x_vec, dx_vec,\
                          outputFilePath.replace('.dat', '_lsparams.tex'))
    logging.info('Done.\n')

def leastChiSquareLinearFit(x, y, dy, LaTeXFilePath):
    logging.info('Fitting with the least square method...')
    sx  = 0
    sxx = 0
    sy  = 0
    sxy = 0
    sdy = 0
    n   = len(x)
    for i in range(n):
        sx  += x[i]/(dy[i]**2)
        sxx += x[i]*x[i]/(dy[i]**2)
        sy  += y[i]/(dy[i]**2)
        sxy += x[i]*y[i]/(dy[i]**2)
        sdy += 1./(dy[i]**2)
    x0  = (sy*sxx - sx*sxy)/(sdy*sxx - sx*sx)
    v0  = (sdy*sxy - sx*sy)/(sdy*sxx - sx*sx)
    dx0 = sqrt(sxx/(sdy*sxx - sx*sx))
    dv0 = sqrt(sdy/(sdy*sxx - sx*sx))
    LaTeXFile = file(LaTeXFilePath, 'w')
    LaTeXFile.writelines('\\begin{eqnarray*}\n')
    LaTeXFile.writelines('x_0 & = & %.2f \pm %.2f \\\\\n' % (x0, dx0))
    LaTeXFile.writelines('v_0 & = & %.2f \pm %.2f \\\\\n' % (v0, dv0))
    LaTeXFile.writelines('\\end{eqnarray*}\n')
    LaTeXFile.close()
    logging.info('x0 = %.2f +- %.2f' % (x0, dx0))
    logging.info('v0 = %.2f +- %.2f' % (v0, dv0))
    chiSquareTest(x, y, dy, x0, v0, LaTeXFilePath.replace('params', 'chitest'))

def chiSquareTest(x, y, dy, x0, v0, LaTeXFilePath):
    logging.info('Running the chisquare test...')
    chi2 = 0
    n    = len(x)
    ndof = n - 2
    for i in range(n):
        chi2 += ((y[i] - x0 - v0*x[i])**2)/(dy[i]**2)
    LaTeXFile = file(LaTeXFilePath, 'w')
    LaTeXFile.writelines('$$\n')
    LaTeXFile.writelines('S = %.2f \\qquad (\\nu = %d)\n' %\
                         (chi2, ndof))
    LaTeXFile.writelines('$$\n')
    LaTeXFile.close()
    logging.info('chi^2 = %.2f (ndof %d)' % (chi2, ndof))

def general():
    pass


leastSquares('least_squares.dat')
leastChiSquare('least_chisquare.dat')
leastChiSquare('least_chisquare_test.dat')
