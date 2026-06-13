FROM nginx:1.27-alpine

LABEL org.opencontainers.image.title="Sagar Kerhalkar Global Portfolio"
LABEL org.opencontainers.image.description="Static production image for the IT Infrastructure & DevOps Leader portfolio"
LABEL org.opencontainers.image.source="https://github.com/sagarkerhalkar/Profile"

RUN rm -rf /usr/share/nginx/html/*

COPY docker/nginx.conf /etc/nginx/conf.d/default.conf
COPY index.html 404.html robots.txt sitemap.xml .nojekyll /usr/share/nginx/html/
COPY assets/ /usr/share/nginx/html/assets/
COPY cv/ /usr/share/nginx/html/cv/
COPY admin/ /usr/share/nginx/html/admin/
COPY projects/ /usr/share/nginx/html/projects/

EXPOSE 80

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD wget -qO- http://127.0.0.1/healthz || exit 1
