# Tibia Cortical Bone Segmentation for µCT and XRM
Documentation and Model of the results presented in the publication "Tibia Cortical Bone Segmentation in Micro-CT and X-ray Microscopy Data Using a Single Neural Network" published in Bildverarbeitung für die Medizin (BVM) conference 2022. 


# Instructions

To use the Model (Model.zip) for your own µCT datasets follow these instructions:

1. Install the nnU-Net (https://github.com/MIC-DKFZ/nnUNet)
2. Install the Model with the cmd line " nnUNet_install_pretrained_model_from_zip "
3. Convert your data into .nii.gz file format. Potentially remove pixel sizes and reduce to 16-bit if necessary.
4. Place your files in a new folder and create an output folder.
5. Run: " nnUNet_predict -i PATH_INPUT_FOLDER -o PATH_OUTPUT_FOLDER -tr nnUNetTrainerV2 -ctr nnUNetTrainerV2CascadeFullRes -m 3d_fullres -p nnUNetPlansv2.1 -t Task503_µCTTibiaBVM " Only change "PATH_INPUT_FOLDER" and "PATH_OUTPUT_FOLDER" to their respective paths. 

If you decide to use the model for your research, we would greatly appreciate if you could cite as follows:

TBA
