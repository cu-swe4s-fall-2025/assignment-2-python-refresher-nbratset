import sys 

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
        print(f'Could not find file: {file_name}')
    except PermissionError:
        print(f'Could not open file: {file_name}')
    
    column_header = f.readline()                          # reads first line to get column headers
    
    try:
        query_index=int(query_column)
    except ValueError:
        query_index = column_header.index(query_column)       # finds column index for the query_column string value
    
    try:                                                      # checks if result_column is a string or int
        result_index=int(result_column)
    except ValueError:
        try:
            result_column in column_header
            result_index = column_header.index(result_column) # finds column index for the result_column string value
        except ValueError:
            print(f'{result_column} column not in {file_name}')
                                                                                                        
    result_array = []                                         # Final result list to be appended to

    for line in f:                                            # iterrates over all lines in csv
        line_array = line.rstrip().split(',')                 # splits line into an array
        
        if line_array[query_index] == query_value:            # checks for query_value in the query_column
            try:
                value=float(line_array[result_index])         # Saves value as a float
                result_array.append(int(value))               # appends value as an integer to an array (since the instructions wanted integers)
            except IndexError:
                print(f'{result_column} column not in {file_name}')
    
    f.close()

    return result_array

def mean(array):
    ''' Calculates mean via (sum of all values in array) / (number of values in array). '''
    try:
        total = len(array)
    except IndexError:
        print('Array provided was empty!')
        return None
    
    if total == 0:
        print('Array provided was empty!')
        return None
    
    sum = 0.0
    for value in array:
        try:
            sum += float(value)
        except (ValueError, TypeError):
            print('Array contains non-number characters!')
            return None
    
    return sum / total

def median(array):
    ''' Calculates median for both odd and even number arrays by finding the middle index of the sorted list. 
        For an even array, the funtion finds the middle two indexes and returns the average of the two. '''
    try:
        length = len(array)
    except IndexError:
        print('Array provided was empty!')
        sys.exit(1)

    sorted_array = sorted(array)
    median_index = length // 2

    if length % 2 == 0:
        second_index = median_index - 1
        return (sorted_array[median_index] + sorted_array[second_index]) / 2
    else:
        return sorted_array[median_index]

def stdev(array):
    ''' Calculates the standard deviation of an array via:
        Sqrt(Summation of (x-mean)^2 / N) where N is the number of elements in the array. '''
    array_mean = mean(array)
    
    if len(array) == 1:
        print('Cannot compute stdev of an array with length 1')
        return None
    
    sum = 0
    for value in array:
        delta_x_squared = (value - array_mean) ** 2
        sum += delta_x_squared
    
    return (sum / len(array)) ** 0.5