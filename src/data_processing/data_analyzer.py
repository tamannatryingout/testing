from src.data_processing.data_processor import DataProcessor
import pandas as pd

class DataAnalyzer(DataProcessor):

    # Get column names and their corresponding data types.
    def get_column_names_and_datatypes(self) -> pd.Series:
        column_names_and_data_types = self.df.dtypes
        return column_names_and_data_types
    
    # Get the number of entries (rows) in the DataFrame.
    def get_entry_count(self) -> int:
        entry_count = len(self.df)
        return entry_count

    # Get the number of columns in the DataFrame.
    def get_column_count(self) -> int:
        column_count = len(self.df.columns)
        return column_count

    # Get unique values for each column.
    def get_unique_values_per_column(self) -> dict:
        unique_values_per_column = {col: self.df[col].unique() for col in self.df.columns}
        return unique_values_per_column
    
    # Get the total number of missing values in the DataFrame.
    def get_total_missing_values_count(self) -> int:
        total_missing_values = self.df.isnull().sum().sum()
        return total_missing_values

    # Get the number of missing values per column.
    def get_missing_values_per_column(self) -> pd.Series:
        missing_values_pro_column = self.df.isnull().sum()
        return missing_values_pro_column

    # Check for duplicates across all entries.
    def check_for_duplicates(self) -> bool:
        duplicates = self.df.duplicated().any()
        return duplicates

    # Check for duplicates based on an identifier column.
    def check_for_duplicates_by_identifier(self, identifier_column) -> bool:
        duplicates_identifier = self.df.duplicated(subset=identifier_column).any()
        return duplicates_identifier

    # Get basic statistical values for numeric columns.
    def get_basic_statistics_for_numeric_columns(self) -> pd.DataFrame:
        numerical_columns = self.df.select_dtypes(include=['number'])
        statistics_df = numerical_columns.describe()
        return statistics_df
