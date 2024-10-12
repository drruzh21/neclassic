from json_handler import StringHandler
import openpyxl


class ExcelJsonStat:
    def __init__(self, filename):
        self.filename = filename
        self.rows_number = 20

    def get_jsons_from_sheet(self, sheet_name='Лист1', column="I"):
        workbook = openpyxl.load_workbook(self.filename)
        sheet = workbook[sheet_name]

        jsons = []
        for i in range(2, self.rows_number + 2):
            raw = sheet[f"{column}{i}"]
            jsons.append(raw.value)

        return jsons

    def get_sheet_stat(self, sheet_name='Лист1', column="I"):
        jsons = self.get_jsons_from_sheet(sheet_name, column)
        handler = StringHandler(jsons)
        handler.handle()

        return handler.keys
