'''
This will read CSV_IN and loop over it until SAMPLE_SIZE is reached and
output it to CSV_OUT. Be sure to specify the delimiter and quote char.
It will maintain these values in the sample output csv.

Notes:
    * This will truncate the output file or create it if needed
'''

import csv

CSV_IN = 'OUTPUT_1528387783_1734714987.csv'
CSV_OUT = 'sample_output.csv'

SAMPLE_SIZE = 1

CSV_DELIMITER = ','
CSV_QUOTECHAR = '"'

with open(CSV_IN) as infile, open(CSV_OUT, 'w') as outfile:
    rownum = 0
    reader = csv.reader(
        infile,
        delimiter=CSV_DELIMITER,
        quotechar=CSV_QUOTECHAR,
    )
    writer = csv.writer(
        outfile,
        delimiter=CSV_DELIMITER,
        quotechar=CSV_QUOTECHAR,
        quoting=csv.QUOTE_ALL,
    )
    for row in reader:
        if rownum <= SAMPLE_SIZE:
            writer.writerow(row)
            rownum += 1
        else:  # if the desired sample size has been achieved exit
            break
