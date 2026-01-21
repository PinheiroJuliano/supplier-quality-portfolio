import requests
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///data/suppliers.db")

users = requests.get("https://jsonplaceholder.typicode.com/users").json()
posts = requests.get("https://jsonplaceholder.typicode.com/posts").json()

df_users = pd.DataFrame(users)
df_posts = pd.DataFrame(posts)

kpis = (
    df_posts.groupby("userId")
    .size()
    .reset_index(name="orders")
)

kpis["delivery_on_time"] = (kpis["orders"] % 100)
kpis["non_conformity"] = 100 - kpis["delivery_on_time"]

kpis.to_sql("suppliers_kpis", engine, if_exists="replace", index=False)
