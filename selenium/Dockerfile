FROM registry.cn-beijing.aliyuncs.com/shannonai/python
LABEL maintainer="taoshibo@shannonai.com"

RUN set -ex && apt-get update -y && apt-get install -y --no-install-recommends \
        build-essential \
        gcc \
        git \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /home/work
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --default-timeout=120 -r requirements.txt
COPY scrapyd.conf scrapyd.conf
RUN chown -R work: /home/work

EXPOSE 6800

USER work
ENTRYPOINT ["scrapyd"]
