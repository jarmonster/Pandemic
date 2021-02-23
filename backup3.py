import templates as tp
from random import randint as rn
import random
import matplotlib
import matplotlib.pyplot as plt

b = tp.Building()
p = 228

x  = []
y_s = []
y_i = []
y_r = []

days = 20 #int(input("days nigga, i need days: "))
fams  = 500
buildings = 250
school_lockdown =True
ldstart = 0
ldstop = 50

school = []
city = []
families = []
testing_grounds = []
testing_grounds2 = []

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

f = 0
for i in families:
        for j in i.room:
            f+=1
print(f)


#patient 0 sequence
patient_0 = rn(0, len(families))
families[patient_0].room[0].infectify()
families[patient_0].room[0].infection_date = 0

#DAY LOOP SEQUENCE:
"""for i in families:
    for j in range(0, len(i.room)):
        print(i.room[j].nr, i.room[j].Student) """

for day in range(0, days):
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

    #adults are sorted into buildings
    for j in city:
        for i in range(0, int(adults_per_building)):
            j.insert(testing_grounds2[0])
            testing_grounds2.pop(0)

    #in the city boys
    for i in city:
        for j in range(0, int(adults_per_building)):
            if i.room[j].status() == "I":
                for y in i.room:
                    c=rn(0, 1000)
                    if p>=c:
                        y.sickify()
                    else:
                        continue

    #in the school boys
    for i in school:
        if i.status() == "I":
            for j in school:
                c=rn(0, 1000)
                if p>=c:
                    j.sickify()


    #retreat
    for j in range(0, len(school)):
        retreat(school[0], school)
    for j in city:
        for i in range(0, int(adults_per_building)):
            retreat(j.room[0], j)

    #sickening
    for i in families:
        for j in i.room:
            if j.status() == "I":
                for y in i.room:
                    c=rn(0, 1000)
                    if p>=c:
                        y.sickify()
                    else:
                        continue

    #status update
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

#check
g = 0
for i in families:
        for j in i.room:
            g+=1
print(g)

plt.plot(x, y_s, "blue")
plt.plot(x, y_i, "red")
plt.plot(x, y_r, "grey")

plt.show()

"""for i in families:
    for j in range(0, len(i.room)):
        print("Family: ", i.room[j].nr, "is Student: ",  i.room[j].Student, "Status: ",  i.room[j].status())"""


"""print(type(testing_grounds2[0]))
city[0].insert(testing_grounds2[0])"""


"""print("school: ")
for i in school:
    print(i.Student, i.nr)
"""


"""print("city: ")
for i in testing_grounds2:
    print(i.Student, i.nr)"""


