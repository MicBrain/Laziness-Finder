import csv
				# Finding States' Laziness Rankings: #
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

gdps = []
with open('gdp data.csv', 'rb') as csvfile: 
    dataReader = csv.reader(csvfile, delimiter=',')
    for row in dataReader:
        for letter in row[1]:
            if letter == ',':
                row[1].remove(letter)
        gdps.append((row[0], float(row[1])))
gdps.sort(key=lambda x: x[0])

obesitylevels = []
with open('Obesity data.csv', 'rb') as csvfile:
    dataReader = csv.reader(csvfile, delimiter=',')
    for row in dataReader:
        for letter in row[1]:
            if letter == ',':
                row[1].remove(letter)
        obesitylevels.append((row[0], float(row[1])))

educationlevels = []
with open('education data.csv', 'rb') as csvfile:
    dataReader = csv.reader(csvfile, delimiter=',')
    for row in dataReader:
        for letter in row[1]:
            if letter == ',':
                row[1].remove(letter)
        educationlevels.append((row[0], float(row[1])))
educationlevels.sort(key=lambda x: x[0])


projectedmeans = map(float, projectedmeans)

meanlist = []
for i in dataDict:
	i = [i]
	meanlist.append(i)

index = 0
while index < 50:
	meanlist[index].append(projectedmeans[index])
	index +=1

    # Add relevant information #
meanlist.sort(key=lambda x: x[0])
index = 0
while index<50:
    meanlist[index].append(gdps[index][1])
    meanlist[index].append(obesitylevels[index][1])
    meanlist[index].append(educationlevels[index][1])
    index +=1

meanlist.sort(key=lambda x: x[1], reverse= True)

	# Adding rank to each state#

index = 0
rank = 10
n = 0
go = True
while go:
	for i in range(0,5):
		meanlist[index].insert(0, rank)
		index +=1
	rank -=1
	if rank ==0:
		go = False

				#Finding your laziness ranking: #

answers = []
import os

os.system('clear')
print("Laziness Ranker Version 1.0")
print
print("Question 1")
print
print("Which of the following activities is your favorite?")
print
print("A. Going rock climbing.")
print("B. Gardening")
print("C. Hanging out with friends")
print("D. Playing GTA V")
print
answer = raw_input("Please enter the letter of your answer here: ").lower()
answers.append(answer)


os.system('clear')
print
print("Question 2")
print
print("If you saw a baby drowning in a pool, what would you do FIRST?")
print
print("A. Jump in immediately to save it.")
print("B. Make sure no one else is already diving in before saving it.")
print("C. Call 911")
print("D. Slowly put down your sweaty cheesburger and wipe the ketchup from your fingers before applying sun lotion to make sure you don't get burnt whilst saving the poor kid")
print
answer = raw_input("Please enter the letter of your answer here: ").lower()
answers.append(answer)

os.system('clear')
print
print("Question 3")
print
print("What is the reminder of 47/2?")
print
print("A. 1")
print("B. 47")
print("C. Can I phone a friend?")
print("D. I'm skipping this question.")
print
answer = raw_input("Please enter the letter of your answer here: ").lower()
answers.append(answer)

os.system('clear')
print
print("Question 4")
print
print("What's your favorite movie?")
print
print("A. Donnie Darko")
print("B. Inception")
print("C. The Avengers")
print("D. Anything with Adam Sandler.")
print
answer = raw_input("Please enter the letter of your answer here: ").lower()
answers.append(answer)

os.system('clear')
print
print("Question 5")
print
print("Approximately how much of your leisure time is spent doing physical activity?")
print
print("A. 80%")
print("B. 50%")
print("C. 30%")
print("D. 10%")
print
answer = raw_input("Please enter the letter of your answer here: ").lower()
answers.append(answer)

os.system('clear')
print
print("Question 6")
print
print("What would you do if someone ran by and snatched your purse/wallet?")
print
print("A. Trip the basterd.")
print("B. Run after the stealer.")
print("C. Call 911")
print("D. 'Eh. Wasn't that great of a wallet anyway.'")
print
answer = raw_input("Please enter the letter of your answer here: ").lower()
answers.append(answer)

os.system('clear')
print
print("Question 7")
print
print("What is your favorite nightly activity?")
print
print("A. Krav Maga.")
print("B. Taking the dog for a walk")
print("C. Watching TV")
print("D. Watching cat videos on Youtube")
print
answer = raw_input("Please enter the letter of your answer here: ").lower()
answers.append(answer)

os.system('clear')
print
print("Question 8")
print
print("Which item is closest to you at your desk in your room?")
print
print("A. Treadmill")
print("B. Stress ball")
print("C. Potato chips")
print("D. Everything is way too far away for my arm to reach.")
print
answer = raw_input("Please enter the letter of your answer here: ").lower()
answers.append(answer)

os.system('clear')
print
print("Question 9")
print
print("What's your favorite animal?")
print
print("A. Freakin' Tigers")
print("B. Hawks")
print("C. Turtles")
print("D. Sloths")
print
answer = raw_input("Please enter the letter of your answer here: ").lower()
answers.append(answer)

os.system('clear')
print
print("Question 10")
print
print("Why are we here?")
print
print("A. To understand our world, and help each other out at the same time")
print("B. To eat and mate.")
print("C. It's way too early in the morning for this type of question.")
print("D. It's way too late in the evening for this type of question.")
print
answer = raw_input("Please enter the letter of your answer here: ").lower()
answers.append(answer)

def score(inputlist):
    total = 0
    for i in inputlist:
        if i=='a':
            total += 4
        elif i =='b':
            total += 3
        elif i =='c':
            total += 2
        elif i =='d':	
            total += 1
    return total

def rank(score):
    if score<=13:
        return 10
    elif score>13 and score<=16:
        return 9
    elif score>16 and score<=19:
        return 8
    elif score>19 and score<=22:
        return 7
    elif score>22 and score<=25:
        return 6
    elif score>25 and score<=28:
        return 5
    elif score>28 and score<=31:
        return 4
    elif score>31 and score<=34:
        return 3
    elif score>34 and score<=37:
        return 2
    elif score>37:
        return 1

rank = rank(score(answers))

				# Matching you with a group of states #

def correctstate(somelist):
	if somelist[0]==rank:
		return True
	else:
		return False

yourstates1 = filter(correctstate, meanlist)
yourstates = []
index = 0
while index<len(yourstates1):
    yourstates.append(yourstates1[index])
    index +=1

def returnstates(listvalues, index):
    print
    print listvalues[index][1]
    print
    print("GDP per Capita: $" + str(listvalues[index][3]))
    print("Obesity percentage: " + str(listvalues[index][4]) + "%")
    print("Education ranking (out of 100): " + str(listvalues[index][5]))

os.system('clear')
print("Based on your level of physical activity, we suggest you move to one of these states:")
print
returnstates(yourstates, 0)
returnstates(yourstates, 1)
returnstates(yourstates, 2)
returnstates(yourstates, 3)
returnstates(yourstates, 4)