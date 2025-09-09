def get_column(file_name, query_column, query_value, result_column=1):
    '''Reads a CSV file and finds lines with a given value in a given column. Returns value of speficied column as an array.
    
    Parameters
    ----------
    file_name : csv file name

    query_column : Column index to filter by

    query_value : Value within specified query_column to filter by

    result_column : Column index or named column to get result values from

    Returns 
    -------
    result_array :  List of values from result_column where query_column contains the query_value
    
    '''
    
    f = open(file_name, 'r')
    
    if type(result_column) == str:                         # checks if result_column is a string
        column_header = f.readline()                       # reads first line to get column headers
        result_index = column_header.index(result_column)  # finds column index for the result_column value
    elif type(result_column) == int:
        result_index = result_column
    
    result_array = []                                      # Final result list to be appended to
    for line in f:                                         # iterrates over all lines in csv
        line_array = line.rstrip().split(',')              # splits line into an array
        if line_array[query_column] == query_value:        # checks for query_value in the query_column
            result_array.append(line_array[result_index]) # appends value if conditions are met to an array
    f.close()
    return result_array