from setuptools import setup, find_packages

setup(
    name="analyze-elementary",
    version="0.1.0",
    description="Matatika datasets for the Elementary test results",
    packages=find_packages(),
    package_data={
        "bundle": [
            "analyze/**/*.yml",
            "notebook/*.ipynb",
            "pipelines/*.yml"
        ]
    },
)
