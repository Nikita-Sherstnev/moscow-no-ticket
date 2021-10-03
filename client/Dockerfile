FROM node:14.18 AS build
RUN apt-get update \
    && apt-get install --yes --no-install-recommends make build-essential
WORKDIR /home/node
COPY ./ .
RUN yarn install && yarn build

FROM nginx:1.17.10-alpine
ENV NGINX_PORT=8080
COPY --from=build /home/node/dist /usr/share/nginx/html
