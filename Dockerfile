FROM python:3.9

ADD config.ini .
ADD twitter_api_stream.py .
ADD twitter_api.py .

RUN pip install requests tweepy
RUN pip install requests pandas

CMD ["python","./twitter_api_stream.py"]
