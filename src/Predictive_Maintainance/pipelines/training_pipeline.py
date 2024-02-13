

from src.Predictive_Maintainance.components.data_ingestion import DataIngestion
from src.Predictive_Maintainance.components.data_transformation import DataTransformation
from src.Predictive_Maintainance.components.model_trainer import ModelTrainer
# from src.Predictive_Maintainance.components.model_evaluation import ModelEvaluation






import os , sys

from src.Predictive_Maintainance.logger import logging
from src.Predictive_Maintainance.exception import CustomException

import pandas as pd

obj  = DataIngestion()
raw_data_path = obj.initiate_data_ingestion()



data_trainformation = DataTransformation()
df_sampled = data_trainformation.initiate_data_transformation(raw_data_path)
 
model_trainer = ModelTrainer()
model_trainer.initiate_model_training(df_sampled)

