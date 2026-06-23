import pandas as pd
import numpy as np
import datetime

def main(n, categories, status, amount_baselines, amount_devs, continents):
    arr = list()
    for i in range(n):
        cat = np.random.choice(categories)
        stat = np.random.choice(status)
        amnt = np.round(amount_baselines[stat] + np.random.choice(np.arange(-amount_devs[stat], stop=amount_devs[stat]+1, step=0.1)), decimals=3)
        cont = np.random.choice(continents)
        arr.append([cat, amnt, stat, cont])

    df = pd.DataFrame(arr, columns=['Category', 'Amount', 'Status', 'Continent'])
    df.to_csv("dataset.csv")

if __name__ == '__main__':
    print(type(datetime.date.today().day))
    main()