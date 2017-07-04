#
# copied from thomasweise/texlive and heavily modified
#
# This is an image with a basic TeX Live installation.
# Source: https://github.com/thomasWeise/docker-texlive/
# License: GNU GENERAL PUBLIC LICENSE, Version 3, 29 June 2007
# The license applies to the way the image is built, while the
# software components inside the image are under the respective
# licenses chosen by their respective copyright holders.
#
FROM debian:9
MAINTAINER wayne warren <wayne.warren.s@gmail.com>

RUN export LANG=C.UTF-8 &&\
    apt-get clean &&\
    apt-get update &&\
    apt-get autoclean -y &&\
    apt-get autoremove -y &&\
    apt-get update &&\
# install general utilities
    apt-get install -f -y apt-utils &&\
# install utilities necessary for tlmgr
    apt-get install -f -y wget xzdec &&\
# install TeX Live and ghostscript
    apt-get install -f -y ghostscript \
                          make \
                          latexmk \
                          texlive &&\
# free huge amount of unused space
    apt-get purge -f -y make-doc \
                        texlive-fonts-extra-doc \
                        texlive-fonts-recommended-doc \
                        texlive-humanities-doc \
                        texlive-latex-base-doc \
                        texlive-latex-extra-doc \
                        texlive-latex-recommended-doc \
                        texlive-metapost-doc \
                        texlive-pictures-doc \
                        texlive-pstricks-doc \
                        texlive-science-doc &&\
# ensure that external fonts and doc folders exists
    mkdir /usr/share/fonts/external/ &&\
    mkdir /doc/ &&\
# clean up all temporary files
    apt-get clean &&\
    apt-get autoclean -y &&\
    apt-get autoremove -y &&\
    apt-get clean &&\
    rm -rf /tmp/* /var/tmp/* &&\
    rm -rf /var/lib/apt/lists/* &&\
    rm -f /etc/ssh/ssh_host_*

VOLUME ["/doc/", "/usr/share/fonts/external/"]
