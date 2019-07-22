# Author:                       Eni Awowale
# Date first written:           June 20, 2019
# Date last updated:            June 27, 2019
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

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, RegularPolygon
from matplotlib.path import Path
from matplotlib.projections.polar import PolarAxes
from matplotlib.projections import register_projection
from matplotlib.spines import Spine
from matplotlib.transforms import Affine2D


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


def example_data():
    #geog_affinities_data = open('affinity_data.txt').readlines()
    data = [
        #below are the program specialities
        ['Human Geography', 'Human Environmental Interactions', 'Physical Geography', 'Geospatial Technologies',
         'Urban and Economic Geography', 'Methods',],
        ('University of Maryland, College Park', [
            [.375, .6666666666666666, 1.0, 1.0,0.14285714285714285,0.42857142857142855,], #this would be specializations for each year
            [0.07, 0.95, 0.04, 0.05, 0.00, 0.97], #year 2
            [0.01, 0.02, 0.85, 0.19, 0.05, 0.10],
            [0.02, 0.01, 0.07, 0.01, 1, 0.12],
            [0.01, 0.01, 0.02, 0.71, 0.74, 0.70]]),
        ('University of Colorado Boulder', [
            [0.625, 0.8333333333333334, 1.0, 1.0, 0.7142857142857143,0.7142857142857143],
            [0.08, 0.94, 0.04, 0.02, 0.00, 0.01],
            [0.01, 0.01, 0.79, 0.10, 0.00, 0.05],
            [0.00, 0.02, 0.03, 0.38, 0.31, 0.31],
            [0.02, 0.02, 0.11, 0.47, 0.69, 0.58]]),
        ('Auburn University', [
            [0.375, 0.3333333333333333, 0.5, 0.6666666666666666, 0.2857142857142857, 0.42857142857142855],
            [0.08, 0.94, 0.04, 0.02, 0.00, 0.01],
            [0.01, 0.01, 0.79, 0.10, 0.00, 0.05],
            [0.00, 0.02, 0.03, 0.38, 0.31, 0.31],
            [0.02, 0.02, 0.11, 0.47, 0.69, 0.58]]),
        ('Arizona State University', [
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [0.07, 0.95, 0.05, 0.04, 0.00, 0.02],
            [0.01, 0.02, 0.86, 0.27, 0.16, 0.19],
            [0.01, 0.03, 0.00, 0.32, 0.29, 0.27],
            [0.02, 0.00, 0.03, 0.37, 0.56, 0.47]]),
        ('University of Alaska', [
            [0.125, 0.16666666666666666, 0.0, 0.3333333333333333, 0.0, 0.0],
            [0.09, 0.95, 0.02, 0.03, 0.00, 0.01],
            [0.01, 0.02, 0.71, 0.24, 0.13, 0.16],
            [0.01, 0.03, 0.00, 0.28, 0.24, 0.23],
            [0.02, 0.00, 0.18, 0.45, 0.64, 0.55]])


    ]
    return data
    #geog_affinities_data.close()

if __name__ == '__main__':
    N = 6
    theta = radar_factory(N, frame='polygon')

    data = example_data()
    spoke_labels = data.pop(0)

    fig, axes = plt.subplots(figsize=(6, 6), nrows=3, ncols=3,
                             subplot_kw=dict(projection='radar'))
    fig.subplots_adjust(wspace=1, hspace=0.40, top=0.85, bottom=0.05)

    colors = ['b', 'r', 'g', 'm', 'y']
    # Plot the four cases from the example data on separate axes
    for ax, (title, case_data) in zip(axes.flat, data):
        ax.set_rgrids([0.2, 0.4, 0.6, 0.8])
        ax.set_title(title, weight='bold', size='medium', position=(0.5, 1.15),
                     horizontalalignment='center', verticalalignment='center')
        for d, color in zip(case_data, colors):
            ax.plot(theta, d, color=color)
            ax.fill(theta, d, facecolor=color, alpha=0.25)
        ax.set_varlabels(spoke_labels)

    # add legend relative to top-left plot
    ax = axes[0, 0]
    labels = ('2012', '2014', '2015', '2016', '2017')
    legend = ax.legend(labels, loc=(1, 0),
                       labelspacing=0.1, fontsize='small')

    fig.text(0.5, 0.965, 'U.S. University\'s Geography Department Affinities',
             horizontalalignment='center', color='black', weight='bold',
             size=22)

    plt.show()


#############################################################################
#
# ------------
#
# References
# """"""""""
#
# The use of the following functions, methods, classes and modules is shown
# in this example:

import matplotlib
matplotlib.path
matplotlib.path.Path
matplotlib.spines
matplotlib.spines.Spine
matplotlib.projections
matplotlib.projections.polar
matplotlib.projections.polar.PolarAxes
matplotlib.projections.register_projection
