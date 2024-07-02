# This is a complete guide to host production ready nginx docker with SSL

## Steps:

 1. Start nginx server only 80 server **(Comment 443 server in nginx config file)**
	```bash
	docker compose up nginx -d
	```
 2. Check this with your browser `http://example.com`
 3. Dry run certbot to validate the ssl
	```bash
	docker compose run --rm certbot certonly --webroot --webroot-path /var/www/certbot/ --dry-run -d example.com
	```
 4. If dry run is success create the certificate without dry run
	```bash
	docker compose run --rm  certbot certonly --webroot --webroot-path /var/www/certbot/ -d example.com
	```
 5. Uncomment the 443 server in nginx config file **(Verify the cert file names with your domain name)**
 7. Restart nginx server
 8. If it shows error finding cert file remove nginx container and recreate it.

For more information
[Click me](https://mindsers.blog/en/post/https-using-nginx-certbot-docker/)

Nginx alias vs root [Click me](https://stackoverflow.com/questions/10631933/nginx-static-file-serving-confusion-with-root-alias)

*Happy Cording*
