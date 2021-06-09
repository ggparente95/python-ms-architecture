
schema_create_user = {
  'name': {'type': 'string', 'required': True},
  'surname': {'type': 'string', 'required': True},
  'dni': {'type': 'string', 'required': True},
  'email': {'type': 'string', 'required': True},
  'password': {'type': 'string', 'required': True},
  'admin': {'type': 'boolean', 'required': True},
  'area_id': {'type': 'integer', 'required': True}
}

schema_edit_user = {
  'name': {'type': 'string', 'required': True},
  'surname': {'type': 'string', 'required': True},
  'dni': {'type': 'string', 'required': True},
  'email': {'type': 'string', 'required': True},
  'admin': {'type': 'boolean', 'required': True},
  'area_id': {'type': 'integer', 'required': True}
}