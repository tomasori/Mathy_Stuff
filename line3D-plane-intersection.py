# -------------------------
# Source: https://stackoverflow.com/questions/71223455/3d-line-vector-and-plane-intersection
# -------------------------

from sympy import Plane, Line3D, Point3D
import numpy as np

def line3D_plane_intersection(pt_on_line, line_dir_vector, plane_joints):

    #plane Points
    a1 = Point3D (plane_joints[0])
    a2 = Point3D (plane_joints[1])
    a3 = Point3D (plane_joints[2])
    #line Points
    p0 = Point3D (pt_on_line) #point in line
    v0 = line_dir_vector #line direction as vector

    #create plane and line
    plane = Plane(a1,a2,a3)
    line = Line3D(p0,direction_ratio=v0)
    # print(f"plane equation: {plane.equation()}")
    # print(f"line equation: {line.equation()}")

    #find intersection:
    intr = plane.intersection(line)
    intersection =np.array(intr[0],dtype=float)
    # print(f"intersection: {intersection}")
    # print(type(intersection))

    # return a list with x, y, and z
    return [intersection[0], intersection[1], intersection[2]]


# define elevation of plane
elev = 10
#plane Points
plane_joints = [[-10000,-10000,elev],
                [10000,-10000,elev],
                [10000,10000,elev]]
#line Points
pt_on_line = [0,0,-50] #point in line
line_dir_vector = [0, 1 ,1] #line direction as vector

print(line3D_plane_intersection(pt_on_line, line_dir_vector, plane_joints))
