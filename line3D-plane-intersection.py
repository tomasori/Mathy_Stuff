# -------------------------
# Source: https://stackoverflow.com/questions/71223455/3d-line-vector-and-plane-intersection
# -------------------------


from sympy import Plane, Line3D, Point3D
import numpy as np

#plane Points
a1 = Point3D (-100,-100,10)
a2 = Point3D (100,-100,10)
a3 = Point3D (100,100,10)
#line Points
p0 = Point3D (0,0,-50) #point in line
v0 = [0, 1 ,1] #line direction as vector

#create plane and line
plane = Plane(a1,a2,a3)
line = Line3D(p0,direction_ratio=v0)

print(f"plane equation: {plane.equation()}")
print(f"line equation: {line.equation()}")

#find intersection:
intr = plane.intersection(line)

intersection =np.array(intr[0],dtype=float)
print(f"intersection: {intersection}")
print(type(intersection))

x = intersection[0]
y = intersection[1]
z = intersection[2]
print(x,y,z)
