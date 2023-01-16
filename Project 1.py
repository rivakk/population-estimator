"""
Name: Riva Kansakar
CSC 201
Programming Project 1
Description: 
    This program is a Population growth estimator where the program asks the user number of countries and years
    to input country names, their population and its growth/decline rate. Then, shows a summay report where
    average of all countries, number of countries with high growth rate, number of countries with low growth rate,
    country with highest growth rate, country with maximum population and country with maximum population
    is shown.

Assistance:

I gave and received no assistance on this project.

"""
from math import *
def main():
    print("=== POPULATION GROWTH ESTIMATOR ===")
    print("This program estimates population growth of several countries")
    print()
    
    #initializing variables for calculation
    
    highest_coun = 0
    lowest_coun = 0
    highest_counName = ''
    highest_growth = -101
    max_year = 0
    max_yearLast = 0
    max_yearCountry = ''
    max_yearLastCountry = ''
    sum_year = 0
    
    coun = int(input("Number of countries: ")) # assume that coun means countries
    
    #to create error: coun is not a valid input output
    
    if coun > 0:
        
        numYears = int(input("Number of years: "))
        
        if numYears>0:
            
            print()

            for i in range (1, coun+1):
                print ("--- Country", i, " ---")
                coun_name = input("Country name: ")
                year1 = float(input(f'Year 1 population of {coun_name} (in millions): '))
                pop = float(input("Population growth rate (% per year): "))
                
                if pop > 1:
                    highest_coun = highest_coun+1
                    
                if pop <= 0.1:
                    lowest_coun = lowest_coun+1
                 
                if pop > highest_growth:
                    highest_growth = pop
                    highest_counName = coun_name

                if year1 > max_year:
                    max_year = year1
                    max_yearCountry = coun_name
                year_pop = year1
                
                for i in range (2, numYears+1):
                    per_pop = pop/100
                    year_pop = (per_pop*year_pop) + year_pop
                    print ("Year", i, "population of", coun_name, "(in millions):", round(year_pop,3))
                    
                    if i == numYears:
                        if year_pop > max_yearLast:
                            max_yearLast = year_pop
                            max_yearLastCountry = coun_name
                sum_year = sum_year +year_pop
                avg = sum_year/coun
                print()
                
            print('Summary Report')
            print('    Average year', numYears, 'population of all countries:', round(avg,3))
            print('    Number of countries with high growth rate:', highest_coun)
            print('    Number of countries with low growth rate:', lowest_coun)
            print('    Country with highest growth rate:', highest_counName)
            print('    Country with maximum Year 1 population (', round(max_year, 3), ' million): ', max_yearCountry, sep='')
            print('    Country with maximum Year ', numYears, ' population (', round(max_yearLast, 3), ' million): ', max_yearLastCountry, sep='')
            
        else:
            print('Error:', numYears, 'is not a valid input')
    else:
        print('Error:', coun, 'is not a valid input')

main()
