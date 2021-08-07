"""
https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/install-microsoft-odbc-driver-sql-server-macos?view=sql-server-ver15

brew install unixodbc
brew tap microsoft/mssql-release https://github.com/Microsoft/homebrew-mssql-release
brew update
HOMEBREW_NO_ENV_FILTERING=1 ACCEPT_EULA=Y brew reinstall msodbcsql mssql-tools
odbcinst -j
otool -L /usr/local/lib/libmsodbcsql.17.dylib
"""

import argparse
import json
import pyodbc

parser = argparse.ArgumentParser()
parser.add_argument('--server', default='localhost,1433')
parser.add_argument('--database', required=True)
parser.add_argument('--uid', default='sa')
parser.add_argument('--pwd', required=True)
args = parser.parse_args()


driver = '{ODBC Driver 17 for SQL Server}'
server = args.server
database = args.database
uid = args.uid
pwd = args.pwd

connstring = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={uid};PWD={pwd}'


if __name__ == '__main__':
    cnxn = pyodbc.connect(connstring)
    cursor = cnxn.cursor()

    tsql = "select id, first_name, last_name, created_dt from users order by last_name, first_name"
    with cursor.execute(tsql):
        rows = cursor.fetchall()
        for row in rows:
            resp = {'id': row[0], 'last_name': row[2], 'first_name': row[1], 'created_dt': str(row[3])}
            print(json.dumps(resp, indent=4))