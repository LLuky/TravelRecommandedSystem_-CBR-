# This file is for transforing data form csv file (we already parse and convert original version by java)
#                                       into a data structure Dictionary (java called HashMap)

import csv
import arff

# Fail to connect with weka
# from weka.core.converters import Loader

# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.pyplot as pyplot
# from matplotlib.colors import LogNorm


# Read  *.csv column by column



# INITIALIZE:  attrMap["Key"]="Value"

class Loading:


    # name = fileName

    def __init__(self, fileName):
        # Two dictionaries
        self.fileName = fileName




    def accessData(self, fileName, list, str):
        i=0
        with open(fileName) as f:
            reader = csv.DictReader(f)
            for row in reader:
                list.insert(i, row[str]) # need parse to float -> float(row[str])
                i=i+1

    # Read  *.csv row by row
    def loadCase(self):
        fileName = self.fileName
        caseMap={}
        with open(fileName) as f:
            reader = csv.DictReader(f)
            i=0
            for row in reader:
                i=i+1
                caseMap[i] = row

        return caseMap



    def loadData(self):
        attrMap={}
        fileName_csv = self.fileName

        # Key Strings
        j='JourneyCode'
        ht='HolidayType'
        p='Price'
        n='NumberOfPersons'
        r='Region'
        t='Transportation'
        d='Duration'
        s='Season'
        a='Accommodation'
        h='Hotel'
        attrList=[j,ht,p,n,r,t,d,s,a,h]


        # Value Lists
        JourneyCodeList = []
        HolyList = []
        PriceList =[]
        NumberIfPersonsList = []
        RegionList = []
        TransportationList = []
        DurationList = []
        SeasonList = []
        AccommodationList = []
        HotelList = []


        # PerPersonList = []
        # PerDayList = []
        # PerPerList = []



        self.accessData(fileName_csv, JourneyCodeList, j)
        self.accessData(fileName_csv, HolyList, ht)
        self.accessData(fileName_csv, PriceList, p)

        self.accessData(fileName_csv, NumberIfPersonsList, n)
        self.accessData(fileName_csv, RegionList, r)
        self.accessData(fileName_csv, TransportationList, t)
        self.accessData(fileName_csv, DurationList, d)
        self.accessData(fileName_csv, SeasonList, s)
        self.accessData(fileName_csv, AccommodationList, a)
        self.accessData(fileName_csv, HotelList, h)
        # accessData(fileName_csv, PerPersonList, str='per Person')
        # accessData(fileName_csv, PerDayList, str='per Day')
        # accessData(fileName_csv, PerPerList, str='per per')

        # e.g. Convert all items in a list from String to Integer --- [int(i) for i in JourneyCodeList]
        attrMap[j]=[int(i) for i in JourneyCodeList] # JourneyCodeList
        attrMap[ht]=HolyList
        attrMap[p]= [float(i) for i in PriceList] # PriceList
        attrMap[n]= [float(i) for i in NumberIfPersonsList] # NumberIfPersonsList
        attrMap[r]=RegionList
        attrMap[t]=TransportationList
        attrMap[d]=[int(i) for i in DurationList] # DurationList
        attrMap[s]=[int(i) for i in SeasonList]# SeasonList
        attrMap[a]=[int(i) for i in AccommodationList] # AccommodationList
        attrMap[h]=HotelList

        return attrMap,attrList

'''
    def htList(self):
        for row in arff.load(self.fileName,".arff"):
            x=row.'HolidayType'

        loader = Loader(classname="weka.core.converters.ArffLoader")

        data = loader.load_file(data_dir + "iris.arff")
        data.class_is_last()

        print(data)

        return

l = Loading("TRAVEL")
l.htList()
'''