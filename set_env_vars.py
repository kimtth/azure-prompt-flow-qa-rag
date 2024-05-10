import os
from promptflow import tool


# The 'dummy_arg' is for the dependency injection before executing 'lookup_ai_search'
@tool
def set_env_var(dummy_arg):
    def read_config(file_name):
        config = {}
        with open(file_name, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line.strip():
                    key, value = line.strip().split('=')
                    config[key] = value
        return config

    config = read_config('env_var.config')

    return config