FROM debian:9
MAINTAINER wayne warren <wayne.warren.s@gmail.com>

VOLUME \
  # Location of pyresume source.
  /src/pyresume \
  # Location of .yaml files for processing.
  /mnt/pyresume

WORKDIR /mnt/pyresume
COPY $PWD /src/pyresume

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

RUN \
  # Install dependencies.
  apt-get update &&\
  apt-get -fy install ca-certificates python3 python3-setuptools &&\
  # Install pyresume.
  cd /src/pyresume &&\
  python3 setup.py develop &&\
  # Clean up all temporary files.
  apt-get clean &&\
  apt-get autoclean -y &&\
  apt-get autoremove -y &&\
  apt-get clean &&\
  rm -rf /tmp/* /var/tmp/* &&\
  rm -rf /var/lib/apt/lists/*
