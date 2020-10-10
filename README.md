# Assignment-2
#### In this project I have made an python library and published it on pypi.
#### This library gives you the the functionality to plot the graph between any two numeric value columns of your google sheet.

### How to pubish library on pypi:

1) Firstly create a directory and make a __init__.py file inside it and define the methods you want in your library through this you can directly access this 
method wherever you import.

2) After doing this you have to made 5 files :
  1) LICENSE.txt : This file will contain the license of your library belongs in my case I have used MIT license.
  2) CHANGELOG.txt : In this file you can mention version of your library and its updates.
  3) MANIFEST.in : This will contain the information regarding what file will be included like .txt and .py
  4) README.txt : This will contain the information regarding the methods and class and functionality of our library and its uses cases.
  5) setup.py : This is the most important file which sets up the platform for our library. It contain name of our library, which others libraries are required to run our library
  smoothly.
  
3) Now to publish your library on pypi first you should have a pypi account.

4) After that run the following commands from the same directory where you have you setup.py file.
i) python setup.py sdist
ii) twine upload --repository-url https://upload.pypi.org/legacy/ dist/* 
After running the (ii) command it will ask you for pypi username and password so keep them handly. And at last it will provide you the link of your pypi library.

After completing the above process you can install your library using pip command.


### How to install my library:

You can see my library documents here https://pypi.org/project/plotmygsheet/

### To install just write the following command in the command line :
pip install plotmygsheet

### You can initilize plotmygsheet library by following line :
from plotmygsheet import *

After intilializing you can make use of the function like : get_all_columns(url), plot_graph(url,column1,column2,path=”assets”)

#### get_all_columns(url) : 

this will return the list of all the columns name form your google sheet.

#### plot_graph(url,column1,column2,path=”assets”) : 
this method will plot the graph and save in "assets" directory make sure you have "assests" directory already present.

I have used django to make it use case: 

In my apps views.py I have import plotmysheet library and used both of the above methods.




