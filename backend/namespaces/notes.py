from flask_restplus import abort, Resource, Namespace

api = Namespace("notes", description="APIs to handle notes related queries")

@api.route("/lmao")
class lmao(Resource):
    def get(self):
        return "success"