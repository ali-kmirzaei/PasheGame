import math
import random

def invertedNormal(x0, x1):
  x0pdf = 1-math.exp(-(x0*x0))
  x1pdf = 1-math.exp(-(x1*x1))
  ymax = max(x0pdf, x1pdf)
  while True:
    x=random.random()*(x1-x0)+x0
    y=random.random()*ymax
    if y < 1-math.exp(-(x*x)):
      return int(x)