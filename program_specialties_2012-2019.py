# Author:                       Eni Awowale & Coline Dony
# Date first written:           June 27, 2019
# Date last updated:            July 23, 2019
# Purpose:                      Determine U.S. University's levels of specialization

# Problem Statement:
# University Geography Departments have varying levels of specializations. Using AGG Guide to Geography Programs in the
# Americas this script will extract information about the vary levels of specialization

# Set up environment
import os
import sys

#folder = r'C:\Users\oawowale\Documents\GitHub\affinities-of-geog-departments\program_specialties'
folder = r'C:\Users\cdony\Google Drive\GitHub\affinities-of-geog-departments'
os.chdir(folder)

# Read input data:
#No Program Data for 2013
#Excluding 2016 temporarily because it is in different format than the rest
unwanted_specialties = ['Program Specialties', 'Associates', 'Bachelors','Masters','PhD', 'Certificate Program','Distance / Online','North America', 'Middle America', 'South America', 'Europe', 'Africa', 'Asia', 'Australia Oceania',
                             'Polar World', 'Middle East', 'Former Soviet Union', 'World Regional\n', '\t', '\n','']
specialty_groups_db={}
geog_programs_data_db = {}
for year in [2012, 2014, 2015, 2016, 2017, 2018, 2019]:
    # Need to create exception for 2012 due to formatting
    if year == 2012:
        file_name_2012 = r'program_specialties_2012.txt'
        input_as_text_2012 = open(file_name_2012).readlines()
        headers_2012 = ''.join(input_as_text_2012[1:3]).replace('\n', '').split('\t')
        headers_2012[0] = 'University name'
        for line_as_text_2012 in input_as_text_2012[3:272]:
            line_as_list_2012 = line_as_text_2012.split('\t')
            if 'X' in line_as_list_2012:
                program_data_2012 = dict(zip(headers_2012, line_as_list_2012))
                university_name_2012_draft = program_data_2012['University name']
                university_name_2012 = university_name_2012_draft.replace(', ', ' ').replace(' - ', ' ').replace('-', ' ')\
                    .replace('"','').replace('University of Alaska', 'University of Alaska Fairbanks').replace('.', '')\
                    .replace('United States', 'US').replace(' at ', ' ').replace('University of Hawaii', 'University of Hawaii Manoa')\
                    .replace('Univeristy', 'University').replace(' of the State University of New York', ' SUNY').replace(' State University of New York', ' SUNY')\
                    .replace(' of the City University of New York', ' CUNY').replace('State University of New York', 'SUNY').replace('University of Arkansas Fayettville', 'University of Arkansas')
                university_name_2012 = university_name_2012.lower()
                geog_programs_data_db[university_name_2012] = {}
                geog_programs_data_db[university_name_2012][year] = program_data_2012
                geog_programs_data_db[university_name_2012][year]['Specialty groups'] = {}
                geog_programs_data_db[university_name_2012][year]['Specialty groups'] = {'Human Geography': [headers_2012[specialty_2012] for specialty_2012 in [16,20,27,32,39,38,33,29]],
                                                                                         'Human-Environmental Interactions': [headers_2012[specialty_2012] for specialty_2012 in [15,14,19,9,42,26,]],
                                                                                         'Physical Geography': [headers_2012[specialty_2012] for specialty_2012 in [11,13,23,30]],
                                                                                         'Geospatial Technologies': [headers_2012[specialty_2012] for specialty_2012 in [37,24,25]],
                                                                                         'Urban and Economic Geography': [headers_2012[specialty_2012] for specialty_2012 in [41,36,35,31,40,17,18]],
                                                                                         'Methods': [headers_2012[specialty_2012] for specialty_2012 in [21,22,28,10,12,34,]]}
    else:
        input_filename = r'program_specialties_%s.txt' % year
        input_as_text = open(input_filename).readlines()
        if input_as_text[0].split('\t')[1] == '': headers_index = 1
        else: headers_index = 0
        headers = input_as_text[headers_index].split('\t')
        headers[0] = 'University name'
        #do you think you can help format this so it stops before it gets to Canada
        for line_as_text in input_as_text[headers_index+1:]:
            line_as_list = line_as_text.split('\t')
            if 'CANADA' in line_as_list: break
            if 'X' in line_as_list:
                program_data = dict(zip(headers, line_as_list))
                university_name_draft = program_data['University name']
                #start modifying the university names here
                university_name = university_name_draft.replace(', ', ' ').replace(' - ', ' ').replace('-', ' ').replace('"', '') \
                    .replace('.', '').replace('United States', 'US').replace(' at ', ' ').replace('Univeristy', 'University').replace(' (UCLA)', '') \
                    .replace('University of Arkansas Fayettville', 'University of Arkansas').replace('University of Arkansas Fayetteville', 'University of Arkansas')
                university_name = university_name.lower()
                if university_name not in geog_programs_data_db:
                    geog_programs_data_db[university_name] = {}
                geog_programs_data_db[university_name][year] = program_data
                if year == 2016:
                    headers_2016 = headers
                    geog_programs_data_db[university_name][year]['Specialty groups'] = {
                    'Human Geography': [headers_2016[specialty_2016] for specialty_2016 in
                                        [8, 14, 21, 26, 32, 27, 33, 23]],
                    'Human-Environmental Interactions': [headers_2016[specialty_2016] for specialty_2016 in
                                                         [13, 7, 6, 1, 36, 20, 12]],
                    'Physical Geography': [headers_2016[specialty_2016] for specialty_2016 in [3, 5, 17, 24]],
                    'Geospatial Technologies': [headers_2016[specialty_2012] for specialty_2012 in [18, 19, 31]],
                    'Urban and Economic Geography': [headers_2016[specialty_2016] for specialty_2016 in
                                                     [35, 30, 29, 25, 34, 10, 11]],
                    'Methods': [headers_2016[specialty_2016] for specialty_2016 in [15, 16, 22, 2, 4, 28]]}
                geog_programs_data_db[university_name][year]['Specialty groups'] = {}
    #trying to figure out a method for organizing the original specialties into the group specialties for the years
    #2014, 2015, 2017, 2018, and 2019. 2014 and 2015 have the same number of specialties/headers while 2018 and 2019
    #2016 has the same number 2016 but i did 2016 separately because it has 'Distance / Online Program' as a unique speciality

#use to check for repeated universities
for university, years in geog_programs_data_db.items():
    if len(years) < 4:
        #print(university, len(years))
        print(len(years),university, years)

