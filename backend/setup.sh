#!/bin/sh
# TODO: Write whatever else we need in the future to populate the database
rm ../database/everything.db
python3 init.py
python3 utilFunc.py
python3 utilFuncNotes.py
python3 utilFuncChat.py