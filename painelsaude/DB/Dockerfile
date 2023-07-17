FROM postgres

ADD ./DB/esus.db /esus.db
ADD ./DB/restore.sh /docker-entrypoint-initdb.d

EXPOSE 5432