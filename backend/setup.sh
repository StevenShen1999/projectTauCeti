#!/bin/sh
rm ../database/everything.db
python3 init.py
python3 utilFunc.py
python3 utilFuncNotes.py
python3 utilFuncChat.py