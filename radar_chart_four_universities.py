# Author:                       Eni Awowale
# Date first written:           June 20, 2019
# Date last updated:            August 13, 2019
# Summary:                      Create a Radar Chart of University Geography Departments Program Specialities


"""
Purpose:
Using a Radar chart (spider or star chart) visualize university program specialties.
Each year since 2012 the AAG (American Association of Geographers)
publishes a Guide to Geography Programs in the Americas, Program Specialties section.
The data used is from Program Specialties published from 2012-2019, excluding 2013,
(the Guide was not published in 2013). The four universities selected are:
Auburn University, University of Maryland, College Park, University of North Carolina, Charlotte, and
Kent State University.
"""

import numpy as np
import os
import sys
import ast
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = 'DejaVu Sans'
from matplotlib.patches import Circle, RegularPolygon
from matplotlib.path import Path
from matplotlib.projections.polar import PolarAxes
from matplotlib.projections import register_projection
from matplotlib.spines import Spine
from matplotlib.transforms import Affine2D

folder = r'C:\Users\oawowale\Documents\GitHub\affinities-of-geog-departments'
os.chdir(folder)

def radar_factory(num_vars, frame='circle'):
    """Create a radar chart with `num_vars` axes.

    This function creates a RadarAxes projection and registers it.

    Parameters
    ----------
    num_vars : int
        Number of variables for radar chart.
    frame : {'circle' | 'polygon'}
        Shape of frame surrounding axes.

    """
    # calculate evenly-spaced axis angles
    theta = np.linspace(0, 2*np.pi, num_vars, endpoint=False)

    class RadarAxes(PolarAxes):

        name = 'radar'
        # use 1 line segment to connect specified points
        RESOLUTION = 1

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # rotate plot such that the first axis is at the top
            self.set_theta_zero_location('N')

        def fill(self, *args, closed=True, **kwargs):
            """Override fill so that line is closed by default"""
            return super().fill(closed=closed, *args, **kwargs)

        def plot(self, *args, **kwargs):
            """Override plot so that line is closed by default"""
            lines = super().plot(*args, **kwargs)
            for line in lines:
                self._close_line(line)

        def _close_line(self, line):
            x, y = line.get_data()
            # FIXME: markers at x[0], y[0] get doubled-up
            if x[0] != x[-1]:
                x = np.concatenate((x, [x[0]]))
                y = np.concatenate((y, [y[0]]))
                line.set_data(x, y)

        def set_varlabels(self, labels):
            self.set_thetagrids(np.degrees(theta), labels)

        def _gen_axes_patch(self):
            # The Axes patch must be centered at (0.5, 0.5) and of radius 0.5
            # in axes coordinates.
            if frame == 'circle':
                return Circle((0.5, 0.5), 0.5)
            elif frame == 'polygon':
                return RegularPolygon((0.5, 0.5), num_vars,
                                      radius=.5, edgecolor="k")
            else:
                raise ValueError("unknown value for 'frame': %s" % frame)

        def _gen_axes_spines(self):
            if frame == 'circle':
                return super()._gen_axes_spines()
            elif frame == 'polygon':
                # spine_type must be 'left'/'right'/'top'/'bottom'/'circle'.
                spine = Spine(axes=self,
                              spine_type='circle',
                              path=Path.unit_regular_polygon(num_vars))
                # unit_regular_polygon gives a polygon of radius 1 centered at
                # (0, 0) but we want a polygon of radius 0.5 centered at (0.5,
                # 0.5) in axes coordinates.
                spine.set_transform(Affine2D().scale(.5).translate(.5, .5)
                                    + self.transAxes)
                return {'polar': spine}
            else:
                raise ValueError("unknown value for 'frame': %s" % frame)

    register_projection(RadarAxes)
    return theta

#Radar Chart Data
data_for_reading = open('final_radar_chart_data.txt').readline()
data_list = ast.literal_eval(data_for_reading)
data=[]
for data_index in [1, 94, 143, 147]:
    data.append(data_list[data_index])

if __name__ == '__main__':
    N = 6
    theta = radar_factory(N, frame='polygon')

    spoke_labels = data_list.pop(0)
    spoke_labels[0] = '\n\nMethods'
    spoke_labels[1] = 'Human\nGeography'
    spoke_labels[2] = 'Physical\nGeography'
    spoke_labels[3] = 'Human-Environmental\nInteractions'
    spoke_labels[4] = 'Geospatial\nTechnologies'
    spoke_labels[5] = 'Urban and Economic\nGeography'


    fig, axes = plt.subplots(figsize=(11, 8.5), nrows=2, ncols=2,
                             subplot_kw=dict(projection='radar'))
    #axes.spines.set_visible(False)
    fig.subplots_adjust(wspace=0.15, hspace=0.55, top=0.85, bottom=0.08, left=0.10, right=0.90)

#Various color styles and schemes:
    #linewidths for thick lines:
    #linewidths = [.5, 1, 1.75, 2.75, 4, 5.5, 7.25][::-1]
    #standard progressive thickness
    linewidths = [1, 1.5, 2, 2.5, 3, 3.5, 4][::-1]
    colors = ['b', 'r', 'g', 'm', 'y', 'c', '#fc9403'][::-1]
    #Plotting the data
    for ax, (title, case_data) in zip(axes.flat, data):
        ax.tick_params(axis='x', which='major', grid_alpha=0, direction='out', labelsize='small', pad=12)
        ax.set_rgrids([0.2, 0.4, 0.6, 0.8], size='small')
        ax.set_title(title.title(), weight='bold' ,size='medium', position=(0.5, 1.15),
                     horizontalalignment='center', verticalalignment='top')
        for d, color, widths in zip(case_data, colors, linewidths):
            ax.plot(theta, d, color=color, linewidth=widths, linestyle=':')
            ax.fill(theta, d, facecolor='#02113A', alpha=0.25)
        ax.set_varlabels(spoke_labels)

        #set legend relative to top right ax
        #ax = axes[0,0]

        #when in for loop adds a legend to all of them
        labels = ('2012', '2014', '2015', '2016', '2017', '2018', '2019')
        legend = ax.legend(labels, loc=(1.20, 0),
                       labelspacing=0.1, fontsize='small')
    #Main title
    fig.text(0.5, 0.965, 'U.S. University\'s Geography Department Affinities',
             horizontalalignment='center', color='black', weight='bold',
             size=20)
    #saves current figure
    fig.savefig('four_universities_radar_chart.png')
    plt.show()
