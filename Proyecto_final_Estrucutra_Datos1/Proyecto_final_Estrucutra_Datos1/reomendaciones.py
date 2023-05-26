from pyDatalog import pyDatalog
from pyDatalog import logic

# Define the facts using pyDatalog

# Fact: X is the parent of Y
parent = pyDatalog.Variable()

+parent('John', 'Alice')
+parent('John', 'Bob')
+parent('Alice', 'Carol')

# Query: Who are the grandparents of Carol?
def grandparent(X, Z):
    Y = pyDatalog.Variable()  # Define the variable Y
    return logic.MultipleResults() & (X, Z) <= parent(X, Y) & parent(Y, Z)

result = []
X = pyDatalog.Variable()
Z = pyDatalog.Variable()
for res in grandparent(X, Z):
    result.append((res[X], res[Z]))

print('X\t\t|\tZ')
print('---------------|---------------')
for Xval, Zval in result:
    print(f'{Xval}\t\t|\t{Zval}')
