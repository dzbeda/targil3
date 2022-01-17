FROM ubuntu:latest
ENV VERSION=1.2.0
RUN apt-get update && apt-get install -y \
    python3 \
    zip \
    unzip \
    vim \
    python3-pip
COPY zip_job.py /tmp
COPY get_info.sh /tmp
RUN chmod 777 /tmp/get_info.sh
CMD ["/tmp/get_info.sh"]


