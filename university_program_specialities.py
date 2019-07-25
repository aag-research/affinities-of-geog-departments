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

# Read input data
input_filename = r'program_specialties_2012.txt'
input_as_text = open(input_filename).readlines()


# Extract headers (note: there is a newline character (\n) in on of the
# headers, which is why the headers seem to be on 2 lines
headers = ''.join(input_as_text[1:3]).replace('\n', '').split('\t')
headers[0] = 'University name'
#Names of shortened specialities
short_specialities_name = ['Human Geography', 'Human-Environmental Interactions', 'Physical Geography', 'Geospatial Technologies',
                            'Urban and Economic Geography', 'Methods']
#creating short specialty database
specialty_groups_db={}
for specialty in short_specialities_name:
       if specialty not in specialty_groups_db:
              specialty_groups_db[specialty]=[]

# Store the input data as a dictionary
geog_programs_data_db = {}
for line_as_text in input_as_text[3:]:
       line_as_list = line_as_text.split('\t')
       #print(line_as_list[1])
       if line_as_list[1] != '':
              program_data = dict(zip(headers, line_as_list))
              print(program_data)
              geog_programs_data_db[program_data['University name']] = program_data

# Store the specialties of each progam in a format
# that would work for radar charts (in matplotlib)
specialties = headers[9:-12]
data_for_radar_chart = [specialties]
short_specialty_list = [[] for specialty in range(0,6)]

#adding specialities to short_specialties_db
specialty_groups_db['Human Geography']= [specialties[sp_index] for sp_index in [7,11,18,20,23,24,29,30]]
specialty_groups_db['Human-Environmental Interactions']= [specialties[sp_index] for sp_index in [6,10,17,5,0,33]]
specialty_groups_db['Physical Geography']= [specialties[sp_index] for sp_index in [2,4,14,21]]
specialty_groups_db['Geospatial Technologies']= [specialties[sp_index] for sp_index in [15,16,28]]
specialty_groups_db['Urban and Economic Geography']= [specialties[sp_index] for sp_index in [8,9,31,32,22,27,26]]
specialty_groups_db['Methods']= [specialties[sp_index] for sp_index in [3,13,12,19,1,2,25]]

#Directory for university specializations
'''
for university, university_data in geog_programs_data_db.items():
       #specialty_groups_db = {'group': {'list': [], 'count':0} for group in specialty_groups_db}
       for short_specialty, specialty in specialty_groups_db.items():
              if university_data[specialty] == 'X':
                     group_specialty = specialty_groups_db[specialty]
                     #specialty_groups_db['group']['list']=[specialty]
       # for group in specialty_groups_db:
       #        specialty_groups_db['group']['count']=len(specialty_groups_db[group]['list'])
'''
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

specialties_count = [0]*len(specialties)
for university, program_data in geog_programs_data_db.items():
       program_specialties = [1 if program_data[specialty] == 'X' else 0 for specialty in specialties]
       #print(program_specialties)
       data_for_radar_chart += [(university, program_specialties)]
       specialties_count = [sum(values) for values in zip(specialties_count, program_specialties)]

specialties_count_db = dict(zip(specialties, specialties_count))
number_of_universities = len(geog_programs_data_db.keys())
