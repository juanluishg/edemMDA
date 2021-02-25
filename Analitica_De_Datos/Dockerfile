FROM tensorflow/tensorflow:latest-gpu-jupyter
USER root
RUN /usr/bin/python3 -m pip install --upgrade pip
RUN pip install notebook
RUN pip install pandas
RUN pip install scikit-learn
RUN useradd -ms /bin/bash tensor
USER tensor
WORKDIR /home/tensor
VOLUME D:\Master\edemMDA\Analitica_De_Datos\pruebas:/home/tensor/
EXPOSE 8888
ENTRYPOINT [ "/bin/bash" ]