# This file uses the data from "SimilarityCOmpute.py" adapting cases to solve new problems.
# Basically it just return the k-higest similarity of cases.

from SimilarityCompute import *
import numpy as np
import heapq  # https://docs.python.org/2/library/heapq.html

class Retrieve:
    def __init__(self,fileName, userInput, weightSetting):
        self.fileName, self.userInput, self.weightSetting = fileName, userInput, weightSetting
        self.SimiLists = SimilarityLists(self.fileName, self.userInput, self.weightSetting)
        self.caseMap = self.SimiLists.caseMap
        self.attrList = self.SimiLists.attrList



    # Access CaseMap to retrieve top Cases
    def _retrieve(self,TopMap,topK):

        for k in range(1, topK+1):
            case = self.caseMap[TopMap[k][0]]
            print("Top", k,": (Similarity -- ", TopMap[k][1], "%)")
            print("=======================================================")
            counter = 0
            for key in self.attrList:
                print(self.attrList[counter], ": ", case[key])
                counter = counter+1


            # print("Similarity: ", TopMap[k][1], "%")
            print("=======================================================")
        return



    def _TopK_Manhattan(self,topK):
        mDis = self.SimiLists.ManhattanDist()
        mArr = np.array(mDis)
        TopMap = self.__returnTopMap(topK, mArr)
        self._retrieve(TopMap,topK)
        return TopMap

    def _TopK_Euclidean(self,topK):
        eDis = self.SimiLists.EuclideanDist()
        eArr = np.array(eDis)
        TopMap = self.__returnTopMap(topK, eArr)
        self._retrieve(TopMap,topK)
        return TopMap

    def _TopK_Cosine(self,topK):
        cDis = self.SimiLists.CosineSim()
        cArr = np.array(cDis)

        TopMap = self.__returnTopMap(topK, cArr)
        # print("Top Map: ", TopMap)
        self._retrieve(TopMap,topK)
        return TopMap


    def __returnTopMap(self, topK, arr):

        # Ranking
        rankedIndex = arr.argsort()[-topK:][::-1]
        # all index+1 (0...k-1) -> (1...k)
        rankedIndex = [i+1 for i in rankedIndex]

        # K-nearest neighbours' Value List:
        rankedVal = heapq.nlargest(topK, arr)

        # Wrap the rankedIndex & ranked Val together into TopMap
        TopMap = {}
        for i in range(0,topK):
            TopMap[i+1] = [rankedIndex[i], rankedVal[i]]

        return TopMap


'''

name="TRAVEL.csv"
user={'HolidayType': 'Bathing', 'PriceUp': 2345.0, 'PriceLow': 100.0, "Region": "Mountains",
      'NumberOfPersons': 2, 'Transportation': 'Plane', 'Duration': 5, 'Season': 'Autumn', 'Accommodation': 'Four Stars'}
weightSetting = {'HolidayType': 10.0, 'Price': 2.0, "Region": 1.0, 'NumberOfPersons': 1.0,
                 'Transportation': 1.0, 'Duration': 3, 'Season': 2, 'Accommodation': 3}
sl = Retrieve(name, user,weightSetting)
#sl._TopK_Manhattan(3)
#sl._TopK_Euclidean(3)
sl._TopK_Cosine(2)







hDis = sl.ManhattanDist()
print(hDis)
print("ManhattanDist Max:", max(hDis))
eDis = sl.EuclideanDist()
print(eDis)
print("EuclideanDist Max: ", max(eDis))

eDis = sl.CosineSim()

print(eDis)
print("CosineSim Max: ", max(eDis))
#Sim = sl._examAccommodation()
#print(Sim)
'''