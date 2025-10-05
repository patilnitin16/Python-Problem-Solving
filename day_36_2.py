'''
ABC is a right-angled triangle with the right angle at B.

The lengths of the two perpendicular sides AB and BC are given.

Let M be the midpoint of the hypotenuse AC.

You need to find the measure of ∠MBC (the angle formed at vertex B between line segments BM and BC) in degrees.

'''

#Code
import math

AB = int(input())
BC = int(input())

BMx, BMy = BC/2, AB/2   
BCx, BCy = BC, 0            

dot = BMx*BCx + BMy*BCy     
BM_len = math.hypot(BMx,BMy)
BC_len = math.hypot(BCx,BCy)

theta = math.degrees(math.acos(dot / (BM_len * BC_len)))
print(f"{round(theta)}\u00B0")