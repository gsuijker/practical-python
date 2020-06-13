# pcost.py
#
# Exercise 1.27
import sys
import csv
import report

def portfolio_cost(filename):

    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    portfolio = report.read_portfolio(filename)
    return sum([s['shares'] *s['price'] for s in portfolio])

    # total_cost = 0

    # f = open(filename, 'rt')
    # rows = csv.reader(f)
    # headers = next(rows)

    # for rowno, row in enumerate(rows, start=1):
    #     record = dict(zip(headers, row))
    #     try:
    #         nshares = int(record['shares'])
    #         price = float(record['price'])
    #         total_cost += nshares * price
    #     except ValueError:
    #         print(f'Row {rowno}: Bad row:{row}')          
    
    # f.close()

    # return total_cost

def main(args):
    if len(args) != 2:
        raise SystemExit(f'Usage: {args[0]} portfoliofile')
    filename = args[1]
    cost = portfolio_cost(filename)
    print('Total cost:', cost)

if __name__ == '__main__':
    main(sys.argv)


