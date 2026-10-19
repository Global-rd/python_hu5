import logging
import logging.config
from pathlib import Path

 
LOG_DIR = Path(__file__).resolve().parent #Path("")
LOG_DIR.mkdir(exist_ok=True)

LOGGING_CONFIG = {
    "version": 1, 
    "disable_existing_loggers": False,  
    "formatters": {
        "default": {
            "format": "%(asctime)s [%(levelname)s] %(name)s:%(lineno)d | %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "simple": {
            "format": "%(levelname)s - %(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "level": "INFO",
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOG_DIR / "RPapp.log",
            "maxBytes": 10_000_000,  
            "backupCount": 5, 
            "formatter": "default",
            "level": "DEBUG",
        },
    },
    "root": { 
        "handlers": ["console", "file"],
        "level": "DEBUG",
    },
}

def setup_logging():
    logging.config.dictConfig(LOGGING_CONFIG)