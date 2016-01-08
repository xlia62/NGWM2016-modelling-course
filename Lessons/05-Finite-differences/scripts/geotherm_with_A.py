import numpy as np
import matplotlib.pyplot as plt

# Finite difference code to solve the steady state geotherm
# given the boundary condition T=T_surf and the surface
# heatflow q



z_surf = 0.0  # location of upper surface
z_bott = 50e3 # location of bottom boundary

nz = 10        # number of grid points

T_surf = 0.0     # temperature of the upper surface, deg C
q_surf = 60e-3  # surface heat flow, mW/m^2
k = 2.5          # heat conductivity, W/mK
A = 1.1e-6       # radiogenic volumetric heat generation, W/m^3



# Generate the grid
# Regular grid is used, so that in FD calculations
# only dz is needed. Array z is used only for plotting.
dz = (z_bott - z_surf) / (nz - 1)
z = np.zeros(nz)

for i in range(0, nz):
  z[i] = z_surf + i*dz

print("Grid points are:")
print(z)

# Generate an empty array for temperature values
T = np.zeros(nz)



# Set boundary conditions, i.e. the upper surface temperature
T[0] = T_surf

## Grid point one needs special handling as T[-1] is not available
# Calculate "ghost point" outside the model domain, where grid point -1 
# would be, assuming surface heat flow q_surf
Tghost = T[0] - q_surf * dz / k  # = "T[-1]"
# Use the same finite difference formula to calculate T as for 
# the inner points, but replace "T[-1]" by ghost point value
T[1] = ????

# Calculate temperature values inside the model
for i in range(2, nz):   # NB! Grid points 0 and 1 omitted
  T[i] = ????


# Print and plot the depth vs temperature
print("Temperature values are:")
print(T)
plt.plot(T, -z, "o-b")  # minus sign is placed to make z axis point down
plt.xlabel("Temperature")
plt.ylabel("Depth")
plt.show()


