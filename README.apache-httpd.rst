Apach HTTPD
===========

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
