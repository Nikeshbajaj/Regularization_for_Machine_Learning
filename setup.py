import setuptools
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

top_dir, _ = os.path.split(os.path.abspath(__file__))

with open(os.path.join(top_dir, 'Version')) as f:
    version = f.readline().strip()

setuptools.setup(
    name="regml",
    version= version,
    author="Nikesh Bajaj",
    author_email="nikkeshbajaj@gmail.com",
    description="Regularization Methods for Machine Learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://nikeshbajaj.github.io/Regularization_for_Machine_Learning/",
    download_url = 'https://github.com/Nikeshbajaj/Regularization_for_Machine_Learning/tarball/' + version,
    packages=setuptools.find_packages(),
    license = 'MIT',
    keywords = 'Regularization methods Machine Learning Regularized Least Squares Nu-Method Iterative Landweber Method Singular Value Decomposition, Kernal Lerning K-Fold',
    classifiers=[
        "Programming Language :: Python :: 3 and 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    install_requires=['numpy>=1.10.4','matplotlib>=0.98','scipy>=0.12']
)
