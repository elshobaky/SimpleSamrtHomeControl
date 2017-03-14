import os
import sys
import logging


# configuring logging
def config_logging():
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    root.addHandler(ch)

# static directory
MAIN_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(MAIN_DIR, "static")
TEMPLATES_DIR = os.path.join(MAIN_DIR, "templates")
