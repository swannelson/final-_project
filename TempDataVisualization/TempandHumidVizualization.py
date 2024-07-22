import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("temphumid.csv")

plt.plot(pd.to_datetime(data['timestamp']),data['temperature'].astype(float))

plt.title("Temperature Over Time")

plt.xlabel('Day')
plt.ylabel('Temperature')
plt.show()

plt.plot(pd.to_datetime(data['timestamp']),data['humidity'].astype(float))
plt.title("Humidity Over Time")

plt.xlabel('Day')
plt.ylabel('Humidity')

plt.show()
