import pandas as pd

def bmi_calculator(data: pd.DataFrame):
    data['bmi'] = round((data['weight']/((data['height']/1000)**2)),2)
    return data