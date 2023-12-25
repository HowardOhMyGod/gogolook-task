from marshmallow import Schema, fields, validate

class TaskSchema(Schema):
  id = fields.UUID(required=True)
  name = fields.Str(required=True)
  status = fields.Int(required=True, validate=validate.OneOf([0, 1]))