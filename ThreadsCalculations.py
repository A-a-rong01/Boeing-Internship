import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Constants for calculating the total resistance
rhoOne = 1/(1.5*(10**5)) ## Resistivity Coeffiecient
rhoTwo = 1/(1.2*(10**5))
Area = math.pi*(((5.5*(10**-6))/2)**2) ## Cross sectional area for a single thread


# function for calculating the resistance for a single fiber
def Calc_res(lenInMili):
    lenInMet =lenInMili * (10**(-3)) # Takes the length given in centimeters and converts to meters
    resistanceNum = (rhoOne * lenInMet)/ Area #calculated the total resistance in a single fiber
    fiberRes = resistanceNum
    return fiberRes

#function which calculates the resistance in the amount of threads given the whole strip and the half length measurements
def find_Res_eff(TotResMes, halfLengResMes): #parameters are the total measured resistance and half length resistance
    contactRes = (2*halfLengResMes) - TotResMes #Finds the contanct resistance
    R_eff = TotResMes - contactRes #Isolates the wanted R_eff resitance by getting rid of the contact resistance
    return R_eff


#The following function calculates the number of threads
def find_Num_threads(R_eff, R_fiber):   #Takes the resistance found in the strip and resistance per fiber
    numOfThreads = R_fiber/R_eff
    return numOfThreads

def Calc_Threads(nameOfStrip, lengthInMent, fullLengthRes, halfLengthRes):
    fiberRes = Calc_res(lengthInMent)
    stripR_eff = find_Res_eff(fullLengthRes, halfLengthRes)
    numOfThreads = find_Num_threads(stripR_eff,fiberRes)
    
    print("For Strip " + nameOfStrip)
    print("The total resiance of fiber is " + str(round(fiberRes, 2)) +" ohms in length of " + str(lengthInCent) +"cm")
    print("The total resitance in the strip adding all the fibers is " + str(round(stripR_eff, 2)))
    print("Given the parameters above the total number of threads is " +str(round(numOfThreads, 2)))
    print()


# StripA = Calc_Threads("A", 18, 93.3, 47.6)
# StripB = Calc_Threads("B", 8, 7.5, 0.3)
# StripC = Calc_Threads("C", 8, 1.6, 0.1)

testLength = [30, 70, 100, 130, 150, 180, 200]
resObsAvgwithContact = [11.557, 18.894, 25.71957, 31.378, 37.65429, 43.06343, 45.39429]
resObsAvg = [obsAvg -5.0533 for obsAvg in resObsAvgwithContact]

fiberResMatrix = []

for len in testLength:
    fiberRes = Calc_res(len)
    fiberResMatrix.append(fiberRes)
    # print(str(round(fiberRes,3)) + " ohms per a single fiber for the length " + str(len))

  
numOfThreads = [fiberRes / obsAvg for fiberRes, obsAvg in zip(fiberResMatrix, resObsAvg)]
for calc, num in zip(numOfThreads, testLength):
    print("At " + str(num) + "mm in length the 1mm wide copper tape has about " + str(round(calc,3)) + " number of threads")
