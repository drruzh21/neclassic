from typing import Optional

from dotenv import load_dotenv
from openai import OpenAI, BaseModel
from pydantic import Field
from First_step_creating_parameters.Prompt_loader import PromptLoader

load_dotenv()

from pydantic import BaseModel, Field, Extra
from typing import Optional


class ProductCriteria(BaseModel):
    completeness: Optional[str] = Field(None,
                                        description="Indicates the level of completeness of the product, crucial for understanding functionality.")
    category: Optional[str] = Field(None, description="Helps classify products based on intended use or duty level.")
    color: Optional[str] = Field(None,
                                 description="A significant differentiator in product selection, especially for visibility.")
    size: Optional[str] = Field(None,
                                description="Critical for ensuring the right fit and comfort. Ensure size measurements are in meters (SI units). If input is in other units, convert to meters.")
    signs_of_difference: Optional[str] = Field(None,
                                               description="Indicates unique features or certifications influencing purchasing decisions.")
    volume: Optional[str] = Field(None,
                                  description="Relevant for products where size or capacity is a consideration. Ensure volume measurements are in cubic meters (SI units). If input is in other units, convert to cubic meters.")
    material: Optional[str] = Field(None,
                                    description="Important for understanding durability and suitability for specific environments.")
    protection_class: Optional[str] = Field(None,
                                            description="Crucial for safety products, indicating the level of protection offered.")
    temperature_protection: Optional[str] = Field(None,
                                                  description="Relevant for products needing to withstand specific temperature conditions. Ensure temperature is measured in Kelvin or Celsius (SI units). If input is in other units, convert to SI.")
    climate_zones: Optional[str] = Field(None,
                                         description="Important for understanding suitability for different environmental conditions.")
    size_range: Optional[str] = Field(None,
                                      description="Provides additional information about flexibility in sizing options. Ensure size range measurements are in meters (SI units). If input is in other units, convert to meters.")
    regulations: Optional[str] = Field(None, description="Important for compliance with industry standards.")

    class Config:
        extra = Extra.forbid  # Запрещаем дополнительные свойства


def structured_output_agent(data: str):
    # Подготовка данных для structured output агента
    prompt_loader = PromptLoader()
    system_prompt = prompt_loader.load_prompt("system_prompt_struct_output")

    messages = f"""
    Here is the data that you need to analyze:
    <product_description>
    {data}
    </product_description>
    """

    client = OpenAI()

    try:
        # Извлечение структурированной информации
        completion = client.beta.chat.completions.parse(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": messages}
            ],
            response_format=ProductCriteria  # Используем ProductCriteria как response_format
        )

        # Получаем извлеченную информацию
        data_to_save = completion.choices[0].message.parsed
        save_qualification(data_to_save)  # Сохраняем квалификацию в стейте
        return data_to_save

    except Exception as e:
        print(e)


def save_qualification(data_to_save):
    pass


if __name__ == "__main__":
    data_to_gpt = """
    ID: 2317220161, Наименование: КРАСКА ДЕКОРАТИВНАЯ ПОД ДЕРЕВО, Маркировка: KAOWA SEMENTOL, Регламенты (ГОСТ/ТУ): Неизвестно, Параметры: 750МЛ ОРЕХ, OKPD2_NAME: Материалы лакокрасочные для нанесения покрытий прочие, ГОСТ Название: Неизвестно
    """

    x = structured_output_agent(data_to_gpt)

    print(x)