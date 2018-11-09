import numpy as np
import datetime
from sentinelhub import WmsRequest, CRS, BBox
from PIL import Image
import os
import sys 

INSTANCE_ID = "301131b2-14c0-4797-b938-9b48914ae592" 
IMAGE_TYPE = ["TRUE-COLOR-S2-L1C", "NDWI", "NDVI"]
PATH_TYPE = ["Main", "Water", "Vegetation"]

def downloadImage(name,  coord, type = 0, date = "latest", width = 1920):

    #TODO get coord by name

    coords = [coord[1]-0.053,coord[0]+0.03,coord[1]+0.053,coord[0]-0.03]

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
#downloadImage("NOME_SETTLEMENT",coord = [31.9, 36.58])

coords = [92.13, 21.218, 92.172, 21.18]

bbox = BBox(bbox=coords, crs=CRS.WGS84)

true_color_request = WmsRequest(layer=IMAGE_TYPE[2],
                                        bbox=bbox,
                                        data_folder='test_dir/up2/NDVI',
                                        time=("2012-01-01","2018-12-31"), 
                                        width=1920,
                                        maxcc=0.2,
                                        instance_id=INSTANCE_ID)

true_color_request.save_data()
    