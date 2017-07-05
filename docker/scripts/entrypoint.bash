#!/usr/bin/env bash

set -e
set -x

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Check for required variables

user=${USER:-jenkins}
uid=${UID:-9999}
group=${GROUP:-jenkins}
gid=${GID:-9999}
home=${HOME:?}

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Create users and groups if necessary.

if id ${user} ;then
    # If the user exists, then just get some required information from its
    # passwd entry and use those later in the script.
    home="$(getent passwd ${user} | cut -d: -f6)"
    group="$(id -ng ${user})"
else
    # If the specified user doesn't exist, create it and its corresponding
    # primary group.
    addgroup --gid ${gid} ${group} || true
    useradd -m -d ${home} \
            -g ${gid} \
            -u ${uid} \
            -s /bin/bash \
            ${user} || true
fi

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Add user to the group that has access to /var/run/docker.sock. This allows the
# docker container to spin up new docker containers. 🐢 on 🐢

DOCKER_SOCKET="/var/run/docker.sock"

if [ -S $DOCKER_SOCKET ]; then
    DOCKER_GID=$(stat -c '%g' $DOCKER_SOCKET)

    if [ ! $(getent group $DOCKER_GID) ] ;then
      groupadd -r -g $DOCKER_GID custom_docker
    fi

    usermod -aG $DOCKER_GID $user
fi

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Copy files from volume-mapped directory to their proper places in the
# filesystem.
chown -R ${user}.${group} ${home}

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Install user-specified latex modules from CTAN via tlmgr.
# Input format is a line-delimited list of CTAN package names stored in
# /ctan-packages.txt

sudo -E -u $user bash <<MEOW
tlmgr init-usertree
tlmgr install $(cat resources/ctan-packages.txt | tr '\n' ' ')

set -x
exec $@
MEOW
