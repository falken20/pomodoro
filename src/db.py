from mimetypes import init
import sqlite3
import sys
import os
from dotenv import load_dotenv, find_dotenv

from logger import Log, console

# Load env file
load_dotenv(find_dotenv())

DATABASE_URL = "pomodoro.db"
USER_APP = os.getenv("USER_APP", "RICHI")

conn = sqlite3.connect(DATABASE_URL)
cursor = conn.cursor()


def drop_tables(cursor: sqlite3.Cursor) -> None:
    try:
        Log.info("Deleting SUMMARY table...")
        cursor.execute("DROP TABLE IF EXISTS summary")

        conn.commit()

    except Exception as err:
        Log.error("Error deleting tables", err, sys)


def create_table_summary(cursor: sqlite3.Cursor) -> None:
    try:
        Log.info("Creating SUMMARY table...")
        sql = """CREATE TABLE summary (
                    user VARCHAR(40),
                    pomodoro_count INT,
                    cycles_count INT,
                    total_cycles_count INT
                );"""

        cursor.execute(sql)

        conn.commit()

    except Exception as err:
        Log.error("Error creating SUMMARY table", err, sys)


def init_table_summary(cursor: sqlite3.Cursor = cursor) -> None:
    try:
        Log.info("Initialazing SUMMARY table...")
        sql = f"""INSERT INTO summary (user, pomodoro_count, cycles_count, total_cycles_count)
                    VALUES ("{USER_APP}", 0, 0, 0);"""

        cursor.execute(sql)

        conn.commit()

        Log.info(f"Initialized table succesfully... {get_summary(cursor)}")

    except Exception as err:
        Log.error(
            f"Error initialazing SUMMARY table:\n{sql if 'sql' in locals() else ''}", err, sys)


def get_summary(cursor=cursor) -> list:
    """ Get data from summary table """
    try:
        Log.info(
            f"Getting data from summary table with filter user {USER_APP}")

        sql = f"SELECT * FROM summary WHERE user = '{USER_APP}'"
        cursor.execute(sql)

        # It is the same that "return cursor.execute(sql)" but you dont have to go over the object
        return cursor.fetchone()

    except Exception as err:
        Log.error(
            f"Error initialazing SUMMARY table:\n{sql if 'sql' in locals() else ''}", err, sys)


def update_summary(cursor=cursor) -> None:
    """ Update summary table adding new pomodoro """
    try:
        Log.info("Updating summary table...")

        summary = get_summary(cursor)
        Log.info(f"Getting summary data to update: {summary}")

        pomodoro_count = summary[1] + 1
        cycles_count = summary[2]
        total_cycles_count = summary[3]

        if pomodoro_count >= 4:
            cycles_count += 1
            total_cycles_count += 1
            pomodoro_count = 0

        sql = f"""UPDATE summary SET 
                    pomodoro_count = {pomodoro_count},
                    cycles_count = {cycles_count}, 
                    total_cycles_count = {total_cycles_count}
                  WHERE user = "{USER_APP}";"""

        cursor.execute(sql)

        conn.commit()

    except Exception as err:
        Log.error(
            f"Error updating SUMMARY table:\n{sql if 'sql' in locals() else ''}", err, sys)


def main():
    try:
        if input("Could you drop the tables if they exist (y/n)? ") in ["Y", "y"]:
            drop_tables(cursor)

        create_table_summary(cursor)
        init_table_summary(cursor)

    except Exception as err:
        Log.error("Error in config DB", err, sys)
    finally:
        conn.close() if conn else None


if __name__ == "__main__":
    console.rule("Pomodoro DB utils")
    main()
    console.rule("Process finished")
