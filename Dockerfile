FROM ubuntu:20.04


RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get install python3-pip -y \ 
    && apt-get clean

RUN pip3 install virtualenvwrapper

ENV VIRTUAL_ENV=/opt/env
RUN virtualenv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip3 install -r /app/requirements.txt \
    && rm -rf /root/.cache/pip

#RUN sed -e '/Cipher/s/^/#/' -i /etc/ssl/openssl.cnf

COPY . /app/

EXPOSE 8787

CMD ["python3", "/app/simple_sanic.py"]