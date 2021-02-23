import templates as tp
from random import randint as rn
import random
import matplotlib
import matplotlib.pyplot as plt

p = 228

x  = []
y_s = []
y_i = []
y_r = []

#initial variables
days = 20 
fams  = 500
buildings = 250
school_lockdown =True
ldstart = 0
ldstop = 50

#lists for sorting people
school = []
city = []
families = []
testing_grounds = []
testing_grounds2 = []

b = tp.Building()

#retreat function
def retreat(Person, a):
    for i in families: 
        if type(a) == type(b):
            if i.nr == Person.nr:
                i.insert(Person)
                a.room.pop(a.room.index(Person))
        else:
            if i.nr == Person.nr:
                i.insert(Person)
                a.pop(a.index(Person))



#creates families
for i in range(0, fams):
    families.append(tp.Family(i))

#Families sorted in such a way that 10% of the pop is comprised of students
familien = [4, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

#puts people in families
for i in families:
    c = familien[rn(0, len(familien)-1)]
    for j in range(0, c):
        i.insert(tp.Person(False, i.nr, True, False, False, 1000, False))

#creates students in families
for i in families:
    if len(i.room) == 3:
        i.room[0].Student = True
    if len(i.room) == 4:
        i.room[0].Student = True
        i.room[1].Student = True

#puts buildings in city
for i in range(0, buildings):
    city.append(tp.Building())

#check for imital people
f = 0
for i in families:
        for j in i.room:
            f+=1
print('init pop:', f)


#patient 0 sequence
patient_0 = rn(0, len(families))
families[patient_0].room[0].infectify()
families[patient_0].room[0].infection_date = 0


#DAY LOOP SEQUENCE:

for day in range(0, days):

    #inittiate counters for each category of person

    counter_s = 0
    counter_i = 0
    counter_r = 0


    ld = ldstop >= day and day >= ldstart
    #sorts Students form adults
    if school_lockdown and ld:
        for i in families:
            for j in range(0, len(i.room)):
                    if i.room[0].Student:
                        i.room.append(i.room[0])
                        i.room.pop(0)

                    else:
                        testing_grounds2.append(i.room[0])
                        i.room.pop(0)
    else:
        for i in families:
            for j in range(0, len(i.room)):
                if i.room[0].Student:
                    school.append(i.room[0])
                    i.room.pop(0)

                else:
                    testing_grounds2.append(i.room[0])
                    i.room.pop(0)

    #shuffles shit
    random.shuffle(testing_grounds2)
    random.shuffle(school)

    #helpful numbers
    adults = len(testing_grounds2)
    adults_per_building = adults/buildings
    students = len(school)

    people = adults + students

    #people first get sorted into testing grounds2 to then be inserted into builings
    for j in city:
        for i in range(0, int(adults_per_building)):
            j.insert(testing_grounds2[0])
            testing_grounds2.pop(0)

    #Sickness in buildings
    for i in city:
        for j in range(0, int(adults_per_building)):
            if i.room[j].status() == "I":
                for y in i.room:
                    c=rn(0, 1000)
                    if p>=c:
                        y.sickify()
                    else:
                        continue

    #Sickness in school: THERE IS ONLY ONE SCHOOL FOR NOW SO ALL STUDENTS GET SORTED INTO SMA SCHOOL -> should be changed for very large populations
    for i in school:
        if i.status() == "I":
            for j in school:
                c=rn(0, 1000)
                if p>=c:
                    j.sickify()


    #retreat -> people get sent back to original families
    for j in range(0, len(school)):
        retreat(school[0], school)
    for j in city:
        for i in range(0, int(adults_per_building)):
            retreat(j.room[0], j)

    #Sickness in families
    for i in families:
        for j in i.room:
            if j.status() == "I":
                for y in i.room:
                    c=rn(0, 1000)
                    if p>=c:
                        y.sickify()
                    else:
                        continue

    #status update and counters get updated
    for i in families:
        for j in range(0, len(i.room)):
            i.room[j].status_update(day)
            if i.room[j].status() == "S":
                counter_s +=1
            if i.room[j].status() == "I":
                counter_i+=1
            if i.room[j].status() == "R":
                counter_r+=1

    x.append(day)
    y_s.append(counter_s)
    y_i.append(counter_i)
    y_r.append(counter_r)

#check for people
g = 0
for i in families:
        for j in i.room:
            g+=1
print('end pop', g)

plt.plot(x, y_s, "blue", label = 'Susceptible')
plt.plot(x, y_i, "red", label = 'Infected')
plt.plot(x, y_r, "grey", label = 'Recovered')

plt.title('Pandemic Simulation')
plt.xlabel('days')
plt.ylabel('people')

plt.legend(loc = 'best')

plt.show()




