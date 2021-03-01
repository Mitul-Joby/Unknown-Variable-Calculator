'''
MyMath.py is a module containing various functions to calculate operations on shapes 
Format of each function : <SHAPE>_<OPEARATION>_<UNKNOWN>(length,breadth,height,radius,area/volume/csa/tsa)
'''

import math
import cmath

#-------------------TRIANGLE-------------------
#AREA
def TRIANGLE_AREA_BREADTH(l,b,h,r,k):
	return ( 2.0 * float(k) ) / float(h)
def TRIANGLE_AREA_HEIGHT(l,b,h,r,k):
	return ( 2.0 * float(k) ) / float(b)
def TRIANGLE_AREA_AREA(l,b,h,r,k):
	return float(b) * float(h) * 0.5

#-------------------RECTANGLE------------------
#AREA
def RECTANGLE_AREA_LENGTH(l,b,h,r,k):
	return float(k) / float(h)
def RECTANGLE_AREA_BREADTH(l,b,h,r,k):
	return float(k) / float(l)
def RECTANGLE_AREA_AREA(l,b,h,r,k):
	return float(l) * float(h)

#--------------------CIRCLE--------------------
#AREA
def CIRCLE_AREA_RADIUS(l,b,h,r,k):
	return ( float(k) / math.pi )**0.5
def CIRCLE_AREA_AREA(l,b,h,r,k):
	return math.pi * ( float(r)**2.0 )

#---------------------CUBE---------------------
#VOLUME
def CUBE_VOLUME_LENGTH(l,b,h,r,k):
	return float(k)**(1.0/3.0) 
def CUBE_VOLUME_VOLUME(l,b,h,r,k):
	return float(l)**3.0

#LSA
def CUBE_LSA_LENGTH(l,b,h,r,k):
	return ( float(k) / 4.0 )**0.5
def CUBE_LSA_LSA(l,b,h,r,k):
	return 4.0 * (float(l)**2.0)

#TSA
def CUBE_TSA_LENGTH(l,b,h,r,k):
	return ( float(k) / 6.0 )**0.5
def CUBE_TSA_TSA(l,b,h,r,k):
	return 6.0 * (float(l)**2.0)

#--------------------CUBOID---------------------
#VOLUME
def CUBOID_VOLUME_LENGTH(l,b,h,r,k):
	return float(k)/(float(b) * float(h))
def CUBOID_VOLUME_BREADTH(l,b,h,r,k):
	return float(k)/(float(l) * float(h))
def CUBOID_VOLUME_HEIGHT(l,b,h,r,k):
	return float(k)/(float(l) * float(b))
def CUBOID_VOLUME_VOLUME(l,b,h,r,k):
	return float(l) * float(b) * float(h)

#LSA
def CUBOID_LSA_LENGTH(l,b,h,r,k):
	return ( float(k)/(2.0 * float(h)) ) - float(b)
def CUBOID_LSA_BREADTH(l,b,h,r,k):
	return ( float(k)/(2.0 * float(h)) ) - float(l)
def CUBOID_LSA_HEIGHT(l,b,h,r,k):
	return float(k)/(2.0 * (float(l) + float(b)))
def CUBOID_LSA_LSA(l,b,h,r,k):
	return ( 2.0 * float(h) )*(float(l) + float(b))

#TSA
def CUBOID_TSA_LENGTH(l,b,h,r,k):
	return ((float(k)/2.0) - (float(b)*float(h)))/(float(b)+float(h))
def CUBOID_TSA_BREADTH(l,b,h,r,k):
	return ((float(k)/2.0) - (float(l)*float(h)))/(float(l)+float(h))
def CUBOID_TSA_HEIGHT(l,b,h,r,k):
	return ((float(k)/2.0) - (float(l)*float(b)))/(float(l)+float(b))
def CUBOID_TSA_TSA(l,b,h,r,k):
	return 2.0*( (float(l) * float(b)) + (float(b) * float(h)) + (float(l) * float(h)) )

#--------------------SPHERE----------------------

#VOLUME
def SPHERE_VOLUME_RADIUS(l,b,h,r,k):
	return ( (float(k)*3.0) / (4.0 * math.pi) )**(1.0/3.0)
def SPHERE_VOLUME_VOLUME(l,b,h,r,k):
	return (4.0/3.0) * math.pi * (float(r)**3.0)

#TSA
def SPHERE_TSA_RADIUS(l,b,h,r,k):
	return (float(k) / (4.0 * math.pi))**0.5
def SPHERE_TSA_TSA(l,b,h,r,k):
	return 4.0 * math.pi * (float(r)**2.0)

#------------------HEMISPHERE--------------------

#VOLUME
def HEMISPHERE_VOLUME_RADIUS(l,b,h,r,k):
	return ( (float(k)*3.0) / (2.0 * math.pi) )**(1.0/3.0)
def HEMISPHERE_VOLUME_VOLUME(l,b,h,r,k):
	return (2.0/3.0) * math.pi * (float(r)**3.0)

#CSA
def HEMISPHERE_CSA_RADIUS(l,b,h,r,k):
	return (float(k) / (2.0 * math.pi))**0.5
def HEMISPHERE_CSA_CSA(l,b,h,r,k):
	return 2.0 * math.pi * (float(r)**2.0)

#TSA
def HEMISPHERE_TSA_RADIUS(l,b,h,r,k):
	return (float(k) / (3.0 * math.pi))**0.5
def HEMISPHERE_TSA_TSA(l,b,h,r,k):
	return 3.0 * math.pi * (float(r)**2.0)

#--------------------CYLINDER---------------------
#VOLUME
def CYLINDER_VOLUME_RADIUS(l,b,h,r,k):
	return ( float(k) / (math.pi * float(h)) )**0.5
def CYLINDER_VOLUME_HEIGHT(l,b,h,r,k):
	return float(k) / (math.pi * (float(r)**2.0) )
def CYLINDER_VOLUME_VOLUME(l,b,h,r,k):
	return math.pi * (float(r)**2.0) * float(h)

#CSA
def CYLINDER_CSA_RADIUS(l,b,h,r,k):
	return float(k)/(2.0 * math.pi * float(h) )
def CYLINDER_CSA_HEIGHT(l,b,h,r,k):
	return float(k)/(2.0 * math.pi * float(r) )
def CYLINDER_CSA_CSA(l,b,h,r,k):
	return 2.0 * math.pi * float(r) * float(h)

#TSA
def CYLINDER_TSA_RADIUS(l,b,h,r,k):
	return ( ( ((float(h)**2.0) + 2.0 * float(k) / math.pi) **0.5) - float(h) ) / 2.0
def CYLINDER_TSA_HEIGHT(l,b,h,r,k):
	return ( float(k)/(2.0 * math.pi * float(r)) ) - float(r)
def CYLINDER_TSA_TSA(l,b,h,r,k):
	return 2.0 * math.pi * float(r) * (float(r) + float(h))

#----------------------CONE------------------------
#VOLUME
def CONE_VOLUME_RADIUS(l,b,h,r,k):
	return ( (3.0 * float(k)) / (math.pi * float(h)) )**0.5
def CONE_VOLUME_HEIGHT(l,b,h,r,k):
	return (3.0 * float(k)) / (math.pi * (float(r)**2.0) )
def CONE_VOLUME_VOLUME(l,b,h,r,k):
	return (math.pi * (float(r)**2.0) * float(h))/3.0

#CSA
def CONE_CSA_RADIUS(l,b,h,r,k):
	return float(k)/( math.pi* float(l) )
def CONE_CSA_LENGTH(l,b,h,r,k):
	return float(k)/( math.pi* float(r) )
def CONE_CSA_CSA(l,b,h,r,k):
	return math.pi * float(r) * float(l)

#TSA
def CONE_TSA_RADIUS(l,b,h,r,k):
		a=(float(l)**2)+(4*(float(k)/math.pi))
		b=((float(l))*(-1))
		c=(b+cmath.sqrt(a))/2
		return c
def CONE_TSA_LENGTH(l,b,h,r,k):
	return (float(k)/(math.pi * float(r))) - float(r)
def CONE_TSA_TSA(l,b,h,r,k):
	return math.pi * float(r) * (float(r) + float(l) )
