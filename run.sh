#!/bin/bash

docker run --rm --env-file .env -v $HOME:/root terf/robincache:latest main.py
