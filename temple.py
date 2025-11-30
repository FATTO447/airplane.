import os 
from pathlib import Path 
import logging 

logging.basicConfig(level=logging.INFO , format ='%(asctime)s - %(levelname)s - %(message)s') 

project_name= "airplane_files" 

folders = [
    "data/raw" , 
    "data/processed" , 
    'notebooks' , 
    "src" , 
    "streamlit_app" , 
    "api" , 
    "models" , 
    "reports/figures" , 
    "tests"
]

list_of_files = {
    ".gitignore" : "data/nmodels/.gitignore\n.env\n__pycache__/\n.ipynb_checkpoints/\n.vscode/\n.DS_Store\n", 
    "README.md" : f"# {project_name} Delay forecasting project end to end forecasting project using pipeline , cleaning , eda , ferature engineering , prophet , shap , streamlit , api " ,
    "requirements.txt" : "" , 
    "setup.py" : f"from setupools import setup , find_packages\n\nsetup(name = '{project_name}' , version = '0.0.1' , author = '' , author_email= '' , packages = find_packages() , install_requires = [] )" , 
    "src/data_cleaning.py" : " # python code for cleaning data" ,
    "src/eda.py" : " #python code for exploratory data analysis" , 
    "src/feature_engineering.py" : "# python code for feature engineering" , 
    "src/pieline.py" : "# python code for pipeline" , 
    "src/model.py" : "# python code for model training" , 
    "src/predict.py" : "# python code for prediction" , 
    "src/prophet_forecasting.py" : "# python code for prophet forecasting" , 
    "src/shap_analysis.py" : "# python code for shap analysis" , 
    "src/streamlit_app.py" : "# python code for streamlit app" , 
    "api/app.py" : "# python code for api using fastapi" , 
    "src/utils.py" : "# python code for utility functions" 
} 

for folder in folders : 
    os.makedirs(os.path.join(project_name , folder) , exist_ok = True) 

for file_path , content in list_of_files.items() : 
    file_path = os.path.join(project_name , file_path) 
    with open(file_path , 'w') as f : 
        f.write(content) 

print("Project structure created successufuly.") 

def main(): 
    import logging 

    logging.basicConfig(level=logging.INFO , format ='%(asctime)s - %(levelname)s - %(message)s')
    logging.info("Project airplane start") 

if __name__ == "__main__": 
    main() 

