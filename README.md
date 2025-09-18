[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/_G_SdF8U)
# print_fires.py
This program reads a given csv file, filters by a value (country) in a specific column (country column), and exports all values from another column (fire column).

# How to use
## General commandline format:
> python print_fires.py -f 'file-name.csv' -c 'value' -cc 'country column' -fc 'fire column'

An actual example:
> python print_fires.py -f 'Agrofood_co2_emission.csv' -c 'United States of America' -cc 'Area' -fc 'Forest fires'

Expected result:
> ['54454.7092', '54565.6091', '57469.9273', '54689.318', '55539.8937', '55641.1573', '57001.184', '57728.8676', '53453.6536', '50059.8887', '53054.1566', '57860.5746', '55665.2389', '50144.671', '61980.1758', '61416.6008', '65677.2295', '61160.3566', '59283.771', '55048.0868', '56536.7447', '53561.7556', '51037.2406', '55433.3326', '53366.6183', '53322.7363', '51375.615', '50577.6296', '51007.8455', '43785.9965', '40802.7314']

## Shell Script
You can use **run.sh** instead of commandline to run this script, following the same format as above:
> python print_fires.py -f 'file-name.csv' -c 'value' -cc 'country column' -fc 'fire column'

# How to install
This program uses python3 and imports the argparse library. 
1. Install python3 either [directly](https://www.python.org/downloads/) or with [anaconda](https://www.anaconda.com/download) (recommended).
2. Make sure to have both **my_utils.py**, **print_fires.py**, and **your_file.csv** in your directory. 
3. If running your script with bash, also make sure **run.sh** is installed and modified to match your filenames and arguments.

# Changelog
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