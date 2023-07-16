FROM postgres

ADD ./DB/esus.sql /esus.sql
ADD ./DB/restore.sh /docker-entrypoint-initdb.d

EXPOSE 5432