"""
Template class files
"""

import os
import json


class Template:
    """
    Template class
    """

    def __init__(self, dirs: list, files: dict, data: dict):
        """
        :param dirs:
        :param file:
        """
        self.dirs = dirs
        self.files = files
        self.data = data

    def generate(self):
        self.create_dirs()
        self.create_files()

    def create_dirs(self):
        """

        :return:
        """
        for dirname in self.dirs:
            self.create_dir(dirname, self.data)

    def create_files(self):
        """
        :return:
        """
        for filename, content in self.files.items():
            self.create_file(filename, content, self.data)


    @classmethod
    def create_dir(cls, path: str, data: dict):
        """

        :param data:
        :param path:
        :param dir:
        :return:
        """
        path = os.path.join(data['name'], path)
        try:
            os.mkdir(cls.format_content(path, data))
        except FileExistsError:
            pass


    @classmethod
    def create_file(cls, path: str, content: str, data: dict):
        """

        :param data:
        :param content:
        :param path:
        :param file:
        :return:
        """
        path = os.path.join(data['name'], cls.format_content(path, data))
        print(path)
        with open(cls.format_content(path, data), 'w') as file:
            file.write(content)


    @classmethod
    def format_content(cls, content: str, data: dict):
        """

        :param content:
        :param data:
        :return:
        """
        content = content.format(
            name=data['name']
        )
        return content


    @classmethod
    def from_file(cls, filename: str, data: dict):
        """
        build object from filename (JSON)
        :param filename:
        :param data:
        :return:
        """
        with open(filename, 'r') as file:
            content = json.load(file)
        return Template(content['dirs'], content['files'], data)
