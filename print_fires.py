from my_utils import get_column
import argparse

parser = argparse.ArgumentParser(
            description='',
            prog='')

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
                    help='Type the full filename and extension. ',
                    required=True)

args=parser.parse_args()


# country='United States of America'
# county_column = 0
# # fires_column = 3  # optional integer (index) or string handling for fires_column
# fires_column = 'Forest fires'
# file_name = 'Agrofood_co2_emission.csv'

print(args.file_name,args.country_column,args.country,args.fires_column)
# fires = get_column(args.file_name,args.country_column,args.country,args.fires_column)
# print(fires)