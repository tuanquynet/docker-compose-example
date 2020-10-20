FROM node:lts-alpine3.9

RUN mkdir -p /usr/src/app/src
WORKDIR /usr/src/app/src
COPY src/ /usr/src/app/src/
WORKDIR /usr/src/app/src

CMD ["node", "index"]
