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
#number of observable days
days = 20         
#number of families. rnages form 2 - 4 members
fams  = 500
#number of buildings in which the adults meet 
buildings = 250

#lockdown variables
school_lockdown =False
ldstart = 0
ldstop = 50

#lists for sorting people
school = []
city = []
families = []
waiting_room = []

b = tp.Building()

#retreat function -> returns people from any array to initial family array
def retreat(Person, array):
    #checks for the Family number that corrisponds to the Persons number.
    for family in families: 
        if type(array) == type(b):
            if family.nr == Person.nr:
                #Adult gets deleted from the current arry they find themselves in and inserted into the initila Family array
                family.insert(Person)
                array.room.pop(array.room.index(Person))
        else:
            if family.nr == Person.nr:
                # same thing happens but for Students/ people not in Buildings
                family.insert(Person)
                array.pop(array.index(Person))



#creates families for number of families
for family in range(0, fams):
    families.append(tp.Family(family))

#Families sorted in such a way that 10% of the pop is comprised of students
familien = [4, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

#puts people in families
for family in families:
    c = familien[rn(0, len(familien)-1)]
    for family_length in range(0, c):
        family.insert(tp.Person(False, family.nr, True, False, False, 1000, False))

#creates students in families
for family in families:
    if len(family.room) == 3:
        family.room[0].Student = True
    if len(family.room) == 4:
        family.room[0].Student = True
        family.room[1].Student = True

#puts buildings in city
for building in range(0, buildings):
    city.append(tp.Building())

#check for imital people
def size():
    pop_size = 0
    for family in families:
            for person in family.room:
                pop_size+=1
    print('init pop:', pop_size)


#patient 0 sequence -> 1 person gets infected
patient_0 = rn(0, len(families))
families[patient_0].room[0].infectify()
families[patient_0].room[0].infection_date = 0