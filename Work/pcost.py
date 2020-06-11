# pcost.py
#
# Exercise 1.27
import sys

def portfolio_cost(filename):

    total_cost = 0

    f = open(filename, 'rt')
    _ = next(f)

    for line in f:
        row = line.split(',')
        try:
            total_cost += float(row[1]) * float(row[2])
        except ValueError:
            print('Error in the file')          
    
    f.close()

    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)


