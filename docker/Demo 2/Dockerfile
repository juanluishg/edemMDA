FROM ubuntu:16.04

RUN apt-get update && apt-get install -y curl && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN mkdir /home/edem

ENV USER masfworld
ENV SHELL /bin/bash
ENV LOGNAME masfworld

CMD [ "bash" ]