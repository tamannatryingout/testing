# data_processor.py

from typing import List
import pandas as pd
from pathlib import Path
from abc import ABC

class DataProcessor(ABC):
    def __init__(self, read_data_file, **kwargs) -> pd.DataFrame:
        if 'folder_path' in kwargs:
            self.df = self.read_data_files(kwargs['folder_path'])
        else:
            self.df = read_data_file(**kwargs) 
                

    @staticmethod
    def read_data_file(file_path: str) -> pd.DataFrame:
        file = Path(file_path)
        if file.suffix == '.csv':
            df = pd.read_csv(file)
        elif file.suffix == '.parquet':
            df = pd.read_parquet(file)
        elif file.suffix == '.xlsx':
            df = pd.read_excel(file)
        else:
            raise ValueError(f"Unsupported file format for {file}")
        return df


    @staticmethod
    def read_data_files(folder_path: str) -> List[pd.DataFrame]:

        path = Path(folder_path)
        df = []
        for file in path.iterdir():
            if file.is_file():
                if file.suffix == '.csv':
                    df = pd.read_csv(file)
                elif file.suffix == '.parquet':
                    df = pd.read_parquet(file)
                elif file.suffix == '.xlsx':
                    df = pd.read_excel(file)
                else:
                    raise ValueError(f"Unsupported file format for {file}")
                df.append(df)
        return df
