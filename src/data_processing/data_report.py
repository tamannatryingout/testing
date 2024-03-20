from src.data_processing.data_processor import DataProcessor

import pandas as pd
import pprint

class DataReport:
    
    def pretty_print(data):
        if isinstance(data, dict):
            pprint.pprint(data, width=100)
        elif isinstance(data, pd.DataFrame):
            print(data)
        elif isinstance(data, pd.Series):
            print(data.to_frame().T)
        elif isinstance(data, (list, tuple)):
            pprint.pprint(data, width=100)
        else:
            print(data)
