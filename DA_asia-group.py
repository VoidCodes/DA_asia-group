import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from pandas.core.frame import DataFrame as df

class Statistics:
    countries = pd.read_excel('Project_File.xlsx')
    countries['Brunei Darussalam'] = countries['Brunei Darussalam'].replace(['na'], 0)
    countries['Indonesia'] = countries['Indonesia'].replace(['na'], 0)
    countries['Malaysia'] = countries['Malaysia'].replace(['na'], 0)
    countries['Philippines'] = countries['Philippines'].replace(['na'], 0)
    countries['Thailand'] = countries['Thailand'].replace(['na'], 0)
    countries['Viet Nam'] = countries['Viet Nam'].replace(['na'], 0)
    countries['Myanmar'] = countries['Myanmar'].replace(['na'], 0)

    bruneiTotalVisitors = countries['Brunei Darussalam'].sum()
    bruneiMeanVisitors = countries['Brunei Darussalam'].mean()
    bruneiMedianVisitors = countries['Brunei Darussalam'].median()
    print(bruneiMedianVisitors)

    indonesiaTotalVisitors = countries['Indonesia'].sum()
    indonesiaMeanVisitors = countries['Indonesia'].mean()
    indonesiaMedianVisitors = countries['Indonesia'].median()
    print(indonesiaMedianVisitors)

    malaysiaTotalVisitors = countries['Malaysia'].sum()
    malaysiaMeanVisitors = countries['Malaysia'].mean()
    malaysiaMedianVisitors = countries['Malaysia'].median()
    print(malaysiaMedianVisitors)

    philippinesTotalVisitors = countries['Philippines'].sum()
    philippinesMeanVisitors = countries['Philippines'].mean()
    philippinesMedianVisitors = countries['Philippines'].median()
    print(philippinesMedianVisitors)

    thailandTotalVisitors = countries['Thailand'].sum()
    thailandMeanVisitors = countries['Thailand'].mean()
    thailandMedianVisitors = countries['Thailand'].median()
    print(thailandMedianVisitors)

    vietnamTotalVisitors = countries['Viet Nam'].sum()
    vietnamMeanVisitors = countries['Viet Nam'].mean()
    vietnamMedianVisitors = countries['Viet Nam'].median()
    print(vietnamMedianVisitors)

    myanmarTotalVisitors = countries['Myanmar'].sum()
    myanmarMeanVisitors = countries['Myanmar'].mean()
    myanmarMedianVisitors = countries['Myanmar'].median()
    print(myanmarMedianVisitors)

    malaysiaTotalVisitors = countries['Malaysia'].sum()
    malaysiaMeanVisitors = countries['Malaysia'].mean()
    malaysiaMedianVisitors = countries['Malaysia'].median()
    print(malaysiaMedianVisitors)

    hongkongTotalVisitors = countries['Hong Kong'].sum()
    hongkongMeanVisitors = countries['Hong Kong'].mean()
    hongkongMedianVisitors = countries['Hong Kong'].median()
    print(hongkongMedianVisitors)

    chinaTotalVisitors = countries['China'].sum()
    chinaMeanVisitors = countries['China'].mean()
    chinaMedianVisitors = countries['China'].median()
    print(chinaMedianVisitors)

    taiwanTotalVisitors = countries['Taiwan'].sum()
    taiwanMeanVisitors = countries['Taiwan'].mean()
    taiwanMedianVisitors = countries['Taiwan'].median()
    print(taiwanMedianVisitors)

    koreaTotalVisitors = countries['Korea, Republic Of'].sum()
    koreaMeanVisitors = countries['Korea, Republic Of'].mean()
    koreaMedianVisitors = countries['Korea, Republic Of'].median()
    print(koreaMedianVisitors)

    japanTotalVisitors = countries['Japan'].sum()
    japanMeanVisitors = countries['Japan'].mean()
    japanMedianVisitors = countries['Japan'].median()
    print(japanMedianVisitors)

    print("The top 3 countries with the most visitors are Indonesia, Japan, China")
    print("The total numbers of visitors from the top 3 individual countries are " + str(indonesiaTotalVisitors) + ", " + str(japanTotalVisitors) + " and " + str(chinaTotalVisitors))
    print("The mean value of visitors from the top 3 individual countries countries are " + str(indonesiaMeanVisitors) + ", " + str(japanMeanVisitors) + " and " + str(chinaMeanVisitors))
    print("The median value of visitors from the top 3 individual countries are " + str(indonesiaMedianVisitors) + ", " + str(japanMedianVisitors) + " and " + str(malaysiaMedianVisitors))

    #print(countries)
    years = countries[countries.columns[0]]
    #print(years)



    year = years.str.split(" ", n=1, expand=True)
   # print(year)

    countries = countries.assign(Year=year[0])
    countries = countries.assign(Month=year[1])

    yearstats = countries.groupby("Year").sum().reset_index()
    print(yearstats)
    #print(years[years.str.contains("Jan")])
    plt.plot(yearstats["Japan"])
    plt.xlabel("Year")

    plt.title("Stats")

    plt.legend()
    plt.show()
    

    #test
    print("hi")

    #str.includes(ans[x])