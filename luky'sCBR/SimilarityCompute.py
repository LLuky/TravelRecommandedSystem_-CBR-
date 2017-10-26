# This file compute the similarity for each attribute
# (user will input 9): { HolidayType, Price lowest bound, Price upper bound,NumberOfPersons,
#                       Region, Transportation, Duration, Season, Accommodation }
# attrMap (Dictionary - 10): + "JourneyCode" + "per Person" + only have　"Price"
# caseMap (the JourneyCode is KEY of cases):

# The similarities for each attr calculate seprately into differing ways.
# in the end we will combine them into one double value that is the SIMILARITies of these cases with user input.

from DataLoading import *

import math
# from sklearn.metrics.pairwise import cosine_similarity
from scipy import spatial


class SimilarityLists:
    def __init__(self,fileName, userInput, weightSetting):
        self.fileName = fileName
        self.userInput = userInput
        # Custermize weights
        self.weightSetting = weightSetting;
        self.l = Loading(self.fileName)

        # The Case Base Container:  we did not use this Map in this class
        self.caseMap = self.l.loadCase()

        # The Vocabulary Container:
        self.attrMap,self.attrList  = self.l.loadData()



    # Sim = 1- ManhattanDist Distance
    def ManhattanDist(self):
        similarityList = []
        holySim,prSim,nSim,rSim,tSim,dSim,sSim,aSim = self.examAll()
        totalWeight = sum(self.weightSetting.values())

        for i in range(0, len(holySim)-1):

            similarityList.append(((holySim[i] + prSim[i] + nSim[i] + rSim[i]
                                    + tSim[i] + dSim[i] + sSim[i] + aSim[i])/totalWeight)*100)
        return similarityList

    # Sim = 1- Euclidean Distance
    def EuclideanDist(self):
        similarityList = []
        holySim,prSim,nSim,rSim,tSim,dSim,sSim,aSim = self.examAll()
        totalWeight = math.sqrt(sum( a**2 for a in self.weightSetting.values()))
        for i in range(0, len(holySim)-1):
            similarityList.append((math.sqrt(holySim[i]**2 + prSim[i]**2 + nSim[i]**2 + rSim[i]**2
                                    + tSim[i]**2 + dSim[i]**2 + sSim[i]**2 + aSim[i]**2)/totalWeight)*100)
        return similarityList

    # Cosine Similarity
    def CosineSim(self):
        similarityList = []
        holySim,prSim,nSim,rSim,tSim,dSim,sSim,aSim = self.examAll()
        # the list with 100% similarity
        org = [val for val in self.weightSetting.values()]
        for i in range(0, len(holySim)-1):
            current = []
            current.append(holySim[i])
            current.append(prSim[i])
            current.append(nSim[i])
            current.append(rSim[i])
            current.append(tSim[i])
            current.append(dSim[i])
            current.append(sSim[i])
            current.append(aSim[i])
            # conpare cosine similarity between org & current
            similarityList.append((self.cosine_similarity(org, current))*100)

        return similarityList

    def cosine_similarity(self, x,y):
        result = 1- spatial.distance.cosine(x, y)
        '''
        result = 1- cosine_similarity(x,y)

        # SELF-WRITED
        dotPriduct =
        '''
        return result


    def examAll(self):
        holySim = self._examHoly()
        prSim = self. _examPrice()
        nSim = self._examNumberOfPersons()
        rSim = self. _examRegion()
        tSim = self._examTransportation()
        dSim = self. _examDuration()
        sSim = self._examSeason()
        aSim = self. _examAccommodation()
        return holySim,prSim,nSim,rSim,tSim,dSim,sSim,aSim

    # Classify type later！！！！！！！！！！！！！
    def _examHoly(self):
        ht = "HolidayType"
        holySim = []
        userHoly = self.userInput[ht]
        dataHoly = self.attrMap[ht]
        for HT in dataHoly:
            if (HT == userHoly) or (userHoly is "Arbitrary"):
                holySim.append(self.weightSetting[ht])
            else:
                holySim.append(0.0)

        return holySim

    def _examPrice(self):
        p = "Price"
        prSim = []
        userUpper = self.userInput["PriceUp"]
        userLower = self.userInput["PriceLow"]
        dataPrice = self.attrMap[p]
        for P in dataPrice:
            if userLower < P < userUpper:
                prSim.append(self.weightSetting[p])
            else:
                prSim.append(0.0)
        return prSim


    def _examNumberOfPersons(self):
        n = "NumberOfPersons"
        nSim = []
        userN = self.userInput[n]
        dataN = self.attrMap[n]
        for N in dataN:
            if userN == N:
                nSim.append(self.weightSetting[n]) # user definedable
            elif (userN == N+2) or (userN == N-2):
                nSim.append(self.weightSetting[n]*0.5)
            elif (userN == N+1) or (userN == N-1):
                nSim.append(self.weightSetting[n]*0.1)
            else:
                nSim.append(0.0)
        return nSim

    def _examRegion(self):
        r = "Region"
        rSim = []
        userRegion = self.userInput[r]
        dataRegion = self.attrMap[r]

        waterRegion = ['AdriaticSea', 'BalticSea', 'NorthSea', 'TurkishAegeanSea', 'Allgaeu',
                       'Algarve', 'Atlantic', 'Balaton', 'Bavaria','Belgium', 'Bornholm',
                       'BlackForest', 'Bulgaria', 'Cairo', 'Carinthia', 'Chalkidiki', 'Corfu',
                       'Corsica', 'CostaBlanca', 'CostaBrava','CotedAzur', 'Crete', 'Cyprus',
                       'Denmark', 'Fuerteventura', 'GranCanaria', 'Holland', 'Ibiza', 'Ireland',
                       'Lanzarote','Riviera', 'TurkishRiviera', 'Lolland', 'LowerAustria',
                       'Madeira', 'Mallorca', 'Malta', 'Normandy', 'Poland', 'Rhodes',
                       'Salzkammergut', 'Scotland', 'Sweden', 'Switzerland', 'Teneriffe', 'Wales']
        mountainRegion = ['Allgaeu', 'Alps','Bavaria','BlackForest', 'Bornholm','Carinthia',
                          'Corsica', 'Dolomites', 'ErzGebirge', 'GiantMountains', 'Harz',
                          'HighTatra', 'Ireland', 'LowerAustria', 'Madeira', 'SalzbergerLand',
                          'Salzkammergut', 'Scotland', 'Slowakei', 'Switzerland', 'Styria',
                          'Tyrol', 'Wales']
        cultureRegion = ['Denmark', 'England', 'France', 'Poland', 'Thuringia','Wales']
        for R in dataRegion:
            if (userRegion is "Arbitrary") or (R == userRegion):
                rSim.append(self.weightSetting[r]) # user definedable
            elif(userRegion is "Waters") and (R == reg for reg in waterRegion):
                rSim.append(self.weightSetting[r])
            elif(userRegion is "Mountains") and (R == reg for reg in mountainRegion):
                rSim.append(self.weightSetting[r])
            elif(userRegion is "Culture") and (R == reg for reg in cultureRegion):
                rSim.append(self.weightSetting[r])
            else:
                rSim.append(0.0)
        return rSim

    # DECISION TABLE~~ ！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
    def _examTransportation(self):
        t = "Transportation"
        tSim = []
        userT = self.userInput[t]
        dataT = self.attrMap[t]
        for T in dataT:
            if (userT is "Arbitrary") or (T == userT):
                tSim.append(self.weightSetting[t]) # user definedable
            else:
                tSim.append(0.0)
        return tSim

    def _examDuration(self):
        d = "Duration"
        dSim = []
        userD = self.userInput[d]
        dataD = self.attrMap[d]
        for D in dataD:
            if D == userD:
                dSim.append(self.weightSetting[d]) # user definedable
            elif (userD == D+3) or (userD == D-3):
                dSim.append(self.weightSetting[d]*0.1) # Duration +-3 :  10%
            elif (userD == D+2) or (userD == D-2):
                dSim.append(self.weightSetting[d]*0.4) # Duration +-3 :  40%
            elif (userD == D+1) or (userD == D-1):
                dSim.append(self.weightSetting[d]*0.7) # Duration +-3 :  70%
            else:
                dSim.append(0.0)
        return dSim


    def _examSeason(self):
        s= "Season"
        sSim = []
        userS = self.userInput[s]
        dataS = self.attrMap[s]
        for S in dataS:
            if userS == "Arbitrary":
                sSim.append(self.weightSetting[s])
            elif (S is 1) and ((userS == "January") or (userS == "Winter")):
                sSim.append(self.weightSetting[s])
            elif (S is 2) and ((userS == "February") or (userS == "Winter")):
                sSim.append(self.weightSetting[s])
            elif (S is 3) and ((userS == "March") or (userS == "Spring")):
                sSim.append(self.weightSetting[s])
            elif (S is 4) and ((userS == "April") or (userS == "Spring")):
                sSim.append(self.weightSetting[s])
            elif (S is 5) and ((userS == "May") or (userS == "Spring")):
                sSim.append(self.weightSetting[s])
            elif (S is 6) and ((userS == "June") or (userS == "Summer")):
                sSim.append(self.weightSetting[s])
            elif (S is 7) and ((userS == "July") or (userS == "Summer")):
                sSim.append(self.weightSetting[s])
            elif (S is 8) and ((userS == "August") or (userS == "Summer")):
                sSim.append(self.weightSetting[s])
            elif (S is 9) and ((userS == "September") or (userS == "Autumn")):
                sSim.append(self.weightSetting[s])
            elif (S is 10) and ((userS == "October") or (userS == "Autumn")):
                sSim.append(self.weightSetting[s])
            elif (S is 11) and ((userS == "November") or (userS == "Autumn")):
                sSim.append(self.weightSetting[s])
            elif (S is 12) and ((userS == "December") or (userS == "Winter")):
                sSim.append(self.weightSetting[s])
            else:
                sSim.append(0.0)
        return sSim

    # Convert User Input Accommodation value into IntegerNumber
    def __AccToInt(self, userA):
        score = -1
        if(userA == "HolidayFlat"):
            score=0;
        elif(userA == "OneStar"):
            score=1;
        elif(userA == "TwoStars"):
            score=2;
        elif(userA == "ThreeStars"):
            score=3;
        elif(userA == "FourStars"):
            score=4;
        elif(userA == "FiveStars"):
            score=5;
        else:
            score = userA # "Arbitrary"

        return score


    def _examAccommodation(self):
        a= "Accommodation"
        userA = self.__AccToInt(self.userInput[a])

        if(userA == 'Holiday Flat'):
            userA = 0
        elif(userA == 'One Star'):
            userA = 1
        elif(userA == 'Two Stars'):
            userA = 2
        elif(userA == 'Three Stars'):
            userA = 3
        elif(userA == 'Four Stars'):
            userA = 4
        elif(userA == 'Five Stars'):
            userA = 5



        aSim = []

        dataA = self.attrMap[a]
        for A in dataA:
            if userA == "Arbitrary":
                aSim.append(self.weightSetting[a])
            elif A == userA:
                aSim.append(self.weightSetting[a])
            elif (A+1 == userA) or (A-1 == userA):
                aSim.append(self.weightSetting[a]*0.7)
            elif (A+2 == userA) or (A-2 == userA):
                aSim.append(self.weightSetting[a]*0.4)
            elif (A+3 == userA) or (A-3 == userA):
                aSim.append(self.weightSetting[a]*0.1)
            else:
                aSim.append(0.0)
        return aSim


'''
    def square_rooted(self, x):
        return round(math.sqrt(sum([a*a for a in x])),3)

    def cosine_similarity(self, x,y):
        numerator = sum(a*b for a,b in zip(x,y))
        denominator = self.square_rooted(x)*self.square_rooted(y)
        return round(numerator/float(denominator),3)
'''
















''' Print KEY
        for key,value in self.attrMap.items():
            print(key)
'''