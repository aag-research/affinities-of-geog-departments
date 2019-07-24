# Author:                       Eni Awowale & Coline Dony
# Date first written:           June 27, 2019
# Date last updated:            July 23, 2019
# Purpose:                      Determine U.S. University's levels of specialization

# Problem Statement:
# University Geography Departments have varying levels of specializations. Using AGG Guide to Geography Programs in the
# Americas this script will extract information about the vary levels of specialization

# Set up environment
import os

folder = r'C:\Users\oawowale\Documents\GitHub\affinities-of-geog-departments\program_specialties'
#folder = r'C:\Users\cdony\Google Drive\GitHub\affinities-of-geog-departments'
os.chdir(folder)

# Read input data:
#No Program Data for 2013
input_filename = r'program_specialties_2016.txt'
input_as_text = open(input_filename).readlines()
#Excluding 2016 temporarily because it is in different format than the rest
#input_filenames = [r'program_specialties_2012.txt', r'program_specialties_2014.txt', r'program_specialties_2015.txt',
                   #r'program_specialties_2018.txt', r'program_specialties_2017.txt', r'program_specialties_2019.txt']

headers = ''.join(input_as_text[1:3]).replace('\n', '').split('\t')
headers[0] = 'University name'
#Names of shortened specialities
short_specialities_name = ['Human Geography', 'Human-Environmental Interactions', 'Physical Geography', 'Geospatial Technologies',
                            'Urban and Economic Geography', 'Methods']
#creating specialty groups database
specialty_groups_db={}
for specialty in short_specialities_name:
    if specialty not in specialty_groups_db:
        specialty_groups_db[specialty]=[]

# Store the input data as a dictionary
geog_programs_data_db = {}
for line_as_text in input_as_text[2:]:
    line_as_list = line_as_text.split('\t')
    #print(line_as_list[0])
    if line_as_list[0] != '':
        program_data = dict(zip(headers, line_as_list))
        geog_programs_data_db[program_data['University name']] = program_data

# Store the specialties of each program in a format
# that would work for radar charts (in matplotlib)
specialties = headers[1:37]
data_for_radar_chart = [specialties]
del[specialties[8]]
short_specialty_list = [[] for specialty in range(0,6)]

#adding specialities to short_specialties_db
specialty_groups_db['Human Geography']= [specialties[sp_index] for sp_index in [7,12,19,21,25,30,31,24]]
specialty_groups_db['Human-Environmental Interactions']= [specialties[sp_index] for sp_index in [6,11,18,5,0,34]]
specialty_groups_db['Physical Geography']= [specialties[sp_index] for sp_index in [2,4,15,22]]
specialty_groups_db['Geospatial Technologies']= [specialties[sp_index] for sp_index in [16,17,29]]
specialty_groups_db['Urban and Economic Geography']= [specialties[sp_index] for sp_index in [8,9,32,33,23,28,27,10]]
specialty_groups_db['Methods']= [specialties[sp_index] for sp_index in [3,14,13,20,1,26]]

#Directory for university specializations
university_specialization_db={}
for university_name, specialization in geog_programs_data_db.items():
       university_specialization_db[university_name]={}
       university_total = [i for i in university_specialization_db.keys()]
       for short_specialty,specialty in specialty_groups_db.items():
              count=0
              for spec in specialty:
                     if specialization[spec]== 'X' and university_name in university_total:
                            count=count+1
                            specialty_ratio=count/len(specialty)
                            university_specialization_db[university_name][short_specialty] = specialty_ratio
                     else:
                            count=count+0
                            specialty_ratio=count/len(specialty)
                            university_specialization_db[university_name][short_specialty] = specialty_ratio

#data_for_radar_chart_str = str(lists)
data_for_radar_chart_textfile = open('radar_chart_data.txt', 'w')
#data_for_radar_chart_textfile.write(data_for_radar_chart_str)
data_for_radar_chart_textfile.close()

'''
specialties_count = [0]*len(specialties)
for university, program_data in geog_programs_data_db.items():
       program_specialties = [1 if program_data[specialty] == 'X' else 0 for specialty in specialties]
       #print(program_specialties)
       data_for_radar_chart += [(university, program_specialties)]
       specialties_count = [sum(values) for values in zip(specialties_count, program_specialties)]

specialties_count_db = dict(zip(specialties, specialties_count))
number_of_universities = len(geog_programs_data_db.keys())

'''