import os
import colorama
import termcolor
import datetime

class ADSLogger:
    file_handle = None
    is_open = False

    @staticmethod
    def open():
        colorama.init()
        home_dir = os.path.expanduser("~")
        ADSLogger.file_handle = open(os.path.join(home_dir, "ads.log"), 'a+')
        ADSLogger.is_open = True

    @staticmethod
    def close():
        if ADSLogger.is_open:
            ADSLogger.file_handle.close()

    @staticmethod
    def log(x):
        buf = f"[{str(datetime.datetime.now())}] Info: {x}"
        print(termcolor.colored(buf, 'green'))
        if ADSLogger.is_open:
            ADSLogger.file_handle.write(buf + '\n')

    @staticmethod
    def warn(x):
        buf = f"[{str(datetime.datetime.now())}] Warning: {x}"
        print(termcolor.colored(buf, 'yellow'))
        if ADSLogger.is_open:
            ADSLogger.file_handle.write(buf + '\n')

    @staticmethod
    def error(x):
        buf = f"[{str(datetime.datetime.now())}] ERROR: {x}"
        print(termcolor.colored(buf, 'red'))
        if ADSLogger.is_open:
            ADSLogger.file_handle.write(buf + '\n')