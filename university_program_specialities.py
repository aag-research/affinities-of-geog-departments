# Author:                       Eni Awowale
# Date first written:           June 27, 2019
# Date last updated:            June 27, 2019
# Purpose:                      Determine U.S. University's levels of specialization

# Problem Statement:
# University Geography Departments have varying levels of specializations. Using AGG Guide to Geography Programs in the
# America this script will extract information about the vary levels of specialization

import sys
import os
import csv

program_specialities_csv_name = r'program_specialities.csv'
program_specialities_csv = open(program_specialities_csv_name).readlines()
headers = program_specialities_csv[0].split('\t')
program_specialities1 = program_specialities_csv[1].split(',')
program_specialities2 = program_specialities_csv[2].split(',')
subject_specialities = program_specialities1[9:15] + program_specialities2[0:30]
#stopped here have a list of my specialities now



