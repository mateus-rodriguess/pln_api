from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "API PLN"

    VOCAB_FNAME: str = "apps/pln/services/ttVocab"
    PATH_MY_WEIGHTS: str = 'apps/pln/weights_folder/my_weights'
    SQLALCHEMY_DATABASE_URL: str = "postgresql://admin:admin@db/app"
    TRAIN_CSV:  str = 'apps/pln/data/trainingandtestdata/train.csv'
    TEST_CSV: str = "apps/pln/data/trainingandtestdata/test.csv"
    
    SECRET_KEY: str = "hfaushbfub4u23b4u32b4b324j3" # default
    ALGORITHM: str = "HS256" # default
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 80

    class Config:
        case_sensitive = True
        env_prefix = ''
        env_file = '../.env'
        env_file_encoding = 'utf-8'



@lru_cache()
def get_settings():
    return Settings(_env_file='.env', _env_file_encoding='utf-8')
