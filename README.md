# Regularization methods for machine learning
### These contents were taugh in summer school [**RegML 2016**](http://lcsl.mit.edu/courses/regml/regml2016/) by [Lorenzo Rosasco](http://web.mit.edu/lrosasco/www/) and this GUI in python was submitted as part of final exam.

[![DOI](https://zenodo.org/badge/107844831.svg)](https://zenodo.org/badge/latestdoi/107844831)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version fury.io](https://badge.fury.io/py/regml.svg)](https://pypi.org/project/regml/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/regml.svg)](https://pypi.python.org/pypi/regml/)
[![GitHub release](https://img.shields.io/github/release/nikeshbajaj/Regularization_for_Machine_Learning.svg)](https://github.com/Nikeshbajaj/Regularization_for_Machine_Learning/releases/)
[![PyPI format](https://img.shields.io/pypi/format/regml.svg)](https://pypi.python.org/pypi/regml/)
[![PyPI implementation](https://img.shields.io/pypi/implementation/regml.svg)](https://pypi.python.org/pypi/regml/)
[![HitCount](http://hits.dwyl.io/nikeshbajaj/regml.svg)](http://hits.dwyl.io/nikeshbajaj/regml)
![GitHub commit activity](https://img.shields.io/github/commit-activity/y/nikeshbajaj/Regularization_for_Machine_Learning?style=plastic)
[![Percentage of issues still open](http://isitmaintained.com/badge/open/nikeshbajaj/Regularization_for_Machine_Learning.svg)](http://isitmaintained.com/project/nikeshbajaj/Regularization_for_Machine_Learning "Percentage of issues still open")


[![PyPI download month](https://img.shields.io/pypi/dm/regml.svg)](https://pypi.org/project/regml/)
[![PyPI download week](https://img.shields.io/pypi/dw/regml.svg)](https://pypi.org/project/regml/)

[![Generic badge](https://img.shields.io/badge/pip%20install-regml-blue.svg)](https://pypi.org/project/regml/)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](mailto:n.bajaj@qmul.ac.uk)

![PyPI - Downloads](https://img.shields.io/pypi/dm/regml?style=social)

Total: [![PyPI download total](https://static.pepy.tech/personalized-badge/regml?period=total&units=international_system&left_color=black&right_color=orange&left_text=downloads)](https://pepy.tech/project/regml)

#### All the coded and tested functions are in [RegML.py](https://github.com/Nikeshbajaj/Regularization_for_Machine_Learning/blob/master/RegML.py) and GUIs code structure is in [RegML_GUIv2.1.py](https://github.com/Nikeshbajaj/Regularization_for_Machine_Learning/blob/master/RegML_GUIv2.1.py)

## [Github Page](https://nikeshbajaj.github.io/Regularization_for_Machine_Learning/)
## [PyPi -project](https://pypi.org/project/regml/)

## Installation
```
pip install regml
```

## Opening GUI:

```
import regml
regml.GUI()

```


### Regularization Methods
* Regularized Least Squares -RLS [Referance](https://en.wikipedia.org/wiki/Regularized_least_squares)
* Nu-Method [Referance]()
* Iterative Landweber Method [Referance](https://en.wikipedia.org/wiki/Landweber_iteration)
* Singular Value Decomposition [Reference](https://en.wikipedia.org/wiki/Singular-value_decomposition)
* Trunctated SVD [Referance 1](http://arxiv.org/pdf/0909.4061) [Referance 2](http://langvillea.people.cofc.edu/DISSECTION-LAB/Emmie%27sLSI-SVDModule/p5module.html)
* Spectral cut-off

### Kernal Learning 
(Linear, Polynomial, Gaussian)
* **Linear**: $K(X,Y) = X'Y$ 
  * ![equation1](http://latex.codecogs.com/gif.latex?%5Clarge%20K%28X%2CY%29%20%3D%20X%5ETY)
* **Polynomial**: $K(X,Y) = (X'Y +1)^p$ 
  * ![equation2](http://latex.codecogs.com/gif.latex?%5Clarge%20K%28X%2CY%29%20%3D%20%28X%5ET%20Y%20+%201%29%5Ep)
* **Gaussian (RBF)**: $K(X,Y) = exp(-||X-Y||^2/2\sigma^2)$ 
  * ![equation3](https://latex.codecogs.com/gif.latex?K%28X%2CY%29%20%3D%20exp%28-%7C%7CX-Y%7C%7C%5E2/2%5Csigma%5E2%29)
  

### **K-Fold Cross Validation**

## GUI
<p align="center">
  <img src="https://raw.githubusercontent.com/Nikeshbajaj/Regularization_for_Machine_Learning/master/images/GUI_Win_Lin.jpg" width="800"/>
</p>

# Regularization for Machine Learning
---
## Files
1. RegML.py
2. RegML_GUIv2.1.py
3. Getting_Started_Demo.ipynb

## Requirments 
### Following libraries are required to use all the functions in RegML library
1. Python(=2.7)     
2. Numpy(>=1.10.4)     [Numpy](https://pypi.python.org/pypi/numpy) 
3. Matplotlib(>=0.98)  [Matplotlib](https://github.com/matplotlib/matplotlib) 
4. Scipy(>=0.12)       Optional -(If you need to import .mat data files)  [Scipy](https://www.scipy.org/install.html) 

## Tested with following version
GUI is tested on followwing version of libraries
* Python     2.7 / 3 
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
if you have both python 2 and python 3

```
$ python2 RegML_GUIv2.1.py
```

If you are using Spyder or ipython qt, browes to directory, open RegML_GUIv2.1.py file and run it


## Getting Started with DEMO
Getting_Started_Demo is a IPython -Notebook, which can be open in Ipython-Notebook or Jupyter

# [**Notebook**](https://github.com/Nikeshbajaj/Regularization_for_Machine_Learning/blob/master/Getting_Started_Demo.ipynb)


# [**RegML Library**](https://github.com/Nikeshbajaj/Regularization_for_Machine_Learning/blob/master/RegML.py)

______________________

# Cite As
```
@software{nikesh_bajaj_2019_2646550,
  author       = {Nikesh Bajaj},
  title        = {{Nikeshbajaj/Regularization\_for\_Machine\_Learning 
                   0.0.2}},
  month        = apr,
  year         = 2019,
  publisher    = {Zenodo},
  version      = {0.0.2},
  doi          = {10.5281/zenodo.2646550},
  url          = {https://doi.org/10.5281/zenodo.2646550}
}
```


### Nikesh Bajaj

n.bajaj@qmul.ac.uk

nikesh.bajaj@elios.unige.it

[http://nikeshbajaj.in](http://nikeshbajaj.in)
