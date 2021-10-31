from typing import Dict


class SchemaBody:

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
                    "size": size,
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

    def create_node(self, typeof: str = 'string', name: str = None, size: str = None, is_null: str = None, comentarios: str = None):
        is_nullable: bool = True if 'Sim' in is_null else False
        node = {}
        if is_nullable:
            node = {
                "default": "null",
                "doc": comentarios,
                "name": name,
                "type": ["null", self._set_type(typeof, size=size, name=name)],
            }
        else:
            node = {
                "doc": comentarios,
                "name": name,
                "type": self._set_type(typeof, size=size, name=name),
            }
        return node
