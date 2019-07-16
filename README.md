# ludwig-fastscore
try to get ludwig model to run in fastscore


docker build -t localrepo/engine:ludwig .


update fastscore docker-compose.yaml to create an engine using the above image

fastscore model add ludwig-titanic titanic_ludwig.py3

fastscore attachment upload ludwig-titanic titanic_model.tar.gz

fastscore schema add ludwig_titanic_input ludwig_titanic_input.avsc

fastscore schema add ludwig_titanic_output ludwig_titanic_output.avsc

 fastscore stream add rest rest.json
