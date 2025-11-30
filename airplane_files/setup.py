from setupools import setup , find_packages


setup( 
    name="my_airplane",
    version="0.1.0",
    packages=find_packages(),  
    install_requires=[
        "pandas",  
        "numpy", 
        "fastapi",
        "streamlit",
        "prophet",
        "shap",
        "uvicorn"
        "matplotlib",
        "scikit-learn",
        "seaborn"
        "pipelines"
    ],
    entry_points={
        "console_scripts": [
            "run-airplane=temple:main",  
        ],
    },
    author="Fatma Badawy",
    author_email="fbadawy298@gmail.com" , 
    description="My Airplane Python Project",
    python_requires=">=3.8",
)


