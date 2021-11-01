from typing import Dict


class SchemaBody:
    def __init__(self, fields):
        self.fields = fields
        type_of: str = fields['Tipo'],
        name: str = fields["Campo"],
        size: str = fields["Tamanho"],
        is_null: str = fields["Aceita"],
        description: str = fields["Comentários"]

    def __str__(self):
        return self.name + "(" + str(self.fields) + ")"

    def __repr__(self):
        return self.name + "(" + str(self.fields) + ")"

    def _set_type(self, typeof: str = 'string', name: str = None, size: str = None):
        try:
            if typeof == 'string':
                seted_type = "string"
            elif typeof == 'fixed':
                seted_type = {
                    "name": name,
                    "size": int(size),
                    "type": typeof
                }
            elif typeof == 'float':
                seted_type = {
                    "connect.name": "org.apache.kafka.connect.data.Timestamp",
                    "connect.version": 1,
                    "logicalType": "timestamp-millis",
                    "type": "long"
                }
            else:
                raise f"Unknown Type Error: {typeof}"
            return seted_type
        except Exception as e:
            print(e)

    def create_node(self,
                    type_of: str,
                    name: str,
                    size: int,
                    is_null: str,
                    description: str) -> Dict:
        is_nullable: bool = True if 'Sim' in is_null else False
        node = {}

        if is_nullable:
            node = {
                "default": "null",
                "doc": description,
                "name": name,
                "type": ["null", self._set_type(type_of, size=size, name=name)],
            }

        else:
            node = {
                "doc": description,
                "name": name,
                "type": self._set_type(type_of, size=size, name=name),
            }

        return node
