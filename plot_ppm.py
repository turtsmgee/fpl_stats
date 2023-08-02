# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 17:32:54 2023

@author: James
"""

import seaborn as sns


def plot_ppm(fpl_elements):
    minimumPoints = 80
    
    ppm = fpl_elements['total_points'] / fpl_elements['minutes']
    
    plotIDX = fpl_elements['total_points'] > minimumPoints
    
    x = fpl_elements.loc[plotIDX, 'total_points']
    y = ppm[plotIDX]   
    sns.scatterplot(x = x, y = y, hue = y)
    return