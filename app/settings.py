from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = 'taskbuilder'
    description: str = 'Build system to automate and speed up routine processes'
    version: str = "0.1.0"
    contact: dict = {
        'name': 'Artyom Kropp',
        'email': 'artyomkropp@gmail.com',
    }
    tags_metadata: list = [
        {
            "name": "Tasks",
            "description": "Task operations",
        },
    ]
    tasks_dir: str = '/builds'

    class Config:
        case_sensitive = True
        env_file = './.env'


settings = Settings()
