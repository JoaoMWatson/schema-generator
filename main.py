import os

import json
import typer
import pandas as pd
from rich.console import Console
from src.schema.schema_body import SchemaBody
from src.schema.schema_structure import SchemaStructure


app = typer.Typer()
console = Console()
cur_path = os.path.dirname(__file__)


@app.command()
def main(file: str = typer.Argument(..., help="File to parse"),
         sheet_number: int = typer.Argument(..., help="Sheet number to parse"),
         topic_name: str = typer.Argument(..., help="Topic name to parse"),
         schema_description: str = typer.Argument(..., help="Schema description to parse"),):
    """
    Parse a XLSX file to create a schema registry.
    """
    try:
        if not os.path.exists(file):
            raise FileNotFoundError(f"File: {file} not found")
        else:
            dataFrame: pd.DataFrame = pd.read_excel(
                file, sheet_name=sheet_number, header=19, usecols="B:D, F, H").dropna()

            schema_body = SchemaBody(dataFrame).make_body()
            schema_structure = SchemaStructure(
                topic_name=topic_name, schema_description=schema_description, schema_body=schema_body)

            full_schema = schema_structure.create_full_schema()

            with open(f"{topic_name}-value.json", "w", encoding='utf8') as file:
                json.dump(full_schema, file, ensure_ascii=False)

    except Exception as e:
        console.print_exception()
        print(e)

    except OSError as e:
        console.log("[bold red]Could not open/read file: [/bold red]", file)
        console.print_exception()
        print(e)

    except FileNotFoundError as e:
        console.log("[bold red]File could not be found: [/bold red]", file)
        console.print_exception()
        print(e)


if __name__ == "__main__":
    app()
