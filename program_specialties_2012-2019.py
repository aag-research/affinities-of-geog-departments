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



#use to check for repeated universities
# for university, years in geog_programs_data_db.items():
#     if len(years) < 3:
#         print(len(years), university, years.keys())

#Writing data in format usable for radar chart

data_for_radar_chart = [[] for specialty in range(len(geog_programs_data_db))]
data_for_radar_chart [0]=['Human Geography', 'Human Environmental Interactions', 'Physical Geography', 'Geospatial Technologies',
         'Urban and Economic Geography', 'Methods']
years = [2012 ,2014, 2015, 2016, 2017, 2018, 2019]
for university_name, university_specialty_data in geog_programs_data_db.items():
    #I wasn't sure if I should declare a list within a list that has the length of the years yet
    #data_for_radar_chart[1:] = ([university, [[] for i in range(len(years))]] for university, specialty_data in geog_programs_data_db.items())
    data_for_radar_chart[1:] = ([university, []] for university, specialty_data in geog_programs_data_db.items())
    specialty_ratio = [[] for specific_year in range(len(years))]
    for year_index in range(len(specialty_ratio)):
        if years[year_index] in university_specialty_data:
            for group_specialty in university_specialty_data[years[year_index]]['Specialty Groups']:
                ratio_totals = university_specialty_data[years[year_index]]['Specialty Groups'][group_specialty]['Ratio']
                specialty_ratio[year_index].append(ratio_totals)
                for university, data_value in data_for_radar_chart[1:]:
                    data_value.append(specialty_ratio[year_index])
                #Keeps saving the same year values, I tried a few other methods but can't figure out why
        else:
            year_index = year_index+1