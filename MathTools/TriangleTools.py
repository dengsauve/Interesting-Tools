#################################
#
#   Title: TriangleTools
#   Objective: Tools to help solve Triangles through Calculus
#   Author: Dennis Sauve
#   Author URI: http://www.github.com/dengsauve
#   Version: 0.1
#
#################################

import math

def prompt(variable):
    return float(input("What is "+variable+": "))

def output_triangle(triangle):
    print("Triangle - Angle A: %3.2f; Angle B: %3.2f; Angle C: %3.2f" % (triangle[0], triangle[1], triangle[2]))
    print("Triangle - Side a: %3.2f; Side b: %3.2f; Side c: %3.2f" % (triangle[3], triangle[4], triangle[5]))

def side_angle_angle(triangle):
    triangle[0] = prompt("Angle A")
    triangle[1] = prompt("Angle B")
    assert (triangle[0] + triangle[1]) < 180.0
    triangle[2] = 180 - (triangle[0] + triangle[1])
    triangle[3] = prompt("Side a")
    triangle[4] = (triangle[3]*math.sin(math.radians(triangle[1])))/math.sin(math.radians(triangle[0]))
    triangle[5] = (triangle[3]*math.sin(math.radians(triangle[2])))/math.sin(math.radians(triangle[0]))
    return triangle

def angle_side_angle(triangle):
    triangle[0] = prompt("Angle A")
    triangle[1] = prompt("Angle B")
    assert (triangle[0] + triangle[1]) < 180.0
    triangle[2] = 180 - (triangle[0] + triangle[1])
    triangle[5] = prompt("Side c")
    triangle[3] = (triangle[5]*math.sin(math.radians(triangle[0])))/math.sin(math.radians(triangle[2]))
    triangle[4] = (triangle[5]*math.sin(math.radians(triangle[1])))/math.sin(math.radians(triangle[2]))
    return triangle




triangle = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
triangle = side_angle_angle(triangle)
output_triangle(triangle)

triangle = angle_side_angle(triangle)
output_triangle(triangle)
