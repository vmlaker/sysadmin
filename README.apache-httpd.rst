Apach HTTPD
===========

SSL certificate
---------------
Create a 10-year self-signed certificate:
::

   openssl req -x509 -nodes -days 3650 -newkey rsa:2048 -keyout server_name.key -out server_name.crt

Proxy with HTML rewrite
-----------------------
Say you want to proxy anothersite.com content at your site's ``/asdf`` location, use:
::

    ProxyRequests Off
    ProxyPass /asdf http://anothersite.com
    ProxyHTMLURLMap http://anothersite.com /asdf
    <Location /asdf>
        ProxyPassReverse /
        ProxyHTMLURLMap / /asdf/
        RequestHeader unset Accept-Encoding
    </Location>
    SetOutputFilter proxy-html

or, another example, this time proxying ``http://chef/wabbit`` at your site's ``/bunny`` path: 
::

   <Location /bunny>
     ProxyPass http://chef/wabbit
     ProxyPassReverse http://chef/wabbit
     ProxyHTMLURLMap http://chef/wabbit
     AddOutputFilterByType SUBSTITUTE text/html
     Substitute "s|wabbit/|bunny/|ni"
   </Location>

Redirect all traffic to HTTPS
-----------------------------
::

   RewriteEngine On
   RewriteCond %{HTTPS} !on
   RewriteRule (.*) https://%{HTTP_HOST}%{REQUEST_URI}

Redirect select path from HTTP to HTTPS
---------------------------------------
::

   <VirtualHost *:80>
     ...
     # Redirect RStudio to HTTPS.
     Redirect permanent /rstudio https://www.example.com/rstudio
     ...
   </VirtualHost>

Redirect from HTTPS to HTTP
---------------------------
::

   <VirtualHost _default_:443>
     ...
     # Anything other than /rstudio, go back to HTTP
     RewriteEngine On
     RewriteCond %{HTTPS} on
     RewriteCond %{REQUEST_URI} !/rstudio
     RewriteRule (.*) http://%{HTTP_HOST}%{REQUEST_URI}
     ...
   </VirtualHost>

URL substitute
--------------
Flask's ``url_for()`` in Jinja templates generates URLs prefixed with
forward slash. But if you're deploying the site in a domain sub-path
(e.g. http://example.com/my/app) you will need to make the substitution
in all URL strings.
::

   RewriteRule  ^/my/app$  /my/app/  [R]
   <Location /my/app/>
       ProxyPass http://localhost:5000/
       ProxyPassReverse http://localhost:5000/
       AddOutputFilterByType SUBSTITUTE text/html
       Substitute s;href="/;href="/my/app/;n
       Substitute s;src="/;src="/my/app/;n
       ProxyPassReverse /
       RequestHeader unset Accept-Encoding
   </Location>

Restrict direct IP access
-------------------------
::

   <VirtualHost *:80>
      ServerName localhost
      Redirect 403 /
      UseCanonicalName Off
   </VirtualHost>
