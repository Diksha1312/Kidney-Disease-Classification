# Kidney-Disease-Classification
This repository contains code for a kidney disease classification project using machine learning. The project aims to predict kidney disease based on given medical data.
# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/Diksha1312/Kidney-Disease-Classification.git
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n env python=3.8 -y
```

```bash
conda activate env
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```


## MLflow

- [Documentation](https://mlflow.org/docs/latest/index.html)

##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/Diksha1312/Kidney-Disease-Classification.mlflow \
MLFLOW_TRACKING_USERNAME=Diksha1312 \
MLFLOW_TRACKING_PASSWORD=4905255b80b1ead4831d27aa9a4ed88a5a2700d7 \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/Diksha1312/Kidney-Disease-Classification.mlflow

export MLFLOW_TRACKING_USERNAME=Diksha1312 

export MLFLOW_TRACKING_PASSWORD=4905255b80b1ead4831d27aa9a4ed88a5a2700d7

```

### DVC cmd

1. dvc init
2. dvc repro
3. dvc dag
