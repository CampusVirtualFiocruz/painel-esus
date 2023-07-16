FROM ubuntu
# export timezone - for python3.9-dev install
ENV TZ=America/Sao_Paulo

# place timezone data /etc/timezone
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone


RUN apt-get update && apt-get install -y locales && rm -rf /var/lib/apt/lists/* \
	&& locale-gen pt_BR.UTF-8 && localedef -i pt_BR -c -f UTF-8 -A /usr/share/locale/locale.alias pt_BR.UTF-8

ENV LANG pt_BR.utf8

RUN apt update -y 
RUN apt install -y software-properties-common 
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt update -y 

RUN apt install -y python3.9
RUN  ln -s /usr/bint/python3 /usr/bin/python 
RUN python3 --version > /root/runtime.txt


RUN  apt install -y python3-xlrd python3-venv python3-tqdm python3-sqlalchemy python3-sql python3-six python3-psycopg2 python3-openpyxl python3-numpy python3-pandas python3-dev

COPY . app/

WORKDIR app

RUN pip install --upgrade pip wheel
RUN pip install tzdata
RUN pip install -r requirements.txt
RUN python3 -m pip install --upgrade six

EXPOSE 5001

CMD [ "python3", "run.py" ]
