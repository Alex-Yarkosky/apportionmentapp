FROM alpine:3.10
USER root
LABEL maintainers="Alex Yarkosky <yarkoskya@allegheny.edu>"
WORKDIR usr/
# OS setup
RUN set -ex && apk --no-cache add sudo

# Install python and pip
 RUN echo "**** install Python ****" && \
    apk add --no-cache python3 && \
    if [ ! -e /usr/bin/python ]; then ln -sf python3 /usr/bin/python ; fi && \
    \
    echo "**** install pip ****" && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --no-cache --upgrade pip setuptools wheel && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi

# Install python dependencies
# COPY requirements.txt .
RUN pip install pytest

# Copy the rest of your app's source code from your host to your image filesystem
COPY . .

# Copy the CSV file over for tests to pass
COPY test/apportionments.csv .

RUN cd test && pytest
