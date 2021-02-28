#!/usr/bin/env python3

import argparse

import xmlschema

from pathlib import Path

# Configuration ##############################################################

SCRIPT_DIR = Path(__file__).parent

SCHEMA_FILE = 'xcal-component.xsd'
SCHEMA_PATH = SCRIPT_DIR / 'xcal-component.xsd'

# Parse the command line arguments ###########################################

argparser = argparse.ArgumentParser(description='Validate xCal component files.')
argparser.add_argument('files', metavar="FILE", nargs='+', help='xCal component file path')

args = argparser.parse_args()

# Load the schema ############################################################

schema = xmlschema.XMLSchema11(str(SCHEMA_PATH))

# Validate the component files ###############################################

for component_file in args.files:
	schema.validate(component_file)
