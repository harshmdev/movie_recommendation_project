from src.movie_recommendation_project.logging import logger
from src.movie_recommendation_project.pipeline.stage_01_data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.movie_recommendation_project.pipeline.stage_02_data_validation_pipeline import DataValidationPipeline
from src.movie_recommendation_project.pipeline.stage_03_data_transformation_pipeline import DataTransformationPipeline
from src.movie_recommendation_project.pipeline.stage_04_model_building import ModelBuildingPipeline

def run_pipeline():
    stages = [
        ("Data Ingestion Stage", DataIngestionTrainingPipeline),
        ("Data Validation Stage", DataValidationPipeline),
        ("Data Transformation Stage", DataTransformationPipeline),
        ("Model Building Stage", ModelBuildingPipeline)
    ]

    for stage_name, pipeline_class in stages:
        try:
            logger.info(f"started>>>>{stage_name}<<<<started")
            pipeline_instance = pipeline_class()
            pipeline_instance.main()
            logger.info(f">>>> stage {stage_name} completed <<<<\n\nx=====x")
        except Exception as e:
            logger.exception(e)
            raise e

if __name__ == "__main__":
    run_pipeline()
