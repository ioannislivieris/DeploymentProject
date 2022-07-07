def init_logger(log_file = 'logs.log'):
    
    from logging import getLogger
    from logging import INFO
    from logging import FileHandler
    from logging import Formatter
    from logging import StreamHandler
    
    logger = getLogger()
    logger.setLevel(INFO)
    
    handler1 = StreamHandler()
    handler1.setFormatter(Formatter("%(message)s"))
    
    handler2 = FileHandler(filename=log_file)
    handler2.setFormatter(Formatter("%(message)s"))
    
    logger.addHandler(handler1)
    logger.addHandler(handler2)
    
    return logger