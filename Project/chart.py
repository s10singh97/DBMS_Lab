from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

def stockchart(symbol):
    ts = TimeSeries(key='F7CJI1OC9ZJ6DVP3', output_format='pandas')
    data, meta_data = ts.get_intraday(symbol=symbol,interval='1min', outputsize='compact')
    print(data)
    data['4. close'].plot()
    plt.title('Stock chart')
    plt.show()

symbol=input("Enter symbol name:")
stockchart(symbol)
