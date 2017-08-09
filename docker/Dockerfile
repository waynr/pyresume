#
# This is an image with a basic TeX Live installation.
# Source: https://github.com/waynr/pyresume
#
# License: GNU GENERAL PUBLIC LICENSE, Version 3, 29 June 2007
# The license applies to the way the image is built, while the
# software components inside the image are under the respective
# licenses chosen by their respective copyright holders.
#
FROM debian:9
MAINTAINER wayne warren <wayne.warren.s@gmail.com>

RUN export LANG=C.UTF-8 &&\
  echo "APT::Install-Recommends \"0\";" > /etc/apt/apt.conf.d/10norecommends &&\
  echo "APT::Install-Suggests \"0\";" >> /etc/apt/apt.conf.d/10norecommends &&\
  apt-get update &&\
# install general utilities
  apt-get install -f -y apt-utils sudo &&\
# install utilities necessary for tlmgr
  apt-get install -f -y wget xzdec &&\
# install TeX Live and ghostscript
  apt-get install -f -y latexmk \
                        texlive &&\
# ensure that external fonts and doc folders exists
  mkdir /usr/share/fonts/external/ &&\
  mkdir /doc/ &&\
# clean up all temporary files
  apt-get clean &&\
  apt-get autoclean -y &&\
  apt-get autoremove -y &&\
  apt-get clean &&\
  rm -rf /tmp/* /var/tmp/* &&\
  rm -rf /var/lib/apt/lists/*

VOLUME ["/doc/", "/usr/share/fonts/external/"]
ADD scripts /bin/
ENTRYPOINT ["/bin/entrypoint.bash"]
