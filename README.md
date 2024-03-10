# Project for the Challenge "AB InBev MLOps Challenge v7"
 
For this challenge, a DIABETES PREDICTION SYSTEM WITH A DEEP NEURONAL NETWORK was developed.

The starting point is a classification model with a neural network that has been trained to predict diabetes.

We will put this system into production using the Streamlit library and Google Cloud.

## THE STEPS TO FOLLOW ARE THOSE:

### 1. Model training


### 2. Production on local server - environment preparation
We create an environment with python 3.10, and install the necessary dependencies.

- conda create venv
- conda activate venv
- conda install python=3.10
- pip install -r requirements.txt

##### The following line must be executed to initialize the project
- streamlit run home.py


### 3. Production on remote server

- Activate an account in google cloud
- Create project in google cloud
- Install GoogleCloudSDK (https://cloud.google.com/sdk/docs/install)
- Run in terminal:
- - gcloud init
- - gcloud app deploy app.yaml --project "Project name"




#### This developed system has been structured in two modes and three steps.

##### MODES
This diabetes prediction system can be developed in two ways:

Individual mode: a form is filled out for each patient.

Batch mode: processing a batch of patients (for this an excel file with example patient information is provided).

The user can choose the above options in the menu on the left.

##### STEPS OF THE PROCESS
STEP 0: In this step the creation of the inputs is done, these are .json files from the inputs folder with the information of each patient, complying with the parameters with which the grading model was trained.

It is worth mentioning that in a production model it is assumed that the inputs come from a previous process, which we simulate in this step, both in individual mode or batch mode the inputs are created.

STEP 1: In this step, the prediction results are obtained using the trained model and the output .json files are created in the outputs folder with the results obtained.

STEP 2: In this step, the results from the outputs folder are loaded and they are displayed.