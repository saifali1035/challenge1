FROM python

WORKDIR /usr/src/app

COPY server.py ./

EXPOSE 9098

CMD [ "python","./server.py" ]