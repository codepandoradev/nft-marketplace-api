FROM envy42/nft-marketplace-web:latest as web

FROM nginx:1.21.6 as nginx

COPY --from=web /web /etc/nginx/html
