import logging
import os

from get_proj_root import get_project_root


class PromptLoader:
    def __init__(self, directory='prompts'):
        self.directory = directory

    def load_prompt(self, file_name):
        project_root = get_project_root()
        relative_path = f"{project_root}/prompts/{file_name}.txt"
        file_path = os.path.abspath(relative_path)
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                prompt = file.read()
                return prompt
        except FileNotFoundError:
            raise
        except Exception as e:
            raise


if __name__ == "__main__":
    loader = PromptLoader()
    prompt = loader.load_prompt('system_prompt')
    print(prompt)
    prompt = loader.load_prompt('basic_prompt')
    print(prompt)
