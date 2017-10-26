# This file handles all the GUI method.
# use package tk (refer to inforhost.nmt.edu/tcc/help/pubs/tkinter/web/index.html)



from tkinter import *
from tkinter import messagebox, Tk, StringVar, ttk
import tkinter as tk

from TopK_knn import *

class AttributeSettingFrame:

    def __init__(self, parent, fileName): # returnFrame,
        self.fileName = fileName

        # Default Setting 好像并没有什么卵用
        self.userInput = self.defaultInput()

        self.weightSetting = self.defaultWeight()

        # Run Retrieve class
        self.knn = Retrieve(self.fileName,self.userInput,self.weightSetting)

        # Frame
        self.parent = parent
        # self.returnFrame = returnFrame

        #Grab Attribute List
        self.attrList = self.knn.attrList
        #Create Label for each attribute that user could set
        self._keyLabels(self.attrList)

        # Get Information
        self.getUserInput()
        self.getWeights()

        self.retrieveButton = Button(self.parent, text = "Start Retrieve",
                                     command = self.new_window
                                      ).grid(row=18, column=2)


    def new_window(self):
        self.newWindow = tk.Toplevel(self.parent)
        self.app = RetrieveFrame(self.newWindow,self.fileName)


    def updateUserSetting(self):
        self.userInput = self.updateInfo()
        self.weightSetting =self.updateWeight()
        self.knn = Retrieve(self.fileName,self.userInput,self.weightSetting)
        return


    def updateWeight(self):
        weightDic = {}

        weightDic[self.attrList[1]] = self.htV.get()
        weightDic[self.attrList[2]] = self.pV.get()
        weightDic[self.attrList[3]] = self.nV.get()
        weightDic[self.attrList[4]] = self.rV.get()
        weightDic[self.attrList[5]] = self.tV.get()
        weightDic[self.attrList[6]] = self.dV.get()
        weightDic[self.attrList[7]] = self.sV.get()
        weightDic[self.attrList[8]] = self.aV.get()

        print("User Weight setting: ", weightDic)
        return weightDic


    def getWeights(self):
        self.htV = IntVar()
        self.pV = IntVar()
        self.nV = IntVar()
        self.rV = IntVar()
        self.tV = IntVar()
        self.dV = IntVar()
        self.sV = IntVar()
        self.aV = IntVar()
        self.htV.set(self.weightSetting[self.attrList[1]])
        self.pV.set(self.weightSetting[self.attrList[2]])
        self.nV.set(self.weightSetting[self.attrList[3]])
        self.rV.set(self.weightSetting[self.attrList[4]])
        self.tV.set(self.weightSetting[self.attrList[5]])
        self.dV.set(self.weightSetting[self.attrList[6]])
        self.sV.set(self.weightSetting[self.attrList[7]])
        self.aV.set(self.weightSetting[self.attrList[8]])

        weightTitle = Label(self.parent,bg = 'gray',fg='white',text="Customizable Similarity Metrics").grid(row=0,column=3)

        spinbox_ht = Spinbox(self.parent, width=3, bd=3, from_=0, to=20, state = NORMAL, textvariable = self.htV).grid(row=2,column=3)
        spinbox_p = Spinbox(self.parent, width=3, bd=3, from_=0, to=20, state = NORMAL, textvariable = self.pV).grid(row=4,column=3)
        spinbox_n = Spinbox(self.parent, width=3, bd=3, from_=0, to=20, state = NORMAL, textvariable = self.nV).grid(row=7,column=3)
        spinbox_r = Spinbox(self.parent, width=3, bd=3, from_=0, to=20, state = NORMAL, textvariable = self.rV).grid(row=9,column=3)
        spinbox_t = Spinbox(self.parent, width=3, bd=3, from_=0, to=20, state = NORMAL, textvariable = self.tV).grid(row=11,column=3)
        spinbox_d = Spinbox(self.parent, width=3, bd=3, from_=0, to=20, state = NORMAL, textvariable = self.dV).grid(row=13,column=3)
        spinbox_s = Spinbox(self.parent, width=3, bd=3, from_=0, to=20, state = NORMAL, textvariable = self.sV).grid(row=15,column=3)
        spinbox_a = Spinbox(self.parent, width=3, bd=3, from_=0, to=20, state = NORMAL, textvariable = self.aV).grid(row=17,column=3)



    def updateInfo(self):
        userInput = {}
        userInput[self.attrList[1]]=self.htBox.get()
        #userInput[self.attrList[2]]=self.htBox.get()
        userInput['PriceLow']=self.min.get()
        userInput['PriceUp']=self.max.get()
        userInput[self.attrList[3]]=self.n.get()
        userInput[self.attrList[4]]=self.rBox.get()
        userInput[self.attrList[5]]=self.tBox.get()
        userInput[self.attrList[6]]=self.d.get()
        userInput[self.attrList[7]]=self.sBox.get()
        userInput[self.attrList[8]]=self.aBox.get()

        print("User Input: ", userInput)
        return userInput


    def getUserInput(self):
        # Create comboBox
        self.comoBoxs()
        # Create Entry
        self.n,self.d = self.textBoxs()
        # Create Slider
        self.min, self.max = self.slider()



    def slider(self):
        min = IntVar()
        max = IntVar()
        max.set(8007)
        label_1 = Label(self.parent,text="Min:  ").grid(row=4,column=0)
        Slider_1 = Scale(self.parent, orient = HORIZONTAL, length = 180, sliderlength=10, from_=239, to=8007,
                         tickinterval=1800,variable = min).grid(row=4,column=1)

        label_2 = Label(self.parent,text="Max:  ").grid(row=5,column=0)
        Slider_2 = Scale(self.parent, orient = HORIZONTAL, length = 180, sliderlength=10, from_=239, to=8007,
                         tickinterval=1800,variable = max).grid(row=5,column=1)

        return min,max

    def textBoxs(self):
        n=IntVar()
        d=IntVar()
        #row = 6, Number of  People
        nEntry = Entry(self.parent, textvariable = n).grid(column=1, row=7)
        nLabel = Label(self.parent, text="Only integer: [1 ~ 12]").grid(column=2, row=7)

        #row = 12, Duration
        dEntry = Entry(self.parent, textvariable = d).grid(column=1, row=13)
        dLabel = Label(self.parent, text="Only integer: [1 ~ 24]").grid(column=2, row=13)

        return n,d

    def comoBoxs(self):

        #row = 1, ht
        self.htBox_value = StringVar()
        self.htBox = ttk.Combobox(self.parent, textvariable=self.htBox_value,
                                state='readonly')
        self.htBox['values'] = ([htVal for htVal in self.htList()])
        self.htBox.current(0)
        self.htBox.grid(column=1, row=2)


        #row = 8, region
        self.rBox_value = StringVar()
        self.rBox = ttk.Combobox(self.parent, textvariable=self.rBox_value,
                                state='readonly')
        self.rBox['values'] = ([rVal for rVal in self.rList()])
        self.rBox.current(0)
        self.rBox.grid(column=1, row=9)


        #row = 10, transportation
        self.tBox_value = StringVar()
        self.tBox = ttk.Combobox(self.parent, textvariable=self.tBox_value,
                                state='readonly')
        self.tBox['values'] = ([htVal for htVal in self.tList()])
        self.tBox.current(0)
        self.tBox.grid(column=1, row=11)


        #row = 14, season
        self.sBox_value = StringVar()
        self.sBox = ttk.Combobox(self.parent, textvariable=self.sBox_value,
                                state='readonly')
        self.sBox['values'] = ([sVal for sVal in self.sList()])
        self.sBox.current(0)
        self.sBox.grid(column=1, row=15)


        #row = 16, accamadation
        self.aBox_value = StringVar()
        self.aBox = ttk.Combobox(self.parent, textvariable=self.aBox_value,
                                state='readonly')
        self.aBox['values'] = ([aVal for aVal in self.aList()])
        self.aBox.current(0)
        self.aBox.grid(column=1, row=17)

    def _keyLabels(self,list):
        rowCouter=1
        htLabel = Label(self.parent, bg = 'pink',text = (list[1],":")).grid(row = rowCouter,column=1)
        rowCouter=rowCouter+2
        prLabel = Label(self.parent, bg = 'pink',text = (list[2],":")).grid(row = rowCouter,column=1)
        rowCouter=rowCouter+3
        for key in list[3:9]:
            # print(key)
            mLabel = Label(self.parent, bg = 'pink',text = (key,":")).grid(row = rowCouter,column=1)
            rowCouter = rowCouter+2
        return


    def defaultInput(self):
        user = {'HolidayType': 'Bathing', 'PriceUp': 2345.0, 'PriceLow': 100.0, "Region": "Arbitrary",
      'NumberOfPersons': 2, 'Transportation': 'Plane', 'Duration': 5, 'Season': 'Autumn', 'Accommodation': 'FourStars'}
        return user

    def defaultWeight(self):
        weightSetting = {'HolidayType': 10, 'Price': 2, "Region": 1, 'NumberOfPersons': 1,
                 'Transportation': 1, 'Duration': 3, 'Season': 2, 'Accommodation': 3}
        return weightSetting


    # Hotel Type
    def htList(self):
        ht = ['Arbitrary','Active', 'Adventure', 'Bathing', 'City', 'Diving', 'Education', 'Language', 'Recreation',
              'Skiing', 'Shoping', 'Surfing', 'Wandering']

        return ht

    # Region
    def rList(self):
        r = ['Arbitrary','Waters','Mountains','Culture',
             # Austria City, Country, Island, Germany, Paris, ,'Sea',Spain, Turkey , UnitedKingdom,
             'AdriaticSea', 'Algarve', 'Allgaeu', 'Alps', 'Atlantic', 'Attica', 'Balaton', 'BalticSea',
             'Bavaria', 'Belgium', 'BlackForest', 'Bornholm', 'Brittany', 'Bulgaria', 'Cairo', 'Carinthia',
             'Chalkidiki', 'Corfu', 'Corsica', 'CostaBlanca', 'CostaBrava', 'CotedAzur', 'Crete', 'Cyprus',
             'Czechia', 'Denmark', 'Dolomites', 'Egypt', 'England', 'ErzGebirge', 'Fano', 'France', 'Fuerteventura',
             'GiantMountains', 'GranCanaria', 'Harz', 'HighTatra', 'Holland', 'Ibiza', 'Ireland', 'LakeGarda',
             'Lanzarote', 'Lolland', 'LowerAustria', 'Madeira', 'Mallorca', 'Malta', 'Morocco', 'Normandy',
             'NorthSea', 'Poland', 'Rhodes', 'Riviera', 'SalzbergerLand', 'Salzkammergut','Scotland', 'Slowakei',
             'Sweden', 'Switzerland', 'Styria', 'Teneriffe', 'Thuringia', 'Tunisia','TurkishAegeanSea', 'TurkishRiviera',
             'Tyrol', 'Wales']
        return r

    # Transportation
    def tList(self):
        t = ['Arbitrary', 'Car', 'Plane', 'Train', 'Coach']
        return t

    # Season
    def sList(self):
        s = ['Arbitrary', 'Spring', 'Summer', 'Autumn', 'Winter', 'January', 'February', 'March',
             'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        return s

    # Accomadation
    def aList(self):
        a = ['Arbitrary','Holiday Flat', 'One Star', 'Two Stars', 'Three Stars', 'Four Stars', 'Five Stars']
        return a


class RetrieveFrame:
    def __init__(self, parent, fileName):
        self.parent = parent
        self.frame = tk.Frame(self.parent)
        # self.frame.title("CBR Retrieve")

        self.v = IntVar()
        self.v.set(3)  # initializing the choice, i.e. Python

        self.k = IntVar()


        languages = [
            ("Manhattan Distance", 1),
            ("Euclidean Distance", 2),
            ("Cosine Similarity", 3)
        ]



        tk.Label(self.parent,
              text="""Return KNN:""",
              bg = 'PaleTurquoise2',
              justify = LEFT
              #,padx = 20
              ).grid(row=0, column=1)


        ########### Entry ############
        kLabel = tk.Label(self.parent, text="k=").grid(row=2, column=0)
        kInput = tk.Entry(self.parent, width = 10, textvariable = self.k).grid(row=2, column=1)



        ########### Radio Button ###############
        for txt, val in languages:
            tk.Radiobutton(self.parent,
                        text=txt,
                        #padx = 20,
                        variable=self.v,
                        command=self.ShowChoice,
                        value=val).grid(row=(val), column=2)



        ########### Button ############
        knowResult = tk.Button(self.parent,
                            text = "Run"
                            ,command = self._whichSim
                            ).grid(row=5,column=2)

        #self.frame.pack()

    def update_returnFrame(self):
        return_k_f = {}
        return_k_f["k"] = self.k.get()
        return_k_f["function"] = self.v.get()
        return return_k_f


    def ShowChoice(self):
        select = self.update_returnFrame()

        #Always give initial setting
        print("K :", select["k"])
        print("Option~:", select["function"])


    # work good
    def _whichSim(self):
        app.updateUserSetting()
        # print("------- Selecting Algrithm -------")
        print("Input k=", self.k.get())
        if self.v.get() is 1:
            print("                 run Manhattan")
            app.knn._TopK_Manhattan(self.k.get())
        elif self.v.get() is 2:
            print("                 run Euclidean")
            app.knn._TopK_Euclidean(self.k.get())
        elif self.v.get() is 3:
            print("                 run Cosine")
            app.knn._TopK_Cosine(self.k.get())






if __name__ == '__main__':
    root = Tk()
    root.title("Travel Case-Base reasoning System")
    root.geometry('550x560+500+100')
    app = AttributeSettingFrame(root,"TRAVEL.csv")


'''
returnFrame = Tk()
returnFrame.title("CBR Retrieve")
# returnFrame,

    #clickButton()
    #retrieveCase()
'''




'''
def update_messageBox():
    messagebox.showinfo(
        title = "Retrieved case",
        message = "{} changed".format(retrieveCase())
    )
'''

# work good
def _whichSim(self):
    app.updateUserSetting()
    print("------- Selecting Algrithm -------")
    print("Input k=", k.get())
    if radi.get() is 1:
        app.knn._TopK_Manhattan(k.get())
        print("run Manhattan")
    elif radi.get() is 2:
        app.knn._TopK_Euclidean(k.get())
        print("run Euclidean")
    elif radi.get() is 3:
        app.knn._TopK_Cosine(k.get())
        print("run Cosine")





mainloop()