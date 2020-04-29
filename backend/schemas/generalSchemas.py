from marshmallow import Schema, fields, validate
import string

# THis is used for more sensitive fields
generalString = fields.String(required=True, allow_none=False, 
    validate=validate.Regexp("^[a-zA-Z0-9 ,-_]+$", 
    error="Special Characters Not Allowed"))

# More general-er version of a string
generalerString = fields.String(required=True, allow_none=False)

generalInteger = fields.Integer(required=True, allow_none=False, error="That's not an integer")

generalTimeStamp = fields.DateTime(required=True, allow_none=False, error="Not a valid ISO timecode, try again")

email = fields.Email(required=True, allow_none=False)

username = fields.String(required=True, allow_none=False, 
    validate=[validate.Length(max=50), validate.Regexp("^[a-zA-Z0-9_-]+$", 
    error="Special characters (other than _ and -) not allowed in username")])

password = fields.String(required=True, validate=[validate.Length(min=8, max=256), 
    validate.Regexp("^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W)(?!.*\s).{8,}$",
    error="Password not strong enough, requires at least 8 digits, at least one upper case \
character, one lower case character and a special character")])

token = fields.String(required=True, validate=validate.Regexp("^[a-zA-Z0-9+_]+.[a-zA-Z0-9+_]+.[a-zA-Z0-9+_-]+$",
    error='Token format not valid'))

course = fields.String(required=True, allow_none=False, validate=validate.Regexp("^([A-Za-z]){4}([0-9]){4}$"))

semester = fields.String(required=True, allow_none=False, validate=validate.Regexp("^([0-9]){2}[tTsS][0-4]$"))

voteType = fields.String(required=True, allow_none=False,
    validate=validate.OneOf(["upvote", "downvote"], error="Invalid Vote type"))