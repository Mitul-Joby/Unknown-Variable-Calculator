'''
MyMath.py is a module containing various functions to calculate operations on shapes 
Format of each function : <SHAPE>_<OPEARATION>_<UNKNOWN>(length,breadth,height,radius,area/volume/csa/tsa)
'''

import math
import cmath

#-------------------TRIANGLE-------------------
#AREA
def TRIANGLE_AREA_BREADTH(l,b,h,r,k):
	try:
		h = float(h)
	except:
		return 'Enter Height'
	try:
		k = float(k)
	except:
		return 'Enter Area'
	try: 
		return ( 2.0 * k ) / h
	except ZeroDivisionError:
		return 'Height cannot be 0'

def TRIANGLE_AREA_HEIGHT(l,b,h,r,k):
	try:
		b = float(b)
	except:
		return 'Enter Base/Breadth'
	try:
		k = float(k)
	except:
		return 'Enter Area'
	try: 
		return ( 2.0 * k ) / b
	except ZeroDivisionError:
		return 'Base/Breadth cannot be 0'
	
def TRIANGLE_AREA_AREA(l,b,h,r,k):
	try:
		b = float(b)
	except:
		return 'Enter Base/Breadth'
	try:
		h = float(h)
	except:
		return 'Enter Height'
	return b * h * 0.5

#-------------------RECTANGLE------------------
#AREA
def RECTANGLE_AREA_LENGTH(l,b,h,r,k):
	try:
		b = float(b)
	except:
		return 'Enter Breadth'
	try:
		k = float(k)
	except:
		return 'Enter Area'
	try: 
		return k / b
	except ZeroDivisionError:
		return 'Breadth cannot be 0'
	
def RECTANGLE_AREA_BREADTH(l,b,h,r,k):
	try:
		l = float(l)
	except:
		return 'Enter Length'
	try:
		k = float(k)
	except:
		return 'Enter Area'
	try: 
		return k / l
	except ZeroDivisionError:
		return 'Length cannot be 0'
	
def RECTANGLE_AREA_AREA(l,b,h,r,k):
	try:
		l = float(l)
	except:
		return 'Enter Length'
	try:
		b = float(b)
	except:
		return 'Enter Breadth'
	return l * b

#--------------------CIRCLE--------------------
#AREA
def CIRCLE_AREA_RADIUS(l,b,h,r,k):
	try:
		k = float(k)
	except:
		return 'Enter Area'
	return ( k / math.pi )**0.5

def CIRCLE_AREA_AREA(l,b,h,r,k):
	try:
		r = float(r)
	except:
		return 'Enter Radius'
	return math.pi * ( r**2.0 )

#---------------------CUBE---------------------
#VOLUME
def CUBE_VOLUME_LENGTH(l,b,h,r,k):
	try:
		k = float(k)
	except:
		return 'Enter Volume'
	return k**(1.0/3.0) 

def CUBE_VOLUME_VOLUME(l,b,h,r,k):
	try:
		l = float(l)
	except:
		return 'Enter Length/Side'
	return l**3.0

#LSA
def CUBE_LSA_LENGTH(l,b,h,r,k):
	try:
		k = float(k)
	except:
		return 'Enter Area'
	return ( k / 4.0 )**0.5

def CUBE_LSA_LSA(l,b,h,r,k):
	try:
		l = float(l)
	except:
		return 'Enter Length/Side'
	return 4.0 * (l**2.0)

#TSA
def CUBE_TSA_LENGTH(l,b,h,r,k):
	try:
		k = float(k)
	except:
		return 'Enter Area'
	return ( k / 6.0 )**0.5

def CUBE_TSA_TSA(l,b,h,r,k):
	try:
		l = float(l)
	except:
		return 'Enter Length/Side'
	return 6.0 * (l**2.0)

#--------------------CUBOID---------------------
#VOLUME
def CUBOID_VOLUME_LENGTH(l,b,h,r,k):
	try:
		b = float(b)
	except:
		return 'Enter Breadth'
	try:
		h = float(h)
	except:
		return 'Enter Height'
	try:
		k = float(k)
	except:
		return 'Enter Volume'
	try:
		return k/(b * h)
	except ZeroDivisionError:
		return 'Breadth/Height cannot be 0'

def CUBOID_VOLUME_BREADTH(l,b,h,r,k):
	try:
		l = float(l)
	except:
		return 'Enter Length'
	try:
		h = float(h)
	except:
		return 'Enter Height'
	try:
		k = float(k)
	except:
		return 'Enter Volume'
	try:
		return k/(l * h)
	except ZeroDivisionError:
		return 'Length/Height cannot be 0'

def CUBOID_VOLUME_HEIGHT(l,b,h,r,k):
	try:
		l = float(l)
	except:
		return 'Enter Length'
	try:
		b = float(b)
	except:
		return 'Enter Breadth'
	try:
		k = float(k)
	except:
		return 'Enter Volume'
	try:
		return k/(l * b)
	except ZeroDivisionError:
		return 'Length/Breadth cannot be 0'

def CUBOID_VOLUME_VOLUME(l,b,h,r,k):
	try:
		l = float(l)
	except:
		return 'Enter Length'
	try:
		b = float(b)
	except:
		return 'Enter Breadth'
	try:
		h = float(h)
	except:
		return 'Enter Height'
	return l * b * h

#LSA
def CUBOID_LSA_LENGTH(l,b,h,r,k):
	try:
		b = float(b)
	except:
		return 'Enter Breadth'
	try:
		h = float(h)
	except:
		return 'Enter Height'
	try:
		k = float(k)
	except:
		return 'Enter Area'
	try:
		return ( k/(2.0 * h) ) - b
	except ZeroDivisionError:
		return 'Height cannot be 0'
		
def CUBOID_LSA_BREADTH(l,b,h,r,k):
	try:
		l = float(l)
	except:
		return 'Enter Length'
	try:
		h = float(h)
	except:
		return 'Enter Height'
	try:
		k = float(k)
	except:
		return 'Enter Area'
	try: 
		return ( k/(2.0 * h) ) - l
	except ZeroDivisionError:
		return 'Height cannot be 0'

def CUBOID_LSA_HEIGHT(l,b,h,r,k):
	try:
		l = float(l)
	except:
		return 'Enter Length'
	try:
		b = float(b)
	except:
		return 'Enter Breadth'
	try:
		k = float(k)
	except:
		return 'Enter Area'
	try:
		return k/(2.0 * (l + b))
	except ZeroDivisionError:
		return 'Length/Breadth cannot be 0'

def CUBOID_LSA_LSA(l,b,h,r,k):
	try:
		l = float(l)
	except:
		return 'Enter Length'
	try:
		b = float(b)
	except:
		return 'Enter Breadth'
	try:
		h = float(h)
	except:
		return 'Enter Height'
	return ( 2.0 * h )*(l + b)

#TSA
def CUBOID_TSA_LENGTH(l,b,h,r,k):
	try:
		b = float(b)
	except:
		return 'Enter Breadth'
	try:
		h = float(h)
	except:
		return 'Enter Height'
	try:
		k = float(k)
	except:
		return 'Enter Area'
	try:
		return ((k/2.0) - (b*h))/(b+h)
	except ZeroDivisionError:
		return 'Breadth/Height cannot be 0'

def CUBOID_TSA_BREADTH(l,b,h,r,k):
	try:
		l = float(l)
	except:
		return 'Enter Length'
	try:
		h = float(h)
	except:
		return 'Enter Height'
	try:
		k = float(k)
	except:
		return 'Enter Area'
	try:
		return ((k/2.0) - (l*h))/(l+h)
	except ZeroDivisionError:
		return 'Length/Height cannot be 0'

def CUBOID_TSA_HEIGHT(l,b,h,r,k):
	try:
		l = float(l)
	except:
		return 'Enter Length'
	try:
		b = float(b)
	except:
		return 'Enter Breadth'
	try:
		k = float(k)
	except:
		return 'Enter Area'
	try:
		return ((k/2.0) - (l*b))/(l+b)
	except ZeroDivisionError:
		return 'Length/Breadth cannot be 0'
	
def CUBOID_TSA_TSA(l,b,h,r,k):
	try:
		l = float(l)
	except:
		return 'Enter Length'
	try:
		b = float(b)
	except:
		return 'Enter Breadth'
	try:
		h = float(h)
	except:
		return 'Enter Height'
	return 2.0*( (l * b) + (b * h) + (l * h) )

#--------------------SPHERE----------------------

#VOLUME
def SPHERE_VOLUME_RADIUS(l,b,h,r,k):
	try:
		k = float(k)
	except:
		return 'Enter Volume'
	return ( (k*3.0) / (4.0 * math.pi) )**(1.0/3.0)

def SPHERE_VOLUME_VOLUME(l,b,h,r,k):
	try:
		r = float(r)
	except:
		return 'Enter Radius'
	return (4.0/3.0) * math.pi * (r**3.0)

#TSA
def SPHERE_TSA_RADIUS(l,b,h,r,k):
	try:
		k = float(k)
	except:
		return 'Enter Area'
	return (k / (4.0 * math.pi))**0.5

def SPHERE_TSA_TSA(l,b,h,r,k):
	try:
		r = float(r)
	except:
		return 'Enter Radius'
	return 4.0 * math.pi * (r**2.0)

#------------------HEMISPHERE--------------------

#VOLUME
def HEMISPHERE_VOLUME_RADIUS(l,b,h,r,k):
	try:
		k = float(k)
	except:
		return 'Enter Volume'
	return ( (k*3.0) / (2.0 * math.pi) )**(1.0/3.0)

def HEMISPHERE_VOLUME_VOLUME(l,b,h,r,k):
	try:
		r = float(r)
	except:
		return 'Enter Radius'
	return (2.0/3.0) * math.pi * (r**3.0)

#CSA
def HEMISPHERE_CSA_RADIUS(l,b,h,r,k):
	try:
		k = float(k)
	except:
		return 'Enter Area'
	return (k / (2.0 * math.pi))**0.5

def HEMISPHERE_CSA_CSA(l,b,h,r,k):
	try:
		r = float(r)
	except:
		return 'Enter Radius'
	return 2.0 * math.pi * (r**2.0)

#TSA
def HEMISPHERE_TSA_RADIUS(l,b,h,r,k):
	try:
		k = float(k)
	except:
		return 'Enter Area'
	return (k / (3.0 * math.pi))**0.5

def HEMISPHERE_TSA_TSA(l,b,h,r,k):
	try:
		r = float(r)
	except:
		return 'Enter Radius'
	return 3.0 * math.pi * (r**2.0)

#--------------------CYLINDER---------------------
#VOLUME
def CYLINDER_VOLUME_RADIUS(l,b,h,r,k):
	try:
		h = float(h)
	except:
		return 'Enter Height'
	try:
		k = float(k)
	except:
		return 'Enter Volume'
	try:
		return ( k / (math.pi * h) )**0.5
	except ZeroDivisionError:
		return 'Height cannot be 0'

def CYLINDER_VOLUME_HEIGHT(l,b,h,r,k):
	try:
		r = float(r)
	except:
		return 'Enter Radius'
	try:
		k = float(k)
	except:
		return 'Enter Volume'
	try:
		return k / (math.pi * (r**2.0) )
	except ZeroDivisionError:
		return 'Radius cannot be 0'

def CYLINDER_VOLUME_VOLUME(l,b,h,r,k):
	try:
		h = float(h)
	except:
		return 'Enter Height'
	try:
		r = float(r)
	except:
		return 'Enter Radius'
	return math.pi * (r**2.0) * h

#CSA
def CYLINDER_CSA_RADIUS(l,b,h,r,k):
	try:
		h = float(h)
	except:
		return 'Enter Height'
	try:
		k = float(k)
	except:
		return 'Enter Area'
	try:
		return k/(2.0 * math.pi * h )
	except ZeroDivisionError:
		return 'Height cannot be 0'

def CYLINDER_CSA_HEIGHT(l,b,h,r,k):
	try:
		r = float(r)
	except:
		return 'Enter Radius'
	try:
		k = float(k)
	except:
		return 'Enter Area'
	try:
		return k/(2.0 * math.pi * r )
	except:
		return 'Radius cannot be 0'

def CYLINDER_CSA_CSA(l,b,h,r,k):
	try:
		h = float(h)
	except:
		return 'Enter Height'
	try:
		r = float(r)
	except:
		return 'Enter Radius'
	return 2.0 * math.pi * r * h

#TSA
def CYLINDER_TSA_RADIUS(l,b,h,r,k):
	try:
		h = float(h)
	except:
		return 'Enter Height'
	try:
		k = float(k)
	except:
		return 'Enter Area'	
	return ( ( ((h**2.0) + 2.0 * k / math.pi) **0.5) - h ) / 2.0

def CYLINDER_TSA_HEIGHT(l,b,h,r,k):
	try:
		r = float(r)
	except:
		return 'Enter Radius'
	try:
		k = float(k)
	except:
		return 'Enter Area'
	try :
		return ( k/(2.0 * math.pi * r) ) - r
	except ZeroDivisionError:
		return 'Radius cannot be 0'
	
def CYLINDER_TSA_TSA(l,b,h,r,k):
	try:
		h = float(h)
	except:
		return 'Enter Height'
	try:
		r = float(r)
	except:
		return 'Enter Radius'
	return 2.0 * math.pi * r * (r + h)

#----------------------CONE------------------------
#VOLUME
def CONE_VOLUME_RADIUS(l,b,h,r,k):
	try:
		h = float(h)
	except:
		return 'Enter Height'
	try:
		k = float(k)
	except:
		return 'Enter Volume'
	try:
		return ( (3.0 * k) / (math.pi * h) )**0.5
	except:
		return 'Height cannot be 0'

def CONE_VOLUME_HEIGHT(l,b,h,r,k):
	try:
		r = float(r)
	except:
		return 'Enter Radius'
	try:
		k = float(k)
	except:
		return 'Enter Volume'
	try:
		return (3.0 * k) / (math.pi * (r**2.0) )
	except ZeroDivisionError:
		return 'Radius cannot be 0'
	
def CONE_VOLUME_VOLUME(l,b,h,r,k):
	try:
		h = float(h)
	except:
		return 'Enter Height'
	try:
		r = float(r)
	except:
		return 'Enter Radius'
	return (math.pi * (r**2.0) * h)/3.0

#CSA
def CONE_CSA_RADIUS(l,b,h,r,k):
	try:
		l = float(l)
	except:
		return 'Enter Slant Length(Length)'
	try:
		k = float(k)
	except:
		return 'Enter Area'
	try:
		return k/( math.pi* l )
	except ZeroDivisionError:
		return 'Slant Length cannot be 0'

def CONE_CSA_LENGTH(l,b,h,r,k):
	try:
		r = float(r)
	except:
		return 'Enter Radius'
	try:
		k = float(k)
	except:
		return 'Enter Area'
	try:
		return k/( math.pi* r )
	except:
		return 'Radius cannot be 0'
	
def CONE_CSA_CSA(l,b,h,r,k):
	try:
		l = float(l)
	except:
		return 'Enter Slant Length (Length)'
	try:
		r = float(r)
	except:
		return 'Enter Radius'
	return math.pi * r * l

#TSA
def CONE_TSA_RADIUS(l,b,h,r,k):
	try:
		l = float(l)
	except:
		return 'Enter Length'
	try:
		k = float(k)
	except:
		return 'Enter Area'
	a=(l**2)+(4*(k/math.pi))
	b=((l)*(-1))
	c=(b+cmath.sqrt(a))/2
	return c

def CONE_TSA_LENGTH(l,b,h,r,k):
	try:
		r = float(r)
	except:
		return 'Enter Radius'
	try:
		k = float(k)
	except:
		return 'Enter Area'
	try:	
		return (k/(math.pi * r)) - r
	except ZeroDivisionError:
		return 'Radius cannot be 0'
	
def CONE_TSA_TSA(l,b,h,r,k):
	try:
		l = float(l)
	except:
		return 'Enter Length'
	try:
		r = float(r)
	except:
		return 'Enter Radius'
	return math.pi * r * (r + l )
