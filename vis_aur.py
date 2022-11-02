import json
import cartopy.crs as ccrs
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.DataFrame(json.load(open("ovation_aurora_latest.json")))

coor = df['coordinates'].to_list()
coord=np.array(coor)

lons = coord[:,0]
lats =coord[:,1]
z = coord[:,2]

figure=plt.figure()
ax=plt.axes(projection=ccrs.PlateCarree())

cs=ax.tricontourf(lons, lats, z , 
            transform = ccrs.PlateCarree(),cmap='jet',extend='both')

ax.coastlines()

cbar = plt.colorbar(cs)
plt.show()