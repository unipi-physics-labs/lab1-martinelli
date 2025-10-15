

kWheels = ['BA', 'FI', 'MI', 'NA', 'PA', 'RM', 'TO', 'VE', 'CA', 'GE', 'RN']
kInputFilePath = 'lotto.txt'

outcomes = {}
for wheel in kWheels:
    outcomes[wheel] = [0]*91

data = file(kInputFilePath).readlines()
for datum in data:
    datum = datum.strip('\n').strip().split('\t')
    datum = datum[1:]
    wheel = datum[0]
    for i in range(1, 6):
        datum[i] = int(datum[i])
        outcomes[wheel][datum[i]] += 1

for wheel in kWheels:
    entries = sum(outcomes[wheel][1:])
    trials = entries/5
    constant = float(entries)/90
    chisquare = 0
    for i in range(1, 91):
        chisquare += (outcomes[wheel][i] - constant)**2/constant
    outputFile = file('lotto_%s.dat' % wheel, 'w')
    outputFile.writelines('# trials = %d\n' % trials)
    outputFile.writelines('# constamt = %.3f\n' % constant)
    outputFile.writelines('# chisquare = %.3f\n' % chisquare)
    for i in range(1, 91):
        outputFile.writelines('%d\t%d\n' % (i, outcomes[wheel][i]))
    outputFile.close()
