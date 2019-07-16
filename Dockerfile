FROM fastscore/engine:dev-ubuntu 
USER root
RUN apt-get update
RUN apt-get install -y libgmp-dev
ADD ./requirements.txt .
RUN pip3 install -r requirements.txt
