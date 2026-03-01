import logging
import pandas as pd
from datetime import datetime
from typing import Dict

import requests
from airflow.decorators import dag, task



API = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true"


@dag(schedule=None, start_date=datetime(2021, 12, 1), catchup=False)
def sample_taskflow():
    @task(task_id="extract", retries=2)
    def extract_bitcoin_price() -> Dict[str, float]:
        return requests.get(API).json()["bitcoin"]

    @task
    def process_data(response: Dict[str, float]):
        logging.info(response)
        data = {
            "usd": [response["usd"]],
            "change": [response["usd_24h_change"]],
        }
        return pd.DataFrame(data)

    @task
    def store_data(dataframe):
        logging.info(f"Storing USD -  {dataframe['usd'].loc[0]}, change -  {dataframe['change'].loc[0]} ")
        dataframe.to_csv('bitcoin_price.csv', index=False)

    store_data(process_data(extract_bitcoin_price()))

sample_taskflow()