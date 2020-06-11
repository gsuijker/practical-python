# report.py
#
# Exercise 2.4
import csv
from pprint import pprint

def read_portfolio(filename):

    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        _ = next(rows)

        for row in rows:
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append({'name': holding[0], 'shares':holding[1], 'price':holding[2]})
        
        return portfolio

portfolio = read_portfolio('Data/portfolio.csv')
pprint(portfolio)


