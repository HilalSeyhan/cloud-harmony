FROM postgres:13

WORKDIR /docker-entrypoint-initdb.d

COPY init.sql /docker-entrypoint-initdb.d/

ENV POSTGRES_USER=bbuser
ENV POSTGRES_PASSWORD=bbuser
ENV POSTGRES_DB=cloud_harmony_db
