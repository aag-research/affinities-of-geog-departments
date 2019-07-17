# Author:                       Eni Awowale & Coline Dony
# Date first written:           June 27, 2019
# Date last updated:            July 2, 2019
# Purpose:                      Determine U.S. University's levels of specialization

# Problem Statement:
# University Geography Departments have varying levels of specializations. Using AGG Guide to Geography Programs in the
# Americas this script will extract information about the vary levels of specialization

# Set up environment
import os
folder = r'C:\Users\oawowale\Documents\GitHub\affinities-of-geog-departments'
#folder = r'C:\Users\cdony\Google Drive\GitHub\affinities-of-geog-departments'
os.chdir(folder)

# Read input data
input_filename = r'program_specialities.txt'
input_as_text = open(input_filename).readlines()

# Extract headers (note: there is a newline character (\n) in on of the
# headers, which is why the headers seem to be on 2 lines
headers = ''.join(input_as_text[1:3]).replace('\n', '').split('\t')
headers[0] = 'University name'
short_specialities_list = ['Human Geography', 'Human-Environmental Interactions', 'Physical Geography', 'Geospatial Technologies',
                           'Urban and Economic Geography', 'Methods']
# Store the input data as a dictionary
geog_programs_data_db = {}
program_specialty_data={}
for line_as_text in input_as_text[3:]:
       line_as_list = line_as_text.split('\t')
       #print(line_as_list)
       if line_as_list[1] != '':
              program_data = dict(zip(headers, line_as_list))
              geog_programs_data_db[program_data['University name']] = program_data

for university, specialty in geog_programs_data_db.items():
       for short_specialty in short_specialities_list:
              program_specialty_data[short_specialty]={}
              for key, values in specialty.items():
                     if (key, values) == (key, 'X'):
                            program_specialty_data.update({short_specialty:university})
                            print(program_specialty_data)
       #program_specialty_data[short_specialty] = university
#print(program_specialty_data)

human_geog=0
human_env_interactions =0
phys_geog=0
geo_tech=0
urb_econ=0
methods =0

# for key, value in program_data.items():
#        if key == 'Cultural Geography' and key == 'Gender' and key == 'Historical Geography' and key =='Political Geography' and key =='Social Geography' and key == 'Rural Geography' and key == 'Political Geography' and key == 'Population Geography' and key == 'Medical Geography' and  value =='X':
#



# Store the specialties of each progam in a format
# that would work for radar charts (in matplotlib)
specialties = headers[9:-12]
data_for_radar_chart = [specialties]

    #data_for_radar_chart_str = str(lists)

data_for_radar_chart_textfile = open('radar_chart_data.txt', 'w')
#data_for_radar_chart_textfile.write(data_for_radar_chart_str)
data_for_radar_chart_textfile.close()

specialties_count = [0]*len(specialties)




university_list=[]

for university, program_data in geog_programs_data_db.items():
       program_specialties = [1 if program_data[specialty] == 'X' else 0 for specialty in specialties]
       #print(program_specialties)
       data_for_radar_chart += [(university, program_specialties)]
       specialties_count = [sum(values) for values in zip(specialties_count, program_specialties)]

specialties_count_db = dict(zip(specialties, specialties_count))
number_of_universities = len(geog_programs_data_db.keys())
# for specialty, count in specialties_count_db.items():
#        print(specialty, "%.0f%%" % (count/number_of_universities*100))
