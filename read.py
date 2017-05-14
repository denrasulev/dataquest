# -*- coding: utf-8 -*-

'''
Code to load data for DataQuest Guided Project on Transforming Data
Reads in 'hn_stories.csv' file and adds four columns.
'''

import pandas as pd

def load_data():
    '''Reads data file in and adds four columns'''
    hn_stories = pd.read_csv('data/hn_stories.csv')
    hn_stories.columns = ['submission_time', 'upvotes', 'url', 'headline']
    return hn_stories

if __name__ == "__main__":
    STOR = load_data()
    stor1 = load_data() # pylint: disable=locally-disabled, invalid-name
    print STOR, stor1
