from flask_restplus import Resource, abort, Namespace

api = Namespace("courses", description="APIs to handle courses related queries")

@api.route("/")
class courses(Resource):
    def get(self):
        abort(400, "Memes")