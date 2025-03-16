import xarray as xr
import matplotlib.pyplot as plt

for i in range(2):
    ds = xr.open_dataset('run-output/adamselv_v01_0001cold2.nc', decode_times=False).isel(time=i, siglay=0)

    # for k in ds.keys():
    #     print(k)

    fig, axs = plt.subplots(3, 2, figsize=(15, 15))

    # Plot for temp
    sc = axs[0, 0].scatter(ds['x'], ds['y'], c=ds['temp'], cmap='plasma', s=1)
    axs[0, 0].set_title('Temperature')
    axs[0, 0].grid(True)
    fig.colorbar(sc, ax=axs[0, 0], label='temp')

    # Plot for salinity
    sc = axs[0, 1].scatter(ds['x'], ds['y'], c=ds['salinity'], s=1)
    axs[0, 1].set_title('Salinity')
    axs[0, 1].grid(True)
    fig.colorbar(sc, ax=axs[0, 1], label='salinity')

    # Plot for zeta
    sc = axs[1, 0].scatter(ds['x'], ds['y'], c=ds['zeta'], s=1)
    axs[1, 0].set_title('zeta')
    axs[1, 0].grid(True)
    fig.colorbar(sc, ax=axs[1, 0], label='zeta')

    # Plot for h
    sc = axs[1, 1].scatter(ds['x'], ds['y'], c=ds['h'], s=1)
    axs[1, 1].set_title('H')
    axs[1, 1].grid(True)
    fig.colorbar(sc, ax=axs[1, 1], label='h')

    # Plot for u
    sc = axs[2, 0].scatter(ds['xc'], ds['yc'], c=ds['ua'], s=1)
    axs[2, 0].set_title('ua')
    axs[2, 0].grid(True)
    fig.colorbar(sc, ax=axs[2, 0], label='ua')

    # Plot for v
    sc = axs[2, 1].scatter(ds['xc'], ds['yc'], c=ds['va'], s=1)
    axs[2, 1].set_title('va')
    axs[2, 1].grid(True)
    fig.colorbar(sc, ax=axs[2, 1], label='va') 

    plt.tight_layout()
    plt.savefig(f'cold_output_{i}.png', dpi=300, bbox_inches='tight') 