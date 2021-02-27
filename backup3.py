import setup as st
import templates as tp
import random
from random import randint as rn
import matplotlib
import matplotlib.pyplot as plt

#DAY LOOP SEQUENCE:
def main():
    for day in range(0, st.days):

        #inittiate counters for each category of person

        counter_s = 0
        counter_i = 0
        counter_r = 0


        ld = st.ldstop >= day and day >= st.ldstart
        #sorts Students form adults
        if st.school_lockdown and ld:
            for family in st.families:
                for person in range(0, len(family.room)):
                        if family.room[0].Student:
                            family.room.append(family.room[0])
                            family.room.pop(0)

                        else:
                            st.waiting_room.append(family.room[0])
                            family.room.pop(0)
        else:
            for family in st.families:
                for person in range(0, len(family.room)):
                    if family.room[0].Student:
                        st.school.append(family.room[0])
                        family.room.pop(0)

                    else:
                        st.waiting_room.append(family.room[0])
                        family.room.pop(0)

        #shuffles shit
        random.shuffle(st.waiting_room)
        random.shuffle(st.school)

        #helpful numbers
        adults = len(st.waiting_room)
        adults_per_building = adults/st.buildings

        #students = len(st.school)

        #people = adults + students

        #people first get sorted into testing grounds2 to then be inserted into builings
        for building in st.city:
            for person in range(0, int(adults_per_building)):
                building.insert(st.waiting_room[0])
                st.waiting_room.pop(0)

        #Sickness in buildings
        for building in st.city:
            for person in range(0, int(adults_per_building)):
                if building.room[person].status() == "I":
                    for people in building.room:
                        c=rn(0, 1000)
                        if st.p>=c:
                            people.sickify()
                        else:
                            continue

        #Sickness in school: THERE IS ONLY ONE SCHOOL FOR NOW SO ALL STUDENTS GET SORTED INTO SMA SCHOOL -> should be changed for very large populations
        for person in st.school:
            if person.status() == "I":
                for people in st.school:
                    c=rn(0, 1000)
                    if st.p>=c:
                        people.sickify()


        #retreat -> people get sent back to original families
        for person in range(0, len(st.school)):
            st.retreat(st.school[0], st.school)
        for building in st.city:
            for person in range(0, int(adults_per_building)):
                st.retreat(building.room[0], building)

        #Sickness in families
        for family in st.families:
            for person in family.room:
                if person.status() == "I":
                    for people in family.room:
                        c=rn(0, 1000)
                        if st.p>=c:
                            people.sickify()
                        else:
                            continue

        #status update and counters get updated
        for family in st.families:
            for person in range(0, len(family.room)):
                family.room[person].status_update(day)
                if family.room[person].status() == "S":
                    counter_s +=1
                if family.room[person].status() == "I":
                    counter_i+=1
                if family.room[person].status() == "R":
                    counter_r+=1

        st.x.append(day)
        st.y_s.append(counter_s)
        st.y_i.append(counter_i)
        st.y_r.append(counter_r)



if __name__ == "__main__":
    st.size()
    main()
    st.size()

    plt.plot(st.x, st.y_s, "blue", label = 'Susceptible')
    plt.plot(st.x, st.y_i, "red", label = 'Infected')
    plt.plot(st.x, st.y_r, "grey", label = 'Recovered')
    plt.title('Pandemic Simulation')
    plt.xlabel('days')
    plt.ylabel('people')
    plt.legend(loc = 'best')
    plt.show()





