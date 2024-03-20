FROM python

RUN mkdir /usr/src/crm_backoffice
WORKDIR /usr/src/crm_backoffice

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
#ENV SQL_HOST postgres
#ENV SQL_PORT 5432

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/crm_backoffice/entrypoint.sh
RUN chmod +x /usr/src/crm_backoffice/entrypoint.sh

COPY crm_backoffice /usr/src/crm_backoffice


ENTRYPOINT ["/usr/src/crm_backoffice/entrypoint.sh"]
