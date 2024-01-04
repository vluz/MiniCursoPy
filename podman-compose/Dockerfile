FROM python:3.11.7-slim

# install essentials
RUN apt update -y \
    && apt install --yes --no-install-recommends build-essential nano openssh-server git software-properties-common wget curl bash \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir /content \
    && mkdir /root/.jupyter

# Copy examples
RUN git clone https://github.com/vluz/MiniCursoPy.git

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy requirements file
COPY requirements.txt .

# install python dependencies
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && rm -f requirements.txt \
    && echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \
    && apt-get clean

# run jupyter notebook
CMD ["bash"]