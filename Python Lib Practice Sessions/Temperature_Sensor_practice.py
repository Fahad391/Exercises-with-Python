import numpy as np
import pandas as pd

class Sensor_log:
    def __init__(self, capacity = 5):
        # Encapsulation: the raw array is "hidden" behind an underscore.
        # Nobody outside this class should touch _readings directly.
        self._capacity = capacity
        self._readings = np.zeros(capacity)  # NumPy array as internal state
        self._count = 0  # tracks how many slots are filled

    def add_reading(self, value):
        if self._count >= self._capacity:
            raise ValueError("Log is full")
        
        self._readings[self._count] = value  # NumPy indexing (write)
        self._count += 1
    
    def get_reading(self, index):
        # NumPy indexing (read) — but through a controlled method,
        # not raw access. This IS encapsulation.
        return self._readings[index]
    
    def recent(self, n):
         # NumPy slicing: last n readings that are actually filled
        return self._readings[self._count - n : self._count]

    def all_readings(self):
        # Slicing: only return the filled part, not the zero-padding
        return self._readings[:self._count]
    
    def average(self):
        return self._readings[:self._count].mean()
    

class Temperature_log(Sensor_log):
    def __init__(self, capacity=5, min_temp=-50, max_temp=60):
        super().__init__(capacity)  # reuse parent's setup — don't rebuild it
        self._min_temp = min_temp
        self._max_temp = max_temp

    def add_reading(self, value):
        if not (self._min_temp <= value <= self._max_temp):
            raise ValueError(f"Temparature {value} out of range")
        super().add_reading(value)  # let parent do the actual write + count logic

    def is_freezing(self, index):
        return self.get_reading(index) <= 0
    
# Three sensors, three cities
dhaka = Temperature_log(capacity=4)
dhaka.add_reading(28)
dhaka.add_reading(30)

sylhet = Temperature_log(capacity=4)
sylhet.add_reading(-2)
sylhet.add_reading(15)

cox = Temperature_log(capacity=4)
cox.add_reading(32)
cox.add_reading(33)

logs = {"Dhaka": dhaka, "Sylhet": sylhet, "Cox's Bazar": cox}

# Series: one value per key — here, each city's average
avg_series = pd.Series({city: log.average() for city, log in logs.items()})
print("\nAverage series of 3 cities:\n",avg_series)

# DataFrame: each city's full reading list as a row
df = pd.DataFrame({city: log.all_readings() for city, log in logs.items()})
print("\nData Frame\n",df)

# Selection & slicing
print("\nAverage series of Sylhet:\n",avg_series["Sylhet"])       # label-based selection on a Series
print("\nDhaka\n",df["Dhaka"])                 # column selection on a DataFrame
print("\nLoc[0]\n",df.iloc[0])                  # row selection by position
print("\nResult of loc[0:1]\n",df.loc[0:1, ["Dhaka", "Cox's Bazar"]])   # label-based row+column slice

print("\nShape:",df.shape)
print("\nAverage Series mean:",avg_series.mean())
print("\nResult of loc[1]:\n",df.loc[1])
        
