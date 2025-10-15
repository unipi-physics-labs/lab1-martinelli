inputFilePath = 'wendover.tnt'

data = file(inputFilePath).readlines()[2:]
maxFall = 15

buffers = {}
for month in range(13):
    buffers[month] = [0]*maxFall

for datum in data:
    (year, month, fall) = datum.split('\t')
    month = int(month)
    fall  = int(0.5 + float(fall)/10.)
    buffers[month][fall] += 1
    buffers[0][fall]     += 1

#print buffers

for month in range(13):
    average = 0
    entries = sum(buffers[month])
    for bin in range(maxFall):
        average += bin*buffers[month][bin]
    average /= float(entries)
    print 'Month %d, entries %d, average %f' % (month, entries, average)
    outputFile = file('rainfall_%d.dat' % month, 'w')
    outputFile.writelines('# Month %d, entries %d, average %f\n' %\
                          (month, entries, average))
    for bin in range(maxFall):
        outputFile.write('%d\t%d\n' % (bin, buffers[month][bin]))
    outputFile.close()
