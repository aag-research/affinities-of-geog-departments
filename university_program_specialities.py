# Author:                       Eni Awowale & Coline Dony
# Date first written:           June 27, 2019
# Date last updated:            July 2, 2019
# Purpose:                      Determine U.S. University's levels of specialization

# Problem Statement:
# University Geography Departments have varying levels of specializations. Using AGG Guide to Geography Programs in the
# Americas this script will extract information about the vary levels of specialization

# Set up environment
import os
from collections import Counter
cnt = Counter()
folder = r'C:\Users\oawowale\Documents\GitHub\affinities-of-geog-departments'
os.chdir(folder)

# Read input data
input_filename = r'program_specialities.txt'
input_as_text = open(input_filename).readlines()

# Extract headers (note: there is a newline character (\n) in on of the
# headers, which is why the headers seem to be on 2 lines
headers = ''.join(input_as_text[1:3]).replace('\n', '').split('\t')
headers[0] = 'University name'

# Store the input data as a dictionary
geog_programs_data_db = {}
for line_as_text in input_as_text[3:]:
       line_as_list = line_as_text.split('\t')
       #print(line_as_list)
       if line_as_list[1] != '':
              program_data = dict(zip(headers, line_as_list))
              geog_programs_data_db[program_data['University name']] = program_data

# Store the specialties of each progam in a format
# that would work for radar charts (in matplotlib)
specialties = headers[9:-12]
data_for_radar_chart = [specialties]
for university, program_data in geog_programs_data_db.items():
       program_specialties = [1 if program_data[specialty] == 'X' else 0 for specialty in specialties]
       #print(program_specialties)
       data_for_radar_chart += [(university, program_specialties)]

program_data_values={}
# program_values=[]
# for specialty in specialties:
#        program_data_values[specialty]={}
#        for value in program_specialties:
#               #print(program_specialties[34])
#               program_values.append(value)
count = 0
program_data_values  = {}

university_lists=[]
for key, value in geog_programs_data_db.items():
       university_lists.append(key)
       for spec in specialties:
              #print(spec)
              program_data_values[spec] = {}
              if 'X' == value[spec]:
                     count = count+1
                     try:program_data_values[spec] = {count}
                     except:program_data_values[spec] = {'no value'}













              # for content in value.values():
              # #print(value.get('University name'))
              # #print(content)
              #        if content == 'X':
              #               count=count+1
              #               program_data_v[value.get(spec)]={count}
              #        else:
              #               program_data_v[value.get(spec)]={'no value'}


# for key, value in geog_programs_data_db.items():
#        print(value.items())
#        if value.values() == 'X':
#               count=count+1
#               program_data_values['Agricultural Geography'] = {count}






# for val in data_for_radar_chart[1:]:
#        program_data_values[val[0]]={}
#     # for v in val[1]:
    #     program_data_values={}
#stopped here finish tomorrow just need to save key values into program_data_values

# Show the formatted data on the screen
#print(data_for_radar_chart[0:8])
#print(data_for_radar_chart[0:8])
