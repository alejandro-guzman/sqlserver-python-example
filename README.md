## Start a SQL Server

```bash
docker run --name sqlserver -v $(pwd):/tmp -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=P@55word" -p 1433:1433 -d mcr.microsoft.com/mssql/server:2017-latest
```

<details>
<summary>Delete container</summary>

```bash
docker rm -f sqlserver
```
</details>

## Initialize database

```bash
docker exec -it sqlserver /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P P@55word -i /tmp/db-init.sql -e
```

### Use sqlcmd to administrate database

```bash
docker exec -it sqlserver /opt/mssql-tools/bin/sqlcmd -S localhost -d demo1 -U sa -P P@55word
```

## Run script

```bash
python main.py --database='demo1' --pwd='P@55word'
```