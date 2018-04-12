#!/bin/sh

DATABASE_PASSWORD=V96vBX5apwvO8s3eu
PKI_PASSWORD=dt7ltvQew97XJt4uQF

#	--mount type=bind,src=/home/peter/mysql-iwegarde,dst=/var/lib/mysql # For newer dockers...
docker run \
	--name mysql-iwegarde \
	-d \
	--restart unless-stopped \
	-v /home/peter/mysql-iwegarde:/var/lib/mysql \
	-e MYSQL_RANDOM_ROOT_PASSWORD=yes \
	-e MYSQL_DATABASE=iwegarde \
	-e MYSQL_USER=iwegarde \
	-e MYSQL_PASSWORD=$DATABASE_PASSWORD \
	mysql/mysql-server:5.7

docker run \
	-d \
	--restart unless-stopped \
	--name iwe_pki \
	-v /home/peter/iwe_pki/pki:/home/iwepki/easy-rsa3/pki \
	-e SECRET_KEY=$PKI_PASSWORD \
	iwe_pki:latest

#	-p 443:5000 \
#	-it --entrypoint /bin/sh \
docker run \
	-d \
	--restart unless-stopped \
	--name iwegarde-server \
	-v /home/peter/iwe_client_vpn_config:/home/iwegarde/iwe_client_vpn_config \
	--link mysql-iwegarde:dbserver \
	--link iwe_pki:pkiserver \
	-e SECRET_KEY=4iCyF4zG3bxwueOFP32u \
	-e MAIL_SERVER=smtp.googlemail.com \
	-e MAIL_PORT=587 \
	-e MAIL_USE_TLS=true \
	-e MAIL_USERNAME=peter.senna.bot \
	-e MAIL_PASSWORD=5qtn1MGljhAYvq \
	-e DATABASE_URL=mysql+pymysql://iwegarde:$DATABASE_PASSWORD@dbserver/iwegarde \
	-e PKI_URL="https://pkiserver:5000/build_client_full" \
	-e PKI_SECRET=$PKI_PASSWORD \
	iwegarde:latest

#	-e NGINX_PROXY_PASS=http://webserver \
docker run \
	-d \
	--restart unless-stopped \
	-v /home/peter/static-content:/static-content \
	--name nginx-iwegarde \
	-p 443:5000 \
	-p 80:5080 \
	--link iwegarde-server:webserver \
	nginx-iwegarde:latest
