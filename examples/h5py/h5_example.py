import numpy as np
import h5py


a = np.arange(1000, dtype=np.float64).reshape(25, 40)

with h5py.File("test.h5", "w") as f:
    
    # attributes are meta-data that can help describe the data
    # in h5py, they are dictionary keys
    f.attrs["about"] = "a test HDF5 file with h5py"

    # groups can be thought of as subdirectories in the output file,
    # and can help you organize data together logically
    grp = f.create_group("data")
    
    # a numpy array is a dataset in HDF5 -- it will figure out the
    # dimensions and type from the array itself
    grp.create_dataset("a", data=a)

    # there can be attributes in the group too
    grp.attrs["array info"] = "a simple array"


# now we'll try to read it in
with h5py.File("test.h5", "r") as f:

    # access the group we stored our data in
    g = f["data"]

    aread = np.array(g["a"])


# are they the same?
da = a - aread
print(np.max(abs(da)))
