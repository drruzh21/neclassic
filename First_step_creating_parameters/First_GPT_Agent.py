import os

from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

from First_step_creating_parameters.Prompt_loader import PromptLoader

load_dotenv()


class GptService():
    def __init__(self,
                 ai_model: ChatOpenAI = ChatOpenAI(model_name='gpt-4o-mini', temperature=0), parser=StrOutputParser()):
        self.ai_model = ai_model
        self.parser = parser

    def gpt(self, input_data: str, system_prompt_file_name: str, basic_prompt_file_name: str) -> dict:
        prompt_loader = PromptLoader()
        system_prompt = prompt_loader.load_prompt(system_prompt_file_name)
        system_prompt = SystemMessage(content=system_prompt)
        prompt = prompt_loader.load_prompt(basic_prompt_file_name)
        prompt = prompt.replace("{{DATA}}", input_data)

        prompt = HumanMessage(content=prompt)

        messages = [
            system_prompt,
            prompt
        ]

        message = self.ai_model.invoke(messages)
        parsed_result = self.parser.invoke(message)

        res = {
            "parsed_result": parsed_result,
            "token_usage": message.response_metadata["token_usage"]
        }

        return res


if __name__ == "__main__":
    service = GptService()
    result = service.gpt(
        """
        123
        """,

        "first_prompt")
    print('\n')
    print("\n")
    print(result["parsed_result"])
    print('\n')
    print(result["token_usage"])