def get_column(file_name, query_column, query_value, result_column):
    '''Reads a CSV file and finds lines with a given value in a given column. Returns value of speficied column as an array.
    
    Parameters
    ----------
    file_name : csv file name

    query_column : Column index to filter by

    query_value : Value within specified query_column to filter by

    result_column : Column index to get result values from

    Returns 
    -------
    result_array :  List of values from result_column where query_column contains the query_value
    
    '''
    f = open(file_name, 'r')
    result_array = []                                      # Final result list to be appended to
    for line in f:                                         # iterrates over all lines in csv
        line_array = line.rstrip().split(',')              # splits line into an array
        if line_array[query_column] == query_value:        # checks for query_value in the query_column
            result_array.append(line_array[result_column]) # appends value if conditions are met to an array
    f.close()
    return result_array