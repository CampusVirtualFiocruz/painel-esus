from src.errors.logger.csv_handler import CsvFileHandler


def test_get_delete_list():
    csv = CsvFileHandler(
        filename="painel_esus_log.csv",
        formatter="csv",
        when="M",
        interval=1,
        backupCount=2,
        encoding="utf-8",
        mode="a",
        delay=False,
    )
    file_path = csv.get_filename_location(csv.filename)
    result = csv.getFilesToDelete(file_path)
    csv._delete_files()
    assert len(result) > 0



