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

#Read input data from 2012-2019
#No Program Data for 2013
geog_programs_data_db = {}
for year in [2012, 2014, 2015, 2016, 2017, 2018, 2019]:
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
                #Adding subjects to specialty groups
                geog_programs_data_db[university_name_2012][year]['Specialty groups'] = {}
                geog_programs_data_db[university_name_2012][year]['Specialty groups'] = {'Human Geography': [headers_2012[specialty_2012] for specialty_2012 in [16,20,27,32,39,38,33,29]],
                                                                                         'Human-Environmental Interactions': [headers_2012[specialty_2012] for specialty_2012 in [15,14,19,9,42,26,]],
                                                                                         'Physical Geography': [headers_2012[specialty_2012] for specialty_2012 in [11,13,23,30]],
                                                                                         'Geospatial Technologies': [headers_2012[specialty_2012] for specialty_2012 in [37,24,25]],
                                                                                         'Urban and Economic Geography': [headers_2012[specialty_2012] for specialty_2012 in [41,36,35,31,40,17,18]],
                                                                                         'Methods': [headers_2012[specialty_2012] for specialty_2012 in [21,22,28,10,12,34,]]}

                subject_totals_db_2012 = {}
                #Calculates program specialties for universities in 2012
                for group_specialty_name_2012, subject_lists_2012 in geog_programs_data_db[university_name_2012][year]['Specialty groups'].items():
                    subject_totals_2012 = 0
                    for subject in subject_lists_2012:
                        if geog_programs_data_db[university_name_2012][year][subject]== 'X' and subject in subject_lists_2012:
                            subject_totals_2012 = subject_totals_2012+1
                            subject_totals_ratio_2012 = subject_totals_2012/(len(subject_lists_2012))
                        else:
                            subject_totals_2012 = subject_totals_2012 + 0
                            subject_totals_ratio_2012 = subject_totals_2012/(len(subject_lists_2012))
                        subject_totals_db_2012[group_specialty_name_2012] = {}
                        subject_totals_db_2012[group_specialty_name_2012]['Whole number'] = {}
                        subject_totals_db_2012[group_specialty_name_2012]['Whole number'] = subject_totals_2012
                        subject_totals_db_2012[group_specialty_name_2012]['Float'] = {}
                        subject_totals_db_2012[group_specialty_name_2012]['Float'] = subject_totals_ratio_2012
                geog_programs_data_db[university_name_2012][year]['Specialty groups']['subject_totals'] = {}
                geog_programs_data_db[university_name_2012][year]['Specialty groups']['subject_totals'] = subject_totals_db_2012

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
                #Modifying university names for the rest the years
                university_name = university_name_draft.replace(', ', ' ').replace(' - ', ' ').replace('-', ' ').replace('"', '') \
                    .replace('.', '').replace('United States', 'US').replace(' at ', ' ').replace('Univeristy', 'University').replace(' (UCLA)', '') \
                    .replace('University of Arkansas Fayettville', 'University of Arkansas').replace('University of Arkansas Fayetteville', 'University of Arkansas')\
                    .replace('Colege', 'college').replace('Univesity', 'University').replace('The Pennsylvania State University', 'Pennsylvania State University')\
                    .replace('Penn State University', 'Pennsylvania State University').replace('The University of Texas San Antonio','University of Texas San Antonio')\
                    .replace('Virginia Tech University', 'Virginia Tech').replace('Virginia Tech ', 'Virginia Tech')\
                    .replace('University of Arizona ', 'University of Arizona').replace('The Ohio State University', 'Ohio State University')\
                    .replace('Department of State', 'US Department of State').replace('University of Illinois Urbana Champaign', 'University of Illinois')
                university_name = university_name.lower()
                if university_name not in geog_programs_data_db:
                    geog_programs_data_db[university_name] = {}
                geog_programs_data_db[university_name][year] = program_data
                geog_programs_data_db[university_name][year]['Specialty groups'] = {}
                #Exception for 2016 because it specialties have a different index
                if year == 2016:
                    headers_2016 = headers
                    #Adding subjects to 2016 dictionaries
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

                # Adding subjects to specialty groups for all other years
                else:
                    #Years 2014,2015,2017,2018 and 2019 have the same index for their specialties
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

                    #Calculates program specialties for 2014, 2015, 2017, 2018 and 2019
                    subject_totals_db = {}
                    for group_specialty_name, subject_lists in geog_programs_data_db[university_name][year][
                    'Specialty groups'].items():
                        subject_totals = 0
                        for subject in subject_lists:
                            if geog_programs_data_db[university_name][year][
                            subject] == 'X' and subject in subject_lists:
                                subject_totals = subject_totals + 1
                                subject_totals_ratio = subject_totals / (len(subject_lists))
                            else:
                                subject_totals = subject_totals + 0
                                subject_totals_ratio = subject_totals / (len(subject_lists))
                            subject_totals_db[group_specialty_name] = {}
                            subject_totals_db[group_specialty_name]['Whole number'] = {}
                            subject_totals_db[group_specialty_name]['Whole number'] = subject_totals
                            subject_totals_db[group_specialty_name]['Float'] = {}
                            subject_totals_db[group_specialty_name]['Float'] = subject_totals_ratio
                    geog_programs_data_db[university_name][year]['Specialty groups']['subject_totals'] = {}
                    geog_programs_data_db[university_name][year]['Specialty groups'][
                    'subject_totals'] = subject_totals_db

#use to check for repeated universities
# for university, years in geog_programs_data_db.items():
#     if len(years) < 3:
#         print(len(years), university, years.keys())
        #print(len(years),university, years)
