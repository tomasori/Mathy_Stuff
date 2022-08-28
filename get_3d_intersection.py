# need:  pip install scikit-spatial

from skspatial.objects import Line
from skspatial.plotting import plot_3d
import matplotlib.pyplot as plt


def get_3d_intersection(pt1, pt2, vec1, vec2, show_plot=False):
    line_a = Line(point=pt1, direction=vec1)
    line_b = Line(point=pt2, direction=vec2)
    pt_intersect = line_a.intersect_line(line_b)
    if show_plot:
        plot_3d(line_a.plotter(), line_b.plotter(),
                pt_intersect.plotter(c='k', s=75))
        plt.show()
    return pt_intersect


# Example 1
pt1 = [-26.000, -17.333, -200.00]
pt2 = [22.850, -17.333, -137.00]
pt3 = [26.000, -17.333, -200.00]
pt4 = [-22.850, -17.333, -137.00]
v12 = [pt2[0]-pt1[0], pt2[1]-pt1[1], pt2[2]-pt1[2]]
v34 = [pt4[0]-pt3[0], pt4[1]-pt3[1], pt4[2]-pt3[2]]
pt_intersect = get_3d_intersection(pt1, pt3, v12, v34)
print("Face 12 intersection: ({:.3f}, {:.3f}, {:.3f})".format(
    pt_intersect[0], pt_intersect[1], pt_intersect[2]))

# Example 2
pt1 = [26.000, -17.333, -200.00]
pt2 = [0.000, 28.367, -137.00]
pt3 = [0.000, 34.667, -200.00]
pt4 = [22.850, -17.333, -137.00]
v12 = [pt2[0]-pt1[0], pt2[1]-pt1[1], pt2[2]-pt1[2]]
v34 = [pt4[0]-pt3[0], pt4[1]-pt3[1], pt4[2]-pt3[2]]
pt_intersect = get_3d_intersection(pt1, pt3, v12, v34)
print("Face 23 intersection: ({:.3f}, {:.3f}, {:.3f})".format(
    pt_intersect[0], pt_intersect[1], pt_intersect[2]))

# Example 3
pt1 = [0.000,  34.667, -200.00]
pt2 = [-22.850, -17.333, -137.00]
pt3 = [-26.000, -17.333, -200.00]
pt4 = [0.000, 28.367, -137.00]
v12 = [pt2[0]-pt1[0], pt2[1]-pt1[1], pt2[2]-pt1[2]]
v34 = [pt4[0]-pt3[0], pt4[1]-pt3[1], pt4[2]-pt3[2]]
pt_intersect = get_3d_intersection(pt1, pt3, v12, v34)
print("Face 31 intersection: ({:.3f}, {:.3f}, {:.3f})".format(
    pt_intersect[0], pt_intersect[1], pt_intersect[2]))
