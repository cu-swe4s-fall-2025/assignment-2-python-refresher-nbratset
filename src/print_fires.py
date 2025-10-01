import my_utils
import argparse


def main():
    parser = argparse.ArgumentParser(description='This script imports my_utils and uses get_column to print a list of integers for the desired country and fire type.',
                                    prog='print_fires',
                                    epilog='How to Run:\n>python print_fires.py -f "filename.csv" -c "Country Name" -cc "Country_Column" -fc "Fire Column"')

    parser.add_argument('-c',
                        '--country',
                        type=str,
                        help='Type the name of the country you\'d like to filter by.',
                        required=True)

    parser.add_argument('-cc',
                        '--country_column',
                        type=str,
                        help='Type the name or column number for the column containing countires.',
                        required=True)

    parser.add_argument('-fc',
                        '--fires_column',
                        type=str,
                        help='Type the name or column number for the column containing fire information you would like to export.',
                        required=True)

    parser.add_argument('-f',
                        '--file_name',
                        type=str,
                        help='Type the full filename and extension.',
                        required=True)
    
    parser.add_argument('-o',
                        '--operator',
                        type=str,
                        help='Options: mean, median, stdev, or all',
                        required=False)

    args=parser.parse_args()

    fires = my_utils.get_column(args.file_name,
                    args.country_column,
                    args.country,
                    args.fires_column)
    
    print(fires) # I am intentionally choosing to print the list AND the calculations here

    if args.operator:
        function = args.operator.lower()
        if function == 'mean':
            mean = my_utils.mean(fires)
            print(f'Mean: {mean}')
        
        elif function == 'median':
            median = my_utils.median(fires)
            print(f'Median: {median}')
        
        elif function == 'stdev':
            stdev = my_utils.stdev(fires)
            print(f'Standard Deviation: {stdev}')
        
        elif function == 'all':
            mean = my_utils.mean(fires)
            median = my_utils.median(fires)
            stdev = my_utils.stdev(fires)
            print(f'Mean: {mean}')
            print(f'Median: {median}')
            print(f'Standard Deviation: {stdev}')

if __name__ == '__main__':
    main()