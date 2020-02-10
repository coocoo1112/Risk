import random
import ast
peopleFile = open("people.txt")
responsibleFile = open("responsible.txt")
countFile = open("runningCount.txt")
responsibleString = responsibleFile.read()
peopleString = peopleFile.read()
countString = countFile.read()
people = ast.literal_eval(peopleString)
responsible = ast.literal_eval(responsibleString)
count = ast.literal_eval(countString)
def pick(house):
    a = random.choice(house)
    if count[a] > min(count.values()):
        return pick(house)
    else:
        count[a] += 1
        return a
inp = 1001
while(inp != -1):
    print("===========menu=============")
    print("1. add person to responsible")
    print("2. remove person from responsible")
    print("3. view responsible")
    print("4. add person to regular")
    print("5. remove person from regular")
    print("6. view regular")
    print("7. Create duties")
    try:
        inp = int(input("please put down your choice : "))
        print()
    except Exception as e:
        print(e)
    if inp == 1:
        personAdded = input("who do you want to add: ")
        print(responsible)
        responsible.append(personAdded)
        print(responsible)
        responsibleFile = open("responsible.txt", "w+")
        responsibleFile.write(str(responsible))
    if inp == 2:
        personRemoved = input("who do you want to remove: ")
        responsible.remove(personRemoved)
        responsibleFile = open("responsible.txt", "w+")
        responsibleFile.write(str(responsible))
    if inp == 3:
        for i, person in enumerate(responsible):
            print("{}: {}".format(i+1,person))
    if inp == 4:
        personAdded = input("who do you want to add: ")
        people.append(personAdded)
        peopleFile = open("people.txt", "w+")
        peopleFile.write(str(people))
    if inp == 5:
        personRemoved = input("who do you want to remove: ")
        people.remove(personRemoved)
        peopleFile = open("people.txt", "w+")
        peopleFile.write(str(people))
    if inp == 6:
        for i,person in enumerate(people):
            print("{}: {}".format(i+1,person))
    if inp == 7:
        numPeople = input("how many people do you need to work")
        numResponsible = input("how many responsible people do you need")
        print("=========Regular==========")
        for i in range(numPeople):
            print("{}: {}".format(i+1,pick(people)))
        print("=========Responsible==========")
        for i in range(numResponsible):
            print("{}: {}".format(i+1,pick(responsible)))
        countFile = open("runningCount.txt", "w+")
        countFile.write(count)
    if inp == -1:
        print("Thanks")
        peopleFile.close()
        responsibleFile.close()
        countFile.close()




