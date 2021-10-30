from typing import Dict


class SchemaBody:
    def __init__(self, fields):
        self.fields = fields

    def __str__(self):
        return self.name + "(" + str(self.fields) + ")"

    def __repr__(self):
        return self.name + "(" + str(self.fields) + ")"

    def _set_type(self, type: str):
        pass

    def create_node(self):
        is_nullable: bool = True if 'Sim' in self.fields['Aceita Nulo'] else False
        node = {
                "doc": self.fields['Comentários'],
                "name": self.fields['Campo'],
                "type": self._set_type(self.fields['Tipo']),
            }
        return node
