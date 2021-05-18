FROM python:3.9
WORKDIR /Service

COPY requirementspy39.txt ./
RUN pip install -r requirementspy39.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . .

CMD ["gunicorn", "start:create_app", "-c", "./gunicorn.conf.py"]