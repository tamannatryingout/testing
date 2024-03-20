from src.data_processing.data_processor import DataProcessor
import pandas as pd

class DataAnalyzer(DataProcessor):
    """_summary_

    Args:
        DataProcessor (_type_): _description_

    Returns:
        _type_: _description_
    """

    def get_column_names_and_datatypes(self) -> pd.Series:
        """_summary_

        Returns:
            pd.Series: _description_
        """
        column_names_and_data_types = self.df.dtypes
        return column_names_and_data_types
    
    def get_entry_count(self) -> int:
        """_summary_

        Returns:
            int: _description_
        """
        entry_count = len(self.df)
        return entry_count

    def get_column_count(self) -> int:
        """_summary_

        Returns:
            int: _description_
        """
        column_count = len(self.df.columns)
        return column_count

    def get_unique_values_per_column(self) -> dict:
        """_summary_

        Returns:
            dict: _description_
        """
        unique_values_per_column = {col: self.df[col].unique() for col in self.df.columns}
        return unique_values_per_column
    
    def get_total_missing_values_count(self) -> int:
        """_summary_

        Returns:
            int: _description_
        """
        total_missing_values = self.df.isnull().sum().sum()
        return total_missing_values

    def get_missing_values_per_column(self) -> pd.Series:
        """_summary_

        Returns:
            pd.Series: _description_
        """
        missing_values_pro_column = self.df.isnull().sum()
        return missing_values_pro_column

    def check_for_duplicates(self) -> bool:
        """_summary_

        Returns:
            bool: _description_
        """
        duplicates = self.df.duplicated().any()
        return duplicates

    def check_for_duplicates_by_identifier(self, identifier_column) -> bool:
        """_summary_

        Args:
            identifier_column (_type_): _description_

        Returns:
            bool: _description_
        """
        duplicates_identifier = self.df.duplicated(subset=identifier_column).any()
        return duplicates_identifier

    def get_basic_statistics_for_numeric_columns(self) -> pd.DataFrame:
        """_summary_

        Returns:
            pd.DataFrame: _description_
        """
        numerical_columns = self.df.select_dtypes(include=['number'])
        statistics_df = numerical_columns.describe()
        return statistics_df
