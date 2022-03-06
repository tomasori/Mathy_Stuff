import numpy as np

def rotate_2d(p, origin=(0, 0), degrees=0):
    ''' p = point or points to rotate provided in a list of tuples (x,y)
        origin = well, it's the origin
        degrees = angle to rotate COUNTERCLOCK in a 2D plane.
                  use negative angle to rotate clockwise.

        Function returns a list of tuples

        Wode tweaked using the following source:
        https://stackoverflow.com/questions/34372480/rotate-point-about-another-point-in-degrees-python
    '''
    jt_qty = len(p)
    angle = np.deg2rad(degrees)
    R = np.array([[np.cos(angle), -np.sin(angle)],
                  [np.sin(angle),  np.cos(angle)]])
    o = np.atleast_2d(origin)
    p = np.atleast_2d(p)
    # np.squeeze returns an np_ndarray
    a = np.squeeze((R @ (p.T-o.T) + o.T).T)
    # convert np_ndarray to a python list with tuples if more than one joint
    # otherwise, just convert to a tuple and add to a list
    if jt_qty > 1:
        p_list = list(map(tuple, a))
    else:
        tup = tuple(a)
        p_list = [tup]
    return p_list


# try multiple points in a list
points=[(20, 30), (10, 0)]
origin=(0,0)
rot_angle = 45

new_points = rotate_2d(points, origin, rot_angle)
for point in new_points:
    print(point)

print("---------")

# try only one point
points= [(7.07106781187, 7.07106781187)]
origin=(0,0)
rot_angle = 45

new_points = rotate_2d(points, origin, rot_angle)
for point in new_points:
    print(point)
