from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"########### Stage {STAGE_NAME} started ############")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f"########### Stage {STAGE_NAME} completed ###########\n\n")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare base model"
try: 
   logger.info(f"*******************")
   logger.info(f"########### Stage {STAGE_NAME} started ############")
   prepare_base_model = PrepareBaseModelTrainingPipeline()
   prepare_base_model.main()
   logger.info(f"########### Stage {STAGE_NAME} completed ###########\n\n")
except Exception as e:
        logger.exception(e)
        raise e