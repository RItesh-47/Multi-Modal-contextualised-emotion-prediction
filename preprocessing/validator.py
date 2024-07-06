import json
from jsonschema import validate
from optparse import OptionParser
from argparse import ArgumentParser
import sys

def validate_json_file(file_path, schema_path):
    # Load the JSON schema
    with open(schema_path) as schema_file:
        schema = json.load(schema_file)

    # Load the JSON data from the file
    with open(file_path) as json_file:
        json_data = json.load(json_file)

    # Validate the JSON data against the schema
    try:
        validate(instance=json_data, schema=schema)
        print("Validation successful.")
    except Exception as e:
        print(f"Validation failed: {e}")

if __name__ == '__main__':
    args = ArgumentParser()
    args.add_argument('-s', '--schema', dest='schema', help='Schema file to be used for validation')
    args.add_argument('-j', '--json', dest='json', help='JSON file to be validated')
    args, _ = args.parse_known_args(sys.argv)
    
    json_file_path = args.json
    schema_file_path = args.schema
    
    # json_file_path = 'Movie.json'
    # schema_file_path = 'multi-LangMER-schema.json'
    validate_json_file(json_file_path, schema_file_path)
