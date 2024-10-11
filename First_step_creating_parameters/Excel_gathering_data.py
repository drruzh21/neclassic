import openpyxl
import pyodbc

from First_step_creating_parameters.Excel_can_crawl_lists import ExcelSheetManager


class DatabaseHandler:
    """
    Класс для работы с базой данных Access, соединения таблиц и записи данных в Excel.
    """

    def __init__(self, db_path, excel_filename):
        """
        Инициализация объекта класса.

        :param db_path: Путь к базе данных Access.
        :param excel_filename: Имя файла Excel.
        """
        self.db_path = db_path
        self.excel_manager = ExcelSheetManager(excel_filename)

    def get_joined_data(self, group_id):
        """
        Извлекает данные из таблиц MTR, OKPD_2 и GOST с использованием SQL JOIN.

        :param group_id: Первые две цифры ОКПД2 для фильтрации.
        :return: Список данных, объединяющий информацию из таблиц MTR, OKPD_2 и GOST.
        """
        conn_str = (
                r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                r'DBQ=' + self.db_path + ';'
        )
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        # Обновленный SQL-запрос с корректной структурой
        query = f"""
            SELECT 
                MTR.[код СКМТР], 
                MTR.[Наименование], 
                MTR.[Маркировка], 
                MTR.[Регламенты (ГОСТ/ТУ)], 
                MTR.[Параметры], 
                MTR.[Базисная Единица измерения], 
                OKPD_2.[OKPD2_NAME],
                GOST.[GOST#Gost_title],
                GOST.[GOST#Gost_status],
                GOST.[GOST#Gost_data_start],
                GOST.[GOST#Gost_data_end]
            FROM (MTR
            LEFT JOIN OKPD_2 ON MTR.ОКПД2 = OKPD_2.OKPD2)
            LEFT JOIN GOST ON MTR.[Регламенты (ГОСТ/ТУ)] = GOST.[GOST#Gost_code]
            WHERE LEFT(MTR.ОКПД2, 2) = ?
        """

        cursor.execute(query, (group_id,))
        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        return rows

    def write_data_to_excel(self, group_id, data):
        """
        Записывает данные в соответствующий лист Excel.

        :param group_id: Идентификатор группы (лист Excel).
        :param data: Данные для записи.
        """
        workbook = openpyxl.load_workbook(self.excel_manager.filename)

        if str(group_id) in workbook.sheetnames:
            sheet = workbook[str(group_id)]
        else:
            # Создаем лист, если его нет
            sheet = workbook.create_sheet(title=str(group_id))

        # Добавляем заголовки, если они отсутствуют
        if sheet.max_row == 1:
            headers = [
                "Код СКМТР", "Наименование", "Маркировка", "Регламенты (ГОСТ/ТУ)",
                "Параметры", "Базисная Единица измерения", "OKPD2_NAME",
                "ГОСТ Название", "ГОСТ Статус", "ГОСТ Дата начала", "ГОСТ Дата окончания"
            ]
            sheet.append(headers)

        # Записываем данные в лист
        for row in data:
            # Заменяем None на пустую строку
            row = [val if val is not None else "" for val in row]
            sheet.append(row)

        # Сохраняем файл
        workbook.save(self.excel_manager.filename)
        print(f"Данные для group_id {group_id} записаны в файл.")

    def process_group_ids(self):
        """
        Основная функция, которая обрабатывает все group_id и записывает объединенные данные в Excel.
        """
        # Получаем список всех group_id из Excel
        group_ids = self.excel_manager.get_group_ids_from_sheet()

        for group_id in group_ids:
            # Извлекаем объединенные данные для текущего group_id
            data = self.get_joined_data(group_id)
            if data:
                # Записываем данные в соответствующий лист Excel
                self.write_data_to_excel(group_id, data)
            else:
                print(f"Нет данных для group_id {group_id}.")


# Пример использования
if __name__ == "__main__":
    db_path = r"C:\Hackaton_October\neclassic\main_data.accdb"
    excel_filename = 'main_data.xlsx'

    # Создаем объект класса DatabaseHandler
    db_handler = DatabaseHandler(db_path, excel_filename)

    # Запускаем процесс обработки данных
    db_handler.process_group_ids()
