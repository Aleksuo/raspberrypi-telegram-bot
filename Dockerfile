FROM python:3
ADD ./src/
RUN pip install -r requirements.txt
CMD ["python", "./my_script.py"]