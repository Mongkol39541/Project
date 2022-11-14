import pandas as pd

class calculateday:
        def daynumber(number):
            df_day = pd.read_csv("number_day.csv")
            df_month = pd.read_csv("number_month.csv")
            number_day, number_month = number.split("/")
            mean_day = str(int(number_day)) + " : " + df_day["Mean"][int(number_day) - 1]
            mean_month = str(int(number_month)) + " : " + df_month["Mean"][int(number_month) - 1]
            return mean_day, mean_month
print(pd.__version__)