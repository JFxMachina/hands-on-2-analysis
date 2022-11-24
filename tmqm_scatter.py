#!/usr/bin/env python3

from read_tmqm import read_tmqm_properties
import matplotlib.pyplot as plt

tmqm_properties = read_tmqm_properties('tmQM_y.csv','tmQM_X.xyz')

print("Available properties:",tmqm_properties.dtype.names)

x_prop = "Metal_q"
y_prop = "HOMO_Energy"

plt.scatter(tmqm_properties[x_prop],\
            tmqm_properties[y_prop],\
            s=-tmqm_properties["Dispersion_E"],\
            c=tmqm_properties["Dipole_M"],\
            alpha=0.3)

plt.ylabel(y_prop)
plt.xlabel(x_prop)

plt.show()
