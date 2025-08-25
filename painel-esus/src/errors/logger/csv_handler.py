# pylint: disable=E1131,C0103,W0613,R0913,R0902,W0702
import csv
import datetime as dt
import logging
import os
import pathlib
import time
from logging.handlers import TimedRotatingFileHandler


class CsvFileHandler(TimedRotatingFileHandler):

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
        self.when = when.upper()
        super().__init__(
            filename=self.get_filename_location(filename),
            encoding=encoding,
            delay=delay,
            interval=interval,
            when=when,
            backupCount=backupCount,
        )
        self.filename = filename

        self.interval = interval
        self.backupCount = backupCount
        self.writer = csv.writer(self.stream)
        self._configure_intervals()
        self.current_time = int(time.time())

    def _rotate_needed(self):
        current_time = int(time.time())
        diff = current_time - self.current_time
        if diff > self.interval:
            return True
        return False

    def _configure_intervals(self):
        file_split = self.filename.split(".")
        self.postfix = f".{file_split[1]}"
        self.prefix = file_split[0]

        if self.when == "S":
            self.interval = 1  # one second
            self.suffix = "%Y-%m-%d_%H-%M-%S"
            self.extMatch = r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}$"
        elif self.when == "M":
            self.interval = 60  # one minute
            self.suffix = "%Y-%m-%d_%H-%M"
            self.extMatch = r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}$"
        elif self.when == "H":
            self.interval = 60 * 60  # one hour
            self.suffix = "%Y-%m-%d_%H"
            self.extMatch = r"^\d{4}-\d{2}-\d{2}_\d{2}$"
        elif self.when == "D" or self.when.upper() == "MIDNIGHT":
            self.interval = 60 * 60 * 24  # one day
            self.suffix = "%Y-%m-%d"
            self.extMatch = r"^\d{4}-\d{2}-\d{2}$"
        elif self.when.startswith("W"):
            self.interval = 60 * 60 * 24 * 7  # one week
            if len(self.when) != 2:
                raise ValueError(
                    "You must specify a day for weekly rollover from 0 to 6 (0 is Monday): %s"
                    % self.when
                )
            if self.when[1] < "0" or self.when[1] > "6":
                raise ValueError(
                    "Invalid day specified for weekly rollover: %s" % self.when
                )
            self.dayOfWeek = int(self.when[1])
            self.suffix = "%Y-%m-%d"
            self.extMatch = r"^\d{4}-\d{2}-\d{2}$"
        else:
            raise ValueError("Invalid rollover interval specified: %s" % self.when)

    def _get_filename(self, filename):

        now = dt.datetime.now().strftime("%Y-%m-%d %H:%M")
        if self.when.upper() == "MIDNIGHT" or self.when.upper() == "D":
            now = dt.datetime.now().strftime("%Y-%m-%d")
        if self.when.upper() == "S":
            now = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        name = filename.replace(".csv", "")
        return f"{name}{now}.csv"

    def get_filename_location(self, filename=None):
        if filename is not None:
            filename = self._get_filename(filename)
        else:
            filename = self._get_filename(self.filename)

        ROOT_DIR = pathlib.Path(__file__).parent.parent.parent.parent
        config_json_path = os.path.join(
            ROOT_DIR, filename if filename is not None else filename
        )
        config_file = pathlib.Path(config_json_path)
        return config_file

    def doRollover(self):
        if self.stream:
            self.stream.close()
            self.stream = None

        self.baseFilename = self._get_filename(self.filename)
        self.mode = "a"
        self.stream = self._open()
        self.writer = csv.writer(self.stream)
        self.rolloverAt = int(time.time())
        self.current_time = int(time.time())
        self._delete_files()

    def _delete_files(self):
        if self.backupCount > 0:
            for s in self._getFilesToDelete(self.get_filename_location(self.filename)):
                try:
                    os.remove(s)
                except:
                    ...

    def _getFilesToDelete(self, new_file_name):
        dir_name, _ = os.path.split(new_file_name)
        if dir_name == "":
            return []
        file_names = os.listdir(dir_name)
        result = []
        for file_name in file_names:
            if self.prefix in file_name and self.postfix in file_name:
                _date = file_name.replace(self.prefix, "").replace(self.postfix, "")
                result.append({"file": f"{dir_name}/{file_name}", "date": _date})

        result = list(sorted(result, key=lambda x: x["date"]))
        if len(result) > self.backupCount:
            idx = len(result) - self.backupCount
            result = [file["file"] for file in result[:idx]]
        else:
            result = [file["file"] for file in result]
        return result

    def check_header(self):
        if self.stream.tell() == 0:
            self.writer.writerow(["Timestamp", "Level", "Arquivo", "Message"])

    def emit(self, record):
        try:
            self.baseFilename = self.get_filename_location()
            self.check_header()
            # Format the log record into a list of values for the CSV row
            row = [
                dt.datetime.fromtimestamp(record.created, tz=dt.timezone.utc).strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),
                record.levelname,
                f"{record.filename}.{record.funcName}:{record.lineno}",
                str(record.getMessage()),
            ]
            self.writer.writerow(row)
            self.flush()  # Ensure data is written to the file immediately
            if self._rotate_needed():
                self.doRollover()
        except Exception:
            self.handleError(record)


class CsvFormatter(logging.Formatter):
    def __init__(
        self,
        *,
        fmt_keys: dict[str, str] | None = None,
    ):
        super().__init__()
        self.fmt_keys = fmt_keys if fmt_keys is not None else {}

    def format(self, record: logging.LogRecord) -> str:
        return self._prepare_log_row(record)

    def _prepare_log_row(self, record: logging.LogRecord):
        row = {
            "asctime": dt.datetime.fromtimestamp(
                record.created, tz=dt.timezone.utc
            ).strftime("%Y-%m-%d %H:%M:%S"),
            "levelname": record.levelname,
            "filename": f"{record.filename}.{record.funcName}:{record.lineno}",
            "message": str(record.getMessage()),
        }
        return row
