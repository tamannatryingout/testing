import pandas as pd
import pprint

from src.data_processing.data_analyzer import DataAnalyzer
from src.data_processing.data_analyzer import DataProcessor

class DataReport(DataAnalyzer):
    """_summary_
    """
    
    def pretty_print(data: pd.DataFrame) -> None:
        """_summary_

        Args:
            data (pd.DataFrame): _description_
        """
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

    def generate_data_report(self) -> dict:
        data_report = {
            "Column Names and Data Types": self.get_column_names_and_datatypes(),
            "Entry Count": self.get_entry_count(),
            "Column Count": self.get_column_count(),
            "Total Missing Values Count": self.get_total_missing_values_count(),
            "Missing Values per Column": self.get_missing_values_per_column(),
            "Duplicates by Identifier Check": self.check_for_duplicates_by_identifier(identifier_column='DS_100_VON'),
            "Basic Statistics for Numeric Columns": self.get_basic_statistics_for_numeric_columns()
        }
        

        return data_report

