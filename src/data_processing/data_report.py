import pandas as pd
import pprint

class DataReport:
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
