FROM postgres
ENV POSTGRES_DB postgres
COPY dvdrental_bak.sql /docker-entrypoint-initdb.d/
COPY mme_bak.sql /docker-entrypoint-initdb.d/

