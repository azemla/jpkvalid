import pandas as pd


def read_files() -> None:
    data_jpk = pd.read_excel('data/resultJPK-2020.01.29-15-51.xlsx')
    data_jpk.dropna()
    data_matlab = pd.read_excel('data/resultMatlab-2020.01.29-15-51.xlsx', header=None)
   # print(data_jpk)
    print(data_matlab)

    joined = data_matlab.merge(data_jpk, left_on=0, right_on='Position Index', how='left')

    print(joined)
    joined.to_excel("results/joined.xlsx")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    read_files()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
