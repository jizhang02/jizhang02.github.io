---
layout:     post
title:      "MMs Cardiac Dataset with only ED and ES"
subtitle:   "心脏数据集"
date:       2022-02-17
author:     "Jing"
header-img: "img/post-bg.jpg"
tags:
    - Medical Imaging

---

# MMs-Cardiac-Dataset-with-only-ED-and-ES

MMs Cardiac Dataset with only ED (end-diastole) and ES (end of systole). The ground truth is labeled cardiac and the volume of each cardiac structure.

---
### Motivation
This dataset is adpated from [Multi-Centre, Multi-Vendor & Multi-Disease
Cardiac Image Segmentation Challenge (M&Ms)](https://www.ub.edu/mnms/). The compressed original dataset has 14.3 GB. The shape of each subject/cardiac is (n, z, y, x).    
n: number of frames;    
z: number of slices;    
x,y: 2D size.    
This repo aims to share a preprocessed dataset that only has ED and ES frame. Besides, the volume of each cardiac structure (RV, MYO, LV) is given in the file.

---
### Method
#### ED and ES extraction
The ED and ES number are given in the original CSV file.
```
def ExtractPhase(ed=5, es=5, subject=None, ED=None, ES=None):

    itk_img = sitk.ReadImage(subject)
    img = sitk.GetArrayFromImage(itk_img)
    print('The shape of this subject:', img.shape)  # frames, slices, y,x

    for i in range(img.shape[0]):
        if i == ed:
            img_ed = sitk.GetImageFromArray(img[i])
            sitk.WriteImage(img_ed, ED)
        if i == es:
            img_es = sitk.GetImageFromArray(img[i])
            sitk.WriteImage(img_es, ES)
```
#### Volume calculation

``` 
def VolumeStat(image_path):    

    imagelist = sorted(glob.glob(os.path.join(image_path, '*.nii.gz')))    
  
    for i in range(len(imagelist)):    
        itk_img = sitk.ReadImage(imagelist[i])    
        img = sitk.GetArrayFromImage(itk_img)    
        pixel_count_BKG = 0    
        pixel_count_LV = 0    
        pixel_count_MYO = 0    
        pixel_count_RV = 0    
        LV = 1    
        MYO = 2    
        RV = 3    
        for k in range(img.shape[0]):    
            pixel_count_RV += (img[k] == RV).sum()     
            pixel_count_MYO += (img[k] == MYO).sum()    
            pixel_count_LV += (img[k] == LV).sum()     
```

pixel number convert to volume (milliter)    
`Vol_RV = pixelsize_x*pixelsize_y*pixelsize_z*pixel_count_RV/1000`    
The pixelsize can be obtained by `itk_img.GetSpacing()`

---
### Download
You can download the preprocessed data from the link below:    
[Dropbox](https://www.dropbox.com/s/ywz2oruzgqvbaza/M%26Ms_EDES.zip?dl=0)    

