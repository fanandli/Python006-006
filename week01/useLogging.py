import logging

#默认是追加写入模式，且此配置只有效一次，所以要写在前面
logging.basicConfig(filename='test.log',
                    level=logging.DEBUG,
                    datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)s %(name)-8s %(levelname)-10s [line: %(lineno)d] %(message)s',
                    )

logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')