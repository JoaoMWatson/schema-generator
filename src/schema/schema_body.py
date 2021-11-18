from typing import Dict


class SchemaBody:
    def __init__(self, dataFrame):
        self.dataFrame = dataFrame
        type_of: str = dataFrame['Tipo'],
        name: str = dataFrame["Campo"],
        size: str = dataFrame["Tamanho"],
        is_null: str = dataFrame["Aceita"],
        description: str = dataFrame["Comentários"]

    def __str__(self):
        return self.name + "(" + str(self.dataFrame) + ")"

    def __repr__(self):
        return self.name + "(" + str(self.dataFrame) + ")"

    def _set_type(self, typeof: str = 'string', name: str = None, size: str = None):
        try:
            if typeof == 'string' or typeof == 'int':
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
                raise Exception(f"Unknown Type Error: {typeof}")
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
                "doc": repr(description),
                "name": name,
                "type": ["null", self._set_type(type_of, size=size, name=name)],
            }

        else:
            node = {
                "doc": repr(description),
                "name": name,
                "type": self._set_type(type_of, size=size, name=name),
            }

        return node
    

    def make_body(self) -> Dict:
        fields = []
        for index, row in self.dataFrame.iterrows():
            fields.append(self.create_node(
                type_of=row["Tipo"],
                name=row["Campo"],
                size=row["Tamanho"],
                is_null=row["Aceita"],
                description=row['Comentários'])
            )
        
        return {"fields": fields}
