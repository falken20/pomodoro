import sqlite3
import sys
import os
from dotenv import load_dotenv, find_dotenv
from datetime import date, datetime

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

        Log.info("Tables succesfully deleted")

    except Exception as err:
        Log.error("Error deleting tables", err, sys)


def create_table_summary(cursor: sqlite3.Cursor) -> None:
    try:
        Log.info("Creating SUMMARY table...")
        sql = """CREATE TABLE summary (
                    user VARCHAR(40),
                    pomodoro_count INT,
                    cycles_count INT,
                    total_cycles_count INT,
                    date_update timestamp
                );"""

        cursor.execute(sql)

        conn.commit()

        Log.info("SUMMARY table succesfully created")

    except Exception as err:
        Log.error("Error creating SUMMARY table", err, sys)


def init_table_summary(cursor: sqlite3.Cursor = cursor) -> None:
    try:
        Log.info("Dropping and Initializing SUMMARY table...")

        sql = f"DELETE FROM summary WHERE user = '{USER_APP}'"
        cursor.execute(sql)

        sql = f"""INSERT INTO summary (user, pomodoro_count, cycles_count, total_cycles_count, date_update)
                    VALUES (?, ?, ?, ?, ?);"""

        data = (USER_APP, 0, 0, 0, date.today())
        cursor.execute(sql, data)

        conn.commit()

        Log.info(f"Table initialized succesfully... {get_summary(cursor)}")

    except Exception as err:
        Log.error(
            f"Error initializing SUMMARY table:\n{sql if 'sql' in locals() else ''}", err, sys)


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
            f"Error initializing SUMMARY table:\n{sql if 'sql' in locals() else ''}", err, sys)


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


def init_cycles_count(cursor=cursor):
    """ Update cycles count the first time in the day"""
    try:
        Log.info("Checking if date_update is today date")
        date_update = get_summary()[4]
        date_update = datetime.strptime(date_update, "%Y-%m-%d").date()

        if date_update < date.today():
            Log.info("Cycles count initializing...")
            sql = f"""UPDATE summary SET cycles_count = 0, date_update = ?
                        WHERE user = ?"""
            cursor.execute(sql, (date.today(), USER_APP))
            conn.commit()

    except Exception as err:
        Log.error(
            f"Error updating SUMMARY table:\n{sql if 'sql' in locals() else ''}", err, sys)


def exec_sql(cursor, sql) -> list:
    try:
        Log.info(f"Executing the sentence:\n{sql=}")
        data = cursor.execute(sql)
        conn.commit()

        return data

    except Exception as err:
        Log.error(
            f"Error updating SUMMARY table:\n{sql if 'sql' in locals() else ''}", err, sys)


def main():
    try:
        option = None
        while option != "0":
            print("     1. Drop tables")
            print("     2. Create summary table")
            print("     3. Init summary table")
            print("     9. Run SQL sentence")
            print("     0. Exit")
            option = input("Choose the option: ")

            if option == "1":
                drop_tables(cursor)
            elif option == "2":
                create_table_summary(cursor)
            elif option == "3":
                init_table_summary(cursor)
            elif option == "9":
                sql = input("Write SQL: ")
                data = exec_sql(cursor, sql)
                for row in data:
                    print(row)
            elif option != "0":
                print("Sorry, incorrect option")

    except Exception as err:
        Log.error("Error in config DB", err, sys)
    finally:
        conn.close() if conn else None


if __name__ == "__main__":
    console.rule("Pomodoro DB utils")
    main()
    console.rule("Process finished")
