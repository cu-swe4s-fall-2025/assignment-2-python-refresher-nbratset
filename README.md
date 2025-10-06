[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/_G_SdF8U)
# print_fires.py
This program reads a given csv file, filters by a value (country) in a specific column (country column), and exports all values from another column (fire column).

# How to use
## General commandline format:
> python print_fires.py -f 'file-name.csv' -c 'value' -cc 'country column' -fc 'fire column'

An actual example:
> python print_fires.py -f 'Agrofood_co2_emission.csv' -c 'United States of America' -cc 'Area' -fc 'Forest fires' -o 'all'

Expected results:
> [54454, 54565, 57469, 54689, 55539, 55641, 57001, 57728, 53453, 50059, 53054, 57860, 55665, 50144, 61980, 61416, 65677, 61160, 59283, 55048, 56536, 53561, 51037, 55433, 53366, 53322, 51375, 50577, 51007, 43785, 40802]

> Mean: 54602.77419354839

> Median: 54689.0

> Standard Deviation: 4881.5765017625035

## Shell Script
You can use **run.sh** instead of commandline to run this script, following the same format as above:
> python print_fires.py -f 'file-name.csv' -c 'value' -cc 'country column' -fc 'fire column' -o 'mean/median/stdev/all' (optional)

# How to install
This program uses python3 and imports the argparse library. 
1. Install python3 either [directly](https://www.python.org/downloads/) or with [anaconda](https://www.anaconda.com/download) (recommended).
2. Install numpy and pycodestyle packages for python:
    > pip install numpy/pycodestyle
    - See environments.yml for version info if your installations don't work correctly.
3. Make sure to have both **my_utils.py**, **print_fires.py**, and **your_file.csv** in your directory. 
4. If running your script with bash, also make sure **run.sh** is installed and modified to match your filenames and arguments.

# Changelog
## 10-06-2025 by Natalie Bratset
### General
 - Implamented automated testing (see .github/workflows/ci_tests.yml)
 - Added environment.yml to handle numpy and pycodestyle packages
 - General tweaks to my_utils.py to correctly handle errors; no major function changes.

## 9-30-2025 by Natalie Bratset
### General
- added src and test directories
    - src: where the python scripts and any data files live
    - test: where functional and unit tests live
- added functional and unit tests in: test/func and test/unit
### my_utils.py
- added mean, median, and standard deviation functions
    - Input: an array
    - Output: single value float with mean, median, or stdev of all elements in array.

### print_fires.py
- added optional commandline argument for operator
    - Usage: -o or --operator
    - Options: mean, median, stdev, or all


## 9-18-2025 by Natalie Bratset
### my_utils.py
- added error handling
- updated string/integer arguments for result_column to work with commandline

### print_fires.py
- added argparse for commandline use
- added program and argument descriptions through argparse

### run.sh
- added 3 example runs, 1 that works and 2 that throw errors

## 9-7-2025 by Natalie Bratset
### my_utils.py
- added get_column() function
- updated get_column() function to handle string or integer arguments for result_column

### print_fires.py
- added import of my_utils.py
- corrected file args to correctly work with my_utils.py

### run.sh
- created .sh file to run print_fires.py
- changed permissions to be executable