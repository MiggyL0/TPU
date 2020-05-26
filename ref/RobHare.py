import os, sys, math as m, numpy as np

# ASSUMPTIONS
# all units are in feet
# sea floor is flat

# Testing Assumptions
# depth is positive. ergo d = -z
#   Assume a Depth of 10 and a swath with of 120. 
# Our multibeam transducers are note pitched (this can be changed if not true)


# TODO: Import Constants as a shelf object?

# Given Measurements as Shown in Figure 2
theta = m.radians(1)    # beam angle, this is half of the total swath width.
x = 0                   # along-track distance (=0 if the transducer is not pitched)
theta = 60              # 1/2 of our swath width [degrees]
d = 10
r = d / m.cos(m.radians(theta))     # 1/2 of 2-way travel line (geometric range)
print('Assumed Depth is ' + str(d))
print('Range = ' + str(r))

# SOUNDER SYSTEM EQUATIONS

# eq.1 cross-track distance. This is the distance from NADIR to the furthest beam on the seafloor.
y = r * m.sin(theta)
print('Cross Track Distance = ' + str(y) )

R = m.radians(0)        # Roll angle of the body frame (see installation report) 0 for the ewell?
P = m.radians(0)        # Pitch angle of the body frame (see installation report) 0 for the ewell?
alpha = m.radians(0)    # Heading (from north)

# Rotational Reference Frame
# The Local Level Reference Frame is in referenc to the Local Coordinate System and follows a right handed convention
# The Body level is in reference to the body and does not. Roll is in the opposite sign.
# The local-Level vector enables the calculations of 3-dimensional coordinates in the global reference frame using coordinates of the antenna and the coordinate offsets of the antenna from the transducer.

# eq.6 Roll Angle is assumed to be the Euler roll angle.
psi = m.asin((m.sin(R)/m.cos(P))) # TODO: Maybe this would be a good check to make. Add an if statement to check equality.
print('Euler Roll angle = ' + str(psi))

# eq.9 eq.10, and eq.11 Local Level Position (3-dimensional coordinates in the global reference frame)

xLL = -r*m.sin(theta)*(m.cos(alpha)*m.cos(R) + m.sin(alpha)*m.sin(P)*m.sin(R))\
      -r*m.cos(theta)*(m.cos(alpha)*m.sin(R) - m.sin(alpha)*m.sin(P)*m.cos(R))

yLL = r*m.sin(theta)*(m.sin(alpha)*m.cos(R) - m.cos(alpha)*m.sin(P)*m.sin(R))\
    + r*m.cos(theta)*(m.sin(alpha)*m.sin(R) + m.cos(alpha)*m.sin(P)*m.cos(R))

zLL = r*m.sin(theta)*m.cos(P)*m.sin(R) - r*m.cos(theta)*m.cos(P)*m.cos(R)

coordinates = [xLL,yLL,zLL]
print('3D Coordinates in the Global Reference Frame = ' + str(coordinates))

# DEPTHS FROM MBES SYSTEMS










# # measured depth below the transducer
# d = r*m.cos(P)*m.cos(m.radians(theta) + R)
# print('Measured Depth = ' + str(d))








# 36 

# 37 Total Error in Bean Angle
# Where  is beam measurement error
# # Where Sv2 is errors in the sound speed profile
# Sthetam2 = Sthetam2

# # 38 Total Range in Variance
#Sr2 = Srm2 + (rm/vm)^2*Svm2 # eq.36 +eq.37

# # 41 Total Error in Beam Angle
# Stheta2 = Sthetam2 = Sthetav2
# # Sounder measurement variance (range and beam angle):
#Sd1 = float((m.cos(theta**2) * Sr2 + y ** 2 * Stheta2) ** (1/2))
#print(str(Sd1))

# # 2) Depth variance due to beam opening angle: Note, this really should be an approximated equal sign. =~
#Sd2 = ((d(1-m.cos(Psi/2))) ^ 2) ^ (1/2)
# # 3) Roll variance:
# Sd3 = (y ^ 2*S_R ^ 2) ^ (1/2)

# # 4) Pitch variance is assumed to be 0.
Sd4 = (0)**(1/2)
print('Pitch Variance = ' + str(Sd4))

# # 5) Total heave variance:
# Sd5 = (max[a ^ 2, (b*heave) ^ 2 + x ^ 2 S_P ^ 2 + y ^ 2*S_R ^ 2]) ^ (1/2)
# # 6) Refraction variance:
# (Sd6) ^ 2 = (((d/v) ^ 2)+(y ^ 2)((math.tan(theta)/(2*v)) ^ 2+(((math.tan# (theta-delta))/v) ^ 2)))*Sv ^ 2
# # 7) Total depth measurement error:
# Sd = ((Sd1) ^ 2 + (Sd2) ^ 2 + (Sd3) ^ 2 + (Sd4)
#       ^ 2 + (Sd5) ^ 2 + (Sd6) ^ 2) ^ (1/2)
# # 8) Dynamic draught variance:
# (S_dyndrought) ^ 2 = (S_drought) ^ 2 + (S_squat) ^ 2 + (S_load) ^ 2
# # 9) Total reduced depth error:
# S_D = ((Sd ^ 2 + S_dyndrought + S_WL ^ 2)) ^ (1/2)
# # 10) Total radial position error:
# # - [ ] ***[Insert Super Long Equation Here]***
# 1 sounder measurement variance (range and beam angle)

# output
