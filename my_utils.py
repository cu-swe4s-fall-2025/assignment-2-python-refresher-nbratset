def get_column(file_name, query_column, query_value, result_column=1):
    '''Reads a CSV file and finds lines with a given value in a given column. Returns value of speficied column as an array.
    
    Parameters
    ----------
    file_name : csv file name

    query_column : Column index to filter by (can be a string or int)

    query_value : Value within specified query_column to filter by (can be a string or int)

    result_column : Column index or named column to get result values from

    Returns 
    -------
    result_array :  List of values from result_column where query_column contains the query_value
    
    '''
    try:
        f = open(file_name, 'r')
    except FileNotFoundError:
        print('Could not find '+file_name)
    except PermissionError:
        print('Could not open '+file_name)
    
    column_header = f.readline()                             # reads first line to get column headers
    
    try:
        query_index=int(query_column)
    except ValueError:
        query_index = column_header.index(query_column)      # finds column index for the query_column string value
    
    try:                                                     # checks if result_column is a string or int
        result_index=int(result_column)
    except ValueError:
        result_index = column_header.index(result_column)    # finds column index for the result_column string value
                                                                                                        
    result_array = []                                        # Final result list to be appended to

    for line in f:                                           # iterrates over all lines in csv
        line_array = line.rstrip().split(',')                # splits line into an array
        
        if line_array[query_index] == query_value:           # checks for query_value in the query_column
            value=float(line_array[result_index])            # Saves value as a float
            result_array.append(int(value))                  # appends value as an integer to an array (since the instructions wanted integers)
    
    f.close()

    return result_array