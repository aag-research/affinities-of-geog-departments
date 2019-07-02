# Author:                       Eni Awowale
# Date first written:           June 27, 2019
# Date last updated:            July 2, 2019
# Purpose:                      Determine U.S. University's levels of specialization

# Problem Statement:
# University Geography Departments have varying levels of specializations. Using AGG Guide to Geography Programs in the
# Americas this script will extract information about the vary levels of specialization

# Set up environment
import os
folder = r'C:\Users\cdony\Google Drive\GitHub\affinities-of-geog-departments'
os.chdir(folder)

<<<<<<< HEAD
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
=======
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
       if line_as_list[1] != '':
              program_data = dict(zip(headers, line_as_list))
              geog_programs_data_db[program_data['University name']] = program_data

# Store the specialties of each progam in a format
# that would work for radar charts (in matplotlib)
specialties = headers[9:-12]
data_for_radar_chart = [specialties]
for university, program_data in geog_programs_data_db.items():
       program_specialties = [1 if program_data[specialty] == 'X' else 0 for specialty in specialties]
       data_for_radar_chart += [(university, program_specialties)]

# Show the formatted data on the screen
print(data_for_radar_chart[0:8])
>>>>>>> 8298ba66b0bb3fdd053107ab1724d40e31205318
