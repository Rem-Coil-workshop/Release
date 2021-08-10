import logging


def configure():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(process)d] %(levelname)s - %(message)s',
        datefmt='%y-%b-%d %H:%M:%S'
    )
