import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

class Statistics:
    countries = pd.read_excel('Project_File')
    countries['Brunei Darussalam'] = countries['Brunei Darussalam'].replace(['na'], 0)
    countries['Indonesia'] = countries['Indonesia'].replace(['na'], 0)
    countries['Malaysia'] = countries['Malaysia'].replace(['na'], 0)
    countries['Philippines'] = countries['Philippines'].replace(['na'], 0)
    countries['Thailand'] = countries['Thailand'].replace(['na'], 0)
    countries['Viet Nam'] = countries['Viet Nam'].replace(['na'], 0)
    countries['Myanmar'] = countries['Myanmar'].replace(['na'], 0)