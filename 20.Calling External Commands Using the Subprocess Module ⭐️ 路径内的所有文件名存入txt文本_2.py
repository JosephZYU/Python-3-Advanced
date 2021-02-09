import subprocess


def create_project(full_path='/Users/josephyu/Desktop/', project_name='new_project'):

    msg = f"cd {full_path} && \
            python -m venv {project_name}/venv && \
            cd {project_name} && \
            source {full_path}{project_name}/venv/bin/activate && \
            {full_path}{project_name}/venv/bin/python -m pip install --upgrade pip && \
            code ."

    # msg = f'cd {full_path} && python -m venv {project_name}/venv && source {full_path}{project_name}/venv/bin/activate && {full_path}{project_name}/venv/bin/python3 -m pip install --upgrade pip && code {full_path}{project_name}'
    subprocess.run(msg, shell=True)


create_project(project_name='Project_JosephYu')

"""
full_path = '/Users/josephyu/Desktop/'
project_name = 'new_project'

msg = f'cd {full_path} && python -m venv {project_name}/venv && source {project_name}/venv/bin/activate && {full_path}{project_name}/venv/bin/python3 -m pip install --upgrade pip && code {full_path}{project_name}'

subprocess.run(msg, shell=True)

class Manager(Employee):
    def __init__(self, first, last, pay, staffs=None):
        # 🧠 default arguments = None
        super().__init__(first, last, pay)
        if not staffs:
            self.staffs = []
        else:
            self.staffs = staffs
"""
