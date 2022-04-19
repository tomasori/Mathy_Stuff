
import numpy as np

def rotation_matrix(axis, theta):
    """
    Return the rotation matrix associated with counterclockwise rotation about
    the given axis by theta degrees.

    Source: https://stackoverflow.com/questions/6802577/rotation-of-3d-vector
    Source based on: https://en.wikipedia.org/wiki/Euler%E2%80%93Rodrigues_formula

    """
    theta = np.radians(theta)   # convert to radians
    axis = np.asarray(axis)
    axis = axis / np.sqrt(np.dot(axis, axis))
    a = np.cos(theta / 2.0)
    b, c, d = -axis * np.sin(theta / 2.0)
    aa, bb, cc, dd = a * a, b * b, c * c, d * d
    bc, ad, ac, ab, bd, cd = b * c, a * d, a * c, a * b, b * d, c * d
    return np.array([[aa + bb - cc - dd, 2 * (bc + ad), 2 * (bd - ac)],
                     [2 * (bc - ad), aa + cc - bb - dd, 2 * (cd + ab)],
                     [2 * (bd + ac), 2 * (cd - ab), aa + dd - bb - cc]])



v = [10, 0, 0]
axis = [0, 0, 1] # rotate about Z axis
theta = 45  # degrees

# convert to a tuple
tup = tuple(np.dot(rotation_matrix(axis, theta), v))
print(tup)
# expect: (7.071067811865475, 7.0710678118654755, 0.0)



v = [10, 0, 0]
axis = [0, 1, 0]  # rotate about Y axis
theta = 45  # degrees

# convert to a tuple
tup = tuple(np.dot(rotation_matrix(axis, theta), v))
print(tup)
# expect: (7.071067811865475, 0.0, -7.0710678118654755)
