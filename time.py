# -*- coding: utf-8 -*-

'''
DataQuest Guided Project on Transforming Data
Code to extract and print hour and day
'''

import read.py
from dateutil.parser import parse

def extract_hour(arg):
    '''parsing hour from time'''
    return parse(arg).hour

def extract_day(arg):
    '''parsing day from time'''
    return parse(arg).day

df    = read.load_data()
times = df.submission_time
    
df['submission_hour'] = times.apply(lambda x: extract_hour(x))
sub_hour = df.submission_hour
sub_hour_counts = sub_hour.value_counts()
print(sub_hour_counts[:8])

df['submission_day'] = times.apply(lambda x: extract_day(x))
sub_day = df.submission_day
sub_day_counts = sub_day.value_counts()
print sub_day_counts[:8]
