from src.movie_recommendation_project.config.configuration import ConfigurationManager
from src.movie_recommendation_project.components.model_building import ModelBuilding



class ModelBuildingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        model_building_config = config.get_model_building_config()
        model_building = ModelBuilding(config=model_building_config)
        model_building.model_builder()