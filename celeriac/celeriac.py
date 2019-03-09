"""
Authors:
 - Alexandre COMBEAU
"""

import os
import subprocess
import sys

import git


class Celeriac:
    """
    Celeriac app main class
    """

    def __init__(
            self,
            name: str,
            flow: bool = False,
            skinos: bool = False,
            venv: str = 'local'
    ) -> None:
        self.__name = name
        self.__skinos = skinos
        self.__flow = flow
        self.__venv = venv
        self.__repo = None

    @classmethod
    def print_err(cls, msg: str) -> None:
        """
        Basic error print (stderr
        :param msg: str
        :return: None
        """
        print(msg, file=sys.stderr)

    def git_init(self) -> None:
        """
        Init git directory
        :return: None
        """
        if os.path.exists(self.__name):
            self.print_err('"{name}" already exists.'.format(name=self.__name))
            exit(2)

        rorepo = None
        repo = git.Repo(rorepo)

        self.__repo = repo.init(self.__name, mkdir=True)

        if self.__flow:
            self.__git_flow_init()

    def __git_flow_init(self) -> bool:
        """
        git flow init
        :return:
        """
        cmd = ('git', 'flow', 'init', '-d')
        cwd = os.path.join(os.getcwd(), self.__name)

        try:
            process = subprocess.run(
                cmd,
                shell=False,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                cwd=cwd
            )
        except FileNotFoundError:
            self.print_err('"git" command not found.')
            exit(2)
        except subprocess.CalledProcessError as ex:
            self.print_err(str(ex))
            exit(2)

        if process.returncode != 0:
            self.print_err(
                'An error occured during "{}" shell command runtime.'.format(' '.join(cmd))
            )
            exit(2)

    def generate_template(self) -> None:
        """
        Generation of basic directories and files template
        :return:
        """
        # TODO: generate template structure


if __name__ == '__main__':
    C = Celeriac('hello', flow=True)
    C.git_init()
