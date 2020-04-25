from namespaces.notes import api
from flask_restplus import fields
from werkzeug import FileStorage

notesCreationDetails = api.parser()
notesCreationDetails.add_argument('courseID', required=True, type=str, help="uuid of the corresponding course", location="form")
notesCreationDetails.add_argument('name', required=True, type=str, help="My PS notes for COMP1911", location="form")
notesCreationDetails.add_argument('price', required=True, type=int, help="100", location="form")
notesCreationDetails.add_argument('file', required=True, type=FileStorage, help="File for the note", location="files")

notesDetails = api.parser()
notesDetails.add_argument('noteID', required=True, help="uuid of the corresponding note", location="args")

courseNotesDetails = api.parser()
courseNotesDetails.add_argument('courseID', required=True, help="CourseID of the course you want the notes for", location="args")