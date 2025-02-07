FROM python:3.10

RUN mkdir painel-esus
RUN mkdir paineis-v2-front

COPY ./painel-esus ./painel-esus
COPY ./paineis-v2-front/static-files ./paineis-v2-front/static-files

WORKDIR /painel-esus
RUN pip3 install -r requirements.txt

EXPOSE 5001

CMD [ "python", "run.py" ]
