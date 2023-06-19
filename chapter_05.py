#!/usr/bin/env python3

import logging

logging.basicConfig(
    filename="chapter_05.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logging.debug("This is a log message.")
