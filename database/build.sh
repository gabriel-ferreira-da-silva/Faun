#!/bin/bash

mongosh --file musicSchema.js
python3 insertMusic.py