# pylint: disable=E1131,C0103,W0613,R0913
import datetime as dt
import json
import logging
import os
import pathlib
from logging.handlers import TimedRotatingFileHandler

LOG_RECORD_BUILTIN_ATTRS = {
    "args",
    "asctime",
    "created",
    "exc_info",
    "exc_text",
    "filename",
    "funcName",
    "levelname",
    "levelno",
    "lineno",
    "module",
    "msecs",
    "message",
    "msg",
    "name",
    "pathname",
    "process",
    "processName",
    "relativeCreated",
    "stack_info",
    "thread",
    "threadName",
    "taskName",
}


class JSONFileHandler(TimedRotatingFileHandler):

    def __init__(
        self,
        filename="app.jsonl",
        formatter="json",
        when="D",
        interval=10,
        backupCount=2,
        encoding="utf-8",
        mode="a",
        delay=False,
    ):

        super().__init__(
            filename=self.get_filename_location(filename),
            encoding=encoding,
            delay=delay,
            interval=interval,
            when=when,
            backupCount=backupCount,
        )
        self.filename = filename

    def get_filename_location(self, filename=None):
        ROOT_DIR = pathlib.Path(__file__).parent.parent.parent.parent
        config_json_path = os.path.join(
            ROOT_DIR, filename if filename is not None else self.filename
        )
        config_file = pathlib.Path(config_json_path)
        return config_file


class JSONFormatter(logging.Formatter):
    def __init__(
        self,
        *,
        fmt_keys: dict[str, str] | None = None,
    ):
        super().__init__()
        self.fmt_keys = fmt_keys if fmt_keys is not None else {}

    def format(self, record: logging.LogRecord) -> str:
        message = self._prepare_log_dict(record)
        return json.dumps(message, default=str)

    def _prepare_log_dict(self, record: logging.LogRecord):
        message = record.getMessage().split("INPUT_LOG_DATA:")[0]
        always_fields = {
            "message": message,
            "timestamp": dt.datetime.fromtimestamp(
                record.created, tz=dt.timezone.utc
            ).isoformat(),
        }
        if record.exc_info is not None:
            always_fields["exc_info"] = self.formatException(record.exc_info)

        if record.stack_info is not None:
            always_fields["stack_info"] = self.formatStack(record.stack_info)

        message = {
            key: (
                msg_val
                if (msg_val := always_fields.pop(val, None)) is not None
                else getattr(record, val)
            )
            for key, val in self.fmt_keys.items()
        }
        message.update(always_fields)

        for key, val in record.__dict__.items():
            if key not in LOG_RECORD_BUILTIN_ATTRS:
                message[key] = val

        return message
