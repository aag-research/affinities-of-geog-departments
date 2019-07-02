# Author:                       Eni Awowale
# Date first written:           June 27, 2019
# Date last updated:            June 27, 2019
# Purpose:                      Determine U.S. University's levels of specialization

# Problem Statement:
# University Geography Departments have varying levels of specializations. Using AGG Guide to Geography Programs in the
# America this script will extract information about the vary levels of specialization

import sys
import os
import csv

p_speciality = {}

#Openning AAG csv that contains all of the program specialities
program_specialities_csv_name = r'program_specialities.csv'
program_specialities_csv = open(program_specialities_csv_name).readlines()

headers = program_specialities_csv[0].split('\t')
program_specialities1 = program_specialities_csv[1].split(',')
program_specialities2 = program_specialities_csv[2].split(',')
del program_specialities2[18]
subject_specialities = program_specialities1[1:15] + program_specialities2[0:]
#stopped here have a list of my specialities now
university_specialties= []
u_s=[]
#k = program_specialities_csv[5:].split(',')

for uni in program_specialities_csv[5:]:
    university_info = uni.split(',')
    #print(uni)
    university_name = university_info[0]
    university = uni.split(',')
    #print(university)
    if university not in university_specialties:
        university_specialties.append(university)

for university_details in university_specialties:
    p_speciality[university_details[0]]= {}
    for speciality in subject_specialities:
        for val in university_details:
            if val not in p_speciality:
                try: p_speciality[university_details[0]][speciality]= {val}
                except: 'no value'