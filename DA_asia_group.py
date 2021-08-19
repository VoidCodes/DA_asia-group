import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class Statistics:

    def __init__(self):
        self.countries = pd.read_excel(r"Project_File.xlsx")

    def generate_Top3(self):
        countryRegion = self.countries
        countryRegion = countryRegion.replace("na", 0)
        AsiaPacific = countryRegion.iloc[:,lambda df:[0, 8, 9, 10, 11, 12]]
        AsiaPacific = AsiaPacific.set_index('Unnamed: 0')
        countryYear = AsiaPacific.loc['1978 Jan':'1987 Dec']
        #print (countryYear)

        Sums = AsiaPacific.sum(axis=0)
        Sums = Sums.sort_values(ascending=False)
        print (Sums)
        top1 = Sums.index[0]
        top2 = Sums.index[1]
        top3 = Sums.index[2]
        print("The top 3 countries with the most visitors are", top1 , top2 , top3)


        vis1 = Sums[top1]
        vis2 = Sums[top2]
        vis3 = Sums[top3]
        print("The Amount of visitors from the top 3 countries are", vis1 , vis2 , vis3, "respectively")


        means = AsiaPacific.mean(axis=0)
        means = means.sort_values(ascending=False)
        print (means)
        mean1 = round(means[0],2)
        mean2 = round(means[1],2)
        mean3 = round(means[2],2)
        print("The Average visitors from the top 3 countries are", mean1 , mean2 , mean3, "respectively")


        medians = AsiaPacific.median(axis=0)
        medians = medians.sort_values(ascending=False)
        print (medians)
        med1 = medians[0]
        med2 = medians[1]
        med3 = medians[2]
        print("The Median visitors from the top 3 countries are", med1 , med2 , med3, "respectively")

    def generate_linegraph(self):
        countryRegion = self.countries
        countryRegion = countryRegion.replace("na", 0)
        AsiaPacific = countryRegion.iloc[:,lambda df:[0, 8, 9, 10, 11, 12]]
        AsiaPacific = AsiaPacific.set_index('Unnamed: 0')
        countryYear = AsiaPacific.loc['1978 Jan':'1987 Dec']

        date_sum = countryYear.sum(axis=1)
        months = np.zeros((12,), dtype=int).tolist()
        month_names = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        for j in range(0,12):
            for i in np.arange(j,120,12):
                months[j] += date_sum.iat[i]
        print (months)
        plt.plot(month_names,months)
        plt.title("Overview of visitors in asia from 1978 - 1987")
        plt.xlabel("Months")
        plt.ylabel("Visitors")

        plt.show()

    def generate_bargraph(self):
        countryRegion = self.countries
        countryRegion = countryRegion.replace("na", 0)
        AsiaPacific = countryRegion.iloc[:,lambda df:[0, 8, 9, 10, 11, 12]]
        AsiaPacific = AsiaPacific.set_index('Unnamed: 0')
        countryYear = AsiaPacific.loc['1978 Jan':'1987 Dec']

        date_sum = countryYear.mean(axis=1)
        months = np.zeros((12,), dtype=int).tolist()
        month_names = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        for j in range(0,12):
            for i in np.arange(j,120,12):
                months[j] += date_sum.iat[i]
        print (months)
        plt.bar(month_names,months)
        plt.title("Overview of visitors in asia from 1978 - 1987")
        plt.xlabel("Months")
        plt.ylabel("Visitors")

        plt.show()

    # Unit testing stuff
    def getTopCountry(self):
        countries = pd.read_excel(r"Project_File.xlsx")
        countries = countries.iloc[:, lambda countries: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]
        countries = countries.replace("na", 0)
        asia = countries.set_index("Unnamed: 0")
        asia = asia.loc['1978 Jan':'1987 Dec']
        sums = asia.sum(axis=0)
        sums = sums.sort_values(ascending=False)
        top1 = sums.index[0]
        Sum1 = sums[top1]
        print(Sum1)

        return asia["Japan"].sum()

    

#stats = Statistics()
#stats.generate_Top3()
#stats.generate_linegraph()
#stats.generate_bargraph()