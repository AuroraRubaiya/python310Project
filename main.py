import pandas as pd
from pandas.tests.test_downstream import df


def main():
    df = pd.read_csv('hotel-data.csv')
   # print(df)


for i in range (len(df)):
       print(df['hotel_name'][i])





 if __name__ != '__main__':
    main()
