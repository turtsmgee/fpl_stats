# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 10:12:28 2023

@author: James
"""

from import_fantasy_data import import_data
from plot_ppm import plot_ppm


fpl_element_stats, fpl_element_types, fpl_elements, fpl_events, fpl_teams = import_data()

plot_ppm(fpl_elements)






