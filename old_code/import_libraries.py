# Import libraries

### Task 1: ####

# For data analysis
import pandas as pd 
print("Imported 'pandas' as 'pd'.")    
import numpy as np
print("Imported 'numpy' as 'np'.")    

# For searching within strings etc.
import regex as re
print("Imported 'regex' as 're'.")    

# For dates/times
from datetime import datetime
print("Imported 'datetime' from 'datetime'.")

# To safely save lob strings as Python objects
import ast
print("Imported 'ast'.")

### Task 2: ####

# We will use matplotlib to plot our charts
import matplotlib.pyplot as plt
print("Imported 'matplotlib.pyplot' as 'plt'.")

# For the animated chart
from matplotlib.animation import FuncAnimation
print("Imported 'FuncAnimation' from 'matplotlib.animation'.")

# To display the animated chart
from IPython.display import HTML
print("Imported 'HTML' from 'IPython.display'.")

### Task 3: ###

# For regressions
from patsy import dmatrices  
print("Imported 'patsy' from 'dmatrices'.")

import statsmodels.api as sm    
print("Imported 'statsmodels.api' as 'sm'.")

import statsmodels.formula.api as smf  
print("Imported 'statsmodels.formula.api' as 'smf'.")

from statsmodels.stats.diagnostic import het_white
print("Imported 'het_white' from 'statsmodels.stats.diagnostic'.")


