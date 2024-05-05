# HoerFux-Glossary

Mit Proxy:

docker build --build-arg proxy=http://ukd-proxy.med.tu-dresden.de:80/ -t hoerfux-glossary .

Ohne Proxy

docker build -t hoerfux-glossary .


docker run -it hoerfux-glossary
