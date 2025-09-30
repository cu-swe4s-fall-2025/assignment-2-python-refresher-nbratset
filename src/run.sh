#!/bin/bash

echo 'Running print_fires.py'

echo '----------------------'
echo 'First Run'
python print_fires.py -f 'Agrofood_co2_emission.csv' -c 'United States of America' -cc 'Area' -fc 'Forest fires'

echo '----------------------'
echo 'Second Run'
python print_fires.py -f 'Agrofood_co2_emission.csv' -c 'United States of America' -cc 'Area' -fc 'All fires'

echo '----------------------'
echo 'Third Run'
python print_fires.py -f 'fires.csv' -c 'United States of America' -cc 'Area' -fc 'Forest fires'
 