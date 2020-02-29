#!/bin/sh
# TODO: Write whatever else we need in the future to populate the database
if [ -f "../database/everything.db" ] ; then
    rm ../database/everything.db
fi
python3 app.py