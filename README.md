# Regularization for Machine Learning
#### Contents
* Regularized Least Squares -RLS [Referance](https://en.wikipedia.org/wiki/Regularized_least_squares)
* Nu-Method [Referance]()
* Iterative Landweber Method [Referance](https://en.wikipedia.org/wiki/Landweber_iteration)
* Singular Value Decomposition
* Trunctated SVD [Referance 1](http://arxiv.org/pdf/0909.4061) [Referance 2](http://langvillea.people.cofc.edu/DISSECTION-LAB/Emmie%27sLSI-SVDModule/p5module.html)
* Spectral cut-off

* Kernal Learning
  * Linear     * K(X,Y) = X^T Y * 
  * Polynomial * K(X,Y) = (X^T Y + 1)^p *
  * Gaussian   * K(X,Y) = exp(∥X−Y∥^2/2σ2) *

* K-Fold Cross Validation

![equation](http://latex.codecogs.com/gif.latex?%5CLARGE%20K%28X%2CY%29%20%3D%20X%5ETY)

*$$ K(X,Y) = exp(∥X−Y∥^2/2σ2) Y$$*

![equation](http://latex.codecogs.com/gif.latex?P%28s%20%7C%20O_t%20%29%3D%5Ctext%20%7B%20Probability%20of%20a%20sensor%20reading%20value%20when%20sleep%20onset%20is%20observed%20at%20a%20time%20bin%20%7D%20t)

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
