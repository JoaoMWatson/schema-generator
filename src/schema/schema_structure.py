from typing import Dict
from schema_body import SchemaBody

class SchemaStructure:
    def __init__(self, topic_name: str, schema_description: str, schema_body: Dict):
        self.topic_name = topic_name
        self.schema_description = schema_description
        self.class_name = topic_name.title().replace("-", "")
        
        self.body = schema_body
        self.header = self._make_header()
        self.footer = self._make_footer()

    def _make_header(self) -> Dict:
        return {
            "connect.name": "br.com.kroton.{class_name}".format(class_name=self.class_name),
            "doc": repr("* **DESCRIPTION**: {description}\n* **TOPIC**: {topic}\n* **AUTHOR TEAM**: Stream Team  **AUTHOR E-MAIL**: streamteam@cogna.com.br\n* **SUPPORT NAME**: Stream Team   **SUPORT E-MAIL**: streamteam@cogna.com.br **SUPPORT PHONE**: -\n* **SCHEMA CONTEXT**: br.com.kroton".format(description=self.schema_description, topic=self.topic_name))
        }

    def _make_footer(self) -> Dict:
        return {"name": "{}".format(self.class_name),
                "namespace": "br.com.kroton",
                "type": "record"}


    def create_full_schema(self):
        return self.header | self.body | self.footer 