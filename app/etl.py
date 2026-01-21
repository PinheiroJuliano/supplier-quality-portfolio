import requests
import pandas as pd
from app.database import engine

USERS_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_URL = "https://jsonplaceholder.typicode.com/posts"

def run():
    users = requests.get(USERS_URL).json()
    posts = requests.get(POSTS_URL).json()

    df_users = pd.DataFrame(users)[["id", "name"]]
    df_posts = pd.DataFrame(posts)[["userId", "id"]]

    kpis = (
        df_posts.groupby("userId")
        .count()
        .reset_index()
        .rename(columns={"id": "orders"})
    )

    kpis["delivery_on_time_pct"] = (kpis["orders"] % 100)
    kpis["non_conformity_pct"] = 100 - kpis["delivery_on_time_pct"]

    kpis["score"] = (
        kpis["delivery_on_time_pct"] * 0.6
        + (100 - kpis["non_conformity_pct"]) * 0.4
    )

    final_df = kpis.merge(
        df_users, left_on="userId", right_on="id"
    )[
        ["name", "orders", "delivery_on_time_pct", "non_conformity_pct", "score"]
    ]

    final_df.to_sql(
        "suppliers_kpis",
        engine,
        if_exists="replace",
        index=False
    )
