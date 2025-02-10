import os
from src.Udemy_endTOend import logger
from src.Udemy_endTOend.entity.config_entity import (DataValidationConfig)
import pandas as pd

class DataValidation:
    def __init__(self, config:DataValidationConfig):
        self.config = config

    def validate_all_columns(self)-> bool:
        try:
            validation_status = None
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            all_schema = self.config.all_schema.keys()

            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                else:
                    validation_status =  True
                with open(self.config.STATUS_FILE, "a") as f:
                    f.write(f"Validation status: {validation_status}\n")

            return validation_status

        except Exception as e:
            raise e

    def validate_data_type(self) -> bool:
        try:
            validation_status = None
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            all_schema = self.config.all_schema

            for col in all_cols:
                if data[col].dtype == all_schema[col]:
                    validation_status = True
                else:
                    validation_status = False
                with open(self.config.STATUS_FILE, "a") as f:
                    f.write(f"Data type Validation status: {validation_status}\n")

            return validation_status

        except Exception as e:
            raise e
