import my_utils
import argparse


def main():
    parser = argparse.ArgumentParser(description='print a list of integers',
                                     prog='print_fires')

    parser.add_argument('-c',
                        '--country',
                        type=str,
                        help='name of the country',
                        required=True)

    parser.add_argument('-cc',
                        '--country_column',
                        type=str,
                        help='name or column number containing countires',
                        required=True)

    parser.add_argument('-fc',
                        '--fires_column',
                        type=str,
                        help='fire column for export',
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

    args = parser.parse_args()

    fires = my_utils.get_column(args.file_name,
                                args.country_column,
                                args.country,
                                args.fires_column)

    # I'm intentionally choosing to print the list AND the calcs here
    print(fires)

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
