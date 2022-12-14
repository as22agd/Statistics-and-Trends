# -*- coding: utf-8 -*-
"""

Program to explore statistics and trends in given datasets

"""
# Importing required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Funtion to read the csv file to the dataframe
def read_file(filename):
    """
    
    Parameters
    ----------
    filename : csv file

    Returns
    -------
    df : dataframe with years as columns
    df_transpose : dataframe with countries as columns

    """
    df = pd.read_csv(filename)
    #transposing the dataframe keeping 'Country Name' as index
    df_transpose = df.set_index('Country Name').transpose()
    return df, df_transpose


countries = ['Argentina', 'Brazil', 'Cameroon', 'United Kingdom', 'India']


#Function to filter out 5 countries to perform the analysis
def filter_barplot_data(df):
    """
    
    Parameters
    ----------
    df : dataframe with years as columns

    Returns
    -------
    df : filtered dataframe to plot bar graph of the below mentioned countries
        
    """
    df = df[['Country Name', 'Indicator Name', '1995', '2005', '2015']]
    df = df[(df["Country Name"] == "Argentina") |
            (df["Country Name"] == "Brazil") |
            (df["Country Name"] == "Cameroon") |
            (df["Country Name"] == "United Kingdom") |
            (df["Country Name"] == "India")]
    return df


#Function to filter out 5 countries to perform the analysis
def filter_lineplot_data(df):
    """

    Parameters
    ----------
    df : dataframe with years as columns

    Returns
    -------
    df : filtered dataframe to plot line graph of the below mentioned countries

    """
    df = df[['Country Name', 'Indicator Name',
             '1995', '2000', '2005', '2010', '2015']]
    df = df[(df["Country Name"] == "Argentina") |
            (df["Country Name"] == "Brazil") |
            (df["Country Name"] == "Cameroon") |
            (df["Country Name"] == "India") |
            (df["Country Name"] == "United Kingdom")]
    return df


#Function to plot bar graph
def barplot(df, label1, label2): 
    """
    
    Parameters
    ----------
    df : filtered dataframe to plot bar graph of the selected countries
    label1 : string to label y-axis
    label2 : string to display the title of bar graph

    Returns
    -------
    None.

    """
    plt.figure(figsize=(35, 25))
    ax = plt.subplot(1, 1, 1)
    x = np.arange(5)
    width = 0.2

    bar1 = ax.bar(x, df["1995"], width, label=1995, color="red")
    bar2 = ax.bar(x + width, df["2005"], width, label=2005, color="yellow")
    bar3 = ax.bar(x + width*2, df["2015"], width, label=2015, color="black")

    ax.set_xlabel("Country", fontsize=40)
    ax.set_ylabel(label1, fontsize=40)
    ax.set_title(label2, fontsize=40)
    ax.set_xticks(x, countries, fontsize=30, rotation=45)
    ax.legend(fontsize=30)

    ax.bar_label(bar1, padding=2, rotation=90, fontsize=18)
    ax.bar_label(bar2, padding=2, rotation=90, fontsize=18)
    ax.bar_label(bar3, padding=2, rotation=90, fontsize=18)
    #saving the output graph in png format
    plt.savefig("barplot.png")
    plt.show()


#Function to plot line graph
def line_plot(df, label1, label2):
    """
    
    Parameters
    ----------
    df : filtered dataframe to plot line graph of the selected countries
    label1 : string to label y-axis
    label2 : string to display the title of line graph

    Returns
    -------
    None.

    """
    plt.figure(figsize=(25, 10))
    data = df.set_index('Country Name')
    transpose = data.transpose()
    transpose = transpose.drop(index=['Indicator Name'])
    for i in range(len(countries)):
        plt.plot(transpose.index, transpose[countries[i]], label=countries[i])
    plt.title(label2, size=18)
    #labelling x and y-axis
    plt.xlabel("Year", size=18)
    plt.ylabel(label1, size=18)
    plt.xticks(rotation=90)
    plt.legend(fontsize=18)
    #saving the output graph in png format
    plt.savefig("lineplot.png")
    plt.show()


def co2_emission_mean():
    df1, df2 = read_file("C:/Users/cyber/Desktop/UoH/ADS/Assignment 2/co2_emission.csv")
    
    
    data = df1.set_index('Country Name')
    
    transpose = data.transpose()
    transpose = transpose.drop(index='Indicator Name')
    transpose=transpose.drop(index='Country Code')
    transpose=transpose.drop(index='Indicator Code')
    cleaned_data=transpose.fillna(0)
    cleaned_data = cleaned_data[["Argentina", "Brazil", "Cameroon", "United Kingdom", "India"]].mean()
    return cleaned_data
    
    
#Reading data from csv file to two dataframes using the function read_file(filename)
forest_area, forest_area_transpose = read_file("C:/Users/cyber/Desktop/UoH/ADS/Assignment 2/forest_area.csv")
forest_area = filter_barplot_data(forest_area)

population_growth, population_growth_transpose = read_file(
    "C:/Users/cyber/Desktop/UoH/ADS/Assignment 2/population_growth.csv")
population_growth = filter_barplot_data(population_growth)

CO2_emission, CO2_emission_transpose = read_file("C:/Users/cyber/Desktop/UoH/ADS/Assignment 2/co2_emission.csv")
CO2_emission = filter_lineplot_data(CO2_emission)

access_to_electricity, access_to_electricity_transpose = read_file(
    "C:/Users/cyber/Desktop/UoH/ADS/Assignment 2/access_to_electricity.csv")
access_to_electricity = filter_lineplot_data(access_to_electricity)

#Plotting bar graph for forest area and population growth to analyse
barplot(forest_area, "Forest Area (% of land area)", "Forest Area")
barplot(population_growth, "Population growth (annual %)", "Population Growth")

#Plotting line graph for forest area and population growth to analyse
line_plot(CO2_emission, "CO2 Emission in KT", "CO2 Emissions")
line_plot(access_to_electricity,
          "Access to electricity (% of population)", "Access to electricity")

mean = co2_emission_mean()
print(mean)
mean=mean.to_csv("mean_of_co2_emission.csv")
