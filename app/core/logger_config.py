# logger_config.py
import logging
import colorlog
import os

def setup_logging() -> None:
    """
    Set up logging configuration with colorlog, custom format, and log level from an environment variable.
    """
    # Set log level from environment variable if available, default to INFO
    log_level = os.environ.get("LOG_LEVEL", "INFO").upper()
    level = logging.getLevelName(log_level)

    # Create the colorlog formatter
    formatter = colorlog.ColoredFormatter(
        fmt="%(log_color)s[%(levelname)s] [%(asctime)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Set up the logging handler with the colorlog formatter
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    # Set up the logging configuration
    logging.basicConfig(
        level=level,
        handlers=[handler]
    )
