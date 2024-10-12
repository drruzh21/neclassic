import os


def get_project_root():
    """
    Get the root directory of the project.

    :return: Absolute path to the project root directory.
    """
    # Get the absolute path of the current file
    current_path = os.path.abspath(__file__)

    return os.path.dirname(current_path)


if __name__ == "__main__":
    print(get_project_root())