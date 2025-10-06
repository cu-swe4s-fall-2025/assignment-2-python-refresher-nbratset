test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

## Positive cases ##
run test_mean_by_name python src/print_fires.py -f 'src/test_data.csv' -c 'United States of America' -cc 'Area' -fc 'Forest fires' -o 'mean'
assert_in_stdout "1999"
assert_in_stdout "5405"
assert_in_stdout "Mean: 1928.225806451613"
assert_exit_code 0

run test_median_by_index python src/print_fires.py -f 'src/test_data.csv' -c 'United States of America' -cc 'Area' -fc 'Forest fires' -o 'median'
assert_in_stdout "1999"
assert_in_stdout "5405"
assert_in_stdout "Median: 1558.0"
assert_exit_code 0

run test_stdev python src/print_fires.py -f 'src/test_data.csv' -c 'Spain' -cc 'Area' -fc 'Forest fires' -o 'stdev'
assert_in_stdout "55"
assert_in_stdout "Standard Deviation: 72.65564"
assert_exit_code 0

run test_all python src/print_fires.py -f 'src/test_data.csv' -c 'Portugal' -cc 'Area' -fc 'Forest fires' -o 'all'
assert_in_stdout "Mean: 73.28"
assert_in_stdout "Median: 71.0"
assert_in_stdout "Standard Deviation: 97.98058688"
assert_exit_code 0


## Error Cases ##
run test_file_not_found python src/print_fires.py -f 'src/file.csv' -c 'Any' -cc 'Any' -fc 'Any'
assert_in_stderr "Could not find file: file.csv"
assert_exit_code 0

run test_bad_query_column python src/print_fires.py -f 'src/test_data.csv' -c 'USA' -cc 'bad_col' -fc 'Forest fires'
assert_in_stderr "substring not found"
assert_exit_code 0

run test_bad_result_column python src/print_fires.py -f 'src/test_data.csv' -c 'United States of America' -cc 'Area' -fc 'Bad_Fires'
assert_in_stderr "Bad_Fires column not in test_data.csv"
assert_exit_code 0

run test_empty_array python src/print_fires.py -f 'src/test_data.csv' -c 'Not a Country' -cc 'Area' -fc 'Forest fires' -o 'mean'
assert_in_stdout "[]"
assert_in_stdout "Array provided was empty!"
assert_in_stdout "Mean: None"
assert_exit_code 0

run test_wrong_operator python src/print_fires.py -f 'src/test_data.csv' -c 'United States of America' -cc 'Area' -fc 'Forest fires' -o 'mode'
assert_in_stdout "1999"
assert_not_in_stdout "Mean"
assert_exit_code 0