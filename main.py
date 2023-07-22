# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 10:12:28 2023

@author: James
"""

from import_fantasy_data import import_data
import matplotlib.pyplot as plt



fpl_element_stats, fpl_element_types, fpl_elements, fpl_events, \
fpl_phases, fpl_teams, fpl_total_players = import_data()


plt.figure()
ppm = fpl_elements['total_points'] / fpl_elements['minutes']

plt.plot(fpl_elements['total_points'], ppm, 'k.')
plt.xlabel('Total Points')
plt.ylabel('Points Per Minute')
plt.show()

# Select useful variables from element data frame
#data = fpl_elements[['team', 'element_type', 'web_name', 'now_cost', 'minutes',
#                     'total_points', 'form', 'value_season', 'selected_by_percent', 'ict_index']]


