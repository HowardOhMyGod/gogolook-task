from marshmallow import Schema, fields, validate

class TaskSchema(Schema):
  id = fields.UUID(required=True)
  name = fields.Str(required=True)
  status = fields.Int(required=True, validate=validate.OneOf([0, 1]))


class UpdateTaskDTO(Schema):
  name = fields.Str()
  status = fields.Int(validate=validate.OneOf([0, 1]))