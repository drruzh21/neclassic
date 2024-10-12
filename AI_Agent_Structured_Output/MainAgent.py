from openai import OpenAI

from AI_Agent_Structured_Output.AbstractStructure import AbstractStructure
from AI_Agent_Structured_Output.Structures.WarCrimes import ProductCriteria14
from First_step_creating_parameters.Prompt_loader import PromptLoader

from repository.SaveData import save_data

class AiAgentStructuredOutput:
    def __init__(self, base_data: list[str]):
        self.base_data = base_data

    def structured_output_agent(self, data: list[str], criteria: AbstractStructure):
        # Подготовка данных для structured output агента
        prompt_loader = PromptLoader()
        system_prompt = prompt_loader.load_prompt("system_prompt_struct_output")

        final_data = []
        for product_data in data:
            messages = f"""
            Here is the data that you need to analyze:
            <product_description>
            {product_data}
            </product_description>
            """

            client = OpenAI()
            # Извлечение структурированной информации
            completion = client.beta.chat.completions.parse(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": messages}
                ],
                response_format=type(criteria)  # Используем ProductCriteria как response_format
            )

            # Получаем извлеченную информацию
            data_to_save = completion.choices[0].message.parsed

            # Преобразуем объект ProductCriteria в список строк
            data_dict = data_to_save.dict()  # Преобразуем в словарь
            data_to_save = [str(value) for value in data_dict.values()]  # Преобразуем значения в строки

            data_to_save = self.base_data + data_to_save
            final_data.append(data_to_save)
            print(data_to_save)
            print('\n\n')

        save_data(final_data)  # Сохраняем квалификацию в стейте
        print("Data has been saved to sql database:")
        print(final_data)


if __name__ == "__main__":
    data_to_gpt = ["ID: 2317220161, Наименование: КРАСКА ДЕКОРАТИВНАЯ ПОД ДЕРЕВО, Маркировка: KAOWA SEMENTOL, Регламенты (ГОСТ/ТУ): Неизвестно, Параметры: 750МЛ ОРЕХ, OKPD2_NAME: Материалы лакокрасочные для нанесения покрытий прочие, ГОСТ Название: Неизвестно", "ID: 2317220162, Наименование: КРАСКА ДЕКОРАТИВНАЯ ПОД ДЕРЕВО, Маркировка: KAOWA SEMENTOL, Регламенты (ГОСТ/ТУ): Неизвестно, Параметры: 250МЛ ОРЕХ, OKPD2_NAME: Материалы лакокрасочные для нанесения покрытий прочие, ГОСТ Название: Неизвестно"]

    base_data_ = ["14", "ID", "Наименование", "Маркировка", "Регламенты (ГОСТ/ТУ)", "Параметры", "OKPD2_NAME", "ГОСТ Название"]

    agent = AiAgentStructuredOutput(base_data_)

    criteria_ = ProductCriteria14()

    x = agent.structured_output_agent(data_to_gpt, criteria_)

    print(x)