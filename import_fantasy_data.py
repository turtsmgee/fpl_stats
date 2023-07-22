# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 20:34:53 2023

@author: James
"""

import requests
import pandas as pd


def import_data():
    pd.options.mode.chained_assignment = None
    
    url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
    r = requests.get(url)
    json = r.json()
    
    # Separate all data
    fpl_element_stats = pd.DataFrame(json['element_stats'])
    fpl_element_types = pd.DataFrame(json['element_types'])
    fpl_elements = pd.DataFrame(json['elements'])
    fpl_events = pd.DataFrame(json['events'])    
    fpl_phases = pd.DataFrame(json['phases'])
    fpl_teams = pd.DataFrame(json['teams'])
    
    fpl_total_players = json['total_players']
    
    return fpl_element_stats, fpl_element_types, fpl_elements, fpl_events, \
           fpl_game_settings, fpl_phases, fpl_teams, fpl_total_players




