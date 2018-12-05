import pandas as pd
import matplotlib.pyplot as plt
select_by_day = pd.read_excel('4ex_by_day.xlsx')
select_by_hour = pd.read_excel('4ex_by_hour.xlsx')
# select_by_day_tarn = pd.DataFrame(select_by_hour).transpose()
# print(select_by_day)

fig_day = select_by_day.plot(kind='bar', title='select_by_day')
plt.show()
fig_hour = select_by_hour.plot(kind='line', title='select_by_hour')
plt.show()
