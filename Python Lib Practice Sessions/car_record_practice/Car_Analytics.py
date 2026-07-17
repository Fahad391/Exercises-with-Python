import os
import numpy as np
import pandas as pd

class Car_Tracker:
    # Class Variable
    file_path = "car_record_practice/Car_List.csv"

    # Constructor
    def __init__(self):
        # use of os library starts here
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        self.data_frame = self._load_data()

    def _load_data(self):
        """Internal helper to Load the Data Set"""

        # used Exception handling
        try:
            return pd.read_csv(self.file_path)

        except (FileNotFoundError, pd.errors.EmptyDataError):
            return pd.DataFrame(columns=["Brand", "Model"])
        
    def save_data(self):
        self.data_frame.to_csv(self.file_path, index=False)

    def add_car(self, brand, model):
        """Appends a single car record to the DataFrame."""
        new_car = pd.DataFrame([{"Brand": brand, "Model": model}])
        self.data_frame = pd.concat([self.data_frame, new_car], ignore_index=True)

    def show_all_cars(self):
        """Returns the internal dataframe for iteration or display."""
        return self.data_frame
        
    
    def get_total_count(self):
        """Uses NumPy to get total fleet count from dataframe shape."""
        return np.shape(self.data_frame.to_numpy())[0]
    
    def analyze(self):
       # Ignore blank or missing brand names.
        brands_array = (
            self.data_frame["Brand"]
            .dropna()
            .to_numpy()
        )

        unique_brands, counts = np.unique(
            brands_array,
            return_counts=True
        )

        return {
            "total_unique": len(unique_brands),
            "brands_list": list(unique_brands)
        }