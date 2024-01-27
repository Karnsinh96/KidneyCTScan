# KidneyCTScan

# To Activate venv:- venv\Scripts\activate


#Project WorkFlow
Update config.yaml
Update secrets.yaml [Optional]
Update params.yaml
Update the entity
Update the configuration manager in src config
Update the components
Update the pipeline
Update the main.py
Update the dvc.yaml
app.py


#MLFlow
os.environ['MLFLOW_TRACKING_URI']='https://dagshub.com/Karnsinh96/KidneyCTScan.mlflow'
os.environ['MLFLOW_TRACKING_USERNAME']='Karnsinh96'
os.environ['MLFLOW_TRACKING_PASSWORD']='49dfbacbbe38354686de7ff25de3cc5069a5405b'

 

export MLFLOW_TRACKING_URI=https://dagshub.com/Karnsinh96/KidneyCTScan.mlflow
export MLFLOW_TRACKING_USERNAME=Karnsinh96
export MLFLOW_TRACKING_PASSWORD=49dfbacbbe38354686de7ff25de3cc5069a5405b
python script.py