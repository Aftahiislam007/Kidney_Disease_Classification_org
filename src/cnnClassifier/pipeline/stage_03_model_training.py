import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.model_training import Training
from src.cnnClassifier import logger

STAGE_NAME = "Training stage"

class ModelTrainingPipeline:
    """docstring for ClassName."""
    def __init__(self):
        pass
    
    
    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()
        # training.copyFile()
        
        
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx============x")
    except Exception as e:
        logger.exception(e)
        raise e