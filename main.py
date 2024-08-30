from src.movie_recommendation_project.logging import logger
from src.movie_recommendation_project.pipeline.stage_01_data_ingestion_pipeline import DataIngestionTrainingPipeline

STAGE_NAME= "Data Ingestion Stage"

try:
    logger.info(f"started>>>>{STAGE_NAME}<<<<started")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<\n\nx=====x")
except Exception as e:
    logger.exception(e)
    raise e