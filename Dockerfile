FROM python:3.6-stretch
MAINTAINER wayne warren <wayne.warren.s@gmail.com>

# The type of build to invoke from setup.py.
ARG setup="install"

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
  apt-get -fy install ca-certificates libyaml-0-2 python3 python3-setuptools &&\
  # Install pyresume.
  cd /src/pyresume &&\
  python3 setup.py $setup &&\
  # Clean up all temporary files.
  apt-get clean &&\
  apt-get autoclean -y &&\
  apt-get autoremove -y &&\
  apt-get clean &&\
  rm -rf /tmp/* /var/tmp/* &&\
  rm -rf /var/lib/apt/lists/*
