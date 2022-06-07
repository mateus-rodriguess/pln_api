from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "API PLN"
    vocab_fname: str = "apps/pln/services/ttVocab"
    path_my_weights: str = 'apps/pln/weights_folder/my_weights'
    SQLALCHEMY_DATABASE_URL: str = "postgresql://admin:admin@db/app"
    TRAIN_CSV:  str = 'apps/pln/data/trainingandtestdata/train.csv'
    TEST_CSV: str = "apps/pln/data/trainingandtestdata/test.csv"
    
    class Config:
        case_sensitive = True
        env_prefix = ''
        # não estou ultilizando .env
        env_file = '../.env'
        env_file_encoding = 'utf-8'



@lru_cache()
def get_settings():
    return Settings(_env_file='.env', _env_file_encoding='utf-8')
