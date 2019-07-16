FROM fastscore/engine:dev-ubuntu 
ADD ./requirements.txt .

RUN pip3 install --isolated --user -r requirements.txt
