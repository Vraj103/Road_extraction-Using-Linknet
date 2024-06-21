Project updates:

2024-06-21
-[] Retrain the model with lesser data and more epochs.
-[] Implement super resolution to better the resolution of senteniel2 data
-[] Find a dataset with coordinates system if possible to make sequential data work well with arcgis.

2024-06-14
- [X] **The bottleneck is about the pararmeters (functions that classifies the pixel) and about emd file.**
- [X] Did you get the output of an image from the training set?
- [X] Did you get the output of an image from the dataset other than test data?
- [ ] Were you able prepare the Sentinel2 dataset for the experimentation
- [X] Did you get the output of an image from the dataset other than test data?
- [ ] Feed the images/tiles to the model in sequential manner for the area under observation

2024-05-31

- [ ] Feed the images/tiles to the model in sequential manner for the area under observation

2024--05-10

- [X] Create the smaller size images/tiles (the size will be equal to the size of the images given during training of the model) for GTA and San Fricisco.
- [X] Create a python script to create images for given size by considering a parameter of sliding window (make sure the names are generated carefully so that you can use them in the next phase)
- [ ] Feed the images/tiles to the model in sequential manner for the area under observation
- [X] Crete a python script that can stich together the images to make a bigger image and then we will convert that bigger image to extract the road network.

2024-05-02
Notes for that week:
- [x] Updated the jupyter notboook with the code performing an automatic road extraction using deep learning.
- [X] Software used: Arcgis pro to process the data and create necessary files needed to support the library arcgis.learn
- [X] Data used: Downloaded the pre-processed and already uploaded data by Spacenet of city paris.
- [X] Python env used: arcgispro3 enviornment provided by ArcgisPro.
- [X] Model used: MultitaskRoadextractor() provided in arcgis.learn (A cnn implemented with U-net architecture)
- [X] A 99.8% accuracy obtained which might be overfitting so looking into new models with new and unprocessed data
    
=============================
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=14949423&assignment_repo_type=AssignmentRepo)
Project Instructions
==============================

This repo contains the instructions for a machine learning project.

Project Organization
------------

    ├── README.md          <- The top-level README for describing highlights for using this ML project.
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention should snake case.
    │
    ├── reports            
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │   └── README.md      <- Youtube Video Link
    │   └── final_project_report <- final report .pdf format and supporting files
    │   └── presentation   <-  final power point presentation 
    |
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
       ├── __init__.py    <- Makes src a Python module
       ├── data
       │   ├── processed      <- The final, canonical data sets for modeling.
       │   └── raw            <- The original, immutable data dump.
       │
       ├── preprocessing_data           <- Scripts to download or generate data and pre-process the data
       │   └── pre-processing.py
       │
       ├── feature_engineering       <- Scripts to turn raw data into features for modeling
       │   └── build_features.py
       │
       ├── models         <- Scripts to train models and then use trained models to make
       │   │                 predictions
       │   ├── predict_model.py
       │   └── train_model.py
       │
       └── visualization  <- Scripts to create exploratory and results oriented visualizations
       │   └── visualize.py  
       │
       └── main.py  <- main script to run all the models and call appropriate functions
       |
       ├── LICENSE  <- LICENSE terms to be included for the use of the source code distribution



