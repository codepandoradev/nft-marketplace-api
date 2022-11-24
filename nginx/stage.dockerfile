FROM envy42/nft-marketplace-web:latest as web

FROM nginx:1.23.2 as nginx

WORKDIR /etc/nginx

COPY ./nginx.stage.conf.conf ./templates/nginx.conf.conf
COPY --from=web /web ./html
