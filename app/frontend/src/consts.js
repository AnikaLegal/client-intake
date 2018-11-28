// TODO - pull these from backend rather than duplicating
const FIELD_KEYS = [
  'id',
  'start',
  'prompt',
  'options',
  'help',
  'details',
  'follows',
  'type',
]
const FIELD_TYPES = ['TEXT', 'NUMBER', 'BOOLEAN']
const CONDITIONS = ['EQUALS']
const CONDITIONS_DISPLAY = {
  EQUALS: 'equals',
}
const FIELD_TYPES_DISPLAY = {
  TEXT: 'Text',
  NUMBER: 'Number',
  BOOLEAN: 'Yes / No',
}
export {
  FIELD_KEYS,
  FIELD_TYPES,
  FIELD_TYPES_DISPLAY,
  CONDITIONS,
  CONDITIONS_DISPLAY,
}
