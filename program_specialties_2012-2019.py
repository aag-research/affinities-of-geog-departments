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
    else:
        input_filename = r'program_specialties_%s.txt' % year
        input_as_text = open(input_filename).readlines()
        if input_as_text[0].split('\t')[1] == '': headers_index = 1
        else: headers_index = 0
        headers = input_as_text[headers_index].split('\t')
        headers[0] = 'University name'
    #print(input_as_text[0].split('\t')[15])
    #print(input_as_text[0:2])
        for line_as_text in input_as_text[headers_index+1:]:
            line_as_list = line_as_text.split('\t')
            if 'X' in line_as_list:
                program_data = dict(zip(headers, line_as_list))
                university_name = program_data['University name']
                if university_name not in geog_programs_data_db:
                    geog_programs_data_db[university_name] = {}
                geog_programs_data_db[university_name][year] = program_data
