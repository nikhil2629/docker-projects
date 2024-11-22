#FROM nginx:alphine
#RUN apt-get update
#RUN apt-get-install -y nginx zip curl
#RUN echo "daemon off;" >> /etc/nginx/nginx.conf
#RUN curl -o /var/www/html/master.zip -l https://github.com/gabrielecirulli/2048.git/zip/master
#RUN cd /var/www/html/master.zip && mv 2048.master/* . && rm -rf 2048.master master.zip
#EXPOSE 80
#CMD [ "/usr/sbin/nginx","-c","/etc/nginx/nginx.conf" ]

# Use an official Nginx image as the base
#FROM nginx:alpine

# Copy the game files into the Nginx HTML directory
#COPY . /usr/share/nginx/html

# Expose port 80 to access the game
#EXPOSE 80

# Use Alpine-based Nginx image
FROM nginx:alpine

# Install required tools (curl, unzip)
RUN apk add --no-cache curl unzip

# Download the game source code as a zip file
RUN curl -L -o /tmp/2048.zip https://github.com/gabrielecirulli/2048/archive/refs/heads/master.zip

# Unzip the downloaded file and move contents to the Nginx HTML folder
RUN unzip /tmp/2048.zip -d /tmp && \
    mv /tmp/2048-master/* /usr/share/nginx/html && \
    rm -rf /tmp/2048.zip /tmp/2048-master

# Expose port 80
EXPOSE 80

# Start Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]

