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
        for line_as_text_2012 in input_as_text_2012[3:]:
            line_as_list_2012 = line_as_text_2012.split('\t')
            if 'X' in line_as_list_2012:
                program_data_2012 = dict(zip(headers_2012, line_as_list_2012))
                university_name_2012 = program_data_2012['University name']
                if university_name_2012 not in geog_programs_data_db:
                    geog_programs_data_db[university_name_2012] = {}
                geog_programs_data_db[university_name_2012][year] = program_data_2012
                geog_programs_data_db[university_name_2012][year]['Specialty groups'] = {}
                geog_programs_data_db[university_name_2012][year]['Specialty groups'] = {'Human Geography': [headers_2012[specialty_2012] for specialty_2012 in [16,20,27,32,39,38,33,29]],
                                                                                         'Human-Environmental Interactions': [headers_2012[specialty_2012] for specialty_2012 in [15,14,19,9,42,26,]],
                                                                                         'Physical Geography': [headers_2012[specialty_2012] for specialty_2012 in [11,13,23,30]],
                                                                                         'Geospatial Technologies': [headers_2012[specialty_2012] for specialty_2012 in [37,24,25]],
                                                                                         'Urban and Economic Geography': [headers_2012[specialty_2012] for specialty_2012 in [41,36,35,31,40,17,18]],
                                                                                         'Methods': [headers_2012[specialty_2012] for specialty_2012 in [21,22,28,10,12,34,]]}
                #geog_programs_data_db[university_name_2012][year]['Specialty groups'] = headers_2012[headers_2012.index(
                    #'Agricultural Geography'): headers_2012.index('Regional Geography')]
    else:
        input_filename = r'program_specialties_%s.txt' % year
        input_as_text = open(input_filename).readlines()
        if input_as_text[0].split('\t')[1] == '': headers_index = 1
        else: headers_index = 0
        headers = input_as_text[headers_index].split('\t')
        headers[0] = 'University name'
        for line_as_text in input_as_text[headers_index+1:]:
            line_as_list = line_as_text.split('\t')
            if 'X' in line_as_list:
                program_data = dict(zip(headers, line_as_list))
                university_name = program_data['University name']
        #start modifying the university names here
                if university_name not in geog_programs_data_db:
                    geog_programs_data_db[university_name] = {}
                geog_programs_data_db[university_name][year] = program_data
                geog_programs_data_db[university_name][year]['Specialty groups'] = {}
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










#geog_programs_data_db[university_name][year]['Specialty groups'] = headers[headers.index(
#'Agricultural Geography'): headers.index('North America')]
