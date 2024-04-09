# Tibia Cortical Bone Segmentation for µCT and XRM
Documentation and Model of the results presented in the publication "Tibia Cortical Bone Segmentation in Micro-CT and X-ray Microscopy Data Using a Single Neural Network" published in Bildverarbeitung für die Medizin (BVM) conference 2022. This Model was trained on µCT Data of murine tibia samples with a resolution of 8.4µm (isotropic). Unfortunately, we cannot share the training data as some of it is subject to publication.  

# Instructions µCT Data

To use the Model (Model.zip) for your own µCT datasets follow these instructions:

1. Install [nnU-Net V1](https://github.com/MIC-DKFZ/nnUNet/tree/nnunetv1). It is important that you use nnUNet V1, not the newer V2. The model was trained with V1 and is thus only compatible with V1.
2. Download the Model.zip file from this repository.
3. Install the Model with the cmd line:
```
nnUNet_install_pretrained_model_from_zip /your/individual/path/to/Model.zip
```
4. (If performance on your data is poor, remove scale information and convert to 16-bit before running inferrence)
5. Convert your data into .nii.gz file format. You can find a Python script to convert H5 files to .nii.gz (RawsToNiiGz.py) above.
6. Place your files in a new folder and create an output folder.
7. Run: 
```
nnUNet_predict -i PATH_INPUT_FOLDER -o PATH_OUTPUT_FOLDER -tr nnUNetTrainerV2 -ctr nnUNetTrainerV2CascadeFullRes -m 3d_fullres -p nnUNetPlansv2.1 -t Task503_µCTTibiaBVM
```
If the model performs poorly on your data, it might be possible to improve the performance on your data by up or downsampling of your data to simulate a resolution of 8.4µm. Similarly, you could try to adjust your intensity values to more closely resemble that of the training data. Example of a training data histogram:

![grafik](https://user-images.githubusercontent.com/90180771/146957782-899fbe40-e240-4a9d-b7f0-4e45fba9c421.png)


# Instructions XRM Data

To use the Model (Model.zip) for your own µCT datasets follow these instructions. If you already used the model for µCT data you can start from step 4:

1. Install [nnU-Net V1](https://github.com/MIC-DKFZ/nnUNet/tree/nnunetv1). It is important that you use nnUNet V1, not the newer V2. The model was trained with V1 and is thus only compatible with V1.
2. Download the Model.zip file from this repository.
3. Install the Model with the cmd line:
```
nnUNet_install_pretrained_model_from_zip /your/individual/path/to/Model.zip
```
4. Downsample your data with the following formula. Optionally, you can try to use a weaker downsampling factor but this was not tested. We tried to adjust the histogram and other image adjustments to increase the   performance of the model on XRM data but found no improvements.
```
    YourResolution / 8.4 = Downsampling_Factor
```
5. Convert your data into .nii.gz file format. You can find a Python script to convert H5 files to .nii.gz (RawsToNiiGz.py) above.
6. Place your files in a new folder and create an output folder.
7. Run: 
```
nnUNet_predict -i PATH_INPUT_FOLDER -o PATH_OUTPUT_FOLDER -tr nnUNetTrainerV2 -ctr nnUNetTrainerV2CascadeFullRes -m 3d_fullres -p nnUNetPlansv2.1 -t Task503_µCTTibiaBVM
```

# Citation

If you decide to use the model for your research, please cite our paper! You can find the paper under:

Aust, Oliver, et al. "Tibia Cortical Bone Segmentation in Micro-CT and X-ray Microscopy Data Using a Single Neural Network." Bildverarbeitung für die Medizin 2022. Springer Vieweg, Wiesbaden, 2022. 333-338.

Thank you!
