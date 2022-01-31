# My personal website / blog / portfolio / etc


## setup
```
git submodule update --inite --remote
```


## building
```
docker build -t website .
```


## deploying
```
docker run -d --restart always -p 80:80 -p 443:443 -v /etc/ssl/private/certs:/certs:ro website
```
