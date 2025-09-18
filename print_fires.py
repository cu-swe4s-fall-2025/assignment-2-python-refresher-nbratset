from my_utils import get_column
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

    args=parser.parse_args()

    fires = get_column(args.file_name,
                    args.country_column,
                    args.country,
                    args.fires_column)

    print(fires)


if __name__ == '__main__':
    main()