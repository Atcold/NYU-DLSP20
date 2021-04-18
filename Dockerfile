# ベースイメージ名:タグ名
FROM jupyter/base-notebook:python-3.8.8

USER root
COPY environment.yml /tmp/

RUN apt update && \
    apt install -y gcc git

RUN conda env create -f /tmp/environment.yml &&\
    source activate pDL


USER $NB_UID
