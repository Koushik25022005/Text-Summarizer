from src.TextSummarizer.pipeline.stage_1_data_ingestion import DataIngestionPipeline


from src.TextSummarizer.logging import logger
STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>>>> Stage 1 Data Ingestion started <<<<<<<")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.main()
    logger.info(f">>>>>>>> Stage 1 Data Ingestion completed <<<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
    