#!/bin/bash

docker run --env-file .env -v $HOME:/root terf/robincache:latest main.py
