import json
import os
from typing import List, Dict, Any

INPUT_FILE = 'resources/pineDocs.json'
OUTPUT_FILE = 'pinelint/pine_spec.py'

HEADER = '''"""
Pine Script Language Specification.
Auto-generated from pineDocs.json.
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Union
from enum import Enum

class TypeQualifier(Enum):
    SERIES = "series"
    SIMPLE = "simple"
    CONST = "const"
    INPUT = "input"

@dataclass
class Param:
    name: str
    type: str
    required: bool = True
    default: Optional[str] = None

@dataclass
class BuiltinFunction:
    name: str
    params: List[Param]
    return_type: str
    description: str = ""
    version_added: Optional[str] = None

@dataclass
class BuiltinVariable:
    name: str
    type: str
    description: str = ""

'''

def load_data():
    with open(INPUT_FILE, 'r') as f:
        return json.load(f)

def extract_items(data, category):
    items = []
    groups = data.get(category, [])
    for group in groups:
        items.extend(group.get('docs', []))
    return items

def clean_desc(desc):
    if not desc:
        return ""
    if isinstance(desc, list):
        desc = " ".join([str(s) for s in desc])
    return desc.split('\n')[0][:200]

def generate_spec():
    data = load_data()
    
    # Patch data with Manual v6 Additions
    # Manual Functions
    v6_functions = [
        {"name": "str.repeat", "returnedType": "string", "desc": "Repeats string.", "args": [{"name": "source", "displayType": "string"}, {"name": "count", "displayType": "int"}, {"name": "separator", "displayType": "string", "required": False}]},
        {"name": "str.trim", "returnedType": "string", "desc": "Trims string.", "args": [{"name": "source", "displayType": "string"}]},
        {"name": "input.enum", "returnedType": "any", "desc": "Enum input.", "args": [{"name": "defval", "displayType": "any"}, {"name": "options", "displayType": "any"}]},
        {"name": "ta.rci", "returnedType": "float", "desc": "Rank Correlation Index.", "args": [{"name": "source", "displayType": "series float"}, {"name": "length", "displayType": "simple int"}]},
        {"name": "box.set_text_formatting", "returnedType": "void", "desc": "Sets text formatting.", "args": [{"name": "id", "displayType": "box"}, {"name": "formatting", "displayType": "string"}]},
        {"name": "label.set_text_formatting", "returnedType": "void", "desc": "Sets text formatting.", "args": [{"name": "id", "displayType": "label"}, {"name": "formatting", "displayType": "string"}]},
        {"name": "table.cell_set_text_formatting", "returnedType": "void", "desc": "Sets text formatting.", "args": [{"name": "table_id", "displayType": "table"}, {"name": "column", "displayType": "int"}, {"name": "row", "displayType": "int"}, {"name": "formatting", "displayType": "string"}]},
    ]
    if 'functions' not in data: data['functions'] = []
    data['functions'].append({"docs": v6_functions})

    # Manual Variables
    v6_vars = [
        {"name": "ask", "type": "series float", "desc": "Ask price."},
        {"name": "bid", "type": "series float", "desc": "Bid price."},
        {"name": "syminfo.expiration_date", "type": "series int", "desc": "Expiration date."},
        {"name": "syminfo.current_contract", "type": "series string", "desc": "Current contract."},
        {"name": "syminfo.main_tickerid", "type": "simple string", "desc": "Main ticker ID."},
        {"name": "syminfo.mincontract", "type": "simple float", "desc": "Min contract."},
        {"name": "timeframe.isticks", "type": "simple bool", "desc": "Is ticks."},
        {"name": "timeframe.main_period", "type": "simple string", "desc": "Main period."},
        {"name": "text.format_bold", "type": "const string", "desc": "Bold format."},
        {"name": "text.format_italic", "type": "const string", "desc": "Italic format."},
        {"name": "text.format_none", "type": "const string", "desc": "No format."},
    ]
    if 'variables' not in data: data['variables'] = []
    data['variables'].append({"docs": v6_vars})

    # Types
    pine_types = set()
    type_groups = data.get('types', [])
    for group in type_groups:
        for t in group.get('docs', []):
            pine_types.add(t['name'])
    
    # Functions & Methods
    functions = {}
    
    raw_functions = extract_items(data, 'functions')
    raw_methods = extract_items(data, 'methods')
    
    for item in raw_functions + raw_methods:
        name = item.get('name')
        if not name: continue
        
        args = []
        for arg in item.get('args', []):
            args.append({
                "name": arg.get('name'),
                "type": arg.get('displayType', 'any'),
                "required": arg.get('required', True),
            })
            
        rt = item.get('returnedType', 'void')
        if isinstance(rt, list):
            rt = "|".join(rt)
        
        functions[name] = {
            "name": name,
            "params": args,
            "return_type": rt,
            "description": clean_desc(item.get('desc'))
        }

    # Variables & Constants
    variables = {}
    raw_vars = extract_items(data, 'variables')
    raw_consts = extract_items(data, 'constants')
    
    for item in raw_vars + raw_consts:
        name = item.get('name')
        if not name: continue
        
        # Use displayType if available, else type
        v_type = item.get('displayType', item.get('type', 'any'))

        variables[name] = {
            "name": name,
            "type": v_type,
            "description": clean_desc(item.get('desc'))
        }

    # Controls (Keywords)
    keywords = set()
    control_groups = data.get('controls', [])
    for group in control_groups:
        for item in group.get('docs', []):
            if item.get('name'):
                keywords.add(item['name'])

    with open(OUTPUT_FILE, 'w') as f:
        f.write(HEADER)
        
        # PINE_TYPES
        f.write(f"PINE_TYPES = {json.dumps(sorted(list(pine_types)), indent=4)}\n\n")
        
        # PINE_FUNCTIONS
        f.write("PINE_FUNCTIONS: Dict[str, BuiltinFunction] = {\n")
        for name, func in sorted(functions.items()):
            f.write(f'    "{name}": BuiltinFunction(\n')
            f.write(f'        name={json.dumps(func["name"])},\n')
            f.write(f'        return_type={json.dumps(func["return_type"])},\n')
            f.write(f'        description={json.dumps(func["description"])},\n')
            f.write(f'        params=[\n')
            for param in func['params']:
                f.write(f'            Param(name={json.dumps(param["name"])}, type={json.dumps(param["type"])}, required={param["required"]}),\n')
            f.write(f'        ]\n')
            f.write(f'    ),\n')
        f.write("}\n\n")
        
        # PINE_VARIABLES
        f.write("PINE_VARIABLES: Dict[str, BuiltinVariable] = {\n")
        for name, var in sorted(variables.items()):
            f.write(f'    "{name}": BuiltinVariable(\n')
            f.write(f'        name={json.dumps(var["name"])},\n')
            f.write(f'        type={json.dumps(var["type"])},\n')
            f.write(f'        description={json.dumps(var["description"])}\n')
            f.write(f'    ),\n')
        f.write("}\n\n")

        # PINE_KEYWORDS
        f.write(f"PINE_KEYWORDS = {json.dumps(sorted(list(keywords)), indent=4)}\n")

if __name__ == '__main__':
    generate_spec()
