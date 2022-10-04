FROM python:3.9

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD main.py .

#CMD python -m debugpy --listen 0.0.0.0:5678 --wait-for-client main.py
CMD python main.py