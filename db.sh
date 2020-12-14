#!/bin/bash

docker run --name robincache-mysql --restart always --env-file .env -v robincache:/var/lib/mysql --restart always -p 3001:3306 -d mysql
