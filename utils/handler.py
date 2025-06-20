import logging

def logs(filename:str='photopro.log'):
    # logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(filename),
            logging.StreamHandler()
        ]
    )

    return logging.getLogger(__name__)

class PhotoProError(Exception):
    pass