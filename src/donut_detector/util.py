import logging


def get_logger(logger_name, **kwargs):
    # create logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    
    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    if kwargs.has_key('log_file'):
        fh = logging.FileHandler(kwargs['log_file'])
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        logger.addHandler(fh)    
        
    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    
    return logger