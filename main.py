import os
import re
import requests
import sys
from num2words import num2words
import os
import pandas as pd
import numpy as np
import tiktoken
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

df=pd.read_csv(os.path.join(os.getcwd(),f"shakespeare_plays.csv"))

df.rename(columns={"Unnamed: 0": "id"}, inplace=True)