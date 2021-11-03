from typing import Dict

class SchemaStructure:
    def __init__(self, topic_name: str, schema_description: str):
        self.topic_name = topic_name
        self.schema_description = schema_description
        self.class_name = topic_name.title().replace("-", "")

    def make_header(self) -> Dict:
        return {
            "connect.name": "br.com.kroton.{topic_formated}".format(topic_formated=self.class_name),
            "doc": repr("* **DESCRIPTION**: {description}\n* **TOPIC**: {topic}\n* **AUTHOR TEAM**: Stream Team  **AUTHOR E-MAIL**: streamteam@cogna.com.br\n* **SUPPORT NAME**: Stream Team   **SUPORT E-MAIL**: streamteam@cogna.com.br **SUPPORT PHONE**: -\n* **SCHEMA CONTEXT**: br.com.kroton".format(description=self.schema_description, topic=self.topic_name))
        }

    def make_footer(self) -> Dict:
        return {"name": "{}".format(self.class_name),
                "namespace": "br.com.kroton",
                "type": "record"}
