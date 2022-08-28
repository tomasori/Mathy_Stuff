import numpy as np


def get_2d_intersect(a1, a2, b1, b2):
    """
    Returns the point of intersection of the lines passing through a2,a1 and b2,b1.
    a1: [x, y] 1st point on the first line
    a2: [x, y] 2nd point on the first line
    b1: [x, y] 1st point on the second line
    b2: [x, y] 2nd point on the second line
    """
    s = np.vstack([a1, a2, b1, b2])        # s for stacked
    h = np.hstack((s, np.ones((4, 1))))  # h for homogeneous
    l1 = np.cross(h[0], h[1])           # get first line
    l2 = np.cross(h[2], h[3])           # get second line
    x, y, z = np.cross(l1, l2)          # point of intersection

    if z == 0:                          # lines are parallel
        return (float('inf'), float('inf'))
    return (x/z, y/z)


##########
# Examples
#
print(get_2d_intersection((0, 1), (0,  2), (1, 10), (2, 10)))
print(get_2d_intersection((0, 1), (1,  2), (0, 10), (1,  9)))
print(get_2d_intersection((0, 0), (10, 10), (10, 0), (0, 10)))
# parallel lines so do not intersect.  Will return (inf,inf)
print(get_2d_intersection((0, 1), (0, 2), (1, 10), (1, 9)))  # parallel lines
