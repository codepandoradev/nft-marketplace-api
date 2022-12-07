ARG TAG

FROM envy42/nft-marketplace-web:$TAG as web

FROM nginx:1.23.2 as nginx

WORKDIR /etc/nginx

COPY ./certs /certs
COPY ./nginx.prod.conf.conf ./templates/nginx.conf.conf
COPY --from=web /web ./html
