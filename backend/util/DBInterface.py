from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer, ForeignKey, TIMESTAMP, Boolean

class DB():
    users = None
    courses = None
    notes = None
    uploads = None

    def __init__(self):
        engine = create_engine("postgresql://shen:990928ss@localhost/tauCetiDB")
        meta = MetaData(engine)

        self.users = Table("users", meta, Column('email', String, primary_key=True),
            Column('activated', Boolean, nullable=False),
            Column('password', String, nullable=False),
            Column('username', String(20), nullable=False),
            Column('points', Integer, nullable=False),
            Column('link', String, nullable=False),
            Column('createdAt', TIMESTAMP(True), nullable=False)
        )

        self.courses = Table("courses", meta, Column('id', String, primary_key=True),
            Column('code', String, nullable=False),
            Column('name', String(50), nullable=False),
            Column('semester', String(4), nullable=False),
        )

        self.notes = Table("notes", meta, Column('id', String, primary_key=True),
            Column('course', String, ForeignKey("courses.id"), nullable=False),
            Column('points', Integer, nullable=False),
        )

        self.uploads = Table("uploads", meta, Column('uploader', String, ForeignKey("users.email"), primary_key=True),
            Column('notesID', String, ForeignKey("notes.id"), nullable=False),
            Column('uploadTime', TIMESTAMP(True), nullable=False)
        )

        meta.create_all()

        ## Potentially 
        ## Comments For Courses/Notes
        ## Chatroom For Courses
        ## Faculty For Courses Classification
        ## Image/Logo For Courses