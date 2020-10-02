FROM ubuntu

RUN apt-get update && apt-get install -y nginx && apt-get clean && rm -rf /var/lib/apt/lists/*

EXPOSE 80

COPY index.html /var/www/html/

CMD [ "nginx", "-g", "daemon off;" ]