# Author:                       Eni Awowale & Coline Dony
# Date first written:           June 27, 2019
# Date last updated:            July 17, 2019
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
#Names of shortened specialities
short_specialities_name = ['Human Geography', 'Human-Environmental Interactions', 'Physical Geography', 'Geospatial Technologies',
                            'Urban and Economic Geography', 'Methods']
#creating short specialty database
short_specialty_db={}
for specialty in short_specialities_name:
       if specialty not in short_specialty_db:
              short_specialty_db[specialty]=[]

# Store the input data as a dictionary
geog_programs_data_db = {}
program_specialty_data={}
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
short_specialty_list = [[] for specialty in range(0,6)]

#I know this is a little messy but the goal of this is to save the actually specialties into the short specialties dict
for specialty in specialties:
       for index in range(len(specialties)):
              if index in [7,11,18,20,23,24,29,30] and specialty==specialties[index]:
                     short_specialty_db['Human Geography'].append(specialty)
              elif index in [6,7,10,17,5,0,33] and specialty==specialties[index]:
                     short_specialty_db['Human-Environmental Interactions'].append(specialty)
              elif index in [2,4,14,21] and specialty==specialties[index]:
                     short_specialty_db['Physical Geography'].append(specialty)
              elif index in [15,16,28] and specialty==specialties[index]:
                     short_specialty_db['Geospatial Technologies'].append(specialty)
              elif index in [8,9,31,32,22,27,26] and specialty==specialties[index]:
                     short_specialty_db['Urban and Economic Geography'].append(specialty)
              elif index in [3,13,12,19,1,2,25] and specialty==specialties[index]:
                     short_specialty_db['Methods'].append(specialty)

#making a new dictionary for the university specialization
#the float (values) for the short specialities key are the amount of specialities that fall under the short_specialties
#this is number we will put in the radar chart
university_specialization_db={}
for key, value in geog_programs_data_db.items():
       university_specialization_db[key]={}
       university_total = [i for i in university_specialization_db.keys()]
       for short_specialty,specialty in short_specialty_db.items():
              count=0
              for spec in specialty:
                     if value[spec]== 'X' and key in university_total:
                            count=count+1
                            specialty_ratio=count/len(specialty)
                            university_specialization_db[key][short_specialty] = specialty_ratio
                     else:
                            count=count+0
                            specialty_ratio=count/len(specialty)
                            university_specialization_db[key][short_specialty] = specialty_ratio






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

# for university, specialty in geog_programs_data_db.items():
#        for short_specialty in short_specialities_list:
#               program_specialty_data[short_specialty]={}
#               for key, values in specialty.items():
#                      if (key, values) == (key, 'X'):
#                             program_specialty_data.update({short_specialty:university})
#                             print(program_specialty_data)
       #program_specialty_data[short_specialty] = university
#print(program_specialty_data)



# for key, value in program_data.items():
#        if key == 'Cultural Geography' and key == 'Gender' and key == 'Historical Geography' and key =='Political Geography' and key =='Social Geography' and key == 'Rural Geography' and key == 'Political Geography' and key == 'Population Geography' and key == 'Medical Geography' and  value =='X':
#

