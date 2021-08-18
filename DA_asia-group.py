import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from pandas.core.frame import DataFrame as df

class Statistics:

    def __init__(self):
        self.countries = pd.read_excel('Project_File.xlsx')
    
    def generate_Top3(self):
        self.countries['Brunei Darussalam'] = self.countries['Brunei Darussalam'].replace(['na'], 0)
        self.countries['Indonesia'] = self.countries['Indonesia'].replace(['na'], 0)
        self.countries['Malaysia'] = self.countries['Malaysia'].replace(['na'], 0)
        self.countries['Philippines'] = self.countries['Philippines'].replace(['na'], 0)
        self.countries['Thailand'] = self.countries['Thailand'].replace(['na'], 0)
        self.countries['Viet Nam'] = self.countries['Viet Nam'].replace(['na'], 0)
        self.countries['Myanmar'] = self.countries['Myanmar'].replace(['na'], 0)

        bruneiTotalVisitors = self.countries['Brunei Darussalam'].sum()
        print(bruneiTotalVisitors, " - Brunei")

        indonesiaTotalVisitors = self.countries['Indonesia'].sum()
        indonesiaMeanVisitors = self.countries['Indonesia'].mean()
        indonesiaMedianVisitors = self.countries['Indonesia'].median()
        #print(indonesiaMedianVisitors)
        print(indonesiaTotalVisitors, " - Indonesia")

        malaysiaTotalVisitors = self.countries['Malaysia'].sum()
        print(malaysiaTotalVisitors, " - M'sia")

        philippinesTotalVisitors = self.countries['Philippines'].sum()
        print(philippinesTotalVisitors, " - Philipines")

        thailandTotalVisitors = self.countries['Thailand'].sum()
        print(thailandTotalVisitors, " - Thailand")

        vietnamTotalVisitors = self.countries['Viet Nam'].sum()
        print(vietnamTotalVisitors, " - Vietnam")

        myanmarTotalVisitors = self.countries['Myanmar'].sum()
        print(myanmarTotalVisitors, " - Myanmar")

        hongkongTotalVisitors = self.countries['Hong Kong'].sum()
        print(hongkongTotalVisitors, " - Hk")

        chinaTotalVisitors = self.countries['China'].sum()
        chinaMeanVisitors = self.countries['China'].mean()
        chinaMedianVisitors = self.countries['China'].median()
        #print(chinaMedianVisitors)
        print(chinaTotalVisitors, " - China")

        taiwanTotalVisitors = self.countries['Taiwan'].sum()
        print(taiwanTotalVisitors, " - Taiwan")

        koreaTotalVisitors = self.countries['Korea, Republic Of'].sum()
        print(koreaTotalVisitors, " - Korea")

        japanTotalVisitors = self.countries['Japan'].sum()
        japanMeanVisitors = self.countries['Japan'].mean()
        japanMedianVisitors = self.countries['Japan'].median()
        #print(japanMedianVisitors)
        print(japanTotalVisitors, " - Jap")

        print("The top 3 countries with the most visitors are Indonesia, Japan, China")
        print("The total numbers of visitors from the top 3 individual countries are " + str(indonesiaTotalVisitors) + ", " + str(japanTotalVisitors) + " and " + str(chinaTotalVisitors))
        print("The mean value of visitors from the top 3 individual countries countries are " + str(round(indonesiaMeanVisitors, 2)) + ", " + str(round(japanMeanVisitors, 2)) + " and " + str(round(chinaMeanVisitors, 2)))
        print("The median value of visitors from the top 3 individual countries are " + str(indonesiaMedianVisitors) + ", " + str(japanMedianVisitors) + " and " + str(chinaMedianVisitors))

    def generateLineChart(self):            
        #print(countries)
        years = self.countries[self.countries.columns[0]]
        #print(years)

        year = years.str.split(" ", n=1, expand=True)
        #print(year)

        countries = self.countries.assign(Year=year[0])
        countries = countries.assign(Month=year[1])

        yearstats = countries.groupby("Year").sum().reset_index()
        print(yearstats)
        #print(years[years.str.contains("Jan")])
        plt.title("Stats")
        plt.plot(yearstats["Japan"])
        plt.xlabel("Year")
        plt.ylabel("Vistors")

        #plt.legend()
        plt.show()

    def generateBarGraph(self):
        yearStats = self.countries.groupby("Year").sum().reset_index()

        plt.bar(yearStats["Year"], yearStats["Japan"])
        plt.xlabel("Year")
        plt.ylabel("Country")
        plt.show()
    
stats = Statistics()
stats.generate_Top3()
stats.generateLineChart()
#stats.generateBarGraph()