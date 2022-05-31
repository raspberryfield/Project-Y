FROM mysql
COPY AWBackup.sql /docker-entrypoint-initdb.d/
COPY moviedb_dump.sql.gz /docker-entrypoint-initdb.d/
