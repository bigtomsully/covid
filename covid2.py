import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel(r"https://dshs.texas.gov/coronavirus/TexasCOVID19DailyCountyCaseCountData.xlsx")
cases = list(df.iloc[102])

cases[0],cases[1]=0,0 
print(cases)
plt.xlabel('days since beginning of outbreak in harris county')
plt.ylabel('number of confirmed cases')
plt.plot(cases)
plt.show()
