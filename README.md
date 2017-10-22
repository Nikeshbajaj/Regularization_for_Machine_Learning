# Regularization for Machine Learning
#### Contents
* Regularized Least Squares -RLS [Referance](https://en.wikipedia.org/wiki/Regularized_least_squares)
* Nu-Method [Referance]()
* Iterative Landweber Method [Referance](https://en.wikipedia.org/wiki/Landweber_iteration)
* Singular Value Decomposition
* Trunctated SVD [Referance 1](http://arxiv.org/pdf/0909.4061) [Referance 2](http://langvillea.people.cofc.edu/DISSECTION-LAB/Emmie%27sLSI-SVDModule/p5module.html)
* Spectral cut-off

* K-Fold Cross Validation

* Kernal Learning (Linear, Polynomial, Gaussian)
  * Linear ![equation1](http://latex.codecogs.com/gif.latex?%5Clarge%20K%28X%2CY%29%20%3D%20X%5ETY)
  * Polynomail ![equation2](http://latex.codecogs.com/gif.latex?%5Clarge%20K%28X%2CY%29%20%3D%20%28X%5ET%20Y%20+%201%29%5Ep)
  * Gaussian (RBF) ![equation3](http://latex.codecogs.com/gif.latex?%5Clarge%20K%28X%2CY%29%20%3D%20exp%5E%7B-%5Cleft%20%5C%7C%20X-Y%20%5Cright%20%5C%7C%5E2%20/%202%5Csigma%20%5E2%7D)

* K(X,Y) = X^T Y *
* K(X,Y) = (X^T Y + 1)^p *
* K(X,Y) = exp(∥X−Y∥^2/2σ2) *

## GUI
<p align="center">
  <img src="https://raw.githubusercontent.com/Nikeshbajaj/Regularization_for_Machine_Learning/master/GUI_Win_Lin.jpg" width="800"/>
</p>

# Regularization for Machine Learning
---
## Files
1. RegML.py
2. RegML_GUIv2.1.py
3. Getting_Started_Demo.ipynb

## Requirments 
### Following libraries are required to use all the functions in RegML library
1. Python(>=2.7)     
2. Numpy(>=1.10.4)     [Numpy](https://pypi.python.org/pypi/numpy) 
3. Matplotlib(>=0.98)  [Matplotlib](https://github.com/matplotlib/matplotlib) 
4. Scipy(>=0.12)       Optional -(If you need to import .mat data files)  [Scipy](https://www.scipy.org/install.html) 

## Testing
GUI is tested on followwing version of libraries
* Python     2.7     *if you want to use with Python 3, just change all the print command as per python 3*
* Numpy      1.10.4
* Matplotlib 1.15.1
* Scipy      0.17.0

## Getting starting with GUI

### Windows------------------------
After lauching python, go to directory containing RegML.py and RegML_GUIv2.1.py files and run following command on
python shell
```
>> run RegML_GUIv2.1.py
```
If you are using Spyder or ipython qt, browes to directory, open RegML_GUIv2.1.py file and run it

### Ubuntu/Linux-------------------

Open terminal, cd to directory contaning all the files and execute following command
```
$ python RegML_GUIv2.1.py
```

If you are using Spyder or ipython qt, browes to directory, open RegML_GUIv2.1.py file and run it


## Getting Started with DEMO
Getting_Started_Demo is a Ipython -Notebook, which can be open in Ipython-Notebook or Jupyter


______________________

### Nikesh Bajaj

n.bajaj@qmul.ac.uk

nikesh.bajaj@elios.unige.it

[Homepage](http://nikeshbajaj.in)
