# This is a complete guide to host production ready Odoo 17 application with SSL

## Steps:

 1. Start only database and odoo for initial test.
	```bash
	docker compose up db -d
	docker compose up odoo -d
	```
 2. Test this site on your brower `http://example.com:8069`
 3. Start nginx server only 80 **(Comment 443 server in nginx config file)**
	```bash
	docker compose up nginx -d
	```
 4. Check this with your browser `http://example.com`
 5. Dry run certbot to validate the ssl
	```bash
	docker compose run --rm certbot certonly --webroot --webroot-path /var/www/certbot/ --dry-run -d example.com
	```
 6. If dry run is success create the certificate without dry run
	```bash
	docker compose run --rm certbot certonly --webroot --webroot-path /var/www/certbot/ -d example.com
	```
 7. Uncomment the 443 server in nginx config file **(Verify the cert file names with your domain name)**
 8. Restart nginx server
 9. If it shows error finding cert file remove nginx container and recreate it.

For more information
[Click me](https://mindsers.blog/en/post/https-using-nginx-certbot-docker/)

*Happy Cording*
