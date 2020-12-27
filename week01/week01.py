import os,time,logging
'''
编写一个函数, 当函数被调用时，将调用的时间记录在日志中, 日志文件的保存位置建议为：/var/log/python- 当前日期 /xxxx.log
'''

calledTime = time.strftime('%Y-%m-%d',time.localtime())
logPartPath = 'var/log/python-{}/'.format(calledTime)

if not os.path.exists(logPartPath):
    os.mkdir(logPartPath)

logPath = logPartPath + "logging.log"

logging.basicConfig(filename=r"{}".format(logPath),
                    level=logging.DEBUG,
                    datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)s.%(msecs)d %(levelname)s  %(name)s  [line: %(lineno)d] %(message)s')

def log_put():
    logging.info("ok!")

if __name__ == "__main__":
    log_put()
    
 
# 改进：使用pathlib（没验证正确与否，虚拟环境崩了...windows环境下'PureWindowsPath' object has no attribute 'exists'）
# import time,logging
# from pathlib import Path, PurePath

# '''
# 编写一个函数, 当函数被调用时，将调用的时间记录在日志中, 日志文件的保存位置建议为：/var/log/python- 当前日期 /xxxx.log
# '''

# calledTime = time.strftime('%Y-%m-%d',time.localtime())
# logPartPath = PurePath('var/log/python/').joinpath(calledTime)

# if not logPartPath.exists():
#     logPartPath.mkdir()

# logFilePath = logPartPath + "logging.log"

# logging.basicConfig(filename=r"{}".format(logFilePath),
#                     level=logging.DEBUG,
#                     datefmt='%Y-%m-%d %H:%M:%S',
#                     format='%(asctime)s.%(msecs)d %(levelname)s  %(name)s  [line: %(lineno)d] %(message)s')

# def log_put():
#     logging.info("ok!")

# if __name__ == "__main__":
#     log_put()
