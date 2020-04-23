from flask_restplus import Resource, abort, Namespace

api = Namespace("uploads", 
description="APIs to handle uploads related queries (might merge this with notes)")