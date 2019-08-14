# Author:                       Eni Awowale & Coline Dony
# Date first written:           June 27, 2019
# Date last updated:            August 14, 2019
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

# Program specialties groupings
specialty_groups_filename = 'program_specialties\program_specialties_groupings.txt'
input_as_text = open(specialty_groups_filename).readlines()
input_as_list = [line_as_text.strip().replace('"', '').split('\t') for line_as_text in input_as_text[1:]]
specialty_groups_db = {specialty : group for specialty, group in input_as_list}
specialties = list(specialty_groups_db.keys())
specialty_groups = list(set(specialty_groups_db.values()))

#Read input data from 2012-2019 (No Program Data for 2013)
geog_programs_data_db = {}
for year in [2012, 2014, 2015, 2016, 2017, 2018, 2019]:
    input_filename = r'program_specialties\program_specialties_%s.txt' % year
    input_as_text = open(input_filename).readlines()
    # Need to create exception for 2012 due to formatting
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
                             ('United States', 'US'), ('University of Hawaii Manoa', 'University of Hawaii'),
                              ('University of Arkansas Fayetteville', 'University of Arkansas'),
                             (' of the State University of New York', ' SUNY'), (' State University of New York', ' SUNY'),
                             ('State University of New York', 'SUNY'), (' of the City University of New York', ' CUNY'),
                             ('The Pennsylvania State University', 'Pennsylvania State University'), ('Penn State University', 'Pennsylvania State University'),
                             ('The University of Texas San Antonio','University of Texas San Antonio'), ('Virginia Tech University', 'Virginia Tech'),
                             ('The Ohio State University', 'Ohio State University'), ('University of Illinois Urbana Champaign', 'University of Illinois')]:
                university_name = university_name.replace(old, new)
            if university_name == 'University of Alaska': university_name ='University of Alaska Fairbanks'
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

#Use to check for repeated universities
# for university, years in geog_programs_data_db.items():
#     if len(years) < 3:
#         print(len(years), university, years.keys())

#Writing data in format usable for radar chart
data_for_radar_chart = [specialty_groups]
for university_name, university_specialty_data in geog_programs_data_db.items():
    ratios_for_all_years = []
    for year in [2012 ,2014, 2015, 2016, 2017, 2018, 2019]:
        if year in university_specialty_data:
            ratios_for_1_year = []
            for specialty_group in specialty_groups:
                ratios_for_1_year += [university_specialty_data[year]['Specialty Groups'][specialty_group]['Ratio']]
        else: ratios_for_1_year = [0, 0, 0, 0, 0, 0]
        ratios_for_all_years += [ratios_for_1_year]
    data_for_radar_chart += [(university_name, ratios_for_all_years)]

#Data for radar chart
data_for_radar_chart_textfile = open('final_radar_chart_data.txt', 'w')
str_data_radar_text = (str(data_for_radar_chart))
data_for_radar_chart_textfile.write(str_data_radar_text)
radar_chart_data_other_format = ['2012','2014','2015','2016', '2017', '2018', '2019']
data_for_radar_chart_textfile.close()
