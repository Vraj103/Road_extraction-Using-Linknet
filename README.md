Project updates:

    2024-05-02
    |--Updated the jupyter notboook with the code performing an automatic road extraction using deep learning.
    |--Software used: Arcgis pro to process the data and create necessary files needed to support the library arcgis.learn
    |--Data used: Downloaded the pre-processed and already uploaded data by Spacenet of city paris.
    |--Python env used: arcgispro3 enviornment provided by ArcgisPro.
    |--Model used: MultitaskRoadextractor() provided in arcgis.learn (A cnn implemented with U-net architecture)
    |--A 99.8% accuracy obtained which might be overfitting so looking into new models with new and unprocessed data
    
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



