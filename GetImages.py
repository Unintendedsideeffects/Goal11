import numpy as np
import datetime
from sentinelhub import WmsRequest, CRS, BBox
from PIL import Image
import os
import sys 

INSTANCE_ID = "301131b2-14c0-4797-b938-9b48914ae592" 
IMAGE_TYPE = ["TRUE-COLOR-S2-L1C", "NDWI", "NDVI"]
PATH_TYPE = ["Main", "Water", "Vegetation"]

def downloadImage(name,  coords, type = 0, date = "latest", width = 1920):

    #TODO get coord by name

    bbox = BBox(bbox=coords, crs=CRS.WGS84)

    true_color_request = WmsRequest(layer=IMAGE_TYPE[type],
                                        bbox=bbox,
                                        time=date, 
                                        width=width,
                                        maxcc=0.2,
                                        instance_id=INSTANCE_ID)

    wms_true_color_img = true_color_request.get_data()

    im = Image.fromarray(wms_true_color_img[-1])
    path =  "./" + str(name) + "/" + PATH_TYPE[type] 
    if (not os.path.isdir(path)):    
        os.makedirs(path)
    path = path + "/" + str(date) + ".png" 
    im.save(path, 'PNG')
    return path

#test
downloadImage("NOME_SETTLEMENT",coords = [36.541, 31.917, 36.613, 31.887])
