
import os
import sys 
from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import (RandomForestRegressor,GradientBoostingRegressor,AdaBoostRegressor)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from xgboost import XGBRegressor

from src.utils import save_object,evaluate_model

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts','model.pkl')
class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
        
    def initiate_model_trainer(self,train_array,test_array,preprocessor_path):
        try:
            logging.info("Split training and test input data")
            X_train,y_train,X_test,y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "K-Neighbors Regressor": KNeighborsRegressor(),
                "XGBRegressor": XGBRegressor(),
                "CatBoosting Regressor": CatBoostRegressor(verbose=False),
                "AdaBoost Regressor": AdaBoostRegressor()
            }
            model_report: dict = evaluate_model(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,models=models)
            
            ## To get the best model score from dict
            
            best_model_name = max(model_report, key=lambda x: model_report[x]['test_score'])
            best_model_score = model_report[best_model_name]['test_score']
            best_model = models[best_model_name]
            
            if best_model_score < 0.6:
                logging.info("No best model found")
                raise CustomException("No best model found")
            
            logging.info(f"Best found model on both training and testing dataset is {best_model_name}")
            
            save_object(
                file_path = self.model_trainer_config.trained_model_file_path,
                obj = best_model
            )
            
            predicted = best_model.predict(X_test)
            r2_square = r2_score(y_test,predicted)
            logging.info(f"R2 Score of best model is {r2_square}")
            return r2_square
        except Exception as e:
            logging.info("Exception occured at model training")
            raise CustomException(e,sys)