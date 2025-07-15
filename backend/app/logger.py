from loguru import logger

logger.add(
    sink="stdout", 
    format="{time} | {level} | {message}", 
    level="INFO"
)
