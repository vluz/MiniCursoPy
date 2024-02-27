FROM python:3.10.13-slim

MAINTAINER Victor Luz - vluz at me dot com

# install essentials, required utils and make some configurations
RUN apt update -y \
    && apt install --yes --no-install-recommends build-essential nano openssh-server git \
    software-properties-common wget curl bash firefox-esr libasound2-dev python3-tk \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir /content \
    && chmod 777 /content \
    && wget https://github.com/browsh-org/browsh/releases/download/v1.8.0/browsh_1.8.0_linux_amd64.deb \
    && apt install ./browsh_1.8.0_linux_amd64.deb \
    && rm ./browsh_1.8.0_linux_amd64.deb \
    && mkdir /root/.jupyter

# clone course examples to content dir
RUN git clone https://github.com/vluz/MiniCursoPy.git /content

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy requirements file
COPY requirements.txt .

# install python dependencies and cleanup
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && rm -f requirements.txt \
    && echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \
    && apt-get clean

# Expose all ports used
EXPOSE 8888
EXPOSE 80
EXPOSE 443
EXPOSE 8501

# disable heath check
HEALTHCHECK NONE

# change to content dir
WORKDIR /content

# run
CMD ["bash"]
