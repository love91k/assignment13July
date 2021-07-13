# assignment13July




#Test the docker image
# got to the app directory 
docker build -t myapp  .
docker run -e AWS_ACCESS_KEY_ID=# -e AWS_SECRET_ACCESS_KEY=# -e S3_BUCKET=myhelmrepo2401 myapp

#run the curl with private ip and 5000 port, it will provide  all the files in s3 bucket in json format 
#curl  http://172.17.0.2:5000/


