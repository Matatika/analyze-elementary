from setuptools import setup, find_packages

setup(
    name="app-elementary",
    version="0.1.0",
    description="App Elementary, everything you need to get elementary up and running in your Matatika workspace.",
    packages=find_packages(),
    package_data={
        "bundle": [
            "analyze/channels/*.yml",
            "analyze/datasets/elementary/dashboard/**/*.yml",
            "analyze/datasets/elementary/*.yml",
            "notebook/*.ipynb",
            "pipelines/*.yml"
        ]
    },
)
