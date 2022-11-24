#!/usr/bin/env python3

from read_tmqm import read_tmqm_properties
import matplotlib.pyplot as plt

tmqm_properties = read_tmqm_properties('tmQM_y.csv','tmQM_X.xyz')

print("Available properties:",tmqm_properties.dtype.names)

plt.scatter(tmqm_properties["Electronic_E"],\
            tmqm_properties["HL_Gap"],\
            s=-tmqm_properties["Dispersion_E"],\
            c=tmqm_properties["Dipole_M"],\
            alpha=0.3)

plt.ylabel('Dispersion_E')
plt.xlabel('HL_Gap')

plt.show()
