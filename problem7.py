import csv 

def problem3_7(csv_pricefile, flower):
    """Reads a CSV file, looks up the price of a flower and prints it"""
    f = open(csv_pricefile)
    d = {}
    for row in csv.reader(f):
        d[row[0]] = row[1]
    price = str(d[flower])
    print(price)