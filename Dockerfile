FROM python

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
#ENV SQL_HOST db
#ENV SQL_PORT 5432

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh


#ENTRYPOINT ["/usr/src/crm_backoffice/entrypoint.sh"]
