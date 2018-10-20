import h5py

f = h5py.File('test.hdf', 'r')

print(list(f.keys()))