
from secrets import randbelow
import schedule
import time
from .models import *
from numpy.random import randint
import numpy as np
#animals health is reduced by passed random value. n is percentage by which health must reduce
def reduceHealth(n,currentHealthValue):
    newValue = currentHealthValue - (n / 100 * currentHealthValue)
    print(newValue)
    return newValue
#reduce health of animals
def implementHourProvoke():
    print("I'm inside job")
    monkey=Monkey.objects.all()
    giraffe=Giraffe.objects.all()
    elephant=Elephant.objects.all()
    for value in monkey:
        randNumber=(randbelow(21)) #generate a random value for each animal
        newHealthPercentage=reduceHealth(randNumber,value.healthPercentage)
        value.healthPercentage=newHealthPercentage
        if (value.healthPercentage < 30):
            value.animalStatus='Dead'
        elif (value.healthPercentage==100.0):
            value.animalStatus="Very Healthy"
        else:
            value.animalStatus="Healthy"

        value.save()  #save value to the db
    for value in giraffe:
        randNumber=(randbelow(21))
        newHealthPercentage=reduceHealth(randNumber,value.healthPercentage)
        value.healthPercentage=newHealthPercentage
        if (value.healthPercentage < 50):
            value.animalStatus='Dead'
        elif (value.healthPercentage == 100.0):
            value.animalStatus = "Very Healthy"
        else:
            value.animalStatus = "Healthy"
        value.save()
    for value in elephant:
        randNumber=(randbelow(21))
        newHealthPercentage=reduceHealth(randNumber,value.healthPercentage)
        value.healthPercentage=newHealthPercentage
        if (value.healthPercentage < 70):
            value.animalStatus='Dead'
        elif (value.healthPercentage==100.0):
            value.animalStatus="Very Healthy"
        else:
            value.animalStatus="Healthy"

        value.save()



#multiply already fractioned number by its animalHealthPercentage value and set maximum to 100
def randForFeeding(randomList, animalHealthPercentage):
    for n in randomList:
        increment = animalHealthPercentage * n #value by which health would increase
        randomList.remove(n)
        break
    result = (animalHealthPercentage + increment)

    result[result > 100] = 100
    return result.tolist(),randomList


#save the respective health to the database
def impactHealth(monkey,giraffe,elephant,monkeyResult,giraffeResult,elephantResult,count):
    for value in monkey:
         value.healthPercentage=monkeyResult[count]
         #check if monkey health is less than 30
         if (value.healthPercentage < 30):
                value.animalStatus='Dead'
         elif (value.healthPercentage == 100.0):
             value.animalStatus = "Very Healthy"
         else:
             value.animalStatus = "Healthy"

         count+=1
         value.save()
    count=0
    for value in giraffe:
        value.healthPercentage=giraffeResult[count]
        #check if giraffe has health percentage below 50
        if (value.healthPercentage < 50):
            value.animalStatus='Dead'
        elif (value.healthPercentage==100.0):
            value.animalStatus="Very Healthy"
        else:
            value.animalStatus="Healthy"

        count+=1
        value.save()
    count = 0
    for value in elephant:
        value.healthPercentage=elephantResult[count]
        #check if elephant has health percentage below 70
        if (value.healthPercentage < 70):
            value.animalStatus='Dead'
        elif (value.healthPercentage==100.0):
            value.animalStatus="Very Healthy"
        else:
            value.animalStatus="Healthy"

        count+=1
        value.save() #save value to the database


def commenceFeeding():
    #generate three random value
    randomList = randint(10, 26, 3)
    randomList = np.divide(randomList, 100) #generate random number and divide it by 100 to get fraction
    randomList = randomList.tolist()

    #create instances of animals' object
    monkey=Monkey.objects.all()
    giraffe=Giraffe.objects.all()
    elephant=Elephant.objects.all()
    #create a list to append health percentage to
    monkeyValue=list()
    giraffeValue=list()
    elephantValue=list()
     #append health percentages for each animal
    for value in monkey:
        monkeyValue.append(value.healthPercentage)


    for value in giraffe:
        giraffeValue.append(value.healthPercentage)


    for value in elephant:
        elephantValue.append(value.healthPercentage)


    monkeyResult,randomList=randForFeeding(randomList, np.array(monkeyValue)) #returns new health value and list of random values for elephant and giraffe
    giraffeResult,randomList=randForFeeding(randomList, np.array(giraffeValue)) #returns new health value and list of random values for elephant and giraffe
    elephantResult,randomList=randForFeeding(randomList, np.array(elephantValue)) #returns new health value and list of random values for elephant and giraffe

    count=0#keep track of the health of each individual animal of each animal type
    impactHealth(monkey, giraffe, elephant, monkeyResult, giraffeResult, elephantResult, count) #function to save respective health database


