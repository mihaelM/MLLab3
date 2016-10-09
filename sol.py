from labfuns import *
from lab3 import *

X, labels = genBlobs()
mu, sigma = mlParams(X, labels)

print(mu, sigma)