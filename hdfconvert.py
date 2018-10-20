import h5py
import pprint
from pyhdf.SD import SD, SDC
import numpy as np

file= SD('test2.hdf', SDC.READ)

print(file.info())

dataset_dic = file.datasets()

for idx, sds in enumerate(dataset_dic.keys()):
        print("{}{}{}".format(idx, ' ', sds))

sds_obj = file.select('Solar_Zenith')

pprint.pprint(sds_obj.attributes())
