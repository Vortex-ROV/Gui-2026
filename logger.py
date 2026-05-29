import logging
import sys
import os
from datetime import datetime


class _StreamToLogger:
    def __init__(self, logger, level):
        self._logger = logger
        self._level  = level
    def write(self, msg):
        if msg.strip():
            self._logger.log(self._level, msg.strip())
    def flush(self):
        pass


def setup_logger() -> logging.Logger:
    log_dir = os.path.join(os.path.dirname(sys.executable)
                           if getattr(sys, 'frozen', False)
                           else os.path.dirname(os.path.abspath(__file__)),
                           "logs")
    os.makedirs(log_dir, exist_ok=True)

    log_file = os.path.join(log_dir, f"nautix_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

    # Only add StreamHandler if stdout exists (not None in frozen exe)
    handlers = [logging.FileHandler(log_file, encoding="utf-8")]
    if sys.__stdout__ is not None:
        handlers.append(logging.StreamHandler(sys.__stdout__))

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=handlers,
    )

    logger = logging.getLogger("Nautix")

    # Redirect all print() calls to the log file
    sys.stdout = _StreamToLogger(logger, logging.INFO)
    sys.stderr = _StreamToLogger(logger, logging.ERROR)

    logger.info(f"Log file: {log_file}")
    return logger


# Global logger — import this anywhere
log = setup_logger()