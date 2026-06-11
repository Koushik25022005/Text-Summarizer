from src.TextSummarizer.entity import DataIngestionConfig
from src.TextSummarizer.constants import CONFIG_FILEPATH, PARAMS_FILEPATH
from src.TextSummarizer.utils.common import read_yaml, create_directories

class ConfigurationManager:
    def __init__(
        self, 
        config_filepath=CONFIG_FILEPATH,
        params_filepath=PARAMS_FILEPATH
    ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        
        create_directories([self.config.artifacts_root])
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        
        create_directories([config.unzip_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        
        return data_ingestion_config