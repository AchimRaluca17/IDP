#!/usr/bin/env bash

echo "Waiting for management server..."

while ! nc -z managemenet_server 5000; do
  sleep 0.5
done

echo "client started"
python client.py
