# Authors: Mareike Thies (Pattern Recognition Lab, UK Erlangen), Oliver Aust (ISAS Dortmund)

import h5py
import os
import numpy as np
import nibabel as nib

filelist = os.listdir('/path/to/your/data/')
print(filelist)

for i in range(len(filelist)):
    file = h5py.File('/path/to/your/data/' + filelist[i], 'r')
    print(file.keys())

    raw = np.swapaxes(np.asarray(file['channel0']), 0, 2)		# Note, you might have to adjust 'channel0' to the name of the channel in the h5 that you want to convert - e.g. if the original file in the H5 is called 'raw', change 'channel0' to 'raw'.

    raw = nib.Nifti1Image(raw, affine=None)

    nib.save(raw, '/path/to/your/output_folder/' + filelist[i].rsplit(".", 1)[0] + '.nii.gz')
