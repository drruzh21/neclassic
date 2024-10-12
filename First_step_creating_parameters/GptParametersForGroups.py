import json

import openpyxl
from First_step_creating_parameters.Excel_can_crawl_lists import ExcelSheetManager
from First_step_creating_parameters.Excel_json_stat import ExcelJsonStat
from First_step_creating_parameters.First_GPT_Agent import GptService
from json_handler import StringHandler
from repository.PostgresRepository import PostgresRepository


class GptCombinedProcessor:
    """
    Класс для обработки глобального словаря параметров и частот,
    объединения его с данными из первых 20 строк каждого листа,
    передачи в GPT сервис и записи результата в столбец J Excel-файла.
    """

    def __init__(self, excel_filename, system_prompt_file_name, basic_prompt_file_name, gpt_service=None):
        """
        Инициализация объекта класса.

        :param excel_filename: Имя файла Excel.
        :param system_prompt_file_name: Название файла системного промпта.
        :param basic_prompt_file_name: Название файла базового промпта.
        :param gpt_service: Экземпляр класса GptService для взаимодействия с GPT. Если None, создаётся новый.
        """
        self.excel_manager = ExcelSheetManager(excel_filename)
        self.excel_filename = excel_filename
        self.system_prompt_file_name = system_prompt_file_name
        self.basic_prompt_file_name = basic_prompt_file_name
        self.gpt_service = gpt_service if gpt_service else GptService()


    def get_headers(self, json_top_criteria: str):
        table_headers = ['ID', 'Наименование', 'Маркировка', 'Регламенты (ГОСТ/ТУ)', 'Параметры', 'OKPD2_NAME',
                         'ГОСТ Название']

        if '<top_criteria>' in json_top_criteria and '</top_criteria>' in json_top_criteria:
            start = json_top_criteria.find('<top_criteria>') + len('<top_criteria>')
            end = json_top_criteria.find('</top_criteria>')
            json_str = json_top_criteria[start:end].strip()
            try:
                json_data = json.loads(json_str)
                top_criteria_values = json_data.get("top_criteria", [])
                if len(top_criteria_values) > 0:
                    for item in top_criteria_values:
                        table_headers.append(item)
            except json.JSONDecodeError as e:
                print("Ошибка при парсинге JSON:", e)
            return table_headers


    def process_combined_data(self):
        """
        Обрабатывает глобальный словарь параметров и частот,
        объединяет его с данными строк, передаёт в GPT и записывает результат в столбец J каждого листа.

        :param data_dict: Глобальный словарь с параметрами и их частотами.
        :param data_strings: Словарь, где ключ — название листа, а значение — строка с данными первых 20 строк листа.
        """
        # Загружаем Excel-файл с возможностью записи
        workbook = openpyxl.load_workbook(self.excel_filename)
        try:
            excel_file_jsoner = ExcelJsonStat(workbook)

            # Получаем список всех group_id из Excel (предполагается, что они соответствуют названиям листов)
            group_ids = self.excel_manager.get_group_ids_from_sheet()
            print(f"Получено {len(group_ids)} group_id из Excel.")

            for group_id in group_ids:
                data_strings = excel_file_jsoner.get_jsons_from_sheet(group_id)
                data_dict = excel_file_jsoner.get_sheet_stat(group_id)

                data_strings = ' , '.join(data_strings)

                data_dict_string = self.convert_dict_to_string(data_dict)
                print(f"Преобразованный глобальный словарь в строку: {data_dict_string}")

                # Объединяем data_dict и data_string
                combined_input = f"<parameters_frequency>{data_dict_string}</parameters_frequency>\n\nДанные первых 20 строк группы '{group_id}':\n<first_20_rows>{data_strings}</first_20_rows>"

                # Передаём объединённую строку в GPT
                try:
                    result = self.gpt_service.gpt(
                        input_data=combined_input,
                        system_prompt_file_name=self.system_prompt_file_name,
                        basic_prompt_file_name=self.basic_prompt_file_name
                    )
                except Exception as gpt_error:
                    parsed_result = "Ошибка GPT"
                else:
                    # Получаем parsed_result, если он есть
                    parsed_result = result.get('parsed_result', "Неизвестно")
                    if not parsed_result:
                        parsed_result = "Неизвестно"

                self.get_headers(parsed_result)
                # self.repo.create_table(group_id, self.get_headers(parsed_result))

            print("Все словари успешно обработаны и сохранены.")

        except Exception as e:
            workbook.save(self.excel_filename)
            print("Произошла ошибка при обработке словарей:", e)

    @staticmethod
    def convert_dict_to_string(param_freq_dict):
        """
        Преобразует глобальный словарь параметров и их частот в строку.

        :param param_freq_dict: Глобальный словарь с параметрами и их частотами.
        :return: Строка, сформированная из ключей и значений словаря.
        """
        return ", ".join([f"{key}: {value}" for key, value in param_freq_dict.items()])


# Пример использования
if __name__ == "__main__":
    excel_filename = 'main_data_with_analysis.xlsx'
    system_prompt_file_name = "group_parameters_system_prompt"
    basic_prompt_file_name = "group_parameters_basic_prompt"

    # Создаем экземпляр GptService
    gpt_service = GptService()

    # Создаем экземпляр GptCombinedProcessor
    processor = GptCombinedProcessor(
        excel_filename=excel_filename,
        system_prompt_file_name=system_prompt_file_name,
        basic_prompt_file_name=basic_prompt_file_name,
        gpt_service=gpt_service
    )

    # Запускаем процесс обработки данных
    processor.process_combined_data()
