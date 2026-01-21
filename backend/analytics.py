import sqlite3
import pandas as pd
import os

DB_PATH = "database/app.db"

def get_user_chats(user_id):
    """
    Fetch all chat records for a user.
    Returns a DataFrame with columns: mood, message
    """
    if not os.path.exists(DB_PATH):
        return pd.DataFrame(columns=["mood", "message"])

    conn = sqlite3.connect(DB_PATH)

    query = """
    SELECT mood, message
    FROM chats
    WHERE user_id = ?
    """

    df = pd.read_sql(query, conn, params=(user_id,))
    conn.close()

    return df
