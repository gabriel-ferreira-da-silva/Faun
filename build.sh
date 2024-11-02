#!/bin/bash

if [ -z "$1" ]; then
    sudo systemctl start mongod
    cd database
    ./build.sh
    cd ../backend || exit
    python3 main.py &
    cd ../reactApp/faun-app/src || exit
    npm start &
    cd ..
    echo "system is running"
    exit 1
fi

if [ "$1" = "--push" ] || [ "$1" = "-p" ]; then
    if [ -z "$2" ]; then
        echo "no commit message given"
        exit 1
    fi
    COMMIT_MSG="$2"
    BRANCH="$(git rev-parse --abbrev-ref HEAD)"
    git add .
    git commit -m "$COMMIT_MSG"
    git push -u origin "$BRANCH"
    exit 1
fi

if [ "$1" = "--clear" ] || [ "$1" = "-c" ]; then
    mongosh --file clear.gal.js
    exit 1
fi
