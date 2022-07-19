import numpy as np
import pandas as pd
from numpy import nan as NA


def insert_Series(seriesA):
    listA = list(seriesA[seriesA.isnull()].index)
    i = 0
    j = 0
    counter = 0
    while (np.any(seriesA.isnull())):
        i = listA[j]
        tempfirst = listA[j]
        pointer = tempfirst
        while(seriesA.isnull()[i+1] & seriesA.isnull()[i]):
            i+=1
        if(seriesA.isnull()[i] & seriesA.notnull()[i+1]):
            while (seriesA.isnull()[i]):
                x1 = tempfirst-1
                y1 = float(seriesA[x1].copy())
                x2 = i+1
                y2 = float(seriesA[x2].copy())
                result = ((y2-y1)/(x2-x1))*pointer + (y1 - ((y2-y1)/(x2-x1))*x1)
                seriesA[pointer] = result
                pointer+=1
            j+=1

    return seriesA.copy()

data04 = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon',
                                'Pastrami', 'corned beef', 'Bacon',
                                'pastrami', 'honey ham', 'nova lox'],
                       'ounces': [2, 1, np.nan, np.nan, np.nan, np.nan, 3, 5, 6]})
Series04=data04['ounces'].copy()
print(pd.isnull(Series04[2]))

print(pd.isnull(Series04))
Series04_inserted = insert_Series(Series04)
print(Series04_inserted)
