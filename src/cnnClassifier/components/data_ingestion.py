import os
import zipfile
import gdown
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import (DataIngestionConfig)



class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_file(self)-> str:
        '''
        Fetch data from the url
        '''
        
        try:
            dataset_utl = self.config.source_url
            zip_download_dir = self.config.local_data_file
            
            # if not os.path.exists(self.config.local_data_file):
            #     raise FileNotFoundError(f"ZIP file not found: {self.config.local_data_file}")
            
            # if os.path.getsize(self.config.local_data_file) == 0:
            #     raise ValueError("The downloaded file is empty.")
            
            # if not self.config.local_data_file.endswith('.zip'):
            #     raise ValueError("The specified file is not a ZIP file.")
            
            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            logger.info(f"Downloading data from {dataset_utl} into file {zip_download_dir}")
            
            file_id = dataset_utl.split("/")[-2]
            # print(file_id)
            prefix = "https://drive.google.com/uc?export=download&id="
            gdown.download(prefix+file_id, zip_download_dir)
            
            logger.info(f"Downloaded data from {dataset_utl} into file {zip_download_dir}")
        except Exception as e:
            raise e
    
    
    def extract_zip_file(self):
        """
        zip file path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        try:
            unzip_path = self.config.unzip_dir
            os.makedirs(unzip_path, exist_ok=True)
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
                # zip_ref.extractall(self.config.extract_to)
        except zipfile.BadZipFile:
            raise ValueError("The ZIP file is either corrupt or not a valid ZIP.")
        