import csv

dataDict = {}

with open('data.csv', 'rU') as csvfile:
    dataReader = csv.reader(csvfile, delimiter=',')
    for row in dataReader:
        state = row[0]
        row.pop(0)
        dataDict[state] = row

projectedmeans = []
with open('rafadata.csv', 'rb') as csvfile: 
    dataReader = csv.reader(csvfile, delimiter=',')
    for row in dataReader:
        projectedmeans.append(row[0])



projectedmeans = map(float, projectedmeans)

meanlist = []
for i in dataDict:
    i = [i]
    meanlist.append(i)

index = 0
while index < 50:
    meanlist[index].append(projectedmeans[index])
    index +=1


regions = [['Northeast', 'Maine', 'New Hampshire', 'Vermont', 'Massachusetts', 'Rhode Island', 'Connecticut', 'New York', 'Pennsylvania', 'New Jersey'],['Midwest', 'Wisconsin', 'Michigan', 'Illinois', 'Indiana', 'Ohio', 'Missouri','North Dakota','South Dakota', 'Nebraska','Kansas','Minnesota','Iowa'], ['South', 'Delaware','Maryland','Virginia','West Virginia', 'North Carolina','South Carolina', 'Georgia', 'Florida','Kentucky','Tennessee','Mississippi','Alabama','Oklahoma','Texas','Arkansas','Louisiana'], ['West', 'Idaho','Montana','Wyoming','Nevada','Utah','Colorado','Arizona','New Mexico','Alaska','Washington','Oregon','California','Hawaii']]

for i in meanlist:
    if i[0] in regions[0]:
        i.append(regions[0][0])
    elif i[0] in regions[1]:
        i.append(regions[1][0])
    elif i[0] in regions[2]:
        i.append(regions[2][0])
    elif i[0] in regions[3]:
        i.append(regions[3][0])

northeast = []
south = []
midwest = []
west = []
for i in meanlist: 
    if i[2] == 'Northeast':
        northeast.append(i)
    elif i[2] == 'South':
        south.append(i)
    elif i[2] == 'Midwest':
        midwest.append(i)
    else:
        west.append(i)

def meantotal(liststates):
    total = 0
    for i in liststates:
        total += i[1]
    return total

print "midwest average laziness = " + str(meantotal(midwest)/len(midwest))
print "northeast average laziness = " + str(meantotal(northeast)/len(northeast))
print "south average laziness = " + str(meantotal(south)/len(south))
print "west average laziness = " + str(meantotal(west)/len(west))
