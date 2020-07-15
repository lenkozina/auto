FROM python:3.8
ENV DJANGO_SETTINGS_MODULE auto.settings
ENV PYTHONUNBUFFERED 1
RUN mkdir /auto
WORKDIR /auto
ADD . /auto/
RUN pip install -r /auto/requirements.txt
RUN python /auto/manage.py collectstatic --noinput