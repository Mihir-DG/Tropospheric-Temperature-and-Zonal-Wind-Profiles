# Tropospheric Temperature And Zonal Wind Profiles

Evaluates tropospheric temperature and zonal wind pressure profiles over a variety of projections. **The final output is displayed in a report (PDF) entitled 'Temperature And Winds In The Troposhere' that can be found in the root directory**. It elaborates on all of the projections discussed in this README, limited to the zonal wind and temperature profiles.

## Directory Structure: ##

 * **./troposphereWinds/**: This looks at both the zonal and meridional wind components and creates identical profiles. It also contains an anomalies section that looks at seasonal deviations from a simplified model that acts as a mean profile.
 * **./temperature/**: Looks at air temperature profiles.
 * **./tempZonal/**: Secondary directory that examines the relationship between zonal wind and air temperature (epitomized by a thermal wind representation). 

Most profiles were evaluated at the 850 mbar and 250 mbar pressure levels, to provide a clearer picture of lower and upper tropospheric dynamics, respectively.

***Projections used:***
1. Longitudinally-averaged latitudinal profiles at various pressure levels.
2. Seasonal (JJA & DJF) profiles for (1)
3. Contour plots and heatmaps for longitudinally-averaged altitude-latitudinal profiles.
4. Equirectangular global profiles
5. Orthographic global profiles.

## Dependencies: ##
All programs were written in Python 2.7, with all packages installed using pip 2.18.0.
1. *netCDF4 v1.5.2*: Read dataset information to numpy arrays.
2. *numpy 1.19.5*: Extracts significant profiles primarily through its array class.
3. *Cartopy 0.19.2*: Creates global basemaps adaptable to various projections.
4. *Matplotlib 3.3.4*: Primary visualization tool.
5. *pathlib 1.0.1*: Internal file handling.
