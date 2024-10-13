from operator import index

from openai import OpenAI

from AI_Agent_Structured_Output.AbstractStructure import AbstractStructure
from AI_Agent_Structured_Output.Structures.WarCrimes import ProductCriteria14
from First_step_creating_parameters.Prompt_loader import PromptLoader
from repository.PostgresRepository import PostgresRepository


class AiAgentStructuredOutput:
    def __init__(self):
        db_config = {
            'dbname': 'neclassic',
            'user': 'neclassic',
            'password': 'neclassic',
            'host': 'localhost',
            'port': 5434
        }
        self.repo = PostgresRepository(db_config)

    def structured_output_agent(self, data_batch: list[list[str]], criteria: AbstractStructure, sheet_name: str):
        # Подготовка данных для structured output агента
        prompt_loader = PromptLoader()
        system_prompt = prompt_loader.load_prompt("system_prompt_struct_output")

        final_data = []
        for product_data in data_batch:
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

            data_to_save = product_data + data_to_save
            final_data.append(data_to_save)
            print('\n\n==')
            print(data_to_save)
            print('\n\n==')

        self.repo.insert_data(table_index=int(sheet_name), data_batch=final_data)
        print("Data has been saved to sql database:")
        print(final_data)


if __name__ == "__main__":
    data_to_gpt = [["2317220161", "КРАСКА ДЕКОРАТИВНАЯ ПОД ДЕРЕВО", "KAOWA SEMENTOL", "Неизвестно", "750МЛ ОРЕХ",
                    "Материалы лакокрасочные для нанесения покрытий прочие", "Неизвестно"],
                   ["2317220162", "КРАСКА ДЕКОРАТИВНАЯ ПОД ДЕРЕВО", "KAOWA SEMENTOL", "Неизвестно", "250МЛ ОРЕХ",
                    "Материалы лакокрасочные для нанесения покрытий прочие", "Неизвестно"],
                   ["2317220163", "КРАСКА ДЕКОРАТИВНАЯ ПОД ДЕРЕВО", "KAOWA SEMENTOL", "Неизвестно", "500МЛ ОРЕХ",
                    "Материалы лакокрасочные для нанесения покрытий прочие", "Неизвестно"]]

    agent = AiAgentStructuredOutput()
    criteria_ = ProductCriteria14()

    x = agent.structured_output_agent(data_to_gpt, criteria_, "14")

    print(x)
