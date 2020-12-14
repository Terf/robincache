#!/bin/bash

docker run --name robincache-admin --restart always -d --link robincache-mysql:db -p 1996:80 phpmyadmin/phpmyadmin
