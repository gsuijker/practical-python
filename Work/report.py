# report.py
#
# Exercise 2.4
import csv
from collections import Counter

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            record = dict(zip(headers, row))
            stock = {
                 'name'   : record['name'],
                 'shares' : int(record['shares']),
                 'price'   : float(record['price'])
            }
            portfolio.append(stock)

    return portfolio

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass

    return prices

def make_report(portfolio, prices):
    report = []
    stock = ''
    shares = 0
    price = 0.0
    change = 0.0
    
    for s in portfolio:
        stock = s['name']
        shares = s['shares']
        price = prices[stock]
        change = price - s['price']
        report.append((stock, shares, price, change))

    return report


portfolio = read_portfolio('Data/portfolio.csv')
portfolio2 = read_portfolio('Data/portfolio2.csv')
prices    = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)

headers = ('Name', 'Shares', 'Price', 'Change')
stripes = "-"*10

print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')

print(f'{stripes:>10s} {stripes:>10s} {stripes:>10s} {stripes:>10s}')

for name, shares, price, change in report:
    print(f'{name:>10s} {shares:>10d} {f"${price:.2f}":>10s} {change:>10.2f}')

# Calculate the total cost of the portfolio
total_cost = 0.0
for s in portfolio:
    total_cost += s['shares']*s['price']

print('Total cost', total_cost)

# Compute the current value of the portfolio
total_value = 0.0
for s in portfolio:
    total_value += s['shares']*prices[s['name']]

print('Current value', total_value)
print('Gain', total_value - total_cost)


holdings = Counter()
for s in portfolio:
    holdings[s['name']] += s['shares']

print(holdings)

holdings2 = Counter()
for s in portfolio2:
    holdings2[s['name']] += s['shares']

print(holdings2)

combined = holdings + holdings2
print(combined)

cost = sum([s['shares'] * s['price'] for s in portfolio])
value = sum([s['shares'] * prices[s['name']] for s in portfolio])
print(cost)
print(value)

more100 = [s for s in portfolio if s['shares'] > 100]
print(more100)