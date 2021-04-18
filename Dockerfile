# ベースイメージ名:タグ名
FROM continuumio/anaconda3:2020.11

COPY environment.yml /tmp/
COPY ./start_notebook.sh /tmp/

RUN apt-get update && \
    apt-get install -y gcc git sudo wget


RUN conda env create -f /tmp/environment.yml
ENV PATH /opt/conda/envs/pDL/bin:$PATH
RUN echo "source activate pDL" >> ~/.bashrc

CMD ["/bin/bash"]
