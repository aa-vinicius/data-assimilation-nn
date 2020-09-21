import math

# 
# Update a matrix grid point (i,j) based on an array of observations (o) 
#
def influence(o,b,i,j):
  R=5.0
  a=0.0
  c=0.0
  e2=0.0
  K=len(o)
  for k in range(0,K):
    r=math.sqrt((i-o[k][0][0])**2+(j-o[k][0][1])**2)
    a+=weight(r,R)*(o[k][1]-b)
    c+=weight(r,R)+e2
  if c!=0:
    b=b+a/c
  return b

#
# Compute the weight of the influence of a grid point located at a distance r
#
def weight(r,R):
  w=0
  if (r>R):
    w=0
  else:
    w=(R**2-r**2)/(R**2+r**2)
  return w
