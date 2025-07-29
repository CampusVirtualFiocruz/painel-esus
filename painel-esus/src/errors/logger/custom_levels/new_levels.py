import json
import logging

LOG_LEVELS = {
    "LOGIN": (100, "LOGIN"),
    "INSTALACAO": (101, "INSTALACAO"),
    "DOWNLOAD": (102, "DOWNLOAD"),
    "LOG_API": (103, "LOG_API"),
}

for level in LOG_LEVELS.values():
    logging.addLevelName(*level)


def login(self, message, *args, **kws):
    message, extra_info = base_log(message, **kws)
    self._log(LOG_LEVELS["LOGIN"][0], message, args, **kws)


def logapi(self, message, *args, **kws):
    message, extra_info = base_log(message, **kws)
    self._log(LOG_LEVELS["LOG_API"][0], message, args, **kws)


def base_log(message, **kws):
    extra_info = {}
    if len(kws.items()) != 0:
        for key, value in kws.items():
            extra_info[key] = value
        if kws["extra"] is not None:
            message += "\nINPUT_LOG_DATA:\n" + json.dumps(kws["extra"])
    return message, extra_info


def install(self, message, *args, **kws):
    message, extra_info = base_log(message, **kws)
    self._log(LOG_LEVELS["INSTALACAO"][0], message, args, extra=extra_info)

def download(self, message, *args, **kws):
    message, extra_info = base_log(message, **kws)
    self._log(LOG_LEVELS["DOWNLOAD"][0], message, args, extra=extra_info)

logging.Logger.login = login
logging.Logger.install = install
logging.Logger.download = download
logging.Logger.logapi = logapi
