Apach HTTPD
===========

Proxy with HTML rewrite
-----------------------
Say you want to host anothersite.com content at your site's ``/asdf`` location, use:
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
