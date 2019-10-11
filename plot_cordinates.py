"""

# Created on  4/15/2019

# Author: Abhishes Lamsal 

# Purpose: to map the cordinate 


"""
import pandas as pd
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.cm import get_cmap



def plot_latlon_value_map(lats, lons, value=[None],colrange=[0,100], extent=None, resolution='10m', fname='filename.png', save=False):
    rotated_pole = ccrs.RotatedPole(pole_longitude=177.5, pole_latitude=37.5)
    """
    import cartopy.crs as ccrs
    import cartopy.feature as cfeature
    import matplotlib.pyplot as plt
    import pandas as pd

    :param lats: list[float]
    :param lons: list[float]
    :param extent: [-180,180,-90,90]
    :param resolution: string ('10m' or '20m)
    :param fname: name of the file to save with extension 'filename.png'
    :param save: True or False
    :return: None, save automatically.
    """
    proj = ccrs.PlateCarree()
    # ax = plt.axes(projection=ccrs.Mollweide())  # ccrs.Mollweide()  #PlateCarree
    my_dpi = 1000
    # fig = plt.figure(figsize=(2.880, 1.440), dpi=my_dpi)
    ax = plt.axes(projection=proj)
    # ax.coastlines(resolution=resolution)
    # ax.add_feature(cfeature.LAND)
    ax.set_frame_on(False)

    # Create a feature for States/Admin 1 regions at 1:50m from Natural Earth
    states_provinces = cfeature.NaturalEarthFeature(
        category='cultural',
        name='admin_1_states_provinces_lines',
        scale=resolution,
        facecolor='none')

    # ax.add_feature(cfeature.COASTLINE)
    # ax.add_feature(states_provinces, edgecolor='gray')
    if extent == None:
        ax.set_extent([min(lons), max(lons), min(lats), max(lats)])
    else:
        ax.set_extent(extent)
    ax.stock_img()
    if len(value) < 2:
        ax.scatter(lons, lats, color='red', marker='.',
                   transform=proj)
    else:
        # plt.figure(figsize=(1.44,0.72))
        pl = plt.scatter(lons, lats, c=value, vmin=colrange[0], vmax=colrange[1], transform=proj, cmap=get_cmap("jet"))
        # pl=plt.pcolormesh(lons, lats,value,transform=rotated_pole) # Color mesh
        plt.colorbar(pl)
    # cbar=plt.colorbar()
    # cbar.set_label('BBCH')
    if save:
        plt.tight_layout(pad=0)
        plt.savefig(fname, dpi=my_dpi)
        plt.close()
    return

def main():
    Data = pd.read_csv('GrowthStagewithObservations_latlongadded_AL.csv')
    Data = Data[Data.country_code == 'fr']
    extent_eu = None#[-180, 180, -90, 90]
    plot_latlon_map(Data.LAT, Data.LON, extent=extent_eu, fname='filename.png')
    return
if __name__ == "__main__":
    main()
