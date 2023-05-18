import rasterio
import matplotlib.pyplot as plt

with rasterio.open('./data/USGS_1_n36w098_20171218.tif') as src:
    data = src.read(1)

plt.imshow(data[:1000, :1000], cmap='gray')
plt.show()

