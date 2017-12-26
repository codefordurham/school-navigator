FROM nginx:stable-alpine

WORKDIR /code

COPY frontend /code

COPY compose/server/nginx.conf /etc/nginx/conf.d/default.conf
