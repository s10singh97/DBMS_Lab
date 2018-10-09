import pandas_datareader.data as web
import pandas as pd
# data = pd.DataFrame(data, columns=["High", "Low", "Open", "Close", "Volume", "Adj Close"])

import numpy as np
import matplotlib.pyplot as plt
# use ggplot style for more sophisticated visuals
plt.style.use('ggplot')
fig = plt.figure(figsize=(13,6))
data = []
data.append(web.get_data_yahoo('IBM','01/01/2015',interval='m'))
data.append(web.get_data_yahoo('GOOG','01/01/2015',interval='m'))
for i in range(0, len(data)):
    data[i]["Close"].plot()
plt.ylabel('Price')
plt.show()