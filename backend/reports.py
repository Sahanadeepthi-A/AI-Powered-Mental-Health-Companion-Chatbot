import sqlite3
import pandas as pd
from datetime import datetime, timedelta

def get_user_report(user_id, days=7):
    conn = sqlite3.connect("database/app.db")

    since = datetime.now() - timedelta(days=days)

    query = """
    SELECT mood, message
    FROM chats
    WHERE user_id = ?
    """

    df = pd.read_sql(query, conn, params=(user_id,))
    conn.close()

    return df
