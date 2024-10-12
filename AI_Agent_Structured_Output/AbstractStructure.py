from pydantic import Extra, BaseModel


class AbstractStructure(BaseModel):
    class Config:
        extra = Extra.forbid  # Запрещаем дополнительные свойства
