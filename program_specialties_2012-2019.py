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

folder = r'C:\Users\oawowale\Documents\GitHub\affinities-of-geog-departments'
#folder = r'C:\Users\cdony\Google Drive\GitHub\affinities-of-geog-departments'
os.chdir(folder)
<<<<<<< HEAD
<<<<<<< HEAD
#Read input data from 2012-2019
#No Program Data for 2013

# Program specialties groupings
specialty_groups_filename = 'program_specialties\program_specialties_groupings.txt'
input_as_text = open(specialty_groups_filename).readlines()
input_as_list = [line_as_text.strip().replace('"', '').split('\t') for line_as_text in input_as_text[1:]]
specialty_groups_db = {specialty : group for specialty, group in input_as_list}
specialties = list(specialty_groups_db.keys())
specialty_groups = list(set(specialty_groups_db.values()))

#Read input data from 2012-2019 (No Program Data for 2013)
=======

# Read input data:
#No Program Data for 2013
=======

# Read input data:
#No Program Data for 2013
>>>>>>> parent of 4cf33fc... Calculates subject specialties and addes to dictionary
#Excluding 2016 temporarily because it is in different format than the rest
unwanted_specialties = ['Program Specialties', 'Associates', 'Bachelors','Masters','PhD', 'Certificate Program','Distance / Online','North America', 'Middle America', 'South America', 'Europe', 'Africa', 'Asia', 'Australia Oceania',
                             'Polar World', 'Middle East', 'Former Soviet Union', 'World Regional\n', '\t', '\n','']
specialty_groups_db={}
<<<<<<< HEAD
>>>>>>> parent of 4cf33fc... Calculates subject specialties and addes to dictionary
=======
>>>>>>> parent of 4cf33fc... Calculates subject specialties and addes to dictionary
geog_programs_data_db = {}
#subject_totals_db = {}
for year in [2012, 2014, 2015, 2016, 2017, 2018, 2019]:
    input_filename = r'program_specialties\program_specialties_%s.txt' % year
    input_as_text = open(input_filename).readlines()
    # Need to create exception for 2012 due to formatting
    if year == 2012:
        file_name_2012 = r'program_specialties/program_specialties_2012.txt'
        input_as_text_2012 = open(file_name_2012).readlines()
        headers_2012 = ''.join(input_as_text_2012[1:3]).replace('\n', '').split('\t')
        headers_2012[0] = 'University name'
        for line_as_text_2012 in input_as_text_2012[3:272]:
            line_as_list_2012 = line_as_text_2012.split('\t')
            if 'X' in line_as_list_2012:
                program_data_2012 = dict(zip(headers_2012, line_as_list_2012))
                university_name_2012_draft = program_data_2012['University name']
                #Modifying university names so they are consistently formatted
                university_name_2012 = university_name_2012_draft.replace(', ', ' ').replace(' - ', ' ').replace('-', ' ')\
                    .replace('"','').replace('University of Alaska', 'University of Alaska Fairbanks').replace('.', '')\
                    .replace('United States', 'US').replace(' at ', ' ').replace('University of Hawaii', 'University of Hawaii Manoa')\
                    .replace('Univeristy', 'University').replace(' of the State University of New York', ' SUNY')\
                    .replace(' State University of New York', ' SUNY').replace(' of the City University of New York', ' CUNY')\
                    .replace('State University of New York', 'SUNY').replace('University of Arkansas Fayettville', 'University of Arkansas')
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
                subject_totals_db = {}
                #Calculates program specialties per university
                for group_specialty_name, subject_lists in geog_programs_data_db[university_name_2012][year]['Specialty groups'].items():
                    subject_totals = 0
                    for subject in subject_lists:
                        if geog_programs_data_db[university_name_2012][year][subject]== 'X' and subject in subject_lists:
                            subject_totals = subject_totals+1
                            subject_totals_ratio = subject_totals/(len(subject_lists))
                        else:
                            subject_totals = subject_totals + 0
                            subject_totals_ratio = subject_totals/(len(subject_lists))
                        subject_totals_db[group_specialty_name] = {}
                        subject_totals_db[group_specialty_name]['Whole number'] = {}
                        subject_totals_db[group_specialty_name]['Whole number'] = subject_totals
                        subject_totals_db[group_specialty_name]['Float'] = {}
                        subject_totals_db[group_specialty_name]['Float'] = subject_totals_ratio
                geog_programs_data_db[university_name_2012][year]['Specialty groups']['subject_totals'] = {}
                geog_programs_data_db[university_name_2012][year]['Specialty groups']['subject_totals'] = subject_totals_db

    else:
        input_filename = r'program_specialties/program_specialties_%s.txt' % year
        input_as_text = open(input_filename).readlines()
        if input_as_text[0].split('\t')[1] == '': headers_index = 1
        else: headers_index = 0
        headers = input_as_text[headers_index].split('\t')
        headers[0] = 'University name'
        for specialty in headers:
            if specialty == 'Energy' or 'Political Ecology':
                try: headers.remove('Energy')
                except: ValueError
                try: headers.remove('Political Ecology')
                except: ValueError
                try: headers.remove('Distance/Online Degree Program')
                except: ValueError
                try: headers.remove('Distance / Online')
                except: ValueError
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
                geog_programs_data_db[university_name][year]['Specialty groups'] = {}
                if year == 2016:
                    headers_2016 = headers
<<<<<<< HEAD
<<<<<<< HEAD
                    #print(len(headers_2016))
                    #Adding subjects to 2016 dictionaries
=======
>>>>>>> parent of 4cf33fc... Calculates subject specialties and addes to dictionary
=======
>>>>>>> parent of 4cf33fc... Calculates subject specialties and addes to dictionary
                    geog_programs_data_db[university_name][year]['Specialty groups'] = {
                    'Human Geography': [headers_2016[specialty_2016] for specialty_2016 in
                                        [8, 12, 19, 24, 31, 30, 25, 21]],
                    'Human-Environmental Interactions': [headers_2016[specialty_2016] for specialty_2016 in
                                                         [1, 7, 6, 11, 34, 18]],
                    'Physical Geography': [headers_2016[specialty_2016] for specialty_2016 in [3, 5, 22, 15]],
                    'Geospatial Technologies': [headers_2016[specialty_2012] for specialty_2012 in [16, 17, 29]],
                    'Urban and Economic Geography': [headers_2016[specialty_2016] for specialty_2016 in
                                                     [33, 28, 27, 23, 32, 10, 9]],
                    'Methods': [headers_2016[specialty_2016] for specialty_2016 in [2, 13, 20, 14, 4, 26]]}
<<<<<<< HEAD
<<<<<<< HEAD
                    #Calculates program specialties for universities in 2016
                    subject_totals_db_2016 = {}
                    for group_specialty_name_2016, subject_lists_2016 in geog_programs_data_db[university_name][year][
                        'Specialty groups'].items():
                        subject_totals_2016 = 0
                        for subject in subject_lists_2016:
                            if geog_programs_data_db[university_name][year][
                                subject] == 'X' and subject in subject_lists_2016:
                                subject_totals_2016 = subject_totals_2016 + 1
                                subject_totals_ratio_2016 = subject_totals_2016 / (len(subject_lists_2016))
                            else:
                                subject_totals_2016 = subject_totals_2016 + 0
                                subject_totals_ratio_2016 = subject_totals_2016 / (len(subject_lists_2016))
                            subject_totals_db_2016[group_specialty_name_2016] = {}
                            subject_totals_db_2016[group_specialty_name_2016]['Whole number'] = {}
                            subject_totals_db_2016[group_specialty_name_2016]['Whole number'] = subject_totals_2016
                            subject_totals_db_2016[group_specialty_name_2016]['Float'] = {}
                            subject_totals_db_2016[group_specialty_name_2016]['Float'] = subject_totals_ratio_2016
                    geog_programs_data_db[university_name][year]['Specialty groups']['subject_totals'] = {}
                    geog_programs_data_db[university_name][year]['Specialty groups'][
                        'subject_totals'] = subject_totals_db_2016

    if year == 2012: header_start, header_end = 1, 3
    elif year == 2016: header_start, header_end = 1, 2
    else: header_start, header_end = 0, 1
    headers = ''.join(input_as_text[header_start:header_end]).replace('"', '').replace('\n', '')
    headers = headers.split('\t')
    headers[0] = 'University name'
    for specialty in specialties:
        if specialty not in headers:
            for old, new in [(' Resource Management', ''), ('/', ' / '), ('/', ' and '), ('/Communication', ''),
                             ('Conservation, Land Use, Resource Management', 'Cnsrvtn, Land Use, Resource Mngmt'),
                             (', Resource Management', ''),
                             ('Climatology/Meteorology', 'Climatography/Meterology'), ('Certification', 'Certfication')]:
                if specialty.replace(old, new) in headers:
                    header_index = headers.index(specialty.replace(old, new))
                    headers[header_index] = specialty
    for line_as_text in input_as_text[header_end:]:
        line_as_list = line_as_text.split('\t')
        if 'CANADA' in line_as_list: break
        if 'X' in line_as_list:
            program_data = dict(zip(headers, line_as_list))
            university_name = program_data['University name']
            if 'Department of State' in  university_name: continue
            for character in [', ', ' - ', '-', ' at ']: university_name = university_name.replace(character, ' ')
            for character in ['"', '.', ' (UCLA)']: university_name = university_name.replace(character, '')
            for old, new in [('Univeristy', 'University'), ('Univesity', 'University'), ('Fayettville', 'Fayetteville'), ('Colege', 'College'),
                             ('United States', 'US'), ('University of Hawaii', 'University of Hawaii Manoa'),
                             ('University of Alaska', 'University of Alaska Fairbanks'), ('University of Arkansas Fayetteville', 'University of Arkansas'),
                             (' of the State University of New York', ' SUNY'), (' State University of New York', ' SUNY'),
                             ('State University of New York', 'SUNY'), (' of the City University of New York', ' CUNY'),
                             ('The Pennsylvania State University', 'Pennsylvania State University'), ('Penn State University', 'Pennsylvania State University'),
                             ('The University of Texas San Antonio','University of Texas San Antonio'), ('Virginia Tech University', 'Virginia Tech'),
                             ('The Ohio State University', 'Ohio State University'), ('University of Illinois Urbana Champaign', 'University of Illinois')]:
                university_name = university_name.replace(old, new)
            university_name = university_name.lower().strip()
            if university_name not in geog_programs_data_db: geog_programs_data_db[university_name] = {}
            geog_programs_data_db[university_name][year] = program_data
            geog_programs_data_db[university_name][year]['Specialty Groups'] = {specialty_group : {'List': []} for specialty_group in specialty_groups}
            for header in headers:
                if header in specialties:
                    if geog_programs_data_db[university_name][year][header] == 'X':
                        specialty_group = specialty_groups_db[header]
                        geog_programs_data_db[university_name][year]['Specialty Groups'][specialty_group]['List'] += [header]
            for specialty_group in specialty_groups:
                specialties_in_group = geog_programs_data_db[university_name][year]['Specialty Groups'][specialty_group]['List']
                max_spacialties_in_group = list(specialty_groups_db.values()).count(specialty_group)
                if specialty_group == 'Human-Environmental Interactions':
                    if 'Political Ecology' in specialties_in_group and 'Cultural Ecology' in specialties_in_group:
                        specialties_in_group.remove('Political Ecology')
                        if 'Energy' in specialties_in_group and 'Conservation, Land Use, Resource Management' in specialties_in_group:
                            specialties_in_group.remove('Energy')
                    max_spacialties_in_group = max_spacialties_in_group - 2
                geog_programs_data_db[university_name][year]['Specialty Groups'][specialty_group]['Total'] = len(specialties_in_group)
                geog_programs_data_db[university_name][year]['Specialty Groups'][specialty_group]['Ratio'] = len(specialties_in_group)/max_spacialties_in_group

# print an example
# specialty_group = 'Human-Environmental Interactions'
# university_name = 'university of delaware'
# # for year in [2012, 2014, 2015, 2016, 2017, 2018, 2019]:
# #     print(year)
# #     print(geog_programs_data_db[university_name][year]['Specialty Groups'][specialty_group])
# #     print('\n')


data_for_radar_chart = [() for specialty in range(len(geog_programs_data_db))]
data_for_radar_chart [0]=['Human Geography', 'Human Environmental Interactions', 'Physical Geography', 'Geospatial Technologies',
         'Urban and Economic Geography', 'Methods']

for university_name,university_specialty_data in geog_programs_data_db.items():
    for year in university_specialty_data:
        print(university_specialty_data[year]['University name'],university_specialty_data[year]['Specialty Groups'])



=======
=======
>>>>>>> parent of 4cf33fc... Calculates subject specialties and addes to dictionary
                    geog_programs_data_db[university_name][year]['Specialty groups']['count'] = {}
                    geog_programs_data_db[university_name][year]['Specialty groups']['count'] = {'Human Geography': 0,
                                                                                                 'Human-Environmental Interactions': 0,
                                                                                                 'Physical Geography': 0,
                                                                                                 'Geospatial Technologies': 0,
                                                                                                 'Urban and Economic Geography': 0,
                                                                                                 'Methods': 0}
                else:
                    geog_programs_data_db[university_name][year]['Specialty groups'] = {
                        'Human Geography': [headers[specialty_all] for specialty_all in
                                            [13, 17, 24, 29, 30, 36, 35, 26]],
                        'Human-Environmental Interactions': [headers[specialty_all] for specialty_all in
                                                             [16, 12, 11, 6, 23, 39]],
                        'Physical Geography': [headers[specialty_all] for specialty_all in [8, 27, 20, 10]],
                        'Geospatial Technologies': [headers[specialty_all] for specialty_all in [34, 21, 22]],
                        'Urban and Economic Geography': [headers[specialty_all] for specialty_all in
                                                         [38, 33, 32, 28, 37, 14, 15]],
                        'Methods': [headers[specialty_all] for specialty_all in [18, 19, 9, 7, 25, 31]]}
                #creating count dictionary
                geog_programs_data_db[university_name][year]['Specialty groups']['count'] = {}
                geog_programs_data_db[university_name][year]['Specialty groups']['count'] = {'Human Geography' : 0,
                                                                                                 'Human-Environmental Interactions': 0,
                                                                                                 'Physical Geography': 0,
                                                                                                 'Geospatial Technologies': 0,
                                                                                                 'Urban and Economic Geography': 0,
                                                                                                 'Methods': 0}



#use to check for repeated universities
# for university, years in geog_programs_data_db.items():
#     if len(years) < 4:
#         #print(university, len(years))
#         print(len(years),university, years)
<<<<<<< HEAD
>>>>>>> parent of 4cf33fc... Calculates subject specialties and addes to dictionary
=======
>>>>>>> parent of 4cf33fc... Calculates subject specialties and addes to dictionary

###use to check for repeated universities
### for university, years in geog_programs_data_db.items():
###     if len(years) < 3:
###         print(len(years), university, years.keys())
##        #print(len(years),university, years)
##
