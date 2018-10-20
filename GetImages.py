import datetime
import numpy as np

import matplotlib.pyplot as plt

from sentinelhub import WmsRequest, WcsRequest, MimeType, CRS, BBox

INSTANCE_ID = "301131b2-14c0-4797-b938-9b48914ae592" 

def plot_image(image, factor=1):
    """
    Utility function for plotting RGB images.
    """
    fig = plt.subplots(nrows=1, ncols=1, figsize=(15, 7))

    if np.issubdtype(image.dtype, np.floating):
        plt.imshow(np.minimum(image * factor, 1))
    else:
        plt.imshow(image)


coords = [36.541, 31.917, 36.613, 31.887]
bbox = BBox(bbox=coords, crs=CRS.WGS84)

true_color_request = WmsRequest(layer='TRUE-COLOR-S2-L1C',
                                    bbox=bbox,
                                    time='latest',
                                    height=1080,
                                    instance_id=INSTANCE_ID)

wms_true_color_img = true_color_request.get_data()
#print (wms_true_color_img)
#plot_image(wms_true_color_img)
print('Returned data is of type = %s and length %d.' % (type(wms_true_color_img), len(wms_true_color_img)))
print('Single element in the list is of type {} and has shape {}'.format(type(wms_true_color_img[-1]), wms_true_color_img[-1].shape))
#plt.imshow(wms_true_color_img[-1], interpolation='nearest');

from PIL import Image
im = Image.fromarray(wms_true_color_img[-1])
im.save("now.png")