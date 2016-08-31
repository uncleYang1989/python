import matplotlib.pyplot as plt  
import numpy

fig, ax = plt.subplots()
t = numpy.linspace(0, 10, 100)
print  t
ax.plot(t, numpy.cos(t)*numpy.sin(t))
plt.show()