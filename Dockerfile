# Start with the Chainguard Nginx image as the base
FROM cgr.dev/chainguard/nginx:latest

# Copy the 'public' directory from project to the default Nginx web server directory inside the container
COPY public/ /usr/share/nginx/html/
# Copy the custom Nginx configuration file to the Nginx configuration directory inside the container
COPY nginx.conf /etc/nginx/nginx.conf
