# Author:                       Eni Awowale
# Date first written:           June 20, 2019
# Date last updated:            July 23, 2019
# Purpose:                      Create a Radar Chart of University Geography Departments Program Specialities


"""
======================================
Radar chart (aka spider or star chart)
======================================

This example creates a radar chart, also known as a spider or star chart [1]_.

Although this example allows a frame of either 'circle' or 'polygon', polygon
frames don't have proper gridlines (the lines are circles instead of polygons).
It's possible to get a polygon grid by setting GRIDLINE_INTERPOLATION_STEPS in
matplotlib.axis to the desired number of vertices, but the orientation of the
polygon is not aligned with the radial axes.

.. [1] http://en.wikipedia.org/wiki/Radar_chart
"""

import numpy as np
import os
import sys
import ast
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, RegularPolygon
from matplotlib.path import Path
from matplotlib.projections.polar import PolarAxes
from matplotlib.projections import register_projection
from matplotlib.spines import Spine
from matplotlib.transforms import Affine2D
from matplotlib.transforms import Bbox

#folder = r'C:\Users\oawowale\Documents\GitHub\affinities-of-geog-departments'
folder = r'C:\Users\cdony\Google Drive\GitHub\affinities-of-geog-departments'
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

#University program specialties data
data_for_reading = open('final_radar_chart_data.txt').readline()
data_list = ast.literal_eval(data_for_reading)


if __name__ == '__main__':
    N = 6
    theta = radar_factory(N, frame='polygon')

    data = data_list
    spoke_labels = data[0]

    spoke_labels[5] = 'Urban and Economic\n Geography'
    spoke_labels[1] = 'Human-Environmental\n Interactions'
    spoke_labels[2] = 'Physical\n Geography'
    spoke_labels[4] = 'Human\n Geography'
    data = data_list[94]

    #fig, axes = plt.subplots(figsize=(14,12), nrows=2, ncols=2,
    #                         subplot_kw=dict(projection='radar'))
    #fig.subplots_adjust(wspace=0.75, hspace=0.45, top=0.85, bottom=0.05)
    ax = plt.subplot(111, projection='radar')
    #'#fc9403' is color orange
    colors = ['b', 'r', 'g', 'm', 'y', 'c', '#fc9403']

    #Plotting the data
    #for ax, (title, case_data) in zip(axes.flat, data):
    ax.set_rgrids([0.2, 0.4, 0.6, 0.8])
    ax.set_title(data[0].title(), weight='bold', size='medium', position=(0.5, 1.16),
                 horizontalalignment='center', verticalalignment='center')
    for d, color in zip(data[1], colors):
        ax.plot(theta, d, color=color)
        ax.fill(theta, d, facecolor=color, alpha=0.45)
    #I want to increase the spacing but I get an error when I uncomment line 151
    #ax.set_thetagrids(spoke_labels, frac=0.06)
    ax.set_varlabels(spoke_labels)

    # add legend relative to top-left plot
    #ax = axes[0, 0]
    #ax = axes[0,0]
    labels = ('2012', '2014', '2015', '2016', '2017', '2018', '2019')
    legend = ax.legend(labels, loc=(1.15, 0),
                       labelspacing=0.1, fontsize='small')
    #Main title
    #fig.text(0.5, 0.965, 'U.S. University\'s Geography Department Affinities',
    #         horizontalalignment='center', color='black', weight='bold',
    #         size=22)
    ax.set_title('U.S. University\'s Geography Department Affinities',
         horizontalalignment='center', verticalalignment='top')
    plt.tight_layout()
    #saves current figure
    plt.savefig('test_radar_chart.png')
    #extent = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    #fig.savefig('ax2_figure.png', bbox_inches=extent)
    plt.show()

