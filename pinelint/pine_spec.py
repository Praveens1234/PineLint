"""
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


PINE_TYPES = [
    "array<bool>",
    "array<box>",
    "array<chart.point>",
    "array<color>",
    "array<float>",
    "array<int>",
    "array<label>",
    "array<line>",
    "array<linefill>",
    "array<polyline>",
    "array<string>",
    "array<table>",
    "array<type>",
    "bool",
    "bool[]",
    "box",
    "box[]",
    "chart.point",
    "chart.point[]",
    "color",
    "color[]",
    "float",
    "float[]",
    "int",
    "int[]",
    "label",
    "label[]",
    "line",
    "line[]",
    "linefill",
    "linefill[]",
    "map<type,type>",
    "matrix<bool>",
    "matrix<box>",
    "matrix<chart.point>",
    "matrix<color>",
    "matrix<float>",
    "matrix<int>",
    "matrix<label>",
    "matrix<line>",
    "matrix<linefill>",
    "matrix<polyline>",
    "matrix<string>",
    "matrix<table>",
    "matrix<type>",
    "polyline",
    "polyline[]",
    "series",
    "simple",
    "string",
    "string[]",
    "table",
    "table[]",
    "type[]",
]

PINE_FUNCTIONS: Dict[str, BuiltinFunction] = {
    "alert": BuiltinFunction(
        name="alert",
        return_type="void",
        description='Creates an alert event when called during the real-time bar, which will trigger a script alert based on "alert function events" if one was previously created for the indicator or strategy through the ',
        params=[
            Param(name="message", type="series string", required=True),
            Param(name="freq", type="input string", required=True),
        ],
    ),
    "alertcondition": BuiltinFunction(
        name="alertcondition",
        return_type="void",
        description="Creates alert condition, that is available in Create Alert dialog. Please note, that [alertcondition](#fun_alertcondition) does NOT create an alert, it just gives you more options in Create Alert dial",
        params=[
            Param(name="condition", type="series bool", required=True),
            Param(name="title", type="const string", required=False),
            Param(name="message", type="const string", required=False),
        ],
    ),
    "array.abs": BuiltinFunction(
        name="array.abs",
        return_type="array<int>|array<float>",
        description="Returns an array containing the absolute value of each element in the original array.",
        params=[],
    ),
    "array.avg": BuiltinFunction(
        name="array.avg",
        return_type="float|int",
        description="The function returns the mean of an array\\`s elements.",
        params=[],
    ),
    "array.binary_search": BuiltinFunction(
        name="array.binary_search",
        return_type="int",
        description="The function returns the index of the value, or -1 if the value is not found. The array to search must be sorted in ascending order.",
        params=[
            Param(name="val", type="series int|float", required=True),
        ],
    ),
    "array.binary_search_leftmost": BuiltinFunction(
        name="array.binary_search_leftmost",
        return_type="int",
        description="The function returns the index of the value if it is found. When the value is not found, the function returns the index of the next smallest element to the left of where the value would lie if it was ",
        params=[
            Param(name="val", type="series int|float", required=True),
        ],
    ),
    "array.binary_search_rightmost": BuiltinFunction(
        name="array.binary_search_rightmost",
        return_type="int",
        description="The function returns the index of the value if it is found. When the value is not found, the function returns the index of the element to the right of where the value would lie if it was in the array.",
        params=[
            Param(name="val", type="series int|float", required=True),
        ],
    ),
    "array.clear": BuiltinFunction(
        name="array.clear",
        return_type="void",
        description="The function removes all elements from an array.",
        params=[],
    ),
    "array.concat": BuiltinFunction(
        name="array.concat",
        return_type="void",
        description="The function is used to merge two arrays. It pushes all elements from the second array to the first array, and returns the first array.",
        params=[
            Param(name="id2", type="any[]", required=True),
        ],
    ),
    "array.copy": BuiltinFunction(
        name="array.copy",
        return_type="array",
        description="The function creates a copy of an existing array.",
        params=[],
    ),
    "array.covariance": BuiltinFunction(
        name="array.covariance",
        return_type="float",
        description="The function returns the covariance of two arrays.",
        params=[
            Param(name="id2", type="array<int|float>", required=True),
            Param(name="biased", type="series bool", required=False),
        ],
    ),
    "array.every": BuiltinFunction(
        name="array.every",
        return_type="bool",
        description="Returns [true](#op_true) if all elements of the `id` array are [true](#op_true), [false](#op_false) otherwise.",
        params=[],
    ),
    "array.fill": BuiltinFunction(
        name="array.fill",
        return_type="void",
        description="The function sets elements of an array to a single value. If no index is specified, all elements are set. If only a start index (default 0) is supplied, the elements starting at that index are set. If",
        params=[
            Param(name="value", type="any", required=True),
            Param(name="index_from", type="series int", required=False),
            Param(name="index_to", type="series int", required=False),
        ],
    ),
    "array.first": BuiltinFunction(
        name="array.first",
        return_type="void",
        description="Returns the array\\`s first element. Throws a runtime error if the array is empty.",
        params=[],
    ),
    "array.from": BuiltinFunction(
        name="array.from",
        return_type="array<bool>|array<int>|color[]|array<float>|string[]|line[]|label[]|table[]|linefill[]|box[]|array",
        description="The function takes a variable number of arguments with one of the types: int, float, bool, string, label, line, color, box, table, linefill, and returns an array of the corresponding type.",
        params=[
            Param(name="arg0, arg1, ...", type="any", required=True),
        ],
    ),
    "array.get": BuiltinFunction(
        name="array.get",
        return_type="void",
        description="The function returns the value of the element at the specified index.",
        params=[
            Param(name="index", type="series int", required=True),
        ],
    ),
    "array.includes": BuiltinFunction(
        name="array.includes",
        return_type="bool",
        description="The function returns true if the value was found in an array, false otherwise.",
        params=[
            Param(name="value", type="any", required=True),
        ],
    ),
    "array.indexof": BuiltinFunction(
        name="array.indexof",
        return_type="int",
        description="The function returns the index of the first occurrence of the value, or -1 if the value is not found.",
        params=[
            Param(name="value", type="any", required=True),
        ],
    ),
    "array.insert": BuiltinFunction(
        name="array.insert",
        return_type="void",
        description="The function changes the contents of an array by adding new elements in place.",
        params=[
            Param(name="index", type="series int", required=True),
            Param(name="value", type="any", required=True),
        ],
    ),
    "array.join": BuiltinFunction(
        name="array.join",
        return_type="string",
        description="The function creates and returns a new string by concatenating all the elements of an array, separated by the specified separator string.",
        params=[
            Param(name="separator", type="series string", required=True),
        ],
    ),
    "array.last": BuiltinFunction(
        name="array.last",
        return_type="void",
        description="Returns the array\\`s last element. Throws a runtime error if the array is empty.",
        params=[],
    ),
    "array.lastindexof": BuiltinFunction(
        name="array.lastindexof",
        return_type="int",
        description="The function returns the index of the last occurrence of the value, or -1 if the value is not found.",
        params=[
            Param(name="value", type="any", required=True),
        ],
    ),
    "array.max": BuiltinFunction(
        name="array.max",
        return_type="float|int",
        description="The function returns the greatest value, or the nth greatest value in a given array.",
        params=[
            Param(name="nth", type="series int", required=True),
        ],
    ),
    "array.median": BuiltinFunction(
        name="array.median",
        return_type="float|int",
        description="The function returns the median of an array\\`s elements.",
        params=[],
    ),
    "array.min": BuiltinFunction(
        name="array.min",
        return_type="float|int",
        description="The function returns the smallest value, or the nth smallest value in a given array.",
        params=[
            Param(name="nth", type="series int", required=True),
        ],
    ),
    "array.mode": BuiltinFunction(
        name="array.mode",
        return_type="float|int",
        description="The function returns the mode of an array\\`s elements. If there are several values with the same frequency, it returns the smallest value.",
        params=[],
    ),
    "array.new<bool>": BuiltinFunction(
        name="array.new<bool>",
        return_type="array<bool>",
        description="The function creates a new array object of bool type elements.",
        params=[
            Param(name="size", type="series int", required=False),
            Param(name="initial_value", type="series bool", required=False),
        ],
    ),
    "array.new<box>": BuiltinFunction(
        name="array.new<box>",
        return_type="array<box>",
        description="The function creates a new array object of box type elements.",
        params=[
            Param(name="size", type="series int", required=False),
            Param(name="initial_value", type="series box", required=False),
        ],
    ),
    "array.new<color>": BuiltinFunction(
        name="array.new<color>",
        return_type="array<color>",
        description="The function creates a new array object of color type elements.",
        params=[
            Param(name="size", type="series int", required=False),
            Param(name="initial_value", type="series color", required=False),
        ],
    ),
    "array.new<float>": BuiltinFunction(
        name="array.new<float>",
        return_type="array<float>",
        description="The function creates a new array object of float type elements.",
        params=[
            Param(name="size", type="series int", required=False),
            Param(name="initial_value", type="series int|float", required=False),
        ],
    ),
    "array.new<int>": BuiltinFunction(
        name="array.new<int>",
        return_type="array<int>",
        description="The function creates a new array object of int type elements.",
        params=[
            Param(name="size", type="series int", required=False),
            Param(name="initial_value", type="series int", required=False),
        ],
    ),
    "array.new<label>": BuiltinFunction(
        name="array.new<label>",
        return_type="array<label>",
        description="The function creates a new array object of label type elements.",
        params=[
            Param(name="size", type="series int", required=False),
            Param(name="initial_value", type="series label", required=False),
        ],
    ),
    "array.new<line>": BuiltinFunction(
        name="array.new<line>",
        return_type="array<line>",
        description="The function creates a new array object of line type elements.",
        params=[
            Param(name="size", type="series int", required=False),
            Param(name="initial_value", type="series line", required=False),
        ],
    ),
    "array.new<linefill>": BuiltinFunction(
        name="array.new<linefill>",
        return_type="array<linefill>",
        description="The function creates a new array object of linefill type elements.",
        params=[
            Param(name="size", type="series int", required=True),
            Param(name="initial_value", type="series linefill", required=True),
        ],
    ),
    "array.new<string>": BuiltinFunction(
        name="array.new<string>",
        return_type="array<string>",
        description="The function creates a new array object of string type elements.",
        params=[
            Param(name="size", type="series int", required=False),
            Param(name="initial_value", type="series string", required=False),
        ],
    ),
    "array.new<table>": BuiltinFunction(
        name="array.new<table>",
        return_type="array<table>",
        description="The function creates a new array object of table type elements.",
        params=[
            Param(name="size", type="series int", required=False),
            Param(name="initial_value", type="series table", required=False),
        ],
    ),
    "array.new<type>": BuiltinFunction(
        name="array.new<type>",
        return_type="void",
        description="The function creates a new array object of <type> elements.",
        params=[
            Param(name="size", type="series int", required=False),
            Param(name="initial_value", type="<array_type>", required=False),
        ],
    ),
    "array.new_bool": BuiltinFunction(
        name="array.new_bool",
        return_type="array<bool>",
        description="The function creates a new array object of bool type elements.",
        params=[
            Param(name="size", type="series int", required=False),
            Param(name="initial_value", type="series bool", required=False),
        ],
    ),
    "array.new_box": BuiltinFunction(
        name="array.new_box",
        return_type="array<box>",
        description="The function creates a new array object of box type elements.",
        params=[
            Param(name="size", type="series int", required=False),
            Param(name="initial_value", type="series box", required=False),
        ],
    ),
    "array.new_color": BuiltinFunction(
        name="array.new_color",
        return_type="array<color>",
        description="The function creates a new array object of color type elements.",
        params=[
            Param(name="size", type="series int", required=False),
            Param(name="initial_value", type="series color", required=False),
        ],
    ),
    "array.new_float": BuiltinFunction(
        name="array.new_float",
        return_type="array<float>",
        description="The function creates a new array object of float type elements.",
        params=[
            Param(name="size", type="series int", required=False),
            Param(name="initial_value", type="series int|float", required=False),
        ],
    ),
    "array.new_int": BuiltinFunction(
        name="array.new_int",
        return_type="array<int>",
        description="The function creates a new array object of int type elements.",
        params=[
            Param(name="size", type="series int", required=False),
            Param(name="initial_value", type="series int", required=False),
        ],
    ),
    "array.new_label": BuiltinFunction(
        name="array.new_label",
        return_type="array<label>",
        description="The function creates a new array object of label type elements.",
        params=[
            Param(name="size", type="series int", required=False),
            Param(name="initial_value", type="series label", required=False),
        ],
    ),
    "array.new_line": BuiltinFunction(
        name="array.new_line",
        return_type="array<line>",
        description="The function creates a new array object of line type elements.",
        params=[
            Param(name="size", type="series int", required=False),
            Param(name="initial_value", type="series line", required=False),
        ],
    ),
    "array.new_linefill": BuiltinFunction(
        name="array.new_linefill",
        return_type="array<linefill>",
        description="The function creates a new array object of linefill type elements.",
        params=[
            Param(name="size", type="series int", required=True),
            Param(name="initial_value", type="series linefill", required=True),
        ],
    ),
    "array.new_string": BuiltinFunction(
        name="array.new_string",
        return_type="array<string>",
        description="The function creates a new array object of string type elements.",
        params=[
            Param(name="size", type="series int", required=False),
            Param(name="initial_value", type="series string", required=False),
        ],
    ),
    "array.new_table": BuiltinFunction(
        name="array.new_table",
        return_type="array<table>",
        description="The function creates a new array object of table type elements.",
        params=[
            Param(name="size", type="series int", required=False),
            Param(name="initial_value", type="series table", required=False),
        ],
    ),
    "array.percentile_linear_interpolation": BuiltinFunction(
        name="array.percentile_linear_interpolation",
        return_type="float|int",
        description="Returns the value for which the specified percentage of array values (percentile) are less than or equal to it, using linear interpolation.",
        params=[
            Param(name="percentage", type="series int|float", required=True),
        ],
    ),
    "array.percentile_nearest_rank": BuiltinFunction(
        name="array.percentile_nearest_rank",
        return_type="float|int",
        description="Returns the value for which the specified percentage of array values (percentile) are less than or equal to it, using the nearest-rank method.",
        params=[
            Param(name="percentage", type="series int|float", required=True),
        ],
    ),
    "array.percentrank": BuiltinFunction(
        name="array.percentrank",
        return_type="float|int",
        description="Returns the percentile rank of the element at the specified `index`.",
        params=[
            Param(name="index", type="series int", required=True),
        ],
    ),
    "array.pop": BuiltinFunction(
        name="array.pop",
        return_type="void",
        description="The function removes the last element from an array and returns its value.",
        params=[],
    ),
    "array.push": BuiltinFunction(
        name="array.push",
        return_type="void",
        description="The function appends a value to an array.",
        params=[
            Param(name="value", type="any", required=True),
        ],
    ),
    "array.range": BuiltinFunction(
        name="array.range",
        return_type="float|int",
        description="The function returns the difference between the min and max values from a given array.",
        params=[],
    ),
    "array.remove": BuiltinFunction(
        name="array.remove",
        return_type="void",
        description="The function changes the contents of an array by removing the element with the specified index.",
        params=[
            Param(name="index", type="series int", required=True),
        ],
    ),
    "array.reverse": BuiltinFunction(
        name="array.reverse",
        return_type="void",
        description="The function reverses an array. The first array element becomes the last, and the last array element becomes the first.",
        params=[],
    ),
    "array.set": BuiltinFunction(
        name="array.set",
        return_type="void",
        description="The function sets the value of the element at the specified index.",
        params=[
            Param(name="index", type="series int", required=True),
            Param(name="value", type="any", required=True),
        ],
    ),
    "array.shift": BuiltinFunction(
        name="array.shift",
        return_type="void",
        description="The function removes an array\\`s first element and returns its value.",
        params=[],
    ),
    "array.size": BuiltinFunction(
        name="array.size",
        return_type="int",
        description="The function returns the number of elements in an array.",
        params=[],
    ),
    "array.slice": BuiltinFunction(
        name="array.slice",
        return_type="void",
        description="The function creates a slice from an existing array. If an object from the slice changes, the changes are applied to both the new and the original arrays.",
        params=[
            Param(name="index_from", type="series int", required=True),
            Param(name="index_to", type="series int", required=True),
        ],
    ),
    "array.some": BuiltinFunction(
        name="array.some",
        return_type="bool",
        description="Returns [true](#op_true) if at least one element of the `id` array is [true](#op_true), [false](#op_false) otherwise.",
        params=[],
    ),
    "array.sort": BuiltinFunction(
        name="array.sort",
        return_type="void",
        description="The function sorts the elements of an array.",
        params=[
            Param(name="order", type="simple sort_order", required=False),
        ],
    ),
    "array.sort_indices": BuiltinFunction(
        name="array.sort_indices",
        return_type="array<int>",
        description="Returns an array of indices which, when used to index the original array, will access its elements in their sorted order. It does not modify the original array.",
        params=[
            Param(name="order", type="series sort_order", required=False),
        ],
    ),
    "array.standardize": BuiltinFunction(
        name="array.standardize",
        return_type="array<int>|array<float>",
        description="The function returns the array of standardized elements.",
        params=[],
    ),
    "array.stdev": BuiltinFunction(
        name="array.stdev",
        return_type="float|int",
        description="The function returns the standard deviation of an array\\`s elements.",
        params=[
            Param(name="biased", type="series bool", required=False),
        ],
    ),
    "array.sum": BuiltinFunction(
        name="array.sum",
        return_type="float|int",
        description="The function returns the sum of an array\\`s elements.",
        params=[],
    ),
    "array.unshift": BuiltinFunction(
        name="array.unshift",
        return_type="void",
        description="The function inserts the value at the beginning of the array.",
        params=[
            Param(name="value", type="any", required=True),
        ],
    ),
    "array.variance": BuiltinFunction(
        name="array.variance",
        return_type="float|int",
        description="The function returns the variance of an array\\`s elements.",
        params=[
            Param(name="biased", type="series bool", required=False),
        ],
    ),
    "barcolor": BuiltinFunction(
        name="barcolor",
        return_type="void",
        description="Set color of bars.",
        params=[
            Param(name="color", type="series color", required=True),
            Param(name="offset", type="series int", required=False),
            Param(name="editable", type="const bool", required=False),
            Param(name="show_last", type="input int", required=True),
            Param(name="title", type="const string", required=False),
            Param(name="display", type="input plot_simple_display", required=False),
        ],
    ),
    "bgcolor": BuiltinFunction(
        name="bgcolor",
        return_type="void",
        description="Fill background of bars with specified color.",
        params=[
            Param(name="color", type="series color", required=True),
            Param(name="offset", type="series int", required=False),
            Param(name="editable", type="const bool", required=False),
            Param(name="show_last", type="input int", required=True),
            Param(name="title", type="const string", required=False),
            Param(name="display", type="input plot_simple_display", required=False),
        ],
    ),
    "bool": BuiltinFunction(
        name="bool",
        return_type="bool",
        description="Casts na to bool.",
        params=[
            Param(name="x", type="series color", required=True),
        ],
    ),
    "box": BuiltinFunction(
        name="box",
        return_type="box",
        description="Casts na to box.",
        params=[
            Param(name="x", type="series box", required=True),
        ],
    ),
    "box.copy": BuiltinFunction(
        name="box.copy",
        return_type="box",
        description="Clones the box object.",
        params=[],
    ),
    "box.delete": BuiltinFunction(
        name="box.delete",
        return_type="void",
        description="Deletes the specified box object. If it has already been deleted, does nothing.",
        params=[],
    ),
    "box.get_bottom": BuiltinFunction(
        name="box.get_bottom",
        return_type="float",
        description="Returns the price value of the bottom border of the box.",
        params=[],
    ),
    "box.get_left": BuiltinFunction(
        name="box.get_left",
        return_type="int",
        description="Returns the bar index or the UNIX time (depending on the last value used for 'xloc') of the left border of the box.",
        params=[],
    ),
    "box.get_right": BuiltinFunction(
        name="box.get_right",
        return_type="int",
        description="Returns the bar index or the UNIX time (depending on the last value used for 'xloc') of the right border of the box.",
        params=[],
    ),
    "box.get_top": BuiltinFunction(
        name="box.get_top",
        return_type="float",
        description="Returns the price value of the top border of the box.",
        params=[],
    ),
    "box.new": BuiltinFunction(
        name="box.new",
        return_type="box",
        description="Creates a new box object.",
        params=[
            Param(name="left", type="series int", required=True),
            Param(name="top", type="series int|float", required=True),
            Param(name="right", type="series int", required=True),
            Param(name="bottom", type="series int|float", required=True),
            Param(name="border_color", type="series color", required=False),
            Param(name="border_width", type="series int", required=False),
            Param(name="border_style", type="series string", required=False),
            Param(name="extend", type="series string", required=False),
            Param(name="xloc", type="series string", required=False),
            Param(name="bgcolor", type="series color", required=False),
            Param(name="text", type="series string", required=False),
            Param(name="text_size", type="series string", required=False),
            Param(name="text_font_family", type="series string", required=False),
            Param(name="text_color", type="series color", required=False),
            Param(name="text_halign", type="series string", required=False),
            Param(name="text_valign", type="series string", required=False),
            Param(name="text_wrap", type="series string", required=False),
            Param(name="top_left", type="chart.point", required=True),
            Param(name="bottom_right", type="chart.point", required=True),
        ],
    ),
    "box.set_bgcolor": BuiltinFunction(
        name="box.set_bgcolor",
        return_type="void",
        description="Sets the background color of the box.",
        params=[
            Param(name="color", type="series color", required=True),
        ],
    ),
    "box.set_border_color": BuiltinFunction(
        name="box.set_border_color",
        return_type="void",
        description="Sets the border color of the box.",
        params=[
            Param(name="color", type="series color", required=True),
        ],
    ),
    "box.set_border_style": BuiltinFunction(
        name="box.set_border_style",
        return_type="void",
        description="Sets the border style of the box.",
        params=[
            Param(name="style", type="series string", required=True),
        ],
    ),
    "box.set_border_width": BuiltinFunction(
        name="box.set_border_width",
        return_type="void",
        description="Sets the border width of the box.",
        params=[
            Param(name="width", type="series int", required=True),
        ],
    ),
    "box.set_bottom": BuiltinFunction(
        name="box.set_bottom",
        return_type="void",
        description="Sets the bottom coordinate of the box.",
        params=[
            Param(name="bottom", type="series int|float", required=True),
        ],
    ),
    "box.set_bottom_right_point": BuiltinFunction(
        name="box.set_bottom_right_point",
        return_type="void",
        description="Sets the bottom-right corner location of the `id` box to `point`.",
        params=[
            Param(name="point", type="chart.point", required=True),
        ],
    ),
    "box.set_extend": BuiltinFunction(
        name="box.set_extend",
        return_type="void",
        description="Sets extending type of the border of this box object. When [extend.none](#var_extend.none) is used, the horizontal borders start at the left border and end at the right border.  ",
        params=[
            Param(name="extend", type="series string", required=True),
        ],
    ),
    "box.set_left": BuiltinFunction(
        name="box.set_left",
        return_type="void",
        description="Sets the left coordinate of the box.",
        params=[
            Param(name="left", type="series int", required=True),
        ],
    ),
    "box.set_lefttop": BuiltinFunction(
        name="box.set_lefttop",
        return_type="void",
        description="Sets the left and top coordinates of the box.",
        params=[
            Param(name="left", type="series int", required=True),
            Param(name="top", type="series int|float", required=True),
        ],
    ),
    "box.set_right": BuiltinFunction(
        name="box.set_right",
        return_type="void",
        description="Sets the right coordinate of the box.",
        params=[
            Param(name="right", type="series int", required=True),
        ],
    ),
    "box.set_rightbottom": BuiltinFunction(
        name="box.set_rightbottom",
        return_type="void",
        description="Sets the right and bottom coordinates of the box.",
        params=[
            Param(name="right", type="series int", required=True),
            Param(name="bottom", type="series int|float", required=True),
        ],
    ),
    "box.set_text": BuiltinFunction(
        name="box.set_text",
        return_type="void",
        description="The function sets the text in the box.",
        params=[
            Param(name="text", type="series string", required=True),
        ],
    ),
    "box.set_text_color": BuiltinFunction(
        name="box.set_text_color",
        return_type="void",
        description="The function sets the color of the text inside the box.",
        params=[
            Param(name="text_color", type="series color", required=True),
        ],
    ),
    "box.set_text_font_family": BuiltinFunction(
        name="box.set_text_font_family",
        return_type="void",
        description="The function sets the font family of the text inside the box.",
        params=[
            Param(name="text_font_family", type="series string", required=True),
        ],
    ),
    "box.set_text_formatting": BuiltinFunction(
        name="box.set_text_formatting",
        return_type="void",
        description="Sets text formatting.",
        params=[
            Param(name="id", type="box", required=True),
            Param(name="formatting", type="string", required=True),
        ],
    ),
    "box.set_text_halign": BuiltinFunction(
        name="box.set_text_halign",
        return_type="void",
        description="The function sets the horizontal alignment of the box\\`s text.",
        params=[
            Param(name="text_halign", type="series string", required=True),
        ],
    ),
    "box.set_text_size": BuiltinFunction(
        name="box.set_text_size",
        return_type="void",
        description="The function sets the size of the box\\`s text.",
        params=[
            Param(name="text_size", type="series string", required=True),
        ],
    ),
    "box.set_text_valign": BuiltinFunction(
        name="box.set_text_valign",
        return_type="void",
        description="The function sets the vertical alignment of a box\\`s text.",
        params=[
            Param(name="text_valign", type="series string", required=True),
        ],
    ),
    "box.set_text_wrap": BuiltinFunction(
        name="box.set_text_wrap",
        return_type="void",
        description="The function sets the mode of wrapping of the text inside the box.",
        params=[
            Param(name="text_wrap", type="series string", required=True),
        ],
    ),
    "box.set_top": BuiltinFunction(
        name="box.set_top",
        return_type="void",
        description="Sets the top coordinate of the box.",
        params=[
            Param(name="top", type="series int|float", required=True),
        ],
    ),
    "box.set_top_left_point": BuiltinFunction(
        name="box.set_top_left_point",
        return_type="void",
        description="Sets the top-left corner location of the `id` box to `point`.",
        params=[
            Param(name="point", type="chart.point", required=True),
        ],
    ),
    "chart.point.copy": BuiltinFunction(
        name="chart.point.copy",
        return_type="chart.point",
        description="Creates a copy of a [chart.point](#op_chart.point) object with the specified `id`.",
        params=[],
    ),
    "chart.point.from_index": BuiltinFunction(
        name="chart.point.from_index",
        return_type="chart.point",
        description="Returns a [chart.point](#op_chart.point) object with `index` as its x-coordinate and `price` as its y-coordinate.",
        params=[
            Param(name="index", type="series int", required=True),
            Param(name="price", type="series int|float", required=True),
        ],
    ),
    "chart.point.from_time": BuiltinFunction(
        name="chart.point.from_time",
        return_type="chart.point",
        description="Returns a [chart.point](#op_chart.point) object with `time` as its x-coordinate and `price` as its y-coordinate.",
        params=[
            Param(name="time", type="series int", required=True),
            Param(name="price", type="series int|float", required=True),
        ],
    ),
    "chart.point.new": BuiltinFunction(
        name="chart.point.new",
        return_type="void",
        description="Creates a new [chart.point](#op_chart.point) object with the specified `time`, `index`, and `price`.",
        params=[
            Param(name="time", type="series int", required=True),
            Param(name="index", type="series int", required=True),
            Param(name="price", type="series int/float", required=True),
        ],
    ),
    "chart.point.now": BuiltinFunction(
        name="chart.point.now",
        return_type="chart.point",
        description="Returns a [chart.point](#op_chart.point) object with `price` as the y-coordinate",
        params=[
            Param(name="price", type="series int|float", required=False),
        ],
    ),
    "color": BuiltinFunction(
        name="color",
        return_type="color",
        description="Casts na to color",
        params=[
            Param(name="x", type="series color", required=True),
        ],
    ),
    "color.b": BuiltinFunction(
        name="color.b",
        return_type="float",
        description="Retrieves the value of the color\\`s blue component.",
        params=[
            Param(name="color", type="series color", required=True),
        ],
    ),
    "color.from_gradient": BuiltinFunction(
        name="color.from_gradient",
        return_type="color",
        description="Based on the relative position of value in the bottom_value to top_value range, the function returns a color from the gradient defined by bottom_color to top_color.",
        params=[
            Param(name="value", type="series int|float", required=True),
            Param(name="bottom_value", type="series int|float", required=True),
            Param(name="top_value", type="series int|float", required=True),
            Param(name="bottom_color", type="series color", required=True),
            Param(name="top_color", type="series color", required=True),
        ],
    ),
    "color.g": BuiltinFunction(
        name="color.g",
        return_type="float",
        description="Retrieves the value of the color\\`s green component.",
        params=[
            Param(name="color", type="series color", required=True),
        ],
    ),
    "color.new": BuiltinFunction(
        name="color.new",
        return_type="color",
        description="Function color applies the specified transparency to the given color.",
        params=[
            Param(name="color", type="series color", required=True),
            Param(name="transp", type="series int|float", required=True),
        ],
    ),
    "color.r": BuiltinFunction(
        name="color.r",
        return_type="float",
        description="Retrieves the value of the color\\`s red component.",
        params=[
            Param(name="color", type="series color", required=True),
        ],
    ),
    "color.rgb": BuiltinFunction(
        name="color.rgb",
        return_type="color",
        description="Creates a new color with transparency using the RGB color model.",
        params=[
            Param(name="red", type="series int|float", required=True),
            Param(name="green", type="series int|float", required=True),
            Param(name="blue", type="series int|float", required=True),
            Param(name="transp", type="series int|float", required=False),
        ],
    ),
    "color.t": BuiltinFunction(
        name="color.t",
        return_type="float",
        description="Retrieves the color\\`s transparency.",
        params=[
            Param(name="color", type="series color", required=True),
        ],
    ),
    "dayofmonth": BuiltinFunction(
        name="dayofmonth",
        return_type="int",
        description="",
        params=[
            Param(name="time", type="series int", required=True),
            Param(name="timezone", type="series string", required=True),
        ],
    ),
    "dayofweek": BuiltinFunction(
        name="dayofweek",
        return_type="int",
        description="",
        params=[
            Param(name="time", type="series int", required=True),
            Param(name="timezone", type="series string", required=True),
        ],
    ),
    "fill": BuiltinFunction(
        name="fill",
        return_type="void",
        description="Fills background between two plots or hlines with a given color.",
        params=[
            Param(name="hline1", type="hline", required=True),
            Param(name="hline2", type="hline", required=True),
            Param(name="plot1", type="plot", required=True),
            Param(name="plot2", type="plot", required=True),
            Param(name="color", type="series color", required=False),
            Param(name="title", type="const string", required=False),
            Param(name="editable", type="const bool", required=False),
            Param(name="show_last", type="input int", required=True),
            Param(name="fillgaps", type="const bool", required=False),
            Param(name="display", type="input plot_simple_display", required=False),
            Param(name="top_value", type="series int|float", required=True),
            Param(name="bottom_value", type="series int|float", required=True),
            Param(name="top_color", type="series color", required=True),
            Param(name="bottom_color", type="series color", required=True),
        ],
    ),
    "fixnan": BuiltinFunction(
        name="fixnan",
        return_type="float|color|int|bool",
        description="For a given series replaces NaN values with previous nearest non-NaN value.",
        params=[
            Param(name="source", type="series int|float|bool|color", required=True),
        ],
    ),
    "float": BuiltinFunction(
        name="float",
        return_type="float",
        description="Casts na to float",
        params=[
            Param(name="x", type="series float", required=True),
        ],
    ),
    "hline": BuiltinFunction(
        name="hline",
        return_type="hline",
        description="Renders a horizontal line at a given fixed price level.",
        params=[
            Param(name="price", type="input int|float", required=True),
            Param(name="title", type="const string", required=True),
            Param(name="color", type="input color", required=False),
            Param(name="linestyle", type="input hline_style", required=False),
            Param(name="linewidth", type="input int", required=False),
            Param(name="editable", type="const bool", required=False),
            Param(name="display", type="input plot_simple_display", required=False),
        ],
    ),
    "hour": BuiltinFunction(
        name="hour",
        return_type="int",
        description="",
        params=[
            Param(name="time", type="series int", required=True),
            Param(name="timezone", type="series string", required=True),
        ],
    ),
    "indicator": BuiltinFunction(
        name="indicator",
        return_type="void",
        description="This declaration statement designates the script as an indicator and sets a number of indicator-related properties.",
        params=[
            Param(name="title", type="const string", required=True),
            Param(name="shorttitle", type="const string", required=False),
            Param(name="overlay", type="const bool", required=False),
            Param(name="format", type="const string", required=False),
            Param(name="precision", type="const int", required=False),
            Param(name="scale", type="const scale_type", required=False),
            Param(name="max_bars_back", type="const int", required=False),
            Param(name="timeframe", type="const string", required=False),
            Param(name="timeframe_gaps", type="const bool", required=False),
            Param(name="explicit_plot_zorder", type="const bool", required=False),
            Param(name="max_lines_count", type="const int", required=False),
            Param(name="max_labels_count", type="const int", required=False),
            Param(name="max_boxes_count", type="const int", required=False),
            Param(name="max_polylines_count", type="const int", required=False),
        ],
    ),
    "input": BuiltinFunction(
        name="input",
        return_type="string|int|bool|float|color",
        description="Adds an input to the Inputs tab of your script\\`s Settings, which allows you to provide configuration options to script users. This function automatically detects the type of the argument used for 'de",
        params=[
            Param(
                name="defval",
                type="const int|float|bool|string|color|<open|high|low|close|hl2|hlc3|ohlc4|hlcc4>",
                required=True,
            ),
            Param(name="title", type="const string", required=False),
            Param(name="tooltip", type="const string", required=False),
            Param(name="inline", type="const string", required=False),
            Param(name="group", type="const string", required=False),
            Param(name="display", type="const plot_display", required=False),
        ],
    ),
    "input.bool": BuiltinFunction(
        name="input.bool",
        return_type="bool",
        description="Adds an input to the Inputs tab of your script\\`s Settings, which allows you to provide configuration options to script users. This function adds a checkmark to the script\\`s inputs.",
        params=[
            Param(name="defval", type="const bool", required=True),
            Param(name="title", type="const string", required=False),
            Param(name="tooltip", type="const string", required=False),
            Param(name="inline", type="const string", required=False),
            Param(name="group", type="const string", required=False),
            Param(name="confirm", type="const bool", required=False),
            Param(name="display", type="const plot_display", required=False),
        ],
    ),
    "input.color": BuiltinFunction(
        name="input.color",
        return_type="color",
        description="Adds an input to the Inputs tab of your script\\`s Settings, which allows you to provide configuration options to script users. This function adds a color picker that allows the user to select a color ",
        params=[
            Param(name="defval", type="const color", required=True),
            Param(name="title", type="const string", required=False),
            Param(name="tooltip", type="const string", required=False),
            Param(name="inline", type="const string", required=False),
            Param(name="group", type="const string", required=False),
            Param(name="confirm", type="const bool", required=False),
            Param(name="display", type="const plot_display", required=False),
        ],
    ),
    "input.enum": BuiltinFunction(
        name="input.enum",
        return_type="any",
        description="Enum input.",
        params=[
            Param(name="defval", type="any", required=True),
            Param(name="options", type="any", required=True),
        ],
    ),
    "input.float": BuiltinFunction(
        name="input.float",
        return_type="float",
        description="Adds an input to the Inputs tab of your script\\`s Settings, which allows you to provide configuration options to script users. This function adds a field for a float input to the script\\`s inputs.",
        params=[
            Param(name="defval", type="const int|float", required=True),
            Param(name="title", type="const string", required=False),
            Param(name="minval", type="const int|float", required=False),
            Param(name="maxval", type="const int|float", required=False),
            Param(name="step", type="const int|float", required=False),
            Param(
                name="options", type="const int|float [val1, val2, ...]", required=True
            ),
            Param(name="tooltip", type="const string", required=False),
            Param(name="inline", type="const string", required=False),
            Param(name="group", type="const string", required=False),
            Param(name="confirm", type="const bool", required=False),
            Param(name="display", type="const plot_display", required=False),
        ],
    ),
    "input.int": BuiltinFunction(
        name="input.int",
        return_type="int",
        description="Adds an input to the Inputs tab of your script\\`s Settings, which allows you to provide configuration options to script users. This function adds a field for an integer input to the script\\`s inputs.",
        params=[
            Param(name="defval", type="const int", required=True),
            Param(name="title", type="const string", required=False),
            Param(name="minval", type="const int", required=False),
            Param(name="maxval", type="const int", required=False),
            Param(name="step", type="const int", required=False),
            Param(name="options", type="const int [val1, val2, ...]", required=True),
            Param(name="tooltip", type="const string", required=False),
            Param(name="inline", type="const string", required=False),
            Param(name="group", type="const string", required=False),
            Param(name="confirm", type="const bool", required=False),
            Param(name="display", type="const plot_display", required=False),
        ],
    ),
    "input.price": BuiltinFunction(
        name="input.price",
        return_type="float",
        description='Adds a price input to the script\\`s "Settings/Inputs" tab. Using `confirm = true` activates the interactive input mode where a price is selected by clicking on the chart.',
        params=[
            Param(name="defval", type="const int|float", required=True),
            Param(name="title", type="const string", required=False),
            Param(name="tooltip", type="const string", required=False),
            Param(name="inline", type="const string", required=False),
            Param(name="group", type="const string", required=False),
            Param(name="confirm", type="const bool", required=False),
            Param(name="display", type="const plot_display", required=False),
        ],
    ),
    "input.session": BuiltinFunction(
        name="input.session",
        return_type="string",
        description="Adds an input to the Inputs tab of your script\\`s Settings, which allows you to provide configuration options to script users. This function adds two dropdowns that allow the user to specify the begin",
        params=[
            Param(name="defval", type="const string", required=True),
            Param(name="title", type="const string", required=False),
            Param(
                name="options", type="const string [val1, val2, ...]", required=False
            ),
            Param(name="tooltip", type="const string", required=False),
            Param(name="inline", type="const string", required=False),
            Param(name="group", type="const string", required=False),
            Param(name="confirm", type="const bool", required=False),
            Param(name="display", type="const plot_display", required=False),
        ],
    ),
    "input.source": BuiltinFunction(
        name="input.source",
        return_type="float",
        description="Adds an input to the Inputs tab of your script\\`s Settings, which allows you to provide configuration options to script users.  ",
        params=[
            Param(
                name="defval",
                type="<open|high|low|close|hl2|hlc3|ohlc4|hlcc4>",
                required=True,
            ),
            Param(name="title", type="const string", required=False),
            Param(name="tooltip", type="const string", required=False),
            Param(name="inline", type="const string", required=False),
            Param(name="group", type="const string", required=False),
            Param(name="display", type="const plot_display", required=False),
        ],
    ),
    "input.string": BuiltinFunction(
        name="input.string",
        return_type="string",
        description="Adds an input to the Inputs tab of your script\\`s Settings, which allows you to provide configuration options to script users. This function adds a field for a string input to the script\\`s inputs.",
        params=[
            Param(name="defval", type="const string", required=True),
            Param(name="title", type="const string", required=False),
            Param(
                name="options", type="const string [val1, val2, ...]", required=False
            ),
            Param(name="tooltip", type="const string", required=False),
            Param(name="inline", type="const string", required=False),
            Param(name="group", type="const string", required=False),
            Param(name="confirm", type="const bool", required=False),
            Param(name="display", type="const plot_display", required=False),
        ],
    ),
    "input.symbol": BuiltinFunction(
        name="input.symbol",
        return_type="string",
        description="Adds an input to the Inputs tab of your script\\`s Settings, which allows you to provide configuration options to script users. This function adds a field that allows the user to select a specific symb",
        params=[
            Param(name="defval", type="const string", required=True),
            Param(name="title", type="const string", required=False),
            Param(name="tooltip", type="const string", required=False),
            Param(name="inline", type="const string", required=False),
            Param(name="group", type="const string", required=False),
            Param(name="confirm", type="const bool", required=False),
            Param(name="display", type="const plot_display", required=False),
        ],
    ),
    "input.text_area": BuiltinFunction(
        name="input.text_area",
        return_type="string",
        description="Adds an input to the Inputs tab of your script\\`s Settings, which allows you to provide configuration options to script users. This function adds a field for a multiline text input.",
        params=[
            Param(name="defval", type="const string", required=True),
            Param(name="title", type="const string", required=False),
            Param(name="tooltip", type="const string", required=False),
            Param(name="group", type="const string", required=False),
            Param(name="confirm", type="const bool", required=False),
            Param(name="display", type="const plot_display", required=False),
        ],
    ),
    "input.time": BuiltinFunction(
        name="input.time",
        return_type="int",
        description='Adds a time input to the script\\`s "Settings/Inputs" tab. This function adds two input widgets on the same line: one for the date and one for the time.  ',
        params=[
            Param(name="defval", type="const int", required=True),
            Param(name="title", type="const string", required=False),
            Param(name="tooltip", type="const string", required=False),
            Param(name="inline", type="const string", required=False),
            Param(name="group", type="const string", required=False),
            Param(name="confirm", type="const bool", required=False),
            Param(name="display", type="const plot_display", required=False),
        ],
    ),
    "input.timeframe": BuiltinFunction(
        name="input.timeframe",
        return_type="string",
        description="Adds an input to the Inputs tab of your script\\`s Settings, which allows you to provide configuration options to script users. This function adds a dropdown that allows the user to select a specific t",
        params=[
            Param(name="defval", type="const string", required=True),
            Param(name="title", type="const string", required=False),
            Param(
                name="options", type="const string [val1, val2, ...]", required=False
            ),
            Param(name="tooltip", type="const string", required=False),
            Param(name="inline", type="const string", required=False),
            Param(name="group", type="const string", required=False),
            Param(name="confirm", type="const bool", required=False),
            Param(name="display", type="const plot_display", required=False),
        ],
    ),
    "int": BuiltinFunction(
        name="int",
        return_type="int",
        description="Casts na or truncates float value to int.",
        params=[
            Param(name="x", type="series int", required=True),
        ],
    ),
    "label": BuiltinFunction(
        name="label",
        return_type="label",
        description="Casts na to label.",
        params=[
            Param(name="x", type="series label", required=True),
        ],
    ),
    "label.copy": BuiltinFunction(
        name="label.copy",
        return_type="label",
        description="Clones the label object.",
        params=[],
    ),
    "label.delete": BuiltinFunction(
        name="label.delete",
        return_type="void",
        description="Deletes the specified label object. If it has already been deleted, does nothing.",
        params=[],
    ),
    "label.get_text": BuiltinFunction(
        name="label.get_text",
        return_type="string",
        description="Returns the text of this label object.",
        params=[],
    ),
    "label.get_x": BuiltinFunction(
        name="label.get_x",
        return_type="int",
        description="Returns UNIX time or bar index (depending on the last xloc value set) of this label\\`s position.",
        params=[],
    ),
    "label.get_y": BuiltinFunction(
        name="label.get_y",
        return_type="float",
        description="Returns price of this label\\`s position.",
        params=[],
    ),
    "label.new": BuiltinFunction(
        name="label.new",
        return_type="label",
        description="Creates new label object.",
        params=[
            Param(name="x", type="series int", required=True),
            Param(name="y", type="series int|float", required=True),
            Param(name="text", type="series string", required=False),
            Param(name="xloc", type="series string", required=False),
            Param(name="yloc", type="series string", required=False),
            Param(name="color", type="series color", required=False),
            Param(name="style", type="series string", required=False),
            Param(name="textcolor", type="series color", required=False),
            Param(name="size", type="series string", required=False),
            Param(name="textalign", type="series string", required=False),
            Param(name="tooltip", type="series string", required=False),
            Param(name="text_font_family", type="series string", required=False),
            Param(name="point", type="chart.point", required=True),
        ],
    ),
    "label.set_color": BuiltinFunction(
        name="label.set_color",
        return_type="void",
        description="Sets label bgcolor",
        params=[
            Param(name="color", type="series color", required=True),
        ],
    ),
    "label.set_point": BuiltinFunction(
        name="label.set_point",
        return_type="void",
        description="Sets the location of the `id` label to `point`.",
        params=[
            Param(name="point", type="chart.point", required=True),
        ],
    ),
    "label.set_size": BuiltinFunction(
        name="label.set_size",
        return_type="void",
        description="Sets arrow and text size of the specified label object.",
        params=[
            Param(name="size", type="series string", required=True),
        ],
    ),
    "label.set_style": BuiltinFunction(
        name="label.set_style",
        return_type="void",
        description="Sets label style.",
        params=[
            Param(name="style", type="series string", required=True),
        ],
    ),
    "label.set_text": BuiltinFunction(
        name="label.set_text",
        return_type="void",
        description="Sets label text",
        params=[
            Param(name="text", type="series string", required=True),
        ],
    ),
    "label.set_text_font_family": BuiltinFunction(
        name="label.set_text_font_family",
        return_type="void",
        description="The function sets the font family of the text inside the label.",
        params=[
            Param(name="text_font_family", type="series string", required=True),
        ],
    ),
    "label.set_text_formatting": BuiltinFunction(
        name="label.set_text_formatting",
        return_type="void",
        description="Sets text formatting.",
        params=[
            Param(name="id", type="label", required=True),
            Param(name="formatting", type="string", required=True),
        ],
    ),
    "label.set_textalign": BuiltinFunction(
        name="label.set_textalign",
        return_type="void",
        description="Sets the alignment for the label text.",
        params=[
            Param(name="textalign", type="series string", required=True),
        ],
    ),
    "label.set_textcolor": BuiltinFunction(
        name="label.set_textcolor",
        return_type="void",
        description="Sets color of the label text.",
        params=[
            Param(name="textcolor", type="series color", required=True),
        ],
    ),
    "label.set_tooltip": BuiltinFunction(
        name="label.set_tooltip",
        return_type="void",
        description="Sets the tooltip text.",
        params=[
            Param(name="tooltip", type="series string", required=True),
        ],
    ),
    "label.set_x": BuiltinFunction(
        name="label.set_x",
        return_type="void",
        description="Sets bar index or bar time (depending on the xloc) of the label position.",
        params=[
            Param(name="x", type="series int", required=True),
        ],
    ),
    "label.set_xloc": BuiltinFunction(
        name="label.set_xloc",
        return_type="void",
        description="Sets x-location and new bar index/time value.",
        params=[
            Param(name="x", type="series int", required=True),
            Param(name="xloc", type="series string", required=True),
        ],
    ),
    "label.set_xy": BuiltinFunction(
        name="label.set_xy",
        return_type="void",
        description="Sets bar index/time and price of the label position.",
        params=[
            Param(name="x", type="series int", required=True),
            Param(name="y", type="series int|float", required=True),
        ],
    ),
    "label.set_y": BuiltinFunction(
        name="label.set_y",
        return_type="void",
        description="Sets price of the label position",
        params=[
            Param(name="y", type="series int|float", required=True),
        ],
    ),
    "label.set_yloc": BuiltinFunction(
        name="label.set_yloc",
        return_type="void",
        description="Sets new y-location calculation algorithm.",
        params=[
            Param(name="yloc", type="series string", required=True),
        ],
    ),
    "library": BuiltinFunction(
        name="library",
        return_type="void",
        description="Declaration statement identifying a script as a [library](https://www.tradingview.com/pine-script-docs/en/v5/concepts/Libraries.html).",
        params=[
            Param(name="title", type="const string", required=True),
            Param(name="overlay", type="const bool", required=False),
        ],
    ),
    "line": BuiltinFunction(
        name="line",
        return_type="line",
        description="Casts na to line.",
        params=[
            Param(name="x", type="series line", required=True),
        ],
    ),
    "line.copy": BuiltinFunction(
        name="line.copy",
        return_type="line",
        description="Clones the line object.",
        params=[],
    ),
    "line.delete": BuiltinFunction(
        name="line.delete",
        return_type="void",
        description="Deletes the specified line object. If it has already been deleted, does nothing.",
        params=[],
    ),
    "line.get_price": BuiltinFunction(
        name="line.get_price",
        return_type="float",
        description="Returns the price level of a line at a given bar index.",
        params=[
            Param(name="x", type="series int", required=True),
        ],
    ),
    "line.get_x1": BuiltinFunction(
        name="line.get_x1",
        return_type="int",
        description="Returns UNIX time or bar index (depending on the last xloc value set) of the first point of the line.",
        params=[],
    ),
    "line.get_x2": BuiltinFunction(
        name="line.get_x2",
        return_type="int",
        description="Returns UNIX time or bar index (depending on the last xloc value set) of the second point of the line.",
        params=[],
    ),
    "line.get_y1": BuiltinFunction(
        name="line.get_y1",
        return_type="float",
        description="Returns price of the first point of the line.",
        params=[],
    ),
    "line.get_y2": BuiltinFunction(
        name="line.get_y2",
        return_type="float",
        description="Returns price of the second point of the line.",
        params=[],
    ),
    "line.new": BuiltinFunction(
        name="line.new",
        return_type="line",
        description="Creates new line object.",
        params=[
            Param(name="x1", type="series int", required=True),
            Param(name="y1", type="series int|float", required=True),
            Param(name="x2", type="series int", required=True),
            Param(name="y2", type="series int|float", required=True),
            Param(name="xloc", type="series string", required=False),
            Param(name="extend", type="series string", required=False),
            Param(name="color", type="series color", required=False),
            Param(name="width", type="series int", required=False),
            Param(name="style", type="series string", required=False),
            Param(name="first_point", type="chart.point", required=True),
            Param(name="second_point", type="chart.point", required=True),
        ],
    ),
    "line.set_color": BuiltinFunction(
        name="line.set_color",
        return_type="void",
        description="Sets the line color",
        params=[
            Param(name="color", type="series color", required=True),
        ],
    ),
    "line.set_extend": BuiltinFunction(
        name="line.set_extend",
        return_type="void",
        description="Sets extending type of this line object. If extend=[extend.none](#var_extend.none), draws segment starting at point (x1, y1) and ending at point (x2, y2).  ",
        params=[
            Param(name="extend", type="series string", required=True),
        ],
    ),
    "line.set_first_point": BuiltinFunction(
        name="line.set_first_point",
        return_type="void",
        description="Sets the first point of the `id` line to `point`.",
        params=[
            Param(name="point", type="chart.point", required=True),
        ],
    ),
    "line.set_second_point": BuiltinFunction(
        name="line.set_second_point",
        return_type="void",
        description="Sets the second point of the `id` line to `point`.",
        params=[
            Param(name="point", type="chart.point", required=True),
        ],
    ),
    "line.set_style": BuiltinFunction(
        name="line.set_style",
        return_type="void",
        description="Sets the line style",
        params=[
            Param(name="style", type="series string", required=True),
        ],
    ),
    "line.set_width": BuiltinFunction(
        name="line.set_width",
        return_type="void",
        description="Sets the line width.",
        params=[
            Param(name="width", type="series int", required=True),
        ],
    ),
    "line.set_x1": BuiltinFunction(
        name="line.set_x1",
        return_type="void",
        description="Sets bar index or bar time (depending on the xloc) of the first point.",
        params=[
            Param(name="x", type="series int", required=True),
        ],
    ),
    "line.set_x2": BuiltinFunction(
        name="line.set_x2",
        return_type="void",
        description="Sets bar index or bar time (depending on the xloc) of the second point.",
        params=[
            Param(name="x", type="series int", required=True),
        ],
    ),
    "line.set_xloc": BuiltinFunction(
        name="line.set_xloc",
        return_type="void",
        description="Sets x-location and new bar index/time values.",
        params=[
            Param(name="x1", type="series int", required=True),
            Param(name="x2", type="series int", required=True),
            Param(name="xloc", type="series string", required=True),
        ],
    ),
    "line.set_xy1": BuiltinFunction(
        name="line.set_xy1",
        return_type="void",
        description="Sets bar index/time and price of the first point.",
        params=[
            Param(name="x", type="series int", required=True),
            Param(name="y", type="series int|float", required=True),
        ],
    ),
    "line.set_xy2": BuiltinFunction(
        name="line.set_xy2",
        return_type="void",
        description="Sets bar index/time and price of the second point",
        params=[
            Param(name="x", type="series int", required=True),
            Param(name="y", type="series int|float", required=True),
        ],
    ),
    "line.set_y1": BuiltinFunction(
        name="line.set_y1",
        return_type="void",
        description="Sets price of the first point",
        params=[
            Param(name="y", type="series int|float", required=True),
        ],
    ),
    "line.set_y2": BuiltinFunction(
        name="line.set_y2",
        return_type="void",
        description="Sets price of the second point.",
        params=[
            Param(name="y", type="series int|float", required=True),
        ],
    ),
    "linefill": BuiltinFunction(
        name="linefill",
        return_type="linefill",
        description="Casts na to linefill.",
        params=[
            Param(name="x", type="series linefill", required=True),
        ],
    ),
    "linefill.delete": BuiltinFunction(
        name="linefill.delete",
        return_type="void",
        description="Deletes the specified linefill object. If it has already been deleted, does nothing.",
        params=[],
    ),
    "linefill.get_line1": BuiltinFunction(
        name="linefill.get_line1",
        return_type="line",
        description="Returns the ID of the first line used in the `id` linefill.",
        params=[],
    ),
    "linefill.get_line2": BuiltinFunction(
        name="linefill.get_line2",
        return_type="line",
        description="Returns the ID of the second line used in the `id` linefill.",
        params=[],
    ),
    "linefill.new": BuiltinFunction(
        name="linefill.new",
        return_type="linefill",
        description="Creates a new linefill object and displays it on the chart, filling the space between `line1` and `line2` with the color specified in `color`.",
        params=[
            Param(name="line1", type="series line", required=True),
            Param(name="line2", type="series line", required=True),
            Param(name="color", type="series color", required=True),
        ],
    ),
    "linefill.set_color": BuiltinFunction(
        name="linefill.set_color",
        return_type="void",
        description="The function sets the color of the linefill object passed to it.",
        params=[
            Param(name="color", type="series color", required=True),
        ],
    ),
    "log.error": BuiltinFunction(
        name="log.error",
        return_type="void",
        description='Converts the formatting string and value(s) into a formatted string, and sends the result to the "Pine Logs" menu tagged with the "error" debug level. The formatting string can contain literal text an',
        params=[
            Param(name="formatString", type="series string", required=True),
            Param(name="message", type="series string", required=True),
            Param(
                name="arg0, arg1, ...",
                type="series int|float|bool|string|array<int|float|bool|string>|na",
                required=True,
            ),
        ],
    ),
    "log.info": BuiltinFunction(
        name="log.info",
        return_type="void",
        description='Converts the formatting string and value(s) into a formatted string, and sends the result to the "Pine Logs" menu tagged with the "info" debug level. The formatting string can contain literal text and',
        params=[
            Param(name="formatString", type="series string", required=True),
            Param(name="message", type="series string", required=True),
            Param(
                name="arg0, arg1, ...",
                type="series int|float|bool|string|array<int|float|bool|string>|na",
                required=True,
            ),
        ],
    ),
    "log.warning": BuiltinFunction(
        name="log.warning",
        return_type="void",
        description='Converts the formatting string and value(s) into a formatted string, and sends the result to the "Pine Logs" menu tagged with the "warning" debug level. The formatting string can contain literal text ',
        params=[
            Param(name="formatString", type="series string", required=True),
            Param(name="message", type="series string", required=True),
            Param(
                name="arg0, arg1, ...",
                type="series int|float|bool|string|array<int|float|bool|string>|na",
                required=True,
            ),
        ],
    ),
    "map.clear": BuiltinFunction(
        name="map.clear",
        return_type="void",
        description="Clears the map, removing all key-value pairs from it.",
        params=[],
    ),
    "map.contains": BuiltinFunction(
        name="map.contains",
        return_type="bool",
        description="Returns [true](#op_true) if the `key` was found in the `id` map, [false](#op_false) otherwise.",
        params=[
            Param(name="key", type="map<type>", required=True),
        ],
    ),
    "map.copy": BuiltinFunction(
        name="map.copy",
        return_type="map",
        description="Creates a copy of an existing map.",
        params=[],
    ),
    "map.get": BuiltinFunction(
        name="map.get",
        return_type="",
        description="Returns the value associated with the specified `key` in the `id` map.",
        params=[
            Param(name="key", type="map< *keyType* ,valueType>", required=True),
        ],
    ),
    "map.keys": BuiltinFunction(
        name="map.keys",
        return_type="array",
        description="Returns an array of all the keys in the `id` map. The resulting array is a copy and any changes to it are not reflected in the original map.",
        params=[],
    ),
    "map.new<type,type>": BuiltinFunction(
        name="map.new<type,type>",
        return_type="map<keyType, valueType>",
        description="Creates a new map object: a collection that consists of key-value pairs, where all keys are of the `keyType`, and all values are of the `valueType`.",
        params=[],
    ),
    "map.put": BuiltinFunction(
        name="map.put",
        return_type="",
        description="Puts a new key-value pair into the `id` map.",
        params=[
            Param(name="key", type="map<type>", required=True),
            Param(name="value", type="map<type>", required=True),
        ],
    ),
    "map.put_all": BuiltinFunction(
        name="map.put_all",
        return_type="void",
        description="Puts all key-value pairs from the `id2` map into the `id` map.",
        params=[
            Param(name="id2", type="map<type>", required=True),
        ],
    ),
    "map.remove": BuiltinFunction(
        name="map.remove",
        return_type="",
        description="Removes a key-value pair from the `id` map.",
        params=[
            Param(name="key", type="map<type>", required=True),
        ],
    ),
    "map.size": BuiltinFunction(
        name="map.size",
        return_type="int",
        description="Returns the number of key-value pairs in the `id` map.",
        params=[],
    ),
    "map.values": BuiltinFunction(
        name="map.values",
        return_type="array",
        description="Returns an array of all the values in the `id` map. The resulting array is a copy and any changes to it are not reflected in the original map.",
        params=[],
    ),
    "math.abs": BuiltinFunction(
        name="math.abs",
        return_type="float|int",
        description="Absolute value of `number` is `number` if `number` >= 0, or if `number` is < 0 `number` is `(-2 * number)`",
        params=[
            Param(name="number", type="series int|float", required=True),
        ],
    ),
    "math.acos": BuiltinFunction(
        name="math.acos",
        return_type="float",
        description="The acos function returns the arccosine (in radians) of number such that cos(acos(y)) = y for y in range [-1, 1].",
        params=[
            Param(name="angle", type="series int|float", required=True),
        ],
    ),
    "math.asin": BuiltinFunction(
        name="math.asin",
        return_type="float",
        description="The asin function returns the arcsine (in radians) of number such that sin(asin(y)) = y for y in range [-1, 1].",
        params=[
            Param(name="angle", type="series int|float", required=True),
        ],
    ),
    "math.atan": BuiltinFunction(
        name="math.atan",
        return_type="float",
        description="The atan function returns the arctangent (in radians) of number such that tan(atan(y)) = y for any y.",
        params=[
            Param(name="angle", type="series int|float", required=True),
        ],
    ),
    "math.avg": BuiltinFunction(
        name="math.avg",
        return_type="float",
        description="Calculates average of all given series (elementwise).",
        params=[],
    ),
    "math.ceil": BuiltinFunction(
        name="math.ceil",
        return_type="int",
        description="The ceil function returns the smallest (closest to negative infinity) integer that is greater than or equal to the argument.",
        params=[
            Param(name="number", type="series int|float", required=True),
        ],
    ),
    "math.cos": BuiltinFunction(
        name="math.cos",
        return_type="float",
        description="The cos function returns the trigonometric cosine of an angle.",
        params=[
            Param(name="angle", type="series int|float", required=True),
        ],
    ),
    "math.exp": BuiltinFunction(
        name="math.exp",
        return_type="float",
        description="The exp function of `number` is e raised to the power of `number`, where e is Euler\\`s number.",
        params=[
            Param(name="number", type="series int|float", required=True),
        ],
    ),
    "math.floor": BuiltinFunction(
        name="math.floor",
        return_type="int",
        description="The floor function returns the largest (closest to positive infinity) integer that is less than or equal to the argument.",
        params=[
            Param(name="number", type="series int|float", required=True),
        ],
    ),
    "math.log": BuiltinFunction(
        name="math.log",
        return_type="float",
        description="Natural logarithm of any `number` > 0 is the unique y such that e^y = `number`.",
        params=[
            Param(name="number", type="series int|float", required=True),
        ],
    ),
    "math.log10": BuiltinFunction(
        name="math.log10",
        return_type="float",
        description="The common (or base 10) logarithm of `number` is the power to which 10 must be raised to obtain the `number`.  ",
        params=[
            Param(name="number", type="series int|float", required=True),
        ],
    ),
    "math.max": BuiltinFunction(
        name="math.max",
        return_type="float|int",
        description="Returns the greatest of multiple values.",
        params=[
            Param(name="arg0, arg1, ...", type="series int|float", required=True),
        ],
    ),
    "math.min": BuiltinFunction(
        name="math.min",
        return_type="float|int",
        description="Returns the smallest of multiple values.",
        params=[
            Param(name="arg0, arg1, ...", type="series int|float", required=True),
        ],
    ),
    "math.pow": BuiltinFunction(
        name="math.pow",
        return_type="float",
        description="Mathematical power function.",
        params=[
            Param(name="base", type="series int|float", required=True),
            Param(name="exponent", type="series int|float", required=True),
        ],
    ),
    "math.random": BuiltinFunction(
        name="math.random",
        return_type="float",
        description="Returns a pseudo-random value. The function will generate a different sequence of values for each script execution. Using the same value for the optional seed argument will produce a repeatable sequen",
        params=[
            Param(name="min", type="series int|float", required=False),
            Param(name="max", type="series int|float", required=False),
            Param(name="seed", type="series int", required=False),
        ],
    ),
    "math.round": BuiltinFunction(
        name="math.round",
        return_type="float|int",
        description="Returns the value of `number` rounded to the nearest integer, with ties rounding up.  ",
        params=[
            Param(name="number", type="series int|float", required=True),
            Param(name="precision", type="series int", required=False),
        ],
    ),
    "math.round_to_mintick": BuiltinFunction(
        name="math.round_to_mintick",
        return_type="float",
        description="Returns the value rounded to the symbol\\`s mintick, i.e. the nearest value that can be divided by [syminfo.mintick](#var_syminfo.mintick), without the remainder, with ties rounding up.",
        params=[
            Param(name="number", type="series int|float", required=True),
        ],
    ),
    "math.sign": BuiltinFunction(
        name="math.sign",
        return_type="float",
        description="Sign (signum) of `number` is zero if `number` is zero, 1.0 if `number` is greater than zero, -1.0 if `number` is less than zero.",
        params=[
            Param(name="number", type="series int|float", required=True),
        ],
    ),
    "math.sin": BuiltinFunction(
        name="math.sin",
        return_type="float",
        description="The sin function returns the trigonometric sine of an angle.",
        params=[
            Param(name="angle", type="series int|float", required=True),
        ],
    ),
    "math.sqrt": BuiltinFunction(
        name="math.sqrt",
        return_type="float",
        description="Square root of any `number` >= 0 is the unique y >= 0 such that y^2 = `number`.",
        params=[
            Param(name="number", type="series int|float", required=True),
        ],
    ),
    "math.sum": BuiltinFunction(
        name="math.sum",
        return_type="float",
        description="The sum function returns the sliding sum of last y values of x.",
        params=[
            Param(name="source", type="series int|float", required=True),
            Param(name="length", type="series int", required=True),
        ],
    ),
    "math.tan": BuiltinFunction(
        name="math.tan",
        return_type="float",
        description="The tan function returns the trigonometric tangent of an angle.",
        params=[
            Param(name="angle", type="series int|float", required=True),
        ],
    ),
    "math.todegrees": BuiltinFunction(
        name="math.todegrees",
        return_type="float",
        description="Returns an approximately equivalent angle in degrees from an angle measured in radians.",
        params=[
            Param(name="radians", type="series int|float", required=True),
        ],
    ),
    "math.toradians": BuiltinFunction(
        name="math.toradians",
        return_type="float",
        description="Returns an approximately equivalent angle in radians from an angle measured in degrees.",
        params=[
            Param(name="degrees", type="series int|float", required=True),
        ],
    ),
    "matrix.add_col": BuiltinFunction(
        name="matrix.add_col",
        return_type="void",
        description="The function adds a column at the `column` index of the `id` matrix. The column can consist of `na` values, or an array can be used to provide values.",
        params=[
            Param(name="column", type="series int", required=False),
            Param(name="array_id", type="any[]", required=True),
        ],
    ),
    "matrix.add_row": BuiltinFunction(
        name="matrix.add_row",
        return_type="void",
        description="The function adds a row at the `row` index of the `id` matrix. The row can consist of `na` values, or an array can be used to provide values.",
        params=[
            Param(name="row", type="series int", required=False),
            Param(name="array_id", type="any[]", required=True),
        ],
    ),
    "matrix.avg": BuiltinFunction(
        name="matrix.avg",
        return_type="float|int",
        description="The function calculates the average of all elements in the matrix.",
        params=[],
    ),
    "matrix.col": BuiltinFunction(
        name="matrix.col",
        return_type="array",
        description="The function creates a one-dimensional array from the elements of a matrix column.",
        params=[
            Param(name="column", type="series int", required=True),
        ],
    ),
    "matrix.columns": BuiltinFunction(
        name="matrix.columns",
        return_type="int",
        description="The function returns the number of columns in the matrix.",
        params=[],
    ),
    "matrix.concat": BuiltinFunction(
        name="matrix.concat",
        return_type="matrix",
        description="The function appends the `m2` matrix to the `m1` matrix.",
        params=[
            Param(name="id2", type="matrix<any>", required=True),
        ],
    ),
    "matrix.copy": BuiltinFunction(
        name="matrix.copy",
        return_type="matrix",
        description="The function creates a new matrix which is a copy of the original.",
        params=[],
    ),
    "matrix.det": BuiltinFunction(
        name="matrix.det",
        return_type="float|int",
        description="The function returns the [determinant](https://en.wikipedia.org/wiki/Determinant) of a square matrix.",
        params=[],
    ),
    "matrix.diff": BuiltinFunction(
        name="matrix.diff",
        return_type="matrix<float>|matrix<int>",
        description="The function returns a new matrix resulting from the subtraction between matrices `id1` and `id2`, or of matrix `id1` and an `id2` scalar (a numerical value).",
        params=[
            Param(name="id2", type="series int|float|matrix<int|float>", required=True),
        ],
    ),
    "matrix.eigenvalues": BuiltinFunction(
        name="matrix.eigenvalues",
        return_type="array<int>|array<float>",
        description="The function returns an array containing the [eigenvalues](https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors) of a square matrix.",
        params=[],
    ),
    "matrix.eigenvectors": BuiltinFunction(
        name="matrix.eigenvectors",
        return_type="matrix<float>|matrix<int>",
        description="Returns a matrix of [eigenvectors](https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors), in which each column is an eigenvector of the `id` matrix.",
        params=[],
    ),
    "matrix.elements_count": BuiltinFunction(
        name="matrix.elements_count",
        return_type="int",
        description="The function returns the total number of all matrix elements.",
        params=[],
    ),
    "matrix.fill": BuiltinFunction(
        name="matrix.fill",
        return_type="void",
        description="The function fills a rectangular area of the `id` matrix defined by the indices `from_column` to `to_column` (not including it) and `from_row` to `to_row`(not including it) with the `value`.",
        params=[
            Param(name="value", type="any", required=True),
            Param(name="from_row", type="series int", required=False),
            Param(name="to_row", type="series int", required=False),
            Param(name="from_column", type="series int", required=False),
            Param(name="to_column", type="series int", required=False),
        ],
    ),
    "matrix.get": BuiltinFunction(
        name="matrix.get",
        return_type="",
        description="The function returns the element with the specified index of the matrix.",
        params=[
            Param(name="row", type="series int", required=True),
            Param(name="column", type="series int", required=True),
        ],
    ),
    "matrix.inv": BuiltinFunction(
        name="matrix.inv",
        return_type="matrix<float>|matrix<int>",
        description="The function returns the [inverse](https://en.wikipedia.org/wiki/Invertible_matrix) of a square matrix.",
        params=[],
    ),
    "matrix.is_antidiagonal": BuiltinFunction(
        name="matrix.is_antidiagonal",
        return_type="bool",
        description="The function determines if the matrix is [anti-diagonal](https://en.wikipedia.org/wiki/Anti-diagonal_matrix) (all elements outside the secondary diagonal are zero).",
        params=[],
    ),
    "matrix.is_antisymmetric": BuiltinFunction(
        name="matrix.is_antisymmetric",
        return_type="bool",
        description="The function determines if a matrix is [antisymmetric](https://en.wikipedia.org/wiki/Skew-symmetric_matrix) (its [transpose](https://en.wikipedia.org/wiki/Transpose) equals its negative).",
        params=[],
    ),
    "matrix.is_binary": BuiltinFunction(
        name="matrix.is_binary",
        return_type="bool",
        description="The function determines if the matrix is [binary](https://en.wikipedia.org/wiki/Logical_matrix) (when all elements of the matrix are 0 or 1).",
        params=[],
    ),
    "matrix.is_diagonal": BuiltinFunction(
        name="matrix.is_diagonal",
        return_type="bool",
        description="The function determines if the matrix is [diagonal](https://en.wikipedia.org/wiki/Diagonal_matrix) (all elements outside the main diagonal are zero).",
        params=[],
    ),
    "matrix.is_identity": BuiltinFunction(
        name="matrix.is_identity",
        return_type="bool",
        description="The function determines if a matrix is an [identity matrix](https://en.wikipedia.org/wiki/Identity_matrix) (elements with ones on the [main diagonal](https://en.wikipedia.org/wiki/Main_diagonal) and z",
        params=[],
    ),
    "matrix.is_square": BuiltinFunction(
        name="matrix.is_square",
        return_type="bool",
        description="The function determines if the matrix is [square](https://en.wikipedia.org/wiki/Square_matrix) (it has the same number of rows and columns).",
        params=[],
    ),
    "matrix.is_stochastic": BuiltinFunction(
        name="matrix.is_stochastic",
        return_type="bool",
        description="The function determines if the matrix is [stochastic](https://en.wikipedia.org/wiki/Stochastic_matrix).",
        params=[],
    ),
    "matrix.is_symmetric": BuiltinFunction(
        name="matrix.is_symmetric",
        return_type="bool",
        description="The function determines if a [square matrix](https://en.wikipedia.org/wiki/Square_matrix) is [symmetric](https://en.wikipedia.org/wiki/Symmetric_matrix) (elements are symmetric with respect to the [ma",
        params=[],
    ),
    "matrix.is_triangular": BuiltinFunction(
        name="matrix.is_triangular",
        return_type="bool",
        description="The function determines if the matrix is [triangular](https://en.wikipedia.org/wiki/Triangular_matrix) (if all elements above or below the [main diagonal](https://en.wikipedia.org/wiki/Main_diagonal) ",
        params=[],
    ),
    "matrix.is_zero": BuiltinFunction(
        name="matrix.is_zero",
        return_type="bool",
        description="The function determines if all elements of the matrix are zero.",
        params=[],
    ),
    "matrix.kron": BuiltinFunction(
        name="matrix.kron",
        return_type="matrix<float>|matrix<int>",
        description="The function returns the [Kronecker product](https://en.wikipedia.org/wiki/Kronecker_product) for the `id1` and `id2` matrices.",
        params=[
            Param(name="id2", type="matrix<float|int>", required=True),
        ],
    ),
    "matrix.max": BuiltinFunction(
        name="matrix.max",
        return_type="float|int",
        description="The function returns the largest value from the matrix elements.",
        params=[],
    ),
    "matrix.median": BuiltinFunction(
        name="matrix.median",
        return_type="float|int",
        description='The function calculates the [median](https://en.wikipedia.org/wiki/Median) ("the middle" value) of matrix elements.',
        params=[],
    ),
    "matrix.min": BuiltinFunction(
        name="matrix.min",
        return_type="float|int",
        description="The function returns the smallest value from the matrix elements.",
        params=[],
    ),
    "matrix.mode": BuiltinFunction(
        name="matrix.mode",
        return_type="float|int",
        description="The function calculates the [mode](https://en.wikipedia.org/wiki/Mode_(statistics)) of the matrix, which is the most frequently occurring value from the matrix elements.  ",
        params=[],
    ),
    "matrix.mult": BuiltinFunction(
        name="matrix.mult",
        return_type="array<float>|array<int>|matrix<float>|matrix<int>",
        description="The function returns a new matrix resulting from the [product](https://en.wikipedia.org/wiki/Matrix_multiplication) between the matrices `id1` and `id2`, or between an `id1` matrix and an `id2` scalar",
        params=[
            Param(
                name="id2",
                type="series int|float|matrix<int|float>|array<int|float>",
                required=True,
            ),
        ],
    ),
    "matrix.new<bool>": BuiltinFunction(
        name="matrix.new<bool>",
        return_type="void",
        description="Create matrix from random values",
        params=[
            Param(name="rows", type="series int", required=False),
            Param(name="columns", type="series int", required=False),
            Param(name="initial_value", type="matrix<type>", required=False),
        ],
    ),
    "matrix.new<box>": BuiltinFunction(
        name="matrix.new<box>",
        return_type="void",
        description="Create matrix from random values",
        params=[
            Param(name="rows", type="series int", required=False),
            Param(name="columns", type="series int", required=False),
            Param(name="initial_value", type="matrix<type>", required=False),
        ],
    ),
    "matrix.new<color>": BuiltinFunction(
        name="matrix.new<color>",
        return_type="void",
        description="Create matrix from random values",
        params=[
            Param(name="rows", type="series int", required=False),
            Param(name="columns", type="series int", required=False),
            Param(name="initial_value", type="matrix<type>", required=False),
        ],
    ),
    "matrix.new<float>": BuiltinFunction(
        name="matrix.new<float>",
        return_type="void",
        description="Create matrix from random values",
        params=[
            Param(name="rows", type="series int", required=False),
            Param(name="columns", type="series int", required=False),
            Param(name="initial_value", type="matrix<type>", required=False),
        ],
    ),
    "matrix.new<int>": BuiltinFunction(
        name="matrix.new<int>",
        return_type="void",
        description="Create matrix from random values",
        params=[
            Param(name="rows", type="series int", required=False),
            Param(name="columns", type="series int", required=False),
            Param(name="initial_value", type="matrix<type>", required=False),
        ],
    ),
    "matrix.new<label>": BuiltinFunction(
        name="matrix.new<label>",
        return_type="void",
        description="Create matrix from random values",
        params=[
            Param(name="rows", type="series int", required=False),
            Param(name="columns", type="series int", required=False),
            Param(name="initial_value", type="matrix<type>", required=False),
        ],
    ),
    "matrix.new<line>": BuiltinFunction(
        name="matrix.new<line>",
        return_type="void",
        description="Create matrix from random values",
        params=[
            Param(name="rows", type="series int", required=False),
            Param(name="columns", type="series int", required=False),
            Param(name="initial_value", type="matrix<type>", required=False),
        ],
    ),
    "matrix.new<linefill>": BuiltinFunction(
        name="matrix.new<linefill>",
        return_type="void",
        description="Create matrix from random values",
        params=[
            Param(name="rows", type="series int", required=False),
            Param(name="columns", type="series int", required=False),
            Param(name="initial_value", type="matrix<type>", required=False),
        ],
    ),
    "matrix.new<string>": BuiltinFunction(
        name="matrix.new<string>",
        return_type="void",
        description="Create matrix from random values",
        params=[
            Param(name="rows", type="series int", required=False),
            Param(name="columns", type="series int", required=False),
            Param(name="initial_value", type="matrix<type>", required=False),
        ],
    ),
    "matrix.new<table>": BuiltinFunction(
        name="matrix.new<table>",
        return_type="void",
        description="Create matrix from random values",
        params=[
            Param(name="rows", type="series int", required=False),
            Param(name="columns", type="series int", required=False),
            Param(name="initial_value", type="matrix<type>", required=False),
        ],
    ),
    "matrix.new<type>": BuiltinFunction(
        name="matrix.new<type>",
        return_type="void",
        description='The function creates a new matrix object. A matrix is a two-dimensional data structure containing rows and columns. All elements in the matrix must be of the type specified in the type template ("<typ',
        params=[
            Param(name="rows", type="series int", required=False),
            Param(name="columns", type="series int", required=False),
            Param(name="initial_value", type="matrix<type>", required=False),
        ],
    ),
    "matrix.pinv": BuiltinFunction(
        name="matrix.pinv",
        return_type="matrix<float>|matrix<int>",
        description="The function returns the [pseudoinverse](https://en.wikipedia.org/wiki/Moore%E2%80%93Penrose_inverse) of a matrix.",
        params=[],
    ),
    "matrix.pow": BuiltinFunction(
        name="matrix.pow",
        return_type="matrix<float>|matrix<int>",
        description="The function calculates the product of the matrix by itself `power` times.",
        params=[
            Param(name="power", type="series int", required=True),
        ],
    ),
    "matrix.rank": BuiltinFunction(
        name="matrix.rank",
        return_type="int",
        description="The function calculates the [rank](https://en.wikipedia.org/wiki/Rank_(linear_algebra)) of the matrix.",
        params=[],
    ),
    "matrix.remove_col": BuiltinFunction(
        name="matrix.remove_col",
        return_type="array",
        description="The function removes the column at `column` index of the `id` matrix and returns an array containing the removed column\\`s values.",
        params=[
            Param(name="column", type="series int", required=False),
        ],
    ),
    "matrix.remove_row": BuiltinFunction(
        name="matrix.remove_row",
        return_type="array",
        description="The function removes the row at `row` index of the `id` matrix and returns an array containing the removed row\\`s values.",
        params=[
            Param(name="row", type="series int", required=False),
        ],
    ),
    "matrix.reshape": BuiltinFunction(
        name="matrix.reshape",
        return_type="void",
        description="The function rebuilds the `id` matrix to `rows` x `cols` dimensions.",
        params=[
            Param(name="rows", type="series int", required=True),
            Param(name="columns", type="series int", required=True),
        ],
    ),
    "matrix.reverse": BuiltinFunction(
        name="matrix.reverse",
        return_type="void",
        description="The function reverses the order of rows and columns in the matrix `id`. The first row and first column become the last, and the last become the first.",
        params=[],
    ),
    "matrix.row": BuiltinFunction(
        name="matrix.row",
        return_type="array",
        description="The function creates a one-dimensional array from the elements of a matrix row.",
        params=[
            Param(name="row", type="series int", required=True),
        ],
    ),
    "matrix.rows": BuiltinFunction(
        name="matrix.rows",
        return_type="int",
        description="The function returns the number of rows in the matrix.",
        params=[],
    ),
    "matrix.set": BuiltinFunction(
        name="matrix.set",
        return_type="void",
        description="The function assigns `value` to the element at the `row` and `column` of the `id` matrix.",
        params=[
            Param(name="row", type="series int", required=True),
            Param(name="column", type="series int", required=True),
            Param(name="value", type="any", required=True),
        ],
    ),
    "matrix.sort": BuiltinFunction(
        name="matrix.sort",
        return_type="void",
        description="The function rearranges the rows in the `id` matrix following the sorted order of the values in the `column`.",
        params=[
            Param(name="column", type="series int", required=False),
            Param(name="order", type="simple sort_order", required=False),
        ],
    ),
    "matrix.submatrix": BuiltinFunction(
        name="matrix.submatrix",
        return_type="matrix",
        description="The function extracts a submatrix of the `id` matrix within the specified indices.",
        params=[
            Param(name="from_row", type="series int", required=False),
            Param(name="to_row", type="series int", required=False),
            Param(name="from_column", type="series int", required=False),
            Param(name="to_column", type="series int", required=False),
        ],
    ),
    "matrix.sum": BuiltinFunction(
        name="matrix.sum",
        return_type="matrix<float>|matrix<int>",
        description="The function returns a new matrix resulting from the [sum](https://en.wikipedia.org/wiki/Matrix_addition) of two matrices `id1` and `id2`, or of an `id1` matrix and an `id2` scalar (a numerical value)",
        params=[
            Param(name="id2", type="series int|float|matrix<int|float>", required=True),
        ],
    ),
    "matrix.swap_columns": BuiltinFunction(
        name="matrix.swap_columns",
        return_type="void",
        description="The function swaps the columns at the index `column1` and `column2` in the `id` matrix.",
        params=[
            Param(name="column1", type="series int", required=True),
            Param(name="column2", type="series int", required=True),
        ],
    ),
    "matrix.swap_rows": BuiltinFunction(
        name="matrix.swap_rows",
        return_type="void",
        description="The function swaps the rows at the index `row1` and `row2` in the `id` matrix.",
        params=[
            Param(name="row1", type="series int", required=True),
            Param(name="row2", type="series int", required=True),
        ],
    ),
    "matrix.trace": BuiltinFunction(
        name="matrix.trace",
        return_type="float|int",
        description="The function calculates the [trace](https://en.wikipedia.org/wiki/Trace_(linear_algebra)) of a matrix (the sum of the main diagonal\\`s elements).",
        params=[],
    ),
    "matrix.transpose": BuiltinFunction(
        name="matrix.transpose",
        return_type="matrix",
        description="The function creates a new, [transposed](https://en.wikipedia.org/wiki/Transpose#Transpose_of_a_matrix) version of the `id`.  ",
        params=[],
    ),
    "max_bars_back": BuiltinFunction(
        name="max_bars_back",
        return_type="void",
        description="Function sets the maximum number of bars that is available for historical reference of a given built-in or user variable.  ",
        params=[
            Param(
                name="var", type="series int|float|bool|color|label|line", required=True
            ),
            Param(name="num", type="const int", required=True),
        ],
    ),
    "minute": BuiltinFunction(
        name="minute",
        return_type="int",
        description="",
        params=[
            Param(name="time", type="series int", required=True),
            Param(name="timezone", type="series string", required=True),
        ],
    ),
    "month": BuiltinFunction(
        name="month",
        return_type="int",
        description="",
        params=[
            Param(name="time", type="series int", required=True),
            Param(name="timezone", type="series string", required=True),
        ],
    ),
    "na": BuiltinFunction(
        name="na",
        return_type="bool",
        description="Tests if `x` is [na](#var_na).",
        params=[
            Param(name="x", type="series any", required=True),
        ],
    ),
    "nz": BuiltinFunction(
        name="nz",
        return_type="float|color|int|bool",
        description="Replaces NaN values with zeros (or given value) in a series.",
        params=[
            Param(name="source", type="series int|float|bool|color", required=True),
            Param(
                name="replacement", type="series int|float|bool|color", required=True
            ),
        ],
    ),
    "plot": BuiltinFunction(
        name="plot",
        return_type="plot",
        description="Plots a series of data on the chart.",
        params=[
            Param(name="series", type="series int|float", required=True),
            Param(name="title", type="const string", required=True),
            Param(name="color", type="series color", required=False),
            Param(name="linewidth", type="input int", required=False),
            Param(name="style", type="input plot_style", required=False),
            Param(name="trackprice", type="input bool", required=False),
            Param(name="histbase", type="input int|float", required=False),
            Param(name="offset", type="series int", required=False),
            Param(name="join", type="input bool", required=False),
            Param(name="editable", type="const bool", required=False),
            Param(name="show_last", type="input int", required=True),
            Param(name="display", type="input plot_display", required=False),
        ],
    ),
    "plotarrow": BuiltinFunction(
        name="plotarrow",
        return_type="void",
        description="Plots up and down arrows on the chart. Up arrow is drawn at every indicator positive value, down arrow is drawn at every negative value.  ",
        params=[
            Param(name="series", type="series int|float", required=True),
            Param(name="title", type="const string", required=True),
            Param(name="colorup", type="series color", required=False),
            Param(name="colordown", type="series color", required=False),
            Param(name="offset", type="series int", required=False),
            Param(name="minheight", type="input int", required=False),
            Param(name="maxheight", type="input int", required=False),
            Param(name="editable", type="const bool", required=False),
            Param(name="show_last", type="input int", required=True),
            Param(name="display", type="input plot_display", required=False),
        ],
    ),
    "plotbar": BuiltinFunction(
        name="plotbar",
        return_type="void",
        description="Plots ohlc bars on the chart.",
        params=[
            Param(name="open", type="series int|float", required=True),
            Param(name="high", type="series int|float", required=True),
            Param(name="low", type="series int|float", required=True),
            Param(name="close", type="series int|float", required=True),
            Param(name="title", type="const string", required=False),
            Param(name="color", type="series color", required=False),
            Param(name="editable", type="const bool", required=False),
            Param(name="show_last", type="input int", required=True),
            Param(name="display", type="input plot_display", required=False),
        ],
    ),
    "plotcandle": BuiltinFunction(
        name="plotcandle",
        return_type="void",
        description="Plots candles on the chart.",
        params=[
            Param(name="open", type="series int|float", required=True),
            Param(name="high", type="series int|float", required=True),
            Param(name="low", type="series int|float", required=True),
            Param(name="close", type="series int|float", required=True),
            Param(name="title", type="const string", required=False),
            Param(name="color", type="series color", required=False),
            Param(name="wickcolor", type="series color", required=False),
            Param(name="editable", type="const bool", required=False),
            Param(name="show_last", type="input int", required=True),
            Param(name="bordercolor", type="series color", required=False),
            Param(name="display", type="input plot_display", required=False),
        ],
    ),
    "plotchar": BuiltinFunction(
        name="plotchar",
        return_type="void",
        description="Plots visual shapes using any given one Unicode character on the chart.",
        params=[
            Param(name="series", type="series bool", required=True),
            Param(name="title", type="const string", required=True),
            Param(name="char", type="input string", required=True),
            Param(name="location", type="input string", required=False),
            Param(name="color", type="series color", required=False),
            Param(name="offset", type="series int", required=False),
            Param(name="text", type="const string", required=True),
            Param(name="textcolor", type="series color", required=False),
            Param(name="editable", type="const bool", required=False),
            Param(name="show_last", type="input int", required=True),
            Param(name="size", type="const string", required=False),
            Param(name="display", type="input plot_display", required=False),
        ],
    ),
    "plotshape": BuiltinFunction(
        name="plotshape",
        return_type="void",
        description="Plots visual shapes on the chart.",
        params=[
            Param(name="series", type="series bool", required=True),
            Param(name="title", type="const string", required=True),
            Param(name="style", type="input string", required=False),
            Param(name="location", type="input string", required=True),
            Param(name="color", type="series color", required=False),
            Param(name="offset", type="series int", required=False),
            Param(name="text", type="const string", required=True),
            Param(name="textcolor", type="series color", required=False),
            Param(name="editable", type="const bool", required=False),
            Param(name="show_last", type="input int", required=True),
            Param(name="size", type="const string", required=False),
            Param(name="display", type="input plot_display", required=False),
        ],
    ),
    "polyline.delete": BuiltinFunction(
        name="polyline.delete",
        return_type="void",
        description="Deletes the specified [polyline](#op_polyline) object. It has no effect if the `id` doesn't exist.",
        params=[],
    ),
    "polyline.new": BuiltinFunction(
        name="polyline.new",
        return_type="polyline",
        description="Creates a new [polyline](#op_polyline) instance and displays it on the chart, sequentially connecting all of the points in the `points` array with line segments. The segments in the drawing can be str",
        params=[
            Param(name="points", type="chart.point[]", required=True),
            Param(name="curved", type="series bool", required=False),
            Param(name="closed", type="series bool", required=False),
            Param(name="xloc", type="series string", required=False),
            Param(name="line_color", type="series color", required=False),
            Param(name="fill_color", type="series color", required=False),
            Param(name="line_style", type="series string", required=False),
            Param(name="line_width", type="series int", required=False),
        ],
    ),
    "request.currency_rate": BuiltinFunction(
        name="request.currency_rate",
        return_type="float",
        description="Provides a daily rate that can be used to convert a value expressed in the `from` currency to another in the `to` currency.",
        params=[
            Param(name="from", type="simple string", required=True),
            Param(name="to", type="simple string", required=True),
            Param(name="ignore_invalid_currency", type="simple bool", required=False),
        ],
    ),
    "request.dividends": BuiltinFunction(
        name="request.dividends",
        return_type="float",
        description="Requests dividends data for the specified symbol.",
        params=[
            Param(name="ticker", type="simple string", required=True),
            Param(name="field", type="simple string", required=False),
            Param(name="gaps", type="simple barmerge_gaps", required=True),
            Param(name="lookahead", type="simple barmerge_lookahead", required=False),
            Param(name="ignore_invalid_symbol", type="input bool", required=False),
            Param(name="currency", type="simple string", required=False),
        ],
    ),
    "request.earnings": BuiltinFunction(
        name="request.earnings",
        return_type="float",
        description="Requests earnings data for the specified symbol.",
        params=[
            Param(name="ticker", type="simple string", required=True),
            Param(name="field", type="simple string", required=True),
            Param(name="gaps", type="simple barmerge_gaps", required=True),
            Param(name="lookahead", type="simple barmerge_lookahead", required=True),
            Param(name="ignore_invalid_symbol", type="input bool", required=False),
            Param(name="currency", type="simple string", required=False),
        ],
    ),
    "request.economic": BuiltinFunction(
        name="request.economic",
        return_type="float",
        description="Requests economic data for a symbol. Economic data includes information such as the state of a country\\`s economy (GDP, inflation rate, etc.) or of a particular industry (steel production, ICU beds, e",
        params=[
            Param(name="country_code", type="simple string", required=True),
            Param(name="field", type="simple string", required=True),
            Param(name="gaps", type="simple barmerge_gaps", required=False),
            Param(name="ignore_invalid_symbol", type="input bool", required=False),
        ],
    ),
    "request.financial": BuiltinFunction(
        name="request.financial",
        return_type="float",
        description="Requests financial series for symbol.",
        params=[
            Param(name="symbol", type="simple string", required=True),
            Param(name="financial_id", type="simple string", required=True),
            Param(name="period", type="simple string", required=True),
            Param(name="gaps", type="simple barmerge_gaps", required=True),
            Param(name="ignore_invalid_symbol", type="input bool", required=False),
            Param(name="currency", type="simple string", required=False),
        ],
    ),
    "request.quandl": BuiltinFunction(
        name="request.quandl",
        return_type="float",
        description="Requests [Nasdaq Data Link](https://data.nasdaq.com/) (formerly Quandl) data for a symbol.",
        params=[
            Param(name="ticker", type="simple string", required=True),
            Param(name="gaps", type="simple barmerge_gaps", required=True),
            Param(name="index", type="simple int", required=True),
            Param(name="ignore_invalid_symbol", type="input bool", required=False),
        ],
    ),
    "request.security": BuiltinFunction(
        name="request.security",
        return_type="void",
        description="Requests data from another symbol and/or timeframe.",
        params=[
            Param(name="symbol", type="simple string", required=True),
            Param(name="timeframe", type="simple string", required=True),
            Param(
                name="expression",
                type="<variable>|<object>|<function>|array|matrix|int|float|bool|string|color|tuple[...]",
                required=True,
            ),
            Param(name="gaps", type="simple barmerge_gaps", required=False),
            Param(name="lookahead", type="simple barmerge_lookahead", required=False),
            Param(name="ignore_invalid_symbol", type="input bool", required=False),
            Param(name="currency", type="simple string", required=False),
        ],
    ),
    "request.security_lower_tf": BuiltinFunction(
        name="request.security_lower_tf",
        return_type="void",
        description="Requests data from a specified symbol from a lower timeframe than the chart\\`s. The function returns an array containing one element for each closed lower timeframe intrabar inside the current chart\\`",
        params=[
            Param(name="symbol", type="simple string", required=True),
            Param(name="timeframe", type="simple string", required=True),
            Param(
                name="expression",
                type="<variable>|<object>|<function>|array|matrix|int|float|bool|string|color|tuple[...]",
                required=True,
            ),
            Param(name="ignore_invalid_symbol", type="const bool", required=False),
            Param(name="currency", type="simple string", required=False),
        ],
    ),
    "request.seed": BuiltinFunction(
        name="request.seed",
        return_type="void",
        description="Requests data from a user-maintained GitHub repository and returns it as a series.  ",
        params=[
            Param(name="source", type="simple string", required=True),
            Param(name="symbol", type="simple string", required=True),
            Param(name="expression", type="<type>", required=True),
        ],
    ),
    "request.splits": BuiltinFunction(
        name="request.splits",
        return_type="float",
        description="Requests splits data for the specified symbol.",
        params=[
            Param(name="ticker", type="simple string", required=True),
            Param(name="field", type="simple string", required=True),
            Param(name="gaps", type="simple barmerge_gaps", required=True),
            Param(name="lookahead", type="simple barmerge_lookahead", required=True),
            Param(name="ignore_invalid_symbol", type="input bool", required=False),
        ],
    ),
    "runtime.error": BuiltinFunction(
        name="runtime.error",
        return_type="void",
        description="When called, causes a runtime error with the error message specified in the `message` argument.",
        params=[
            Param(name="message", type="series string", required=True),
        ],
    ),
    "second": BuiltinFunction(
        name="second",
        return_type="int",
        description="",
        params=[
            Param(name="time", type="series int", required=True),
            Param(name="timezone", type="series string", required=True),
        ],
    ),
    "str.contains": BuiltinFunction(
        name="str.contains",
        return_type="bool",
        description="Returns true if the `source` string contains the `str` substring, false otherwise.",
        params=[
            Param(name="source", type="series string", required=True),
            Param(name="str", type="series string", required=True),
        ],
    ),
    "str.endswith": BuiltinFunction(
        name="str.endswith",
        return_type="bool",
        description="Returns true if the `source` string ends with the substring specified in `str`, false otherwise.",
        params=[
            Param(name="source", type="series string", required=True),
            Param(name="str", type="series string", required=True),
        ],
    ),
    "str.format": BuiltinFunction(
        name="str.format",
        return_type="string",
        description="Converts the formatting string and value(s) into a formatted string. The formatting string can contain literal text and one placeholder in curly braces {} for each value to be formatted. Each placehol",
        params=[
            Param(name="formatString", type="series string", required=True),
            Param(
                name="arg0, arg1, ...",
                type="array<[int|float|bool|string]>|na ",
                required=True,
            ),
        ],
    ),
    "str.format_time": BuiltinFunction(
        name="str.format_time",
        return_type="string",
        description="Converts the `time` timestamp into a string formatted according to `format` and `timezone`.",
        params=[
            Param(name="time", type="series int", required=True),
            Param(name="format", type="series string", required=True),
            Param(name="timezone", type="series string", required=False),
        ],
    ),
    "str.length": BuiltinFunction(
        name="str.length",
        return_type="int",
        description="Returns an integer corresponding to the amount of chars in that string.",
        params=[
            Param(name="string", type="series string", required=True),
        ],
    ),
    "str.lower": BuiltinFunction(
        name="str.lower",
        return_type="string",
        description="Returns a new string with all letters converted to lowercase.",
        params=[
            Param(name="source", type="series string", required=True),
        ],
    ),
    "str.match": BuiltinFunction(
        name="str.match",
        return_type="string",
        description="Returns the new substring of the `source` string if it matches a `regex` regular expression, an empty string otherwise.",
        params=[
            Param(name="source", type="series string", required=True),
            Param(name="regex", type="series string", required=True),
        ],
    ),
    "str.pos": BuiltinFunction(
        name="str.pos",
        return_type="int",
        description="Returns the position of the first occurrence of the `str` string in the `source` string, 'na' otherwise.",
        params=[
            Param(name="source", type="series string", required=True),
            Param(name="str", type="series string", required=True),
        ],
    ),
    "str.repeat": BuiltinFunction(
        name="str.repeat",
        return_type="string",
        description="Repeats string.",
        params=[
            Param(name="source", type="string", required=True),
            Param(name="count", type="int", required=True),
            Param(name="separator", type="string", required=False),
        ],
    ),
    "str.replace": BuiltinFunction(
        name="str.replace",
        return_type="string",
        description="Returns a new string with the Nth occurrence of the `target` string replaced by the `replacement` string, where N is specified in `occurrence`.",
        params=[
            Param(name="source", type="series string", required=True),
            Param(name="target", type="series string", required=True),
            Param(name="replacement", type="series string", required=True),
            Param(name="occurrence", type="series int", required=False),
        ],
    ),
    "str.replace_all": BuiltinFunction(
        name="str.replace_all",
        return_type="string",
        description="Replaces each occurrence of the target string in the source string with the replacement string.",
        params=[
            Param(name="source", type="series string", required=True),
            Param(name="target", type="series string", required=True),
            Param(name="replacement", type="series string", required=True),
        ],
    ),
    "str.split": BuiltinFunction(
        name="str.split",
        return_type="array<string>",
        description="Divides a string into an array of substrings and returns its array id.",
        params=[
            Param(name="string", type="series string", required=True),
            Param(name="separator", type="series string", required=True),
        ],
    ),
    "str.startswith": BuiltinFunction(
        name="str.startswith",
        return_type="bool",
        description="Returns true if the `source` string starts with the substring specified in `str`, false otherwise.",
        params=[
            Param(name="source", type="series string", required=True),
            Param(name="str", type="series string", required=True),
        ],
    ),
    "str.substring": BuiltinFunction(
        name="str.substring",
        return_type="string",
        description="Returns a new string that is a substring of the `source` string. The substring begins with the character at the index specified by `begin_pos` and extends to 'end_pos - 1' of the `source` string.",
        params=[
            Param(name="source", type="series string", required=True),
            Param(name="begin_pos", type="series int", required=True),
            Param(name="end_pos", type="series int", required=False),
        ],
    ),
    "str.tonumber": BuiltinFunction(
        name="str.tonumber",
        return_type="float",
        description='Converts a value represented in `string` to its "float" equivalent.',
        params=[
            Param(name="string", type="series string", required=True),
        ],
    ),
    "str.tostring": BuiltinFunction(
        name="str.tostring",
        return_type="string",
        description="",
        params=[
            Param(
                name="value",
                type="series matrix|array<int|float|bool|string>",
                required=True,
            ),
            Param(name="format", type="series string", required=True),
        ],
    ),
    "str.trim": BuiltinFunction(
        name="str.trim",
        return_type="string",
        description="Trims string.",
        params=[
            Param(name="source", type="string", required=True),
        ],
    ),
    "str.upper": BuiltinFunction(
        name="str.upper",
        return_type="string",
        description="Returns a new string with all letters converted to uppercase.",
        params=[
            Param(name="source", type="series string", required=True),
        ],
    ),
    "strategy": BuiltinFunction(
        name="strategy",
        return_type="void",
        description="This declaration statement designates the script as a strategy and sets a number of strategy-related properties.",
        params=[
            Param(name="title", type="const string", required=True),
            Param(name="shorttitle", type="const string", required=False),
            Param(name="overlay", type="const bool", required=False),
            Param(name="format", type="const string", required=False),
            Param(name="precision", type="const int", required=False),
            Param(name="scale", type="const scale_type", required=False),
            Param(name="pyramiding", type="const int", required=False),
            Param(name="calc_on_order_fills", type="const bool", required=False),
            Param(name="calc_on_every_tick", type="const bool", required=False),
            Param(name="max_bars_back", type="const int", required=False),
            Param(
                name="backtest_fill_limits_assumption", type="const int", required=False
            ),
            Param(name="default_qty_type", type="const string", required=False),
            Param(name="default_qty_value", type="const int|float", required=False),
            Param(name="initial_capital", type="const int|float", required=False),
            Param(name="currency", type="const string", required=False),
            Param(name="slippage", type="const int", required=False),
            Param(name="commission_type", type="const string", required=False),
            Param(name="commission_value", type="const int|float", required=False),
            Param(name="process_orders_on_close", type="const bool", required=False),
            Param(name="close_entries_rule", type="const string", required=False),
            Param(name="margin_long", type="const int|float", required=False),
            Param(name="margin_short", type="const int|float", required=False),
            Param(name="explicit_plot_zorder", type="const bool", required=False),
            Param(name="max_lines_count", type="const int", required=False),
            Param(name="max_labels_count", type="const int", required=False),
            Param(name="max_boxes_count", type="const int", required=False),
            Param(name="risk_free_rate", type="const int|float", required=False),
            Param(name="use_bar_magnifier", type="const bool", required=False),
            Param(name="fill_orders_on_standard_ohlc", type="any", required=False),
            Param(name="max_polylines_count", type="const int", required=False),
        ],
    ),
    "strategy.cancel": BuiltinFunction(
        name="strategy.cancel",
        return_type="void",
        description="It is a command to cancel/deactivate pending orders by referencing their names, which were generated by the functions: [strategy.order](#fun_strategy.order), [strategy.entry](#fun_strategy.entry) and ",
        params=[
            Param(name="id", type="series string", required=True),
        ],
    ),
    "strategy.cancel_all": BuiltinFunction(
        name="strategy.cancel_all",
        return_type="void",
        description="It is a command to cancel/deactivate all pending orders, which were generated by the functions: [strategy.order](#fun_strategy.order), [strategy.entry](#fun_strategy.entry) and [strategy.exit](#fun_st",
        params=[],
    ),
    "strategy.close": BuiltinFunction(
        name="strategy.close",
        return_type="void",
        description="It is a command to exit from the entry with the specified ID. If there were multiple entry orders with the same ID, all of them are exited at once. If there are no open entries with the specified ID b",
        params=[
            Param(name="id", type="series string", required=True),
            Param(name="comment", type="series string", required=False),
            Param(name="qty", type="series int|float", required=False),
            Param(name="qty_percent", type="series int|float", required=False),
            Param(name="alert_message", type="series string", required=False),
            Param(name="immediately", type="series bool", required=False),
            Param(name="disable_alert", type="series bool", required=False),
        ],
    ),
    "strategy.close_all": BuiltinFunction(
        name="strategy.close_all",
        return_type="void",
        description="Exits the current market position, making it flat.",
        params=[
            Param(name="comment", type="series string", required=False),
            Param(name="alert_message", type="series string", required=False),
            Param(name="immediately", type="series bool", required=False),
            Param(name="disable_alert", type="series bool", required=False),
        ],
    ),
    "strategy.closedtrades.commission": BuiltinFunction(
        name="strategy.closedtrades.commission",
        return_type="float",
        description="Returns the sum of entry and exit fees paid in the closed trade.",
        params=[
            Param(name="trade_num", type="series int", required=True),
        ],
    ),
    "strategy.closedtrades.entry_bar_index": BuiltinFunction(
        name="strategy.closedtrades.entry_bar_index",
        return_type="int",
        description="Returns the bar_index of the closed trade\\`s entry.",
        params=[
            Param(name="trade_num", type="series int", required=True),
        ],
    ),
    "strategy.closedtrades.entry_comment": BuiltinFunction(
        name="strategy.closedtrades.entry_comment",
        return_type="string",
        description="Returns the comment message of the closed trade\\`s entry, or [na](#var_na)",
        params=[
            Param(name="trade_num", type="series int", required=True),
        ],
    ),
    "strategy.closedtrades.entry_id": BuiltinFunction(
        name="strategy.closedtrades.entry_id",
        return_type="string",
        description="Returns the id of the closed trade\\`s entry.",
        params=[
            Param(name="trade_num", type="series int", required=True),
        ],
    ),
    "strategy.closedtrades.entry_price": BuiltinFunction(
        name="strategy.closedtrades.entry_price",
        return_type="float",
        description="Rnumbereturns the price of the closed trade\\`s entry.",
        params=[
            Param(name="trade_num", type="series int", required=True),
        ],
    ),
    "strategy.closedtrades.entry_time": BuiltinFunction(
        name="strategy.closedtrades.entry_time",
        return_type="int",
        description="Returns the UNIX time of the closed trade\\`s entry.",
        params=[
            Param(name="trade_num", type="series int", required=True),
        ],
    ),
    "strategy.closedtrades.exit_bar_index": BuiltinFunction(
        name="strategy.closedtrades.exit_bar_index",
        return_type="int",
        description="Returns the bar_index of the closed trade\\`s exit.",
        params=[
            Param(name="trade_num", type="series int", required=True),
        ],
    ),
    "strategy.closedtrades.exit_comment": BuiltinFunction(
        name="strategy.closedtrades.exit_comment",
        return_type="string",
        description="Returns the comment message of the closed trade\\`s exit, or",
        params=[
            Param(name="trade_num", type="series int", required=True),
        ],
    ),
    "strategy.closedtrades.exit_id": BuiltinFunction(
        name="strategy.closedtrades.exit_id",
        return_type="string",
        description="Returns the id of the closed trade\\`s exit.",
        params=[
            Param(name="trade_num", type="series int", required=True),
        ],
    ),
    "strategy.closedtrades.exit_price": BuiltinFunction(
        name="strategy.closedtrades.exit_price",
        return_type="float",
        description="Returns the price of the closed trade\\`s exit.",
        params=[
            Param(name="trade_num", type="series int", required=True),
        ],
    ),
    "strategy.closedtrades.exit_time": BuiltinFunction(
        name="strategy.closedtrades.exit_time",
        return_type="int",
        description="Returns the UNIX time of the closed trade\\`s exit.",
        params=[
            Param(name="trade_num", type="series int", required=True),
        ],
    ),
    "strategy.closedtrades.max_drawdown": BuiltinFunction(
        name="strategy.closedtrades.max_drawdown",
        return_type="float",
        description="Returns the maximum drawdown of the closed trade, i.e., the maximum possible loss during the trade.",
        params=[
            Param(name="trade_num", type="series int", required=True),
        ],
    ),
    "strategy.closedtrades.max_drawdown_percent": BuiltinFunction(
        name="strategy.closedtrades.max_drawdown_percent",
        return_type="void",
        description="Returns the maximum drawdown of the closed trade, i.e., the maximum possible loss during the trade, expressed as a percentage and calculated by formula: `Lowest Value During Trade  / (Entry Price x Qu",
        params=[
            Param(name="trade_num", type="series int", required=True),
        ],
    ),
    "strategy.closedtrades.max_runup": BuiltinFunction(
        name="strategy.closedtrades.max_runup",
        return_type="float",
        description="Returns the maximum run up of the closed trade, i.e., the maximum possible profit during the trade.",
        params=[
            Param(name="trade_num", type="series int", required=True),
        ],
    ),
    "strategy.closedtrades.max_runup_percent": BuiltinFunction(
        name="strategy.closedtrades.max_runup_percent",
        return_type="void",
        description="Returns the maximum run-up of the closed trade, i.e., the maximum possible profit during the trade, expressed as a percentage and calculated by formula: `Highest Value During Trade / (Entry Price x Qu",
        params=[
            Param(name="trade_num", type="series int", required=True),
        ],
    ),
    "strategy.closedtrades.profit": BuiltinFunction(
        name="strategy.closedtrades.profit",
        return_type="float",
        description="Returns the profit/loss of the closed trade. Losses are expressed as negative values.",
        params=[
            Param(name="trade_num", type="series int", required=True),
        ],
    ),
    "strategy.closedtrades.profit_percent": BuiltinFunction(
        name="strategy.closedtrades.profit_percent",
        return_type="void",
        description="Returns the profit/loss value of the closed trade, expressed as a percentage. Losses are expressed as negative values.",
        params=[
            Param(name="trade_num", type="series int", required=True),
        ],
    ),
    "strategy.closedtrades.size": BuiltinFunction(
        name="strategy.closedtrades.size",
        return_type="float",
        description="Returns the direction and the number of contracts traded in the closed trade. If the value is > 0, the market position was long. If the value is < 0, the market position was short.",
        params=[
            Param(name="trade_num", type="series int", required=True),
        ],
    ),
    "strategy.convert_to_account": BuiltinFunction(
        name="strategy.convert_to_account",
        return_type="float",
        description="Converts the value from the currency that the symbol on the chart is traded in ([syminfo.currency](#var_syminfo.currency)) to the currency used by the strategy ([strategy.account_currency](#var_strate",
        params=[
            Param(name="value", type="series int|float", required=True),
        ],
    ),
    "strategy.convert_to_symbol": BuiltinFunction(
        name="strategy.convert_to_symbol",
        return_type="float",
        description="Converts the value from the currency used by the strategy ([strategy.account_currency](#var_strategy.account_currency)) to the currency that the symbol on the chart is traded in ([syminfo.currency](#v",
        params=[
            Param(name="value", type="series int|float", required=True),
        ],
    ),
    "strategy.default_entry_qty": BuiltinFunction(
        name="strategy.default_entry_qty",
        return_type="void",
        description="Calculates the default quantity, in units, of an entry order from [strategy.entry](#fun_strategy.entry) or [strategy.order](#fun_strategy.order) if it were to fill at the specified `fill_price` value.",
        params=[
            Param(name="fill_price", type="series int/float", required=True),
        ],
    ),
    "strategy.entry": BuiltinFunction(
        name="strategy.entry",
        return_type="void",
        description="It is a command to enter market position. If an order with the same ID is already pending, it is possible to modify the order.  ",
        params=[
            Param(name="id", type="series string", required=True),
            Param(name="direction", type="series strategy_direction", required=True),
            Param(name="qty", type="series int|float", required=False),
            Param(name="limit", type="series int|float", required=False),
            Param(name="stop", type="series int|float", required=False),
            Param(name="oca_name", type="series string", required=False),
            Param(name="oca_type", type="input string", required=False),
            Param(name="comment", type="series string", required=False),
            Param(name="alert_message", type="series string", required=False),
            Param(name="disable_alert", type="series bool", required=False),
        ],
    ),
    "strategy.exit": BuiltinFunction(
        name="strategy.exit",
        return_type="void",
        description="It is a command to exit either a specific entry, or whole market position. If an order with the same ID is already pending, it is possible to modify the order.  ",
        params=[
            Param(name="id", type="series string", required=True),
            Param(name="from_entry", type="series string", required=False),
            Param(name="qty", type="series int|float", required=False),
            Param(name="qty_percent", type="series int|float", required=False),
            Param(name="profit", type="series int|float", required=False),
            Param(name="limit", type="series int|float", required=False),
            Param(name="loss", type="series int|float", required=False),
            Param(name="stop", type="series int|float", required=False),
            Param(name="trail_price", type="series int|float", required=False),
            Param(name="trail_points", type="series int|float", required=False),
            Param(name="trail_offset", type="series int|float", required=False),
            Param(name="oca_name", type="series string", required=False),
            Param(name="comment", type="series string", required=False),
            Param(name="comment_profit", type="series string", required=False),
            Param(name="comment_loss", type="series string", required=False),
            Param(name="comment_trailing", type="series string", required=False),
            Param(name="alert_message", type="series string", required=False),
            Param(name="alert_profit", type="series string", required=False),
            Param(name="alert_loss", type="series string", required=False),
            Param(name="alert_trailing", type="series string", required=False),
            Param(name="disable_alert", type="series bool", required=False),
        ],
    ),
    "strategy.opentrades.commission": BuiltinFunction(
        name="strategy.opentrades.commission",
        return_type="float",
        description="Returns the sum of entry and exit fees paid in the open trade.",
        params=[
            Param(name="trade_num", type="series int", required=True),
        ],
    ),
    "strategy.opentrades.entry_bar_index": BuiltinFunction(
        name="strategy.opentrades.entry_bar_index",
        return_type="int",
        description="Returns the bar_index of the open trade\\`s entry.",
        params=[
            Param(name="trade_num", type="series int", required=True),
        ],
    ),
    "strategy.opentrades.entry_comment": BuiltinFunction(
        name="strategy.opentrades.entry_comment",
        return_type="string",
        description="Returns the comment message of the open trade\\`s entry, or",
        params=[
            Param(name="trade_num", type="series int", required=True),
        ],
    ),
    "strategy.opentrades.entry_id": BuiltinFunction(
        name="strategy.opentrades.entry_id",
        return_type="string",
        description="Returns the id of the open trade\\`s entry.",
        params=[
            Param(name="trade_num", type="series int", required=True),
        ],
    ),
    "strategy.opentrades.entry_price": BuiltinFunction(
        name="strategy.opentrades.entry_price",
        return_type="float",
        description="Returns the price of the open trade\\`s entry.",
        params=[
            Param(name="trade_num", type="series int", required=True),
        ],
    ),
    "strategy.opentrades.entry_time": BuiltinFunction(
        name="strategy.opentrades.entry_time",
        return_type="int",
        description="Returns the UNIX time of the open trade\\`s entry.",
        params=[
            Param(name="trade_num", type="series int", required=True),
        ],
    ),
    "strategy.opentrades.max_drawdown": BuiltinFunction(
        name="strategy.opentrades.max_drawdown",
        return_type="float",
        description="Returns the maximum drawdown of the open trade, i.e., the maximum possible loss during the trade.",
        params=[
            Param(name="trade_num", type="series int", required=True),
        ],
    ),
    "strategy.opentrades.max_drawdown_percent": BuiltinFunction(
        name="strategy.opentrades.max_drawdown_percent",
        return_type="void",
        description="Returns the maximum drawdown of the open trade, i.e., the maximum possible loss during the trade, expressed as a percentage and calculated by formula: `Lowest Value During Trade  / (Entry Price x Quan",
        params=[
            Param(name="trade_num", type="series int", required=True),
        ],
    ),
    "strategy.opentrades.max_runup": BuiltinFunction(
        name="strategy.opentrades.max_runup",
        return_type="float",
        description="Returns the maximum run up of the open trade, i.e., the maximum possible profit during the trade.",
        params=[
            Param(name="trade_num", type="series int", required=True),
        ],
    ),
    "strategy.opentrades.max_runup_percent": BuiltinFunction(
        name="strategy.opentrades.max_runup_percent",
        return_type="void",
        description="Returns the maximum run-up of the open trade, i.e., the maximum possible profit during the trade, expressed as a percentage and calculated by formula: `Highest Value During Trade / (Entry Price x Quan",
        params=[
            Param(name="trade_num", type="series int", required=True),
        ],
    ),
    "strategy.opentrades.profit": BuiltinFunction(
        name="strategy.opentrades.profit",
        return_type="float",
        description="Returns the profit/loss of the open trade. Losses are expressed as negative values.",
        params=[
            Param(name="trade_num", type="series int", required=True),
        ],
    ),
    "strategy.opentrades.profit_percent": BuiltinFunction(
        name="strategy.opentrades.profit_percent",
        return_type="void",
        description="Returns the profit/loss of the open trade, expressed as a percentage. Losses are expressed as negative values.",
        params=[
            Param(name="trade_num", type="series int", required=True),
        ],
    ),
    "strategy.opentrades.size": BuiltinFunction(
        name="strategy.opentrades.size",
        return_type="float",
        description="Returns the direction and the number of contracts traded in the open trade. If the value is > 0, the market position was long. If the value is < 0, the market position was short.",
        params=[
            Param(name="trade_num", type="series int", required=True),
        ],
    ),
    "strategy.order": BuiltinFunction(
        name="strategy.order",
        return_type="void",
        description="It is a command to place order. If an order with the same ID is already pending, it is possible to modify the order.  ",
        params=[
            Param(name="id", type="series string", required=True),
            Param(name="direction", type="series strategy_direction", required=True),
            Param(name="qty", type="series int|float", required=False),
            Param(name="limit", type="series int|float", required=False),
            Param(name="stop", type="series int|float", required=False),
            Param(name="oca_name", type="series string", required=False),
            Param(name="oca_type", type="input string", required=False),
            Param(name="comment", type="series string", required=False),
            Param(name="alert_message", type="series string", required=False),
            Param(name="disable_alert", type="series bool", required=False),
        ],
    ),
    "strategy.risk.allow_entry_in": BuiltinFunction(
        name="strategy.risk.allow_entry_in",
        return_type="void",
        description="This function can be used to specify in which market direction the [strategy.entry](#fun_strategy.entry) function is allowed to open positions.",
        params=[
            Param(name="value", type="simple string", required=True),
        ],
    ),
    "strategy.risk.max_cons_loss_days": BuiltinFunction(
        name="strategy.risk.max_cons_loss_days",
        return_type="void",
        description="The purpose of this rule is to cancel all pending orders, close all open positions and stop placing orders after a specified number of consecutive days with losses. The rule affects the whole strategy",
        params=[
            Param(name="count", type="simple int", required=True),
            Param(name="alert_message", type="simple string", required=False),
        ],
    ),
    "strategy.risk.max_drawdown": BuiltinFunction(
        name="strategy.risk.max_drawdown",
        return_type="void",
        description="The purpose of this rule is to determine maximum drawdown. The rule affects the whole strategy. Once the maximum drawdown value is reached, all pending orders are cancelled, all open positions are clo",
        params=[
            Param(name="value", type="simple int|float", required=True),
            Param(name="displayType", type="simple string", required=True),
            Param(name="alert_message", type="simple string", required=False),
        ],
    ),
    "strategy.risk.max_intraday_filled_orders": BuiltinFunction(
        name="strategy.risk.max_intraday_filled_orders",
        return_type="void",
        description="The purpose of this rule is to determine maximum number of filled orders per 1 day (per 1 bar, if chart resolution is higher than 1 day). The rule affects the whole strategy. Once the maximum number o",
        params=[
            Param(name="count", type="simple int", required=True),
            Param(name="alert_message", type="simple string", required=False),
        ],
    ),
    "strategy.risk.max_intraday_loss": BuiltinFunction(
        name="strategy.risk.max_intraday_loss",
        return_type="void",
        description="The maximum loss value allowed during a day. It is specified either in money (base currency), or in percentage of maximum intraday equity (0 -100).",
        params=[
            Param(name="value", type="simple int|float", required=True),
            Param(name="displayType", type="simple string", required=True),
            Param(name="alert_message", type="simple string", required=False),
        ],
    ),
    "strategy.risk.max_position_size": BuiltinFunction(
        name="strategy.risk.max_position_size",
        return_type="void",
        description="The purpose of this rule is to determine maximum size of a market position. The rule affects the following function: [strategy.entry](#fun_strategy.entry).  ",
        params=[
            Param(name="contracts", type="simple int|float", required=True),
        ],
    ),
    "string": BuiltinFunction(
        name="string",
        return_type="string",
        description="Casts na to string.",
        params=[
            Param(name="x", type="series color", required=True),
        ],
    ),
    "syminfo.prefix": BuiltinFunction(
        name="syminfo.prefix",
        return_type="string",
        description='Returns exchange prefix of the `symbol`, e.g. "NASDAQ".',
        params=[
            Param(name="symbol", type="series string", required=True),
        ],
    ),
    "syminfo.ticker": BuiltinFunction(
        name="syminfo.ticker",
        return_type="string",
        description='Returns `symbol` name without exchange prefix, e.g. "AAPL".',
        params=[
            Param(name="symbol", type="series string", required=True),
        ],
    ),
    "ta.alma": BuiltinFunction(
        name="ta.alma",
        return_type="float",
        description="Arnaud Legoux Moving Average. It uses Gaussian distribution as weights for moving average.",
        params=[
            Param(name="series", type="series int|float", required=True),
            Param(name="length", type="series int", required=True),
            Param(name="offset", type="simple int|float", required=True),
            Param(name="sigma", type="simple int|float", required=True),
            Param(name="floor", type="simple bool", required=True),
        ],
    ),
    "ta.atr": BuiltinFunction(
        name="ta.atr",
        return_type="float",
        description="Function atr (average true range) returns the RMA of true range. True range is max(high - low, abs(high - close[1]), abs(low - close[1])).",
        params=[
            Param(name="length", type="simple int", required=True),
        ],
    ),
    "ta.barssince": BuiltinFunction(
        name="ta.barssince",
        return_type="int",
        description="Counts the number of bars since the last time the condition was true.",
        params=[
            Param(name="condition", type="series bool", required=True),
        ],
    ),
    "ta.bb": BuiltinFunction(
        name="ta.bb",
        return_type="[float, float, float]",
        description="Bollinger Bands. A Bollinger Band is a technical analysis tool defined by a set of lines plotted two standard deviations (positively and negatively) away from a simple moving average (SMA) of the secu",
        params=[
            Param(name="series", type="series int|float", required=True),
            Param(name="length", type="series int", required=True),
            Param(name="mult", type="simple int|float", required=True),
        ],
    ),
    "ta.bbw": BuiltinFunction(
        name="ta.bbw",
        return_type="float",
        description="Bollinger Bands Width. The Bollinger Band Width is the difference between the upper and the lower Bollinger Bands divided by the middle band.",
        params=[
            Param(name="series", type="series int|float", required=True),
            Param(name="length", type="series int", required=True),
            Param(name="mult", type="simple int|float", required=True),
        ],
    ),
    "ta.cci": BuiltinFunction(
        name="ta.cci",
        return_type="float",
        description="The CCI (commodity channel index) is calculated as the difference between the typical price of a commodity and its simple moving average, divided by the mean absolute deviation of the typical price. T",
        params=[
            Param(name="source", type="series int|float", required=True),
            Param(name="length", type="series int", required=True),
        ],
    ),
    "ta.change": BuiltinFunction(
        name="ta.change",
        return_type="float|int|bool",
        description="Compares the current `source` value to its value `length` bars ago and returns the difference.",
        params=[
            Param(name="source", type="series int|float|bool", required=True),
            Param(name="length", type="series int", required=True),
        ],
    ),
    "ta.cmo": BuiltinFunction(
        name="ta.cmo",
        return_type="float",
        description="Chande Momentum Oscillator. Calculates the difference between the sum of recent gains and the sum of recent losses and then divides the result by the sum of all price movement over the same period.",
        params=[
            Param(name="series", type="series int|float", required=True),
            Param(name="length", type="series int", required=True),
        ],
    ),
    "ta.cog": BuiltinFunction(
        name="ta.cog",
        return_type="float",
        description="The cog (center of gravity) is an indicator based on statistics and the Fibonacci golden ratio.",
        params=[
            Param(name="source", type="series int|float", required=True),
            Param(name="length", type="series int", required=True),
        ],
    ),
    "ta.correlation": BuiltinFunction(
        name="ta.correlation",
        return_type="float",
        description="Correlation coefficient. Describes the degree to which two series tend to deviate from their [ta.sma](#fun_ta.sma) values.",
        params=[
            Param(name="source1", type="series int|float", required=True),
            Param(name="source2", type="series int|float", required=True),
            Param(name="length", type="series int", required=True),
        ],
    ),
    "ta.cross": BuiltinFunction(
        name="ta.cross",
        return_type="bool",
        description="",
        params=[
            Param(name="source1", type="series int|float", required=True),
            Param(name="source2", type="series int|float", required=True),
        ],
    ),
    "ta.crossover": BuiltinFunction(
        name="ta.crossover",
        return_type="bool",
        description="The `source1`-series is defined as having crossed over `source2`-series if, on the current bar, the value of `source1` is greater than the value of `source2`, and on the previous bar, the value of `so",
        params=[
            Param(name="source1", type="series int|float", required=True),
            Param(name="source2", type="series int|float", required=True),
        ],
    ),
    "ta.crossunder": BuiltinFunction(
        name="ta.crossunder",
        return_type="bool",
        description="The `source1`-series is defined as having crossed under `source2`-series if, on the current bar, the value of `source1` is less than the value of `source2`, and on the previous bar, the value of `sour",
        params=[
            Param(name="source1", type="series int|float", required=True),
            Param(name="source2", type="series int|float", required=True),
        ],
    ),
    "ta.cum": BuiltinFunction(
        name="ta.cum",
        return_type="float",
        description="Cumulative (total) sum of `source`. In other words it\\`s a sum of all elements of `source`.",
        params=[
            Param(name="source", type="series int|float", required=True),
        ],
    ),
    "ta.dev": BuiltinFunction(
        name="ta.dev",
        return_type="float",
        description="Measure of difference between the series and it\\`s [ta.sma](#fun_ta.sma)",
        params=[
            Param(name="source", type="series int|float", required=True),
            Param(name="length", type="series int", required=True),
        ],
    ),
    "ta.dmi": BuiltinFunction(
        name="ta.dmi",
        return_type="[float, float, float]",
        description="The dmi function returns the directional movement index.",
        params=[
            Param(name="diLength", type="simple int", required=True),
            Param(name="adxSmoothing", type="simple int", required=True),
        ],
    ),
    "ta.ema": BuiltinFunction(
        name="ta.ema",
        return_type="float",
        description="The ema function returns the exponentially weighted moving average. In ema weighting factors decrease exponentially. It calculates by using a formula: EMA = alpha * source + (1 - alpha) * EMA[1], wher",
        params=[
            Param(name="source", type="series int|float", required=True),
            Param(name="length", type="simple int", required=True),
        ],
    ),
    "ta.falling": BuiltinFunction(
        name="ta.falling",
        return_type="bool",
        description="Test if the `source` series is now falling for `length` bars long.",
        params=[
            Param(name="source", type="series int|float", required=True),
            Param(name="length", type="series int", required=True),
        ],
    ),
    "ta.highest": BuiltinFunction(
        name="ta.highest",
        return_type="float",
        description="Highest value for a given number of bars back.",
        params=[
            Param(name="source", type="series int|float", required=True),
            Param(name="length", type="series int", required=True),
        ],
    ),
    "ta.highestbars": BuiltinFunction(
        name="ta.highestbars",
        return_type="int",
        description="Highest value offset for a given number of bars back.",
        params=[
            Param(name="source", type="series int|float", required=True),
            Param(name="length", type="series int", required=True),
        ],
    ),
    "ta.hma": BuiltinFunction(
        name="ta.hma",
        return_type="float",
        description="The hma function returns the Hull Moving Average.",
        params=[
            Param(name="source", type="series int|float", required=True),
            Param(name="length", type="simple int", required=True),
        ],
    ),
    "ta.kc": BuiltinFunction(
        name="ta.kc",
        return_type="[float, float, float]",
        description="Keltner Channels. Keltner channel is a technical analysis indicator showing a central moving average line plus channel lines at a distance above and below.",
        params=[
            Param(name="series", type="series int|float", required=True),
            Param(name="length", type="simple int", required=True),
            Param(name="mult", type="simple int|float", required=True),
            Param(name="useTrueRange", type="simple bool", required=True),
        ],
    ),
    "ta.kcw": BuiltinFunction(
        name="ta.kcw",
        return_type="float",
        description="Keltner Channels Width. The Keltner Channels Width is the difference between the upper and the lower Keltner Channels divided by the middle channel.",
        params=[
            Param(name="series", type="series int|float", required=True),
            Param(name="length", type="simple int", required=True),
            Param(name="mult", type="simple int|float", required=True),
            Param(name="useTrueRange", type="simple bool", required=True),
        ],
    ),
    "ta.linreg": BuiltinFunction(
        name="ta.linreg",
        return_type="float",
        description="Linear regression curve. A line that best fits the prices specified over a user-defined time period.  ",
        params=[
            Param(name="source", type="series int|float", required=True),
            Param(name="length", type="series int", required=True),
            Param(name="offset", type="simple int", required=True),
        ],
    ),
    "ta.lowest": BuiltinFunction(
        name="ta.lowest",
        return_type="float",
        description="Lowest value for a given number of bars back.",
        params=[
            Param(name="source", type="series int|float", required=True),
            Param(name="length", type="series int", required=True),
        ],
    ),
    "ta.lowestbars": BuiltinFunction(
        name="ta.lowestbars",
        return_type="int",
        description="Lowest value offset for a given number of bars back.",
        params=[
            Param(name="source", type="series int|float", required=True),
            Param(name="length", type="series int", required=True),
        ],
    ),
    "ta.macd": BuiltinFunction(
        name="ta.macd",
        return_type="[float, float, float]",
        description="MACD (moving average convergence/divergence). It is supposed to reveal changes in the strength, direction, momentum, and duration of a trend in a stock\\`s price.",
        params=[
            Param(name="source", type="series int|float", required=True),
            Param(name="fastlen", type="simple int", required=True),
            Param(name="slowlen", type="simple int", required=True),
            Param(name="siglen", type="simple int", required=True),
        ],
    ),
    "ta.max": BuiltinFunction(
        name="ta.max",
        return_type="float",
        description="Returns the all-time high value of `source` from the beginning of the chart up to the current bar.",
        params=[
            Param(name="source", type="series int|float", required=True),
        ],
    ),
    "ta.median": BuiltinFunction(
        name="ta.median",
        return_type="float|int",
        description="Returns the median of the series.",
        params=[
            Param(name="source", type="series int|float", required=True),
            Param(name="length", type="series int", required=True),
        ],
    ),
    "ta.mfi": BuiltinFunction(
        name="ta.mfi",
        return_type="float",
        description="Money Flow Index. The Money Flow Index (MFI) is a technical oscillator that uses price and volume for identifying overbought or oversold conditions in an asset.",
        params=[
            Param(name="series", type="series int|float", required=True),
            Param(name="length", type="series int", required=True),
        ],
    ),
    "ta.min": BuiltinFunction(
        name="ta.min",
        return_type="float",
        description="Returns the all-time low value of `source` from the beginning of the chart up to the current bar.",
        params=[
            Param(name="source", type="series int|float", required=True),
        ],
    ),
    "ta.mode": BuiltinFunction(
        name="ta.mode",
        return_type="float|int",
        description="Returns the [mode](https://en.wikipedia.org/wiki/Mode_(statistics)) of the series.  ",
        params=[
            Param(name="source", type="series int|float", required=True),
            Param(name="length", type="series int", required=True),
        ],
    ),
    "ta.mom": BuiltinFunction(
        name="ta.mom",
        return_type="float",
        description="Momentum of `source` price and `source` price `length` bars ago. This is simply a difference: source - source[length].",
        params=[
            Param(name="source", type="series int|float", required=True),
            Param(name="length", type="series int", required=True),
        ],
    ),
    "ta.percentile_linear_interpolation": BuiltinFunction(
        name="ta.percentile_linear_interpolation",
        return_type="float",
        description="Calculates percentile using method of linear interpolation between the two nearest ranks.",
        params=[
            Param(name="source", type="series int|float", required=True),
            Param(name="length", type="series int", required=True),
            Param(name="percentage", type="simple int|float", required=True),
        ],
    ),
    "ta.percentile_nearest_rank": BuiltinFunction(
        name="ta.percentile_nearest_rank",
        return_type="float",
        description="Calculates percentile using method of Nearest Rank.",
        params=[
            Param(name="source", type="series int|float", required=True),
            Param(name="length", type="series int", required=True),
            Param(name="percentage", type="simple int|float", required=True),
        ],
    ),
    "ta.percentrank": BuiltinFunction(
        name="ta.percentrank",
        return_type="float",
        description="Percent rank is the percents of how many previous values was less than or equal to the current value of given series.",
        params=[
            Param(name="source", type="series int|float", required=True),
            Param(name="length", type="series int", required=True),
        ],
    ),
    "ta.pivot_point_levels": BuiltinFunction(
        name="ta.pivot_point_levels",
        return_type="array<float>",
        description="Calculates the pivot point levels using the specified `type` and `anchor`.",
        params=[
            Param(name="displayType", type="series string", required=True),
            Param(name="anchor", type="series bool", required=True),
            Param(name="developing", type="series bool", required=False),
        ],
    ),
    "ta.pivothigh": BuiltinFunction(
        name="ta.pivothigh",
        return_type="float",
        description="This function returns price of the pivot high point. It returns 'NaN', if there was no pivot high point.",
        params=[
            Param(name="source", type="series int|float", required=True),
            Param(name="leftbars", type="series int|float", required=True),
            Param(name="rightbars", type="series int|float", required=True),
        ],
    ),
    "ta.pivotlow": BuiltinFunction(
        name="ta.pivotlow",
        return_type="float",
        description="This function returns price of the pivot low point. It returns 'NaN', if there was no pivot low point.",
        params=[
            Param(name="source", type="series int|float", required=True),
            Param(name="leftbars", type="series int|float", required=True),
            Param(name="rightbars", type="series int|float", required=True),
        ],
    ),
    "ta.range": BuiltinFunction(
        name="ta.range",
        return_type="float|int",
        description="Returns the difference between the min and max values in a series.",
        params=[
            Param(name="source", type="series int|float", required=True),
            Param(name="length", type="series int", required=True),
        ],
    ),
    "ta.rci": BuiltinFunction(
        name="ta.rci",
        return_type="float",
        description="Rank Correlation Index.",
        params=[
            Param(name="source", type="series float", required=True),
            Param(name="length", type="simple int", required=True),
        ],
    ),
    "ta.rising": BuiltinFunction(
        name="ta.rising",
        return_type="bool",
        description="Test if the `source` series is now rising for `length` bars long.",
        params=[
            Param(name="source", type="series int|float", required=True),
            Param(name="length", type="series int", required=True),
        ],
    ),
    "ta.rma": BuiltinFunction(
        name="ta.rma",
        return_type="float",
        description="Moving average used in RSI. It is the exponentially weighted moving average with alpha = 1 / length.",
        params=[
            Param(name="source", type="series int|float", required=True),
            Param(name="length", type="simple int", required=True),
        ],
    ),
    "ta.roc": BuiltinFunction(
        name="ta.roc",
        return_type="float",
        description="Calculates the percentage of change (rate of change) between the current value of `source` and its value `length` bars ago.",
        params=[
            Param(name="source", type="series int|float", required=True),
            Param(name="length", type="series int", required=True),
        ],
    ),
    "ta.rsi": BuiltinFunction(
        name="ta.rsi",
        return_type="float",
        description="Relative strength index. It is calculated using the `ta.rma()` of upward and downward changes of `source` over the last `length` bars.",
        params=[
            Param(name="source", type="series int|float", required=True),
            Param(name="length", type="simple int", required=True),
        ],
    ),
    "ta.sar": BuiltinFunction(
        name="ta.sar",
        return_type="float",
        description="Parabolic SAR (parabolic stop and reverse) is a method devised by J. Welles Wilder, Jr., to find potential reversals in the market price direction of traded goods.",
        params=[
            Param(name="start", type="simple int|float", required=True),
            Param(name="inc", type="simple int|float", required=True),
            Param(name="max", type="simple int|float", required=True),
        ],
    ),
    "ta.sma": BuiltinFunction(
        name="ta.sma",
        return_type="float",
        description="The sma function returns the moving average, that is the sum of last y values of x, divided by y.",
        params=[
            Param(name="source", type="series int|float", required=True),
            Param(name="length", type="series int", required=True),
        ],
    ),
    "ta.stdev": BuiltinFunction(
        name="ta.stdev",
        return_type="float",
        description="",
        params=[
            Param(name="source", type="series int|float", required=True),
            Param(name="length", type="series int", required=True),
            Param(name="biased", type="series bool", required=False),
        ],
    ),
    "ta.stoch": BuiltinFunction(
        name="ta.stoch",
        return_type="float",
        description="Stochastic. It is calculated by a formula: 100 * (close - lowest(low, length)) / (highest(high, length) - lowest(low, length)).",
        params=[
            Param(name="source", type="series int|float", required=True),
            Param(name="high", type="series int|float", required=True),
            Param(name="low", type="series int|float", required=True),
            Param(name="length", type="series int", required=True),
        ],
    ),
    "ta.supertrend": BuiltinFunction(
        name="ta.supertrend",
        return_type="[float, float]",
        description="The Supertrend Indicator. The Supertrend is a trend following indicator.",
        params=[
            Param(name="factor", type="series int|float", required=True),
            Param(name="atrPeriod", type="simple int", required=True),
        ],
    ),
    "ta.swma": BuiltinFunction(
        name="ta.swma",
        return_type="float",
        description="Symmetrically weighted moving average with fixed length: 4. Weights: [1/6, 2/6, 2/6, 1/6].",
        params=[
            Param(name="source", type="series int|float", required=True),
        ],
    ),
    "ta.tr": BuiltinFunction(
        name="ta.tr",
        return_type="float",
        description="",
        params=[
            Param(name="handle_na", type="simple bool", required=True),
        ],
    ),
    "ta.tsi": BuiltinFunction(
        name="ta.tsi",
        return_type="float",
        description="True strength index. It uses moving averages of the underlying momentum of a financial instrument.",
        params=[
            Param(name="source", type="series int|float", required=True),
            Param(name="short_length", type="simple int", required=True),
            Param(name="long_length", type="simple int", required=True),
        ],
    ),
    "ta.valuewhen": BuiltinFunction(
        name="ta.valuewhen",
        return_type="float|color|int|bool",
        description="Returns the value of the `source` series on the bar where the `condition` was true on the nth most recent occurrence.",
        params=[
            Param(name="condition", type="series bool", required=True),
            Param(name="source", type="series int|float|bool|color", required=True),
            Param(name="occurrence", type="simple int", required=True),
        ],
    ),
    "ta.variance": BuiltinFunction(
        name="ta.variance",
        return_type="float",
        description="Variance is the expectation of the squared deviation of a series from its mean ([ta.sma](#fun_ta.sma)), and it informally measures how far a set of numbers are spread out from their mean.",
        params=[
            Param(name="source", type="series int|float", required=True),
            Param(name="length", type="series int", required=True),
            Param(name="biased", type="series bool", required=False),
        ],
    ),
    "ta.vwap": BuiltinFunction(
        name="ta.vwap",
        return_type="float|[float, float, float]",
        description="Volume weighted average price.",
        params=[
            Param(name="source", type="series int|float", required=True),
            Param(name="anchor", type="series bool", required=True),
            Param(name="stdev_mult", type="series int|float", required=True),
        ],
    ),
    "ta.vwma": BuiltinFunction(
        name="ta.vwma",
        return_type="float",
        description="The vwma function returns volume-weighted moving average of `source` for `length` bars back.  ",
        params=[
            Param(name="source", type="series int|float", required=True),
            Param(name="length", type="series int", required=True),
        ],
    ),
    "ta.wma": BuiltinFunction(
        name="ta.wma",
        return_type="float",
        description="The wma function returns weighted moving average of `source` for `length` bars back.  ",
        params=[
            Param(name="source", type="series int|float", required=True),
            Param(name="length", type="series int", required=True),
        ],
    ),
    "ta.wpr": BuiltinFunction(
        name="ta.wpr",
        return_type="float",
        description="Williams %R. The oscillator shows the current closing price in relation to the high and low of the past 'length' bars.",
        params=[
            Param(name="length", type="series int", required=True),
        ],
    ),
    "table": BuiltinFunction(
        name="table",
        return_type="table",
        description="Casts na to table.",
        params=[
            Param(name="x", type="series table", required=True),
        ],
    ),
    "table.cell": BuiltinFunction(
        name="table.cell",
        return_type="void",
        description="The function defines a cell in the table and sets its attributes.",
        params=[
            Param(name="column", type="series int", required=True),
            Param(name="row", type="series int", required=True),
            Param(name="text", type="series string", required=False),
            Param(name="text_font_family", type="series string", required=False),
            Param(name="width", type="series int|float", required=False),
            Param(name="height", type="series int|float", required=False),
            Param(name="text_color", type="series color", required=False),
            Param(name="text_halign", type="series string", required=False),
            Param(name="text_valign", type="series string", required=False),
            Param(name="text_size", type="series string", required=False),
            Param(name="bgcolor", type="series color", required=False),
            Param(name="tooltip", type="series string", required=False),
        ],
    ),
    "table.cell_set_bgcolor": BuiltinFunction(
        name="table.cell_set_bgcolor",
        return_type="void",
        description="The function sets the background color of the cell.",
        params=[
            Param(name="column", type="series int", required=True),
            Param(name="row", type="series int", required=True),
            Param(name="bgcolor", type="series color", required=False),
        ],
    ),
    "table.cell_set_height": BuiltinFunction(
        name="table.cell_set_height",
        return_type="void",
        description="The function sets the height of cell.",
        params=[
            Param(name="column", type="series int", required=True),
            Param(name="row", type="series int", required=True),
            Param(name="height", type="series int|float", required=False),
        ],
    ),
    "table.cell_set_text": BuiltinFunction(
        name="table.cell_set_text",
        return_type="void",
        description="The function sets the text in the specified cell.",
        params=[
            Param(name="column", type="series int", required=True),
            Param(name="row", type="series int", required=True),
            Param(name="text", type="series string", required=True),
        ],
    ),
    "table.cell_set_text_color": BuiltinFunction(
        name="table.cell_set_text_color",
        return_type="void",
        description="The function sets the color of the text inside the cell.",
        params=[
            Param(name="column", type="series int", required=True),
            Param(name="row", type="series int", required=True),
            Param(name="text_color", type="series color", required=True),
        ],
    ),
    "table.cell_set_text_font_family": BuiltinFunction(
        name="table.cell_set_text_font_family",
        return_type="void",
        description="The function sets the font family of the text inside the cell.",
        params=[
            Param(name="column", type="series int", required=True),
            Param(name="row", type="series int", required=True),
            Param(name="text_font_family", type="series string", required=True),
        ],
    ),
    "table.cell_set_text_formatting": BuiltinFunction(
        name="table.cell_set_text_formatting",
        return_type="void",
        description="Sets text formatting.",
        params=[
            Param(name="table_id", type="table", required=True),
            Param(name="column", type="int", required=True),
            Param(name="row", type="int", required=True),
            Param(name="formatting", type="string", required=True),
        ],
    ),
    "table.cell_set_text_halign": BuiltinFunction(
        name="table.cell_set_text_halign",
        return_type="void",
        description="The function sets the horizontal alignment of the cell\\`s text.",
        params=[
            Param(name="column", type="series int", required=True),
            Param(name="row", type="series int", required=True),
            Param(name="text_halign", type="series string", required=True),
        ],
    ),
    "table.cell_set_text_size": BuiltinFunction(
        name="table.cell_set_text_size",
        return_type="void",
        description="The function sets the size of the cell\\`s text.",
        params=[
            Param(name="column", type="series int", required=True),
            Param(name="row", type="series int", required=True),
            Param(name="text_size", type="series string", required=False),
        ],
    ),
    "table.cell_set_text_valign": BuiltinFunction(
        name="table.cell_set_text_valign",
        return_type="void",
        description="The function sets the vertical alignment of a cell\\`s text.",
        params=[
            Param(name="column", type="series int", required=True),
            Param(name="row", type="series int", required=True),
            Param(name="text_valign", type="series string", required=True),
        ],
    ),
    "table.cell_set_tooltip": BuiltinFunction(
        name="table.cell_set_tooltip",
        return_type="void",
        description="The function sets the tooltip in the specified cell.",
        params=[
            Param(name="column", type="series int", required=True),
            Param(name="row", type="series int", required=True),
            Param(name="tooltip", type="series string", required=True),
        ],
    ),
    "table.cell_set_width": BuiltinFunction(
        name="table.cell_set_width",
        return_type="void",
        description="The function sets the width of the cell.",
        params=[
            Param(name="column", type="series int", required=True),
            Param(name="row", type="series int", required=True),
            Param(name="width", type="series int|float", required=False),
        ],
    ),
    "table.clear": BuiltinFunction(
        name="table.clear",
        return_type="void",
        description="The function removes a cell or a sequence of cells from the table. The cells are removed in a rectangle shape where the start_column and start_row specify the top-left corner, and end_column and end_r",
        params=[
            Param(name="start_column", type="series int", required=True),
            Param(name="start_row", type="series int", required=True),
            Param(name="end_column", type="series int", required=False),
            Param(name="end_row", type="series int", required=False),
        ],
    ),
    "table.delete": BuiltinFunction(
        name="table.delete",
        return_type="void",
        description="The function deletes a table.",
        params=[],
    ),
    "table.merge_cells": BuiltinFunction(
        name="table.merge_cells",
        return_type="void",
        description="The function merges a sequence of cells in the table into one cell. The cells are merged in a rectangle shape where the start_column and start_row specify the top-left corner, and end_column and end_r",
        params=[
            Param(name="start_column", type="series int", required=True),
            Param(name="start_row", type="series int", required=True),
            Param(name="end_column", type="series int", required=True),
            Param(name="end_row", type="series int", required=True),
        ],
    ),
    "table.new": BuiltinFunction(
        name="table.new",
        return_type="table",
        description="The function creates a new table.",
        params=[
            Param(name="position", type="series string", required=True),
            Param(name="columns", type="series int", required=True),
            Param(name="rows", type="series int", required=True),
            Param(name="bgcolor", type="series color", required=False),
            Param(name="frame_color", type="series color", required=False),
            Param(name="frame_width", type="series int", required=False),
            Param(name="border_color", type="series color", required=False),
            Param(name="border_width", type="series int", required=False),
        ],
    ),
    "table.set_bgcolor": BuiltinFunction(
        name="table.set_bgcolor",
        return_type="void",
        description="The function sets the background color of a table.",
        params=[
            Param(name="bgcolor", type="series color", required=False),
        ],
    ),
    "table.set_border_color": BuiltinFunction(
        name="table.set_border_color",
        return_type="void",
        description="The function sets the color of the borders (excluding the outer frame) of the table\\`s cells.",
        params=[
            Param(name="border_color", type="series color", required=False),
        ],
    ),
    "table.set_border_width": BuiltinFunction(
        name="table.set_border_width",
        return_type="void",
        description="The function sets the width of the borders (excluding the outer frame) of the table\\`s cells.",
        params=[
            Param(name="border_width", type="series int", required=False),
        ],
    ),
    "table.set_frame_color": BuiltinFunction(
        name="table.set_frame_color",
        return_type="void",
        description="The function sets the color of the outer frame of a table.",
        params=[
            Param(name="frame_color", type="series color", required=False),
        ],
    ),
    "table.set_frame_width": BuiltinFunction(
        name="table.set_frame_width",
        return_type="void",
        description="The function set the width of the outer frame of a table.",
        params=[
            Param(name="frame_width", type="series int", required=False),
        ],
    ),
    "table.set_position": BuiltinFunction(
        name="table.set_position",
        return_type="void",
        description="The function sets the position of a table.",
        params=[
            Param(name="position", type="series string", required=True),
        ],
    ),
    "ticker.heikinashi": BuiltinFunction(
        name="ticker.heikinashi",
        return_type="string",
        description="Creates a ticker identifier for requesting Heikin Ashi bar values.",
        params=[
            Param(name="symbol", type="simple string", required=True),
        ],
    ),
    "ticker.inherit": BuiltinFunction(
        name="ticker.inherit",
        return_type="void",
        description="Constructs a ticker ID for the specified `symbol` with additional parameters inherited from the ticker ID passed into the function call, allowing the script to request a symbol's data using the same m",
        params=[
            Param(name="from_tickerid", type="simple string", required=True),
            Param(name="symbol", type="simple string", required=True),
        ],
    ),
    "ticker.kagi": BuiltinFunction(
        name="ticker.kagi",
        return_type="string",
        description="Creates a ticker identifier for requesting Kagi values.",
        params=[
            Param(name="symbol", type="simple string", required=True),
            Param(name="reversal", type="simple int|float", required=True),
        ],
    ),
    "ticker.linebreak": BuiltinFunction(
        name="ticker.linebreak",
        return_type="string",
        description="Creates a ticker identifier for requesting Line Break values.",
        params=[
            Param(name="symbol", type="simple string", required=True),
            Param(name="number_of_lines", type="simple int", required=True),
        ],
    ),
    "ticker.modify": BuiltinFunction(
        name="ticker.modify",
        return_type="string",
        description="Creates a ticker identifier for requesting additional data for the script.",
        params=[
            Param(name="tickerid", type="simple string", required=True),
            Param(name="session", type="simple string", required=False),
            Param(name="adjustment", type="simple string", required=False),
        ],
    ),
    "ticker.new": BuiltinFunction(
        name="ticker.new",
        return_type="string",
        description="Creates a ticker identifier for requesting additional data for the script.",
        params=[
            Param(name="prefix", type="simple string", required=True),
            Param(name="ticker", type="simple string", required=True),
            Param(name="session", type="simple string", required=False),
            Param(name="adjustment", type="simple string", required=False),
        ],
    ),
    "ticker.pointfigure": BuiltinFunction(
        name="ticker.pointfigure",
        return_type="string",
        description="Creates a ticker identifier for requesting Point & Figure values.",
        params=[
            Param(name="symbol", type="simple string", required=True),
            Param(name="source", type="simple string", required=True),
            Param(name="style", type="simple string", required=True),
            Param(name="param", type="simple int|float", required=True),
            Param(name="reversal", type="simple int", required=True),
        ],
    ),
    "ticker.renko": BuiltinFunction(
        name="ticker.renko",
        return_type="string",
        description="Creates a ticker identifier for requesting Renko values.",
        params=[
            Param(name="symbol", type="simple string", required=True),
            Param(name="style", type="simple string", required=True),
            Param(name="param", type="simple int|float", required=True),
            Param(name="request_wicks", type="simple bool", required=False),
            Param(name="source", type="simple string", required=False),
        ],
    ),
    "ticker.standard": BuiltinFunction(
        name="ticker.standard",
        return_type="string",
        description="Creates a ticker to request data from a standard chart that is unaffected by modifiers like extended session, dividend adjustment, currency conversion, and the calculations of non-standard chart types",
        params=[
            Param(name="symbol", type="simple string", required=False),
        ],
    ),
    "time": BuiltinFunction(
        name="time",
        return_type="int",
        description="The time function returns the UNIX time of the current bar for the specified timeframe and session or NaN if the time point is out of session.",
        params=[
            Param(name="timeframe", type="series string", required=True),
            Param(name="session", type="series string", required=True),
            Param(name="timezone", type="series string", required=True),
        ],
    ),
    "time_close": BuiltinFunction(
        name="time_close",
        return_type="int",
        description="Returns the UNIX time of the current bar\\`s close for the specified timeframe and session, or [na](#var_na) if the time point is outside the session.  ",
        params=[
            Param(name="timeframe", type="series string", required=True),
            Param(name="session", type="series string", required=True),
            Param(name="timezone", type="series string", required=True),
        ],
    ),
    "timeframe.change": BuiltinFunction(
        name="timeframe.change",
        return_type="bool",
        description="Detects changes in the specified `timeframe`.",
        params=[
            Param(name="timeframe", type="series string", required=True),
        ],
    ),
    "timeframe.from_seconds": BuiltinFunction(
        name="timeframe.from_seconds",
        return_type="void",
        description="Converts a number of seconds into a valid timeframe string.  ",
        params=[
            Param(name="seconds", type="series int", required=True),
        ],
    ),
    "timeframe.in_seconds": BuiltinFunction(
        name="timeframe.in_seconds",
        return_type="int",
        description="Converts the timeframe passed to the `timeframe` argument into seconds.",
        params=[
            Param(name="timeframe", type="series string", required=False),
        ],
    ),
    "timestamp": BuiltinFunction(
        name="timestamp",
        return_type="int",
        description="Function timestamp returns UNIX time of specified date and time.",
        params=[
            Param(name="timezone", type="series string", required=True),
            Param(name="year", type="series int", required=True),
            Param(name="month", type="series int", required=True),
            Param(name="day", type="series int", required=True),
            Param(name="hour", type="series int", required=False),
            Param(name="minute", type="series int", required=False),
            Param(name="second", type="series int", required=False),
            Param(name="dateString", type="const string", required=True),
        ],
    ),
    "weekofyear": BuiltinFunction(
        name="weekofyear",
        return_type="int",
        description="",
        params=[
            Param(name="time", type="series int", required=True),
            Param(name="timezone", type="series string", required=True),
        ],
    ),
    "year": BuiltinFunction(
        name="year",
        return_type="int",
        description="",
        params=[
            Param(name="time", type="series int", required=True),
            Param(name="timezone", type="series string", required=True),
        ],
    ),
}

PINE_VARIABLES: Dict[str, BuiltinVariable] = {
    "adjustment.dividends": BuiltinVariable(
        name="adjustment.dividends",
        type="const string",
        description="Constant for dividends adjustment type (dividends adjustment is applied).",
    ),
    "adjustment.none": BuiltinVariable(
        name="adjustment.none",
        type="const string",
        description="Constant for none adjustment type (no adjustment is applied).",
    ),
    "adjustment.splits": BuiltinVariable(
        name="adjustment.splits",
        type="const string",
        description="Constant for splits adjustment type (splits adjustment is applied).",
    ),
    "alert.freq_all": BuiltinVariable(
        name="alert.freq_all",
        type="const string",
        description="A named constant for use with the `freq` parameter of the alert() function.",
    ),
    "alert.freq_once_per_bar": BuiltinVariable(
        name="alert.freq_once_per_bar",
        type="const string",
        description="A named constant for use with the `freq` parameter of the alert() function.",
    ),
    "alert.freq_once_per_bar_close": BuiltinVariable(
        name="alert.freq_once_per_bar_close",
        type="const string",
        description="A named constant for use with the `freq` parameter of the alert() function.",
    ),
    "ask": BuiltinVariable(name="ask", type="series float", description="Ask price."),
    "bar_index": BuiltinVariable(
        name="bar_index",
        type="series int",
        description="Current bar index. Numbering is zero-based, index of the first bar is 0.",
    ),
    "barmerge.gaps_off": BuiltinVariable(
        name="barmerge.gaps_off",
        type="const barmerge_gaps",
        description="Merge strategy for requested data. Data is merged continuously without gaps, all the gaps are filled with the previous nearest existing value.",
    ),
    "barmerge.gaps_on": BuiltinVariable(
        name="barmerge.gaps_on",
        type="const barmerge_gaps",
        description="Merge strategy for requested data. Data is merged with possible gaps ([na](#var_na) values).",
    ),
    "barmerge.lookahead_off": BuiltinVariable(
        name="barmerge.lookahead_off",
        type="const barmerge_lookahead",
        description="Merge strategy for the requested data position. Requested barset is merged with current barset in the order of sorting bars by their close time. This merge strategy disables effect of getting data fro",
    ),
    "barmerge.lookahead_on": BuiltinVariable(
        name="barmerge.lookahead_on",
        type="const barmerge_lookahead",
        description="Merge strategy for the requested data position. Requested barset is merged with current barset in the order of sorting bars by their opening time. This merge strategy can lead to undesirable effect of",
    ),
    "barstate.isconfirmed": BuiltinVariable(
        name="barstate.isconfirmed",
        type="series bool",
        description="Returns true if the script is calculating the last (closing) update of the current bar. The next script calculation will be on the new bar data.",
    ),
    "barstate.isfirst": BuiltinVariable(
        name="barstate.isfirst",
        type="series bool",
        description="Returns true if current bar is first bar in barset, false otherwise.",
    ),
    "barstate.ishistory": BuiltinVariable(
        name="barstate.ishistory",
        type="series bool",
        description="Returns true if current bar is a historical bar, false otherwise.",
    ),
    "barstate.islast": BuiltinVariable(
        name="barstate.islast",
        type="series bool",
        description="Returns true if current bar is the last bar in barset, false otherwise. This condition is true for all real-time bars in barset.",
    ),
    "barstate.islastconfirmedhistory": BuiltinVariable(
        name="barstate.islastconfirmedhistory",
        type="series bool",
        description="Returns true if script is executing on the dataset\\`s last bar when market is closed, or script is executing on the bar immediately preceding the real-time bar, if market is open. Returns false otherw",
    ),
    "barstate.isnew": BuiltinVariable(
        name="barstate.isnew",
        type="series bool",
        description="Returns true if script is currently calculating on new bar, false otherwise. This variable is true when calculating on historical bars or on first update of a newly generated real-time bar.",
    ),
    "barstate.isrealtime": BuiltinVariable(
        name="barstate.isrealtime",
        type="series bool",
        description="Returns true if current bar is a real-time bar, false otherwise.",
    ),
    "bid": BuiltinVariable(name="bid", type="series float", description="Bid price."),
    "box.all": BuiltinVariable(
        name="box.all",
        type="box[]",
        description="Returns an array filled with all the current boxes drawn by the script.",
    ),
    "chart.bg_color": BuiltinVariable(
        name="chart.bg_color",
        type="input color",
        description='Returns the color of the chart\\`s background from the "Chart settings/Appearance/Background" field. When a gradient is selected, the middle point of the gradient is returned.',
    ),
    "chart.fg_color": BuiltinVariable(
        name="chart.fg_color",
        type="input color",
        description="Returns a color providing optimal contrast with [chart.bg_color](#var_chart.bg_color).",
    ),
    "chart.is_heikinashi": BuiltinVariable(
        name="chart.is_heikinashi", type="simple bool", description=""
    ),
    "chart.is_kagi": BuiltinVariable(
        name="chart.is_kagi", type="simple bool", description=""
    ),
    "chart.is_linebreak": BuiltinVariable(
        name="chart.is_linebreak", type="simple bool", description=""
    ),
    "chart.is_pnf": BuiltinVariable(
        name="chart.is_pnf", type="simple bool", description=""
    ),
    "chart.is_range": BuiltinVariable(
        name="chart.is_range", type="simple bool", description=""
    ),
    "chart.is_renko": BuiltinVariable(
        name="chart.is_renko", type="simple bool", description=""
    ),
    "chart.is_standard": BuiltinVariable(
        name="chart.is_standard", type="simple bool", description=""
    ),
    "chart.left_visible_bar_time": BuiltinVariable(
        name="chart.left_visible_bar_time",
        type="input int",
        description="The [time](#var_time) of the leftmost bar currently visible on the chart.",
    ),
    "chart.right_visible_bar_time": BuiltinVariable(
        name="chart.right_visible_bar_time",
        type="input int",
        description="The [time](#var_time) of the rightmost bar currently visible on the chart.",
    ),
    "close": BuiltinVariable(
        name="close",
        type="series float",
        description="Close price of the current bar when it has closed, or last traded price of a yet incomplete, realtime bar.",
    ),
    "color.aqua": BuiltinVariable(
        name="color.aqua",
        type="const color",
        description="Is a named constant for #00BCD4 color.  ",
    ),
    "color.black": BuiltinVariable(
        name="color.black",
        type="const color",
        description="Is a named constant for #363A45 color.  ",
    ),
    "color.blue": BuiltinVariable(
        name="color.blue",
        type="const color",
        description="Is a named constant for #2962ff color.  ",
    ),
    "color.fuchsia": BuiltinVariable(
        name="color.fuchsia",
        type="const color",
        description="Is a named constant for #E040FB color.  ",
    ),
    "color.gray": BuiltinVariable(
        name="color.gray",
        type="const color",
        description="Is a named constant for #787B86 color.  ",
    ),
    "color.green": BuiltinVariable(
        name="color.green",
        type="const color",
        description="Is a named constant for #4CAF50 color.  ",
    ),
    "color.lime": BuiltinVariable(
        name="color.lime",
        type="const color",
        description="Is a named constant for #00E676 color.  ",
    ),
    "color.maroon": BuiltinVariable(
        name="color.maroon",
        type="const color",
        description="Is a named constant for #880E4F color.  ",
    ),
    "color.navy": BuiltinVariable(
        name="color.navy",
        type="const color",
        description="Is a named constant for #311B92 color.  ",
    ),
    "color.olive": BuiltinVariable(
        name="color.olive",
        type="const color",
        description="Is a named constant for #808000 color.  ",
    ),
    "color.orange": BuiltinVariable(
        name="color.orange",
        type="const color",
        description="Is a named constant for #FF9800 color.  ",
    ),
    "color.purple": BuiltinVariable(
        name="color.purple",
        type="const color",
        description="Is a named constant for #9C27B0 color.  ",
    ),
    "color.red": BuiltinVariable(
        name="color.red",
        type="const color",
        description="Is a named constant for #FF5252 color.  ",
    ),
    "color.silver": BuiltinVariable(
        name="color.silver",
        type="const color",
        description="Is a named constant for #B2B5BE color.  ",
    ),
    "color.teal": BuiltinVariable(
        name="color.teal",
        type="const color",
        description="Is a named constant for #00897B color.  ",
    ),
    "color.white": BuiltinVariable(
        name="color.white",
        type="const color",
        description="Is a named constant for #FFFFFF color.  ",
    ),
    "color.yellow": BuiltinVariable(
        name="color.yellow",
        type="const color",
        description="Is a named constant for #FFEB3B color.  ",
    ),
    "currency.AUD": BuiltinVariable(
        name="currency.AUD", type="const string", description="Australian dollar."
    ),
    "currency.BTC": BuiltinVariable(
        name="currency.BTC", type="const string", description="Bitcoin."
    ),
    "currency.CAD": BuiltinVariable(
        name="currency.CAD", type="const string", description="Canadian dollar."
    ),
    "currency.CHF": BuiltinVariable(
        name="currency.CHF", type="const string", description="Swiss franc."
    ),
    "currency.ETH": BuiltinVariable(
        name="currency.ETH", type="const string", description="Ethereum."
    ),
    "currency.EUR": BuiltinVariable(
        name="currency.EUR", type="const string", description="Euro."
    ),
    "currency.GBP": BuiltinVariable(
        name="currency.GBP", type="const string", description="Pound sterling."
    ),
    "currency.HKD": BuiltinVariable(
        name="currency.HKD", type="const string", description="Hong Kong dollar."
    ),
    "currency.INR": BuiltinVariable(
        name="currency.INR", type="const string", description="Indian rupee."
    ),
    "currency.JPY": BuiltinVariable(
        name="currency.JPY", type="const string", description="Japanese yen."
    ),
    "currency.KRW": BuiltinVariable(
        name="currency.KRW", type="const string", description="South Korean won."
    ),
    "currency.MYR": BuiltinVariable(
        name="currency.MYR", type="const string", description="Malaysian ringgit."
    ),
    "currency.NOK": BuiltinVariable(
        name="currency.NOK", type="const string", description="Norwegian krone."
    ),
    "currency.NONE": BuiltinVariable(
        name="currency.NONE", type="const string", description="Unspecified currency."
    ),
    "currency.NZD": BuiltinVariable(
        name="currency.NZD", type="const string", description="New Zealand dollar."
    ),
    "currency.RUB": BuiltinVariable(
        name="currency.RUB", type="const string", description="Russian ruble."
    ),
    "currency.SEK": BuiltinVariable(
        name="currency.SEK", type="const string", description="Swedish krona."
    ),
    "currency.SGD": BuiltinVariable(
        name="currency.SGD", type="const string", description="Singapore dollar."
    ),
    "currency.TRY": BuiltinVariable(
        name="currency.TRY", type="const string", description="Turkish lira."
    ),
    "currency.USD": BuiltinVariable(
        name="currency.USD", type="const string", description="United States dollar."
    ),
    "currency.USDT": BuiltinVariable(
        name="currency.USDT", type="const string", description="Tether."
    ),
    "currency.ZAR": BuiltinVariable(
        name="currency.ZAR", type="const string", description="South African rand."
    ),
    "dayofmonth": BuiltinVariable(
        name="dayofmonth",
        type="series int",
        description="Date of current bar time in exchange timezone.",
    ),
    "dayofweek": BuiltinVariable(
        name="dayofweek",
        type="series int",
        description="Day of week for current bar time in exchange timezone.",
    ),
    "dayofweek.friday": BuiltinVariable(
        name="dayofweek.friday",
        type="const int",
        description="Is a named constant for return value of [dayofweek](#fun_dayofweek) function and value of [dayofweek](#var_dayofweek) variable.",
    ),
    "dayofweek.monday": BuiltinVariable(
        name="dayofweek.monday",
        type="const int",
        description="Is a named constant for return value of [dayofweek](#fun_dayofweek) function and value of [dayofweek](#var_dayofweek) variable.",
    ),
    "dayofweek.saturday": BuiltinVariable(
        name="dayofweek.saturday",
        type="const int",
        description="Is a named constant for return value of [dayofweek](#fun_dayofweek) function and value of [dayofweek](#var_dayofweek) variable.",
    ),
    "dayofweek.sunday": BuiltinVariable(
        name="dayofweek.sunday",
        type="const int",
        description="Is a named constant for return value of [dayofweek](#fun_dayofweek) function and value of [dayofweek](#var_dayofweek) variable.",
    ),
    "dayofweek.thursday": BuiltinVariable(
        name="dayofweek.thursday",
        type="const int",
        description="Is a named constant for return value of [dayofweek](#fun_dayofweek) function and value of [dayofweek](#var_dayofweek) variable.",
    ),
    "dayofweek.tuesday": BuiltinVariable(
        name="dayofweek.tuesday",
        type="const int",
        description="Is a named constant for return value of [dayofweek](#fun_dayofweek) function and value of [dayofweek](#var_dayofweek) variable.",
    ),
    "dayofweek.wednesday": BuiltinVariable(
        name="dayofweek.wednesday",
        type="const int",
        description="Is a named constant for return value of [dayofweek](#fun_dayofweek) function and value of [dayofweek](#var_dayofweek) variable.",
    ),
    "display.all": BuiltinVariable(
        name="display.all",
        type="const plot_simple_display",
        description="A named constant for use with the `display` parameter of `plot*()` and `input*()` functions.  ",
    ),
    "display.data_window": BuiltinVariable(
        name="display.data_window",
        type="const plot_display",
        description="A named constant for use with the `display` parameter of `plot*()` and `input*()` functions.  ",
    ),
    "display.none": BuiltinVariable(
        name="display.none",
        type="const plot_simple_display",
        description="A named constant for use with the `display` parameter of `plot*()` and `input*()` functions. `plot*()` functions using this will not display their plotted values anywhere.  ",
    ),
    "display.pane": BuiltinVariable(
        name="display.pane",
        type="const plot_display",
        description="A named constant for use with the `display` parameter of `plot*()` functions. Displays plotted values in the chart pane used by the script.",
    ),
    "display.price_scale": BuiltinVariable(
        name="display.price_scale",
        type="const plot_display",
        description="A named constant for use with the `display` parameter of `plot*()` functions. Displays the plot\u2019s label and value on the price scale if the chart\\`s settings allow it.",
    ),
    "display.status_line": BuiltinVariable(
        name="display.status_line",
        type="const plot_display",
        description="A named constant for use with the `display` parameter of `plot*()` and `input*()` functions.  ",
    ),
    "dividends.future_amount": BuiltinVariable(
        name="dividends.future_amount",
        type="series float",
        description="Returns the payment amount of the upcoming dividend in the currency of the current instrument, or [na](#var_na) if this data isn't available.",
    ),
    "dividends.future_ex_date": BuiltinVariable(
        name="dividends.future_ex_date",
        type="series int",
        description="Returns the Ex-dividend date (Ex-date) of the current instrument's next dividend payment, or [na](#var_na) if this data isn't available. Ex-dividend date signifies when investors are no longer entitle",
    ),
    "dividends.future_pay_date": BuiltinVariable(
        name="dividends.future_pay_date",
        type="series int",
        description="Returns the Payment date (Pay date) of the current instrument's next dividend payment, or [na](#var_na) if this data isn't available. Payment date signifies the day when eligible investors will receiv",
    ),
    "dividends.gross": BuiltinVariable(
        name="dividends.gross",
        type="const string",
        description="A named constant for the [request.dividends](#fun_request.dividends) function.  ",
    ),
    "dividends.net": BuiltinVariable(
        name="dividends.net",
        type="const string",
        description="A named constant for the [request.dividends](#fun_request.dividends) function.  ",
    ),
    "earnings.actual": BuiltinVariable(
        name="earnings.actual",
        type="const string",
        description="A named constant for the [request.earnings](#fun_request.earnings) function.  ",
    ),
    "earnings.estimate": BuiltinVariable(
        name="earnings.estimate",
        type="const string",
        description="A named constant for the [request.earnings](#fun_request.earnings) function.  ",
    ),
    "earnings.future_eps": BuiltinVariable(
        name="earnings.future_eps",
        type="series float",
        description="Returns the estimated Earnings per Share of the next earnings report in the currency of the instrument, or [na](#var_na) if this data isn't available.",
    ),
    "earnings.future_period_end_time": BuiltinVariable(
        name="earnings.future_period_end_time",
        type="series float",
        description="Checks the data for the next earnings report and returns the UNIX timestamp of the day when the financial period covered by those earnings ends, or [na](#var_na) if this data isn't available.",
    ),
    "earnings.future_revenue": BuiltinVariable(
        name="earnings.future_revenue",
        type="series float",
        description="Returns the estimated Revenue of the next earnings report in the currency of the instrument, or [na](#var_na) if this data isn't available.",
    ),
    "earnings.future_time": BuiltinVariable(
        name="earnings.future_time",
        type="series float",
        description="Returns a UNIX timestamp indicating the expected time of the next earnings report, or [na](#var_na) if this data isn't available.",
    ),
    "earnings.standardized": BuiltinVariable(
        name="earnings.standardized",
        type="const string",
        description="A named constant for the [request.earnings](#fun_request.earnings) function.  ",
    ),
    "extend.both": BuiltinVariable(
        name="extend.both",
        type="const string",
        description="A named constant for [line.new](#fun_line.new) and [line.set_extend](#fun_line.set_extend) functions.",
    ),
    "extend.left": BuiltinVariable(
        name="extend.left",
        type="const string",
        description="A named constant for [line.new](#fun_line.new) and [line.set_extend](#fun_line.set_extend) functions.",
    ),
    "extend.none": BuiltinVariable(
        name="extend.none",
        type="const string",
        description="A named constant for [line.new](#fun_line.new) and [line.set_extend](#fun_line.set_extend) functions.",
    ),
    "extend.right": BuiltinVariable(
        name="extend.right",
        type="const string",
        description="A named constant for [line.new](#fun_line.new) and [line.set_extend](#fun_line.set_extend) functions.",
    ),
    "font.family_default": BuiltinVariable(
        name="font.family_default",
        type="const string",
        description="Default text font for [box.new](#fun_box.new), [box.set_text_font_family](#fun_box.set_text_font_family), [label.new](#fun_label.new), [label.set_text_font_family](#fun_label.set_text_font_family), [t",
    ),
    "font.family_monospace": BuiltinVariable(
        name="font.family_monospace",
        type="const string",
        description="Monospace text font for [box.new](#fun_box.new), [box.set_text_font_family](#fun_box.set_text_font_family), [label.new](#fun_label.new), [label.set_text_font_family](#fun_label.set_text_font_family), ",
    ),
    "format.inherit": BuiltinVariable(
        name="format.inherit",
        type="const string",
        description="Is a named constant for selecting the formatting of the script output values from the parent series in the [indicator](#fun_indicator) function.",
    ),
    "format.mintick": BuiltinVariable(
        name="format.mintick",
        type="const string",
        description="Is a named constant to use with the [str.tostring](#fun_str.tostring) function.  ",
    ),
    "format.percent": BuiltinVariable(
        name="format.percent",
        type="const string",
        description="Is a named constant for selecting the formatting of the script output values as a percentage in the indicator function. It adds a percent sign after values.",
    ),
    "format.price": BuiltinVariable(
        name="format.price",
        type="const string",
        description="Is a named constant for selecting the formatting of the script output values as prices in the [indicator](#fun_indicator) function.",
    ),
    "format.volume": BuiltinVariable(
        name="format.volume",
        type="const string",
        description="Is a named constant for selecting the formatting of the script output values as volume in the [indicator](#fun_indicator) function, e.g. '5183' will be formatted as '5.183K'.",
    ),
    "high": BuiltinVariable(
        name="high", type="series float", description="Current high price."
    ),
    "hl2": BuiltinVariable(
        name="hl2", type="series float", description="Is a shortcut for (high + low)/2"
    ),
    "hlc3": BuiltinVariable(
        name="hlc3",
        type="series float",
        description="Is a shortcut for (high + low + close)/3",
    ),
    "hlcc4": BuiltinVariable(
        name="hlcc4",
        type="series float",
        description="Is a shortcut for (high + low + close + close)/4",
    ),
    "hline.style_dashed": BuiltinVariable(
        name="hline.style_dashed",
        type="const hline_style",
        description="Is a named constant for dashed linestyle of [hline](#fun_hline) function.",
    ),
    "hline.style_dotted": BuiltinVariable(
        name="hline.style_dotted",
        type="const hline_style",
        description="Is a named constant for dotted linestyle of [hline](#fun_hline) function.",
    ),
    "hline.style_solid": BuiltinVariable(
        name="hline.style_solid",
        type="const hline_style",
        description="Is a named constant for solid linestyle of [hline](#fun_hline) function.",
    ),
    "hour": BuiltinVariable(
        name="hour",
        type="series int",
        description="Current bar hour in exchange timezone.",
    ),
    "label.all": BuiltinVariable(
        name="label.all",
        type="label[]",
        description="Returns an array filled with all the current labels drawn by the script.",
    ),
    "label.style_arrowdown": BuiltinVariable(
        name="label.style_arrowdown",
        type="const string",
        description="Label style for [label.new](#fun_label.new) and [label.set_style](#fun_label.set_style) functions.",
    ),
    "label.style_arrowup": BuiltinVariable(
        name="label.style_arrowup",
        type="const string",
        description="Label style for [label.new](#fun_label.new) and [label.set_style](#fun_label.set_style) functions.",
    ),
    "label.style_circle": BuiltinVariable(
        name="label.style_circle",
        type="const string",
        description="Label style for [label.new](#fun_label.new) and [label.set_style](#fun_label.set_style) functions.",
    ),
    "label.style_cross": BuiltinVariable(
        name="label.style_cross",
        type="const string",
        description="Label style for [label.new](#fun_label.new) and [label.set_style](#fun_label.set_style) functions.",
    ),
    "label.style_diamond": BuiltinVariable(
        name="label.style_diamond",
        type="const string",
        description="Label style for [label.new](#fun_label.new) and [label.set_style](#fun_label.set_style) functions.",
    ),
    "label.style_flag": BuiltinVariable(
        name="label.style_flag",
        type="const string",
        description="Label style for [label.new](#fun_label.new) and [label.set_style](#fun_label.set_style) functions.",
    ),
    "label.style_label_center": BuiltinVariable(
        name="label.style_label_center",
        type="const string",
        description="Label style for [label.new](#fun_label.new) and [label.set_style](#fun_label.set_style) functions.",
    ),
    "label.style_label_down": BuiltinVariable(
        name="label.style_label_down",
        type="const string",
        description="Label style for [label.new](#fun_label.new) and [label.set_style](#fun_label.set_style) functions.",
    ),
    "label.style_label_left": BuiltinVariable(
        name="label.style_label_left",
        type="const string",
        description="Label style for [label.new](#fun_label.new) and [label.set_style](#fun_label.set_style) functions.",
    ),
    "label.style_label_lower_left": BuiltinVariable(
        name="label.style_label_lower_left",
        type="const string",
        description="Label style for [label.new](#fun_label.new) and [label.set_style](#fun_label.set_style) functions.",
    ),
    "label.style_label_lower_right": BuiltinVariable(
        name="label.style_label_lower_right",
        type="const string",
        description="Label style for [label.new](#fun_label.new) and [label.set_style](#fun_label.set_style) functions.",
    ),
    "label.style_label_right": BuiltinVariable(
        name="label.style_label_right",
        type="const string",
        description="Label style for [label.new](#fun_label.new) and [label.set_style](#fun_label.set_style) functions.",
    ),
    "label.style_label_up": BuiltinVariable(
        name="label.style_label_up",
        type="const string",
        description="Label style for [label.new](#fun_label.new) and [label.set_style](#fun_label.set_style) functions.",
    ),
    "label.style_label_upper_left": BuiltinVariable(
        name="label.style_label_upper_left",
        type="const string",
        description="Label style for [label.new](#fun_label.new) and [label.set_style](#fun_label.set_style) functions.",
    ),
    "label.style_label_upper_right": BuiltinVariable(
        name="label.style_label_upper_right",
        type="const string",
        description="Label style for [label.new](#fun_label.new) and [label.set_style](#fun_label.set_style) functions.",
    ),
    "label.style_none": BuiltinVariable(
        name="label.style_none",
        type="const string",
        description="Label style for [label.new](#fun_label.new) and [label.set_style](#fun_label.set_style) functions.",
    ),
    "label.style_square": BuiltinVariable(
        name="label.style_square",
        type="const string",
        description="Label style for [label.new](#fun_label.new) and [label.set_style](#fun_label.set_style) functions.",
    ),
    "label.style_text_outline": BuiltinVariable(
        name="label.style_text_outline",
        type="const string",
        description="Label style for [label.new](#fun_label.new) and [label.set_style](#fun_label.set_style) functions.",
    ),
    "label.style_triangledown": BuiltinVariable(
        name="label.style_triangledown",
        type="const string",
        description="Label style for [label.new](#fun_label.new) and [label.set_style](#fun_label.set_style) functions.",
    ),
    "label.style_triangleup": BuiltinVariable(
        name="label.style_triangleup",
        type="const string",
        description="Label style for [label.new](#fun_label.new) and [label.set_style](#fun_label.set_style) functions.",
    ),
    "label.style_xcross": BuiltinVariable(
        name="label.style_xcross",
        type="const string",
        description="Label style for [label.new](#fun_label.new) and [label.set_style](#fun_label.set_style) functions.",
    ),
    "last_bar_index": BuiltinVariable(
        name="last_bar_index",
        type="series int",
        description="Bar index of the last chart bar. Bar indices begin at zero on the first bar.",
    ),
    "last_bar_time": BuiltinVariable(
        name="last_bar_time",
        type="series int",
        description="Time in UNIX format of the last chart bar. It is the number of milliseconds that have elapsed since 00:00:00 UTC, 1 January 1970.",
    ),
    "line.all": BuiltinVariable(
        name="line.all",
        type="line[]",
        description="Returns an array filled with all the current lines drawn by the script.",
    ),
    "line.style_arrow_both": BuiltinVariable(
        name="line.style_arrow_both",
        type="const string",
        description="Line style for [line.new](#fun_line.new) and [line.set_style](#fun_line.set_style) functions.  ",
    ),
    "line.style_arrow_left": BuiltinVariable(
        name="line.style_arrow_left",
        type="const string",
        description="Line style for [line.new](#fun_line.new) and [line.set_style](#fun_line.set_style) functions.  ",
    ),
    "line.style_arrow_right": BuiltinVariable(
        name="line.style_arrow_right",
        type="const string",
        description="Line style for [line.new](#fun_line.new) and [line.set_style](#fun_line.set_style) functions.  ",
    ),
    "line.style_dashed": BuiltinVariable(
        name="line.style_dashed",
        type="const string",
        description="Line style for [line.new](#fun_line.new) and [line.set_style](#fun_line.set_style) functions.",
    ),
    "line.style_dotted": BuiltinVariable(
        name="line.style_dotted",
        type="const string",
        description="Line style for [line.new](#fun_line.new) and [line.set_style](#fun_line.set_style) functions.",
    ),
    "line.style_solid": BuiltinVariable(
        name="line.style_solid",
        type="const string",
        description="Line style for [line.new](#fun_line.new) and [line.set_style](#fun_line.set_style) functions.",
    ),
    "linefill.all": BuiltinVariable(
        name="linefill.all",
        type="linefill[]",
        description="Returns an array filled with all the current linefill objects drawn by the script.",
    ),
    "location.abovebar": BuiltinVariable(
        name="location.abovebar",
        type="const string",
        description="Location value for [plotshape](#fun_plotshape), [plotchar](#fun_plotchar) functions.  ",
    ),
    "location.absolute": BuiltinVariable(
        name="location.absolute",
        type="const string",
        description="Location value for [plotshape](#fun_plotshape), [plotchar](#fun_plotchar) functions.  ",
    ),
    "location.belowbar": BuiltinVariable(
        name="location.belowbar",
        type="const string",
        description="Location value for [plotshape](#fun_plotshape), [plotchar](#fun_plotchar) functions.  ",
    ),
    "location.bottom": BuiltinVariable(
        name="location.bottom",
        type="const string",
        description="Location value for [plotshape](#fun_plotshape), [plotchar](#fun_plotchar) functions.  ",
    ),
    "location.top": BuiltinVariable(
        name="location.top",
        type="const string",
        description="Location value for [plotshape](#fun_plotshape), [plotchar](#fun_plotchar) functions.  ",
    ),
    "low": BuiltinVariable(
        name="low", type="series float", description="Current low price."
    ),
    "math.e": BuiltinVariable(
        name="math.e",
        type="const float",
        description="Is a named constant for [Euler\\`s number](https://en.wikipedia.org/wiki/E_(mathematical_constant)).  ",
    ),
    "math.phi": BuiltinVariable(
        name="math.phi",
        type="const float",
        description="Is a named constant for the [golden ratio](https://en.wikipedia.org/wiki/Golden_ratio).  ",
    ),
    "math.pi": BuiltinVariable(
        name="math.pi",
        type="const float",
        description="Is a named constant for [Archimedes' constant](https://en.wikipedia.org/wiki/Pi).  ",
    ),
    "math.rphi": BuiltinVariable(
        name="math.rphi",
        type="const float",
        description="Is a named constant for the [golden ratio conjugate](https://en.wikipedia.org/wiki/Golden_ratio#Golden_ratio_conjugate).  ",
    ),
    "minute": BuiltinVariable(
        name="minute",
        type="series int",
        description="Current bar minute in exchange timezone.",
    ),
    "month": BuiltinVariable(
        name="month",
        type="series int",
        description="Current bar month in exchange timezone.",
    ),
    "na": BuiltinVariable(
        name="na",
        type="null",
        description='A keyword signifying "not available", indicating that a variable has no assigned value.',
    ),
    "ohlc4": BuiltinVariable(
        name="ohlc4",
        type="series float",
        description="Is a shortcut for (open + high + low + close)/4",
    ),
    "open": BuiltinVariable(
        name="open", type="series float", description="Current open price."
    ),
    "order.ascending": BuiltinVariable(
        name="order.ascending",
        type="const sort_order",
        description="Determines the sort order of the array from the smallest to the largest value.",
    ),
    "order.descending": BuiltinVariable(
        name="order.descending",
        type="const sort_order",
        description="Determines the sort order of the array from the largest to the smallest value.",
    ),
    "plot.style_area": BuiltinVariable(
        name="plot.style_area",
        type="const plot_style",
        description="A named constant for the 'Area' style, to be used as an argument for the `style` parameter in the [plot](#fun_plot) function.",
    ),
    "plot.style_areabr": BuiltinVariable(
        name="plot.style_areabr",
        type="const plot_style",
        description="A named constant for the 'Area With Breaks' style, to be used as an argument for the `style` parameter in the [plot](#fun_plot) function.  ",
    ),
    "plot.style_circles": BuiltinVariable(
        name="plot.style_circles",
        type="const plot_style",
        description="A named constant for the 'Circles' style, to be used as an argument for the `style` parameter in the [plot](#fun_plot) function.",
    ),
    "plot.style_columns": BuiltinVariable(
        name="plot.style_columns",
        type="const plot_style",
        description="A named constant for the 'Columns' style, to be used as an argument for the `style` parameter in the [plot](#fun_plot) function.",
    ),
    "plot.style_cross": BuiltinVariable(
        name="plot.style_cross",
        type="const plot_style",
        description="A named constant for the 'Cross' style, to be used as an argument for the `style` parameter in the [plot](#fun_plot) function.",
    ),
    "plot.style_histogram": BuiltinVariable(
        name="plot.style_histogram",
        type="const plot_style",
        description="A named constant for the 'Histogram' style, to be used as an argument for the `style` parameter in the [plot](#fun_plot) function.",
    ),
    "plot.style_line": BuiltinVariable(
        name="plot.style_line",
        type="const plot_style",
        description="A named constant for the 'Line' style, to be used as an argument for the `style` parameter in the [plot](#fun_plot) function.",
    ),
    "plot.style_linebr": BuiltinVariable(
        name="plot.style_linebr",
        type="const plot_style",
        description="A named constant for the 'Line With Breaks' style, to be used as an argument for the `style` parameter in the [plot](#fun_plot) function.  ",
    ),
    "plot.style_stepline": BuiltinVariable(
        name="plot.style_stepline",
        type="const plot_style",
        description="A named constant for the 'Step Line' style, to be used as an argument for the `style` parameter in the [plot](#fun_plot) function.",
    ),
    "plot.style_stepline_diamond": BuiltinVariable(
        name="plot.style_stepline_diamond",
        type="const plot_style",
        description="A named constant for the 'Step Line With Diamonds' style, to be used as an argument for the `style` parameter in the [plot](#fun_plot) function.  ",
    ),
    "plot.style_steplinebr": BuiltinVariable(
        name="plot.style_steplinebr",
        type="const plot_style",
        description="A named constant for the 'Step line with Breaks' style, to be used as an argument for the `style` parameter in the [plot](#fun_plot) function.",
    ),
    "polyline.all": BuiltinVariable(
        name="polyline.all",
        type="polyline[]",
        description="Returns an array containing all current [polyline](#op_polyline) instances drawn by the script.",
    ),
    "position.bottom_center": BuiltinVariable(
        name="position.bottom_center",
        type="const string",
        description="Table position is used in [table.new](#fun_table.new), [table.cell](#fun_table.cell) functions.",
    ),
    "position.bottom_left": BuiltinVariable(
        name="position.bottom_left",
        type="const string",
        description="Table position is used in [table.new](#fun_table.new), [table.cell](#fun_table.cell) functions.",
    ),
    "position.bottom_right": BuiltinVariable(
        name="position.bottom_right",
        type="const string",
        description="Table position is used in [table.new](#fun_table.new), [table.cell](#fun_table.cell) functions.",
    ),
    "position.middle_center": BuiltinVariable(
        name="position.middle_center",
        type="const string",
        description="Table position is used in [table.new](#fun_table.new), [table.cell](#fun_table.cell) functions.",
    ),
    "position.middle_left": BuiltinVariable(
        name="position.middle_left",
        type="const string",
        description="Table position is used in [table.new](#fun_table.new), [table.cell](#fun_table.cell) functions.",
    ),
    "position.middle_right": BuiltinVariable(
        name="position.middle_right",
        type="const string",
        description="Table position is used in [table.new](#fun_table.new), [table.cell](#fun_table.cell) functions.",
    ),
    "position.top_center": BuiltinVariable(
        name="position.top_center",
        type="const string",
        description="Table position is used in [table.new](#fun_table.new), [table.cell](#fun_table.cell) functions.",
    ),
    "position.top_left": BuiltinVariable(
        name="position.top_left",
        type="const string",
        description="Table position is used in [table.new](#fun_table.new), [table.cell](#fun_table.cell) functions.",
    ),
    "position.top_right": BuiltinVariable(
        name="position.top_right",
        type="const string",
        description="Table position is used in [table.new](#fun_table.new), [table.cell](#fun_table.cell) functions.",
    ),
    "scale.left": BuiltinVariable(
        name="scale.left",
        type="const scale_type",
        description="Scale value for [indicator](#fun_indicator) function.  ",
    ),
    "scale.none": BuiltinVariable(
        name="scale.none",
        type="const scale_type",
        description="Scale value for [indicator](#fun_indicator) function.  ",
    ),
    "scale.right": BuiltinVariable(
        name="scale.right",
        type="const scale_type",
        description="Scale value for [indicator](#fun_indicator) function.  ",
    ),
    "second": BuiltinVariable(
        name="second",
        type="series int",
        description="Current bar second in exchange timezone.",
    ),
    "session.extended": BuiltinVariable(
        name="session.extended",
        type="const string",
        description="Constant for extended session type (with extended hours data).",
    ),
    "session.isfirstbar": BuiltinVariable(
        name="session.isfirstbar",
        type="series bool",
        description="Returns [true](#op_true) if the current bar is the first bar of the day\\`s session, `false` otherwise.  ",
    ),
    "session.isfirstbar_regular": BuiltinVariable(
        name="session.isfirstbar_regular",
        type="series bool",
        description="Returns [true](#op_true) on the first regular session bar of the day, `false` otherwise.  ",
    ),
    "session.islastbar": BuiltinVariable(
        name="session.islastbar",
        type="series bool",
        description="Returns [true](#op_true) if the current bar is the last bar of the day\\`s session, `false` otherwise.  ",
    ),
    "session.islastbar_regular": BuiltinVariable(
        name="session.islastbar_regular",
        type="series bool",
        description="Returns [true](#op_true) on the last regular session bar of the day, `false` otherwise.  ",
    ),
    "session.ismarket": BuiltinVariable(
        name="session.ismarket",
        type="series bool",
        description="Returns true if the current bar is a part of the regular trading hours (i.e. market hours), false otherwise",
    ),
    "session.ispostmarket": BuiltinVariable(
        name="session.ispostmarket",
        type="series bool",
        description="Returns true if the current bar is a part of the post-market, false otherwise. On non-intraday charts always returns false.",
    ),
    "session.ispremarket": BuiltinVariable(
        name="session.ispremarket",
        type="series bool",
        description="Returns true if the current bar is a part of the pre-market, false otherwise. On non-intraday charts always returns false.",
    ),
    "session.regular": BuiltinVariable(
        name="session.regular",
        type="const string",
        description="Constant for regular session type (no extended hours data).",
    ),
    "shape.arrowdown": BuiltinVariable(
        name="shape.arrowdown",
        type="const string",
        description="Shape style for [plotshape](#fun_plotshape) function.",
    ),
    "shape.arrowup": BuiltinVariable(
        name="shape.arrowup",
        type="const string",
        description="Shape style for [plotshape](#fun_plotshape) function.",
    ),
    "shape.circle": BuiltinVariable(
        name="shape.circle",
        type="const string",
        description="Shape style for [plotshape](#fun_plotshape) function.",
    ),
    "shape.cross": BuiltinVariable(
        name="shape.cross",
        type="const string",
        description="Shape style for [plotshape](#fun_plotshape) function.",
    ),
    "shape.diamond": BuiltinVariable(
        name="shape.diamond",
        type="const string",
        description="Shape style for [plotshape](#fun_plotshape) function.",
    ),
    "shape.flag": BuiltinVariable(
        name="shape.flag",
        type="const string",
        description="Shape style for [plotshape](#fun_plotshape) function.",
    ),
    "shape.labeldown": BuiltinVariable(
        name="shape.labeldown",
        type="const string",
        description="Shape style for [plotshape](#fun_plotshape) function.",
    ),
    "shape.labelup": BuiltinVariable(
        name="shape.labelup",
        type="const string",
        description="Shape style for [plotshape](#fun_plotshape) function.",
    ),
    "shape.square": BuiltinVariable(
        name="shape.square",
        type="const string",
        description="Shape style for [plotshape](#fun_plotshape) function.",
    ),
    "shape.triangledown": BuiltinVariable(
        name="shape.triangledown",
        type="const string",
        description="Shape style for [plotshape](#fun_plotshape) function.",
    ),
    "shape.triangleup": BuiltinVariable(
        name="shape.triangleup",
        type="const string",
        description="Shape style for [plotshape](#fun_plotshape) function.",
    ),
    "shape.xcross": BuiltinVariable(
        name="shape.xcross",
        type="const string",
        description="Shape style for [plotshape](#fun_plotshape) function.",
    ),
    "size.auto": BuiltinVariable(
        name="size.auto",
        type="const string",
        description="Size value for [plotshape](#fun_plotshape), [plotchar](#fun_plotchar) functions.  ",
    ),
    "size.huge": BuiltinVariable(
        name="size.huge",
        type="const string",
        description="Size value for [plotshape](#fun_plotshape), [plotchar](#fun_plotchar) functions.  ",
    ),
    "size.large": BuiltinVariable(
        name="size.large",
        type="const string",
        description="Size value for [plotshape](#fun_plotshape), [plotchar](#fun_plotchar) functions.  ",
    ),
    "size.normal": BuiltinVariable(
        name="size.normal",
        type="const string",
        description="Size value for [plotshape](#fun_plotshape), [plotchar](#fun_plotchar) functions.  ",
    ),
    "size.small": BuiltinVariable(
        name="size.small",
        type="const string",
        description="Size value for [plotshape](#fun_plotshape), [plotchar](#fun_plotchar) functions.  ",
    ),
    "size.tiny": BuiltinVariable(
        name="size.tiny",
        type="const string",
        description="Size value for [plotshape](#fun_plotshape), [plotchar](#fun_plotchar) functions.  ",
    ),
    "splits.denominator": BuiltinVariable(
        name="splits.denominator",
        type="const string",
        description="A named constant for the [request.splits](#fun_request.splits) function.  ",
    ),
    "splits.numerator": BuiltinVariable(
        name="splits.numerator",
        type="const string",
        description="A named constant for the [request.splits](#fun_request.splits) function.  ",
    ),
    "strategy.account_currency": BuiltinVariable(
        name="strategy.account_currency",
        type="simple string",
        description="Returns the currency used to calculate results, which can be set in the strategy\\`s properties.",
    ),
    "strategy.cash": BuiltinVariable(
        name="strategy.cash",
        type="const string",
        description="This is one of the arguments that can be supplied to the `default_qty_type` parameter in the [strategy](#fun_strategy) declaration statement.  ",
    ),
    "strategy.closedtrades": BuiltinVariable(
        name="strategy.closedtrades",
        type="series int",
        description="Number of trades, which were closed for the whole trading interval.",
    ),
    "strategy.commission.cash_per_contract": BuiltinVariable(
        name="strategy.commission.cash_per_contract",
        type="const string",
        description="Commission type for an order. Money displayed in the account currency per contract.",
    ),
    "strategy.commission.cash_per_order": BuiltinVariable(
        name="strategy.commission.cash_per_order",
        type="const string",
        description="Commission type for an order. Money displayed in the account currency per order.",
    ),
    "strategy.commission.percent": BuiltinVariable(
        name="strategy.commission.percent",
        type="const string",
        description="Commission type for an order. A percentage of the cash volume of order.",
    ),
    "strategy.direction.all": BuiltinVariable(
        name="strategy.direction.all",
        type="const string",
        description="It allows strategy to open both long and short positions.",
    ),
    "strategy.direction.long": BuiltinVariable(
        name="strategy.direction.long",
        type="const string",
        description="It allows strategy to open only long positions.",
    ),
    "strategy.direction.short": BuiltinVariable(
        name="strategy.direction.short",
        type="const string",
        description="It allows strategy to open only short positions.",
    ),
    "strategy.equity": BuiltinVariable(
        name="strategy.equity",
        type="series float",
        description="Current equity ([strategy.initial_capital](#var_strategy.initial_capital) + [strategy.netprofit](#var_strategy.netprofit) + [strategy.openprofit](#var_strategy.openprofit)).",
    ),
    "strategy.eventrades": BuiltinVariable(
        name="strategy.eventrades",
        type="series int",
        description="Number of breakeven trades for the whole trading interval.",
    ),
    "strategy.fixed": BuiltinVariable(
        name="strategy.fixed",
        type="const string",
        description="This is one of the arguments that can be supplied to the `default_qty_type` parameter in the [strategy](#fun_strategy) declaration statement.  ",
    ),
    "strategy.grossloss": BuiltinVariable(
        name="strategy.grossloss",
        type="series float",
        description="Total currency value of all completed losing trades.",
    ),
    "strategy.grossloss_percent": BuiltinVariable(
        name="strategy.grossloss_percent",
        type="series float",
        description="The total value of all completed losing trades, expressed as a percentage of the initial capital.",
    ),
    "strategy.grossprofit": BuiltinVariable(
        name="strategy.grossprofit",
        type="series float",
        description="Total currency value of all completed winning trades.",
    ),
    "strategy.grossprofit_percent": BuiltinVariable(
        name="strategy.grossprofit_percent",
        type="series float",
        description="The total currency value of all completed winning trades, expressed as a percentage of the initial capital.",
    ),
    "strategy.initial_capital": BuiltinVariable(
        name="strategy.initial_capital",
        type="series float",
        description="The amount of initial capital set in the strategy properties.",
    ),
    "strategy.long": BuiltinVariable(
        name="strategy.long",
        type="const strategy_direction",
        description="Long position entry.",
    ),
    "strategy.losstrades": BuiltinVariable(
        name="strategy.losstrades",
        type="series int",
        description="Number of unprofitable trades for the whole trading interval.",
    ),
    "strategy.margin_liquidation_price": BuiltinVariable(
        name="strategy.margin_liquidation_price",
        type="series float",
        description="When margin is used in a strategy, returns the price point where a simulated margin call will occur and liquidate enough of the position to meet the margin requirements.",
    ),
    "strategy.max_contracts_held_all": BuiltinVariable(
        name="strategy.max_contracts_held_all",
        type="series float",
        description="Maximum number of contracts/shares/lots/units in one trade for the whole trading interval.",
    ),
    "strategy.max_contracts_held_long": BuiltinVariable(
        name="strategy.max_contracts_held_long",
        type="series float",
        description="Maximum number of contracts/shares/lots/units in one long trade for the whole trading interval.",
    ),
    "strategy.max_contracts_held_short": BuiltinVariable(
        name="strategy.max_contracts_held_short",
        type="series float",
        description="Maximum number of contracts/shares/lots/units in one short trade for the whole trading interval.",
    ),
    "strategy.max_drawdown": BuiltinVariable(
        name="strategy.max_drawdown",
        type="series float",
        description="Maximum equity drawdown value for the whole trading interval.",
    ),
    "strategy.max_drawdown_percent": BuiltinVariable(
        name="strategy.max_drawdown_percent",
        type="series float",
        description="The maximum equity drawdown value for the whole trading interval, expressed as a percentage and calculated by formula: `Lowest Value During Trade / (Entry Price x Quantity) * 100`.",
    ),
    "strategy.max_runup": BuiltinVariable(
        name="strategy.max_runup",
        type="series float",
        description="Maximum equity run-up value for the whole trading interval.",
    ),
    "strategy.max_runup_percent": BuiltinVariable(
        name="strategy.max_runup_percent",
        type="series float",
        description="The maximum equity run-up value for the whole trading interval, expressed as a percentage and calculated by formula: `Highest Value During Trade / (Entry Price x Quantity) * 100`.",
    ),
    "strategy.netprofit": BuiltinVariable(
        name="strategy.netprofit",
        type="series float",
        description="Total currency value of all completed trades.",
    ),
    "strategy.netprofit_percent": BuiltinVariable(
        name="strategy.netprofit_percent",
        type="series float",
        description="The total value of all completed trades, expressed as a percentage of the initial capital.",
    ),
    "strategy.oca.cancel": BuiltinVariable(
        name="strategy.oca.cancel",
        type="const string",
        description="OCA type value for strategy\\`s functions. The parameter determines that an order should belong to an OCO group, where as soon as an order is filled, all other orders of the same group are cancelled. N",
    ),
    "strategy.oca.none": BuiltinVariable(
        name="strategy.oca.none",
        type="const string",
        description="OCA type value for strategy\\`s functions. The parameter determines that an order should not belong to any particular OCO group.",
    ),
    "strategy.oca.reduce": BuiltinVariable(
        name="strategy.oca.reduce",
        type="const string",
        description="OCA type value for strategy\\`s functions. The parameter determines that an order should belong to an OCO group, where if X number of contracts of an order is filled, number of contracts for each other",
    ),
    "strategy.openprofit": BuiltinVariable(
        name="strategy.openprofit",
        type="series float",
        description="Current unrealized profit or loss for all open positions.",
    ),
    "strategy.openprofit_percent": BuiltinVariable(
        name="strategy.openprofit_percent",
        type="series float",
        description="The current unrealized profit or loss for all open positions, expressed as a percentage and calculated by formula: `openPL / realizedEquity * 100`.",
    ),
    "strategy.opentrades": BuiltinVariable(
        name="strategy.opentrades",
        type="series int",
        description="Number of market position entries, which were not closed and remain opened. If there is no open market position, 0 is returned.",
    ),
    "strategy.percent_of_equity": BuiltinVariable(
        name="strategy.percent_of_equity",
        type="const string",
        description="This is one of the arguments that can be supplied to the `default_qty_type` parameter in the [strategy](#fun_strategy) declaration statement.  ",
    ),
    "strategy.position_avg_price": BuiltinVariable(
        name="strategy.position_avg_price",
        type="series float",
        description="Average entry price of current market position. If the market position is flat, 'NaN' is returned.",
    ),
    "strategy.position_entry_name": BuiltinVariable(
        name="strategy.position_entry_name",
        type="series string",
        description="Name of the order that initially opened current market position.",
    ),
    "strategy.position_size": BuiltinVariable(
        name="strategy.position_size",
        type="series float",
        description="Direction and size of the current market position. If the value is > 0, the market position is long. If the value is < 0, the market position is short. The absolute value is the number of contracts/sh",
    ),
    "strategy.short": BuiltinVariable(
        name="strategy.short",
        type="const strategy_direction",
        description="Short position entry.",
    ),
    "strategy.wintrades": BuiltinVariable(
        name="strategy.wintrades",
        type="series int",
        description="Number of profitable trades for the whole trading interval.",
    ),
    "syminfo.basecurrency": BuiltinVariable(
        name="syminfo.basecurrency",
        type="simple string",
        description="Base currency for the symbol. For the symbol 'BTCUSD' returns 'BTC'.",
    ),
    "syminfo.country": BuiltinVariable(
        name="syminfo.country",
        type="simple string",
        description="Returns the two-letter code of the country where the symbol is traded, in the [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format, or [na](#var_na) if the exchange is not dir",
    ),
    "syminfo.currency": BuiltinVariable(
        name="syminfo.currency",
        type="simple string",
        description="Currency for the current symbol. Returns currency code: 'USD', 'EUR', etc.",
    ),
    "syminfo.current_contract": BuiltinVariable(
        name="syminfo.current_contract",
        type="series string",
        description="Current contract.",
    ),
    "syminfo.description": BuiltinVariable(
        name="syminfo.description",
        type="simple string",
        description="Description for the current symbol.",
    ),
    "syminfo.employees": BuiltinVariable(
        name="syminfo.employees",
        type="simple int",
        description="The number of employees the company has.",
    ),
    "syminfo.expiration_date": BuiltinVariable(
        name="syminfo.expiration_date",
        type="series int",
        description="Expiration date.",
    ),
    "syminfo.industry": BuiltinVariable(
        name="syminfo.industry",
        type="simple string",
        description="Returns the industry of the symbol, or [na](#var_na) if the symbol has no industry.  ",
    ),
    "syminfo.main_tickerid": BuiltinVariable(
        name="syminfo.main_tickerid",
        type="simple string",
        description="Main ticker ID.",
    ),
    "syminfo.mincontract": BuiltinVariable(
        name="syminfo.mincontract", type="simple float", description="Min contract."
    ),
    "syminfo.minmove": BuiltinVariable(
        name="syminfo.minmove",
        type="simple int",
        description="Returns a whole number used to calculate the smallest increment between a symbol\\`s price movements ([syminfo.mintick](#var_syminfo.mintick)).  ",
    ),
    "syminfo.mintick": BuiltinVariable(
        name="syminfo.mintick",
        type="simple float",
        description="Min tick value for the current symbol.",
    ),
    "syminfo.pointvalue": BuiltinVariable(
        name="syminfo.pointvalue",
        type="simple float",
        description="Point value for the current symbol.",
    ),
    "syminfo.prefix": BuiltinVariable(
        name="syminfo.prefix",
        type="simple string",
        description="Prefix of current symbol name (i.e. for 'CME_EOD:TICKER' prefix is 'CME_EOD').",
    ),
    "syminfo.pricescale": BuiltinVariable(
        name="syminfo.pricescale",
        type="simple int",
        description="Returns a whole number used to calculate the smallest increment between a symbol\\`s price movements ([syminfo.mintick](#var_syminfo.mintick)).  ",
    ),
    "syminfo.recommendations_buy": BuiltinVariable(
        name="syminfo.recommendations_buy",
        type="series int",
        description='The number of analysts who gave the current symbol a "Buy" rating.',
    ),
    "syminfo.recommendations_buy_strong": BuiltinVariable(
        name="syminfo.recommendations_buy_strong",
        type="series int",
        description='The number of analysts who gave the current symbol a "Strong Buy" rating.',
    ),
    "syminfo.recommendations_date": BuiltinVariable(
        name="syminfo.recommendations_date",
        type="series int",
        description="The starting date of the last set of recommendations for the current symbol.",
    ),
    "syminfo.recommendations_hold": BuiltinVariable(
        name="syminfo.recommendations_hold",
        type="series int",
        description='The number of analysts who gave the current symbol a "Hold" rating.',
    ),
    "syminfo.recommendations_sell": BuiltinVariable(
        name="syminfo.recommendations_sell",
        type="series int",
        description='The number of analysts who gave the current symbol a "Sell" rating.',
    ),
    "syminfo.recommendations_sell_strong": BuiltinVariable(
        name="syminfo.recommendations_sell_strong",
        type="series int",
        description='The number of analysts who gave the current symbol a "Strong Sell" rating.',
    ),
    "syminfo.recommendations_total": BuiltinVariable(
        name="syminfo.recommendations_total",
        type="series int",
        description="The total number of recommendations for the current symbol.",
    ),
    "syminfo.root": BuiltinVariable(
        name="syminfo.root",
        type="simple string",
        description="Root for derivatives like futures contract. For other symbols returns the same value as [syminfo.ticker](#var_syminfo.ticker).",
    ),
    "syminfo.sector": BuiltinVariable(
        name="syminfo.sector",
        type="simple string",
        description="Returns the sector of the symbol, or [na](#var_na) if the symbol has no sector.  ",
    ),
    "syminfo.session": BuiltinVariable(
        name="syminfo.session",
        type="simple string",
        description="Session type of the chart main series. Possible values are [session.regular](#const_session.regular), [session.extended](#const_session.extended).",
    ),
    "syminfo.shareholders": BuiltinVariable(
        name="syminfo.shareholders",
        type="simple int",
        description="The number of shareholders the company has.",
    ),
    "syminfo.shares_outstanding_float": BuiltinVariable(
        name="syminfo.shares_outstanding_float",
        type="simple float",
        description="The total number of shares outstanding a company has available, excluding any of its restricted shares.",
    ),
    "syminfo.shares_outstanding_total": BuiltinVariable(
        name="syminfo.shares_outstanding_total",
        type="simple int",
        description="The total number of shares outstanding a company has available, including restricted shares held by insiders, major shareholders, and employees.",
    ),
    "syminfo.target_price_average": BuiltinVariable(
        name="syminfo.target_price_average",
        type="series float",
        description="The average of the last yearly price targets for the symbol predicted by analysts.",
    ),
    "syminfo.target_price_date": BuiltinVariable(
        name="syminfo.target_price_date",
        type="series int",
        description="The starting date of the last price target prediction for the current symbol.",
    ),
    "syminfo.target_price_estimates": BuiltinVariable(
        name="syminfo.target_price_estimates",
        type="series float",
        description="The latest total number of price target predictions for the current symbol.",
    ),
    "syminfo.target_price_high": BuiltinVariable(
        name="syminfo.target_price_high",
        type="series float",
        description="The last highest yearly price target for the symbol predicted by analysts.",
    ),
    "syminfo.target_price_low": BuiltinVariable(
        name="syminfo.target_price_low",
        type="series float",
        description="The last lowest yearly price target for the symbol predicted by analysts.",
    ),
    "syminfo.target_price_median": BuiltinVariable(
        name="syminfo.target_price_median",
        type="series float",
        description="The median of the last yearly price targets for the symbol predicted by analysts.",
    ),
    "syminfo.ticker": BuiltinVariable(
        name="syminfo.ticker",
        type="simple string",
        description="Symbol name without exchange prefix, e.g. 'MSFT'.",
    ),
    "syminfo.tickerid": BuiltinVariable(
        name="syminfo.tickerid",
        type="simple string",
        description="Returns the full form of the ticker ID representing a symbol, for use as an argument in functions with a `ticker` or `symbol` parameter.  ",
    ),
    "syminfo.timezone": BuiltinVariable(
        name="syminfo.timezone",
        type="simple string",
        description="Timezone of the exchange of the chart main series. Possible values see in [timestamp](#fun_timestamp).",
    ),
    "syminfo.type": BuiltinVariable(
        name="syminfo.type",
        type="simple string",
        description="Type of the current symbol. Possible values are stock, futures, index, forex, crypto, fund, dr.",
    ),
    "syminfo.volumetype": BuiltinVariable(
        name="syminfo.volumetype",
        type="simple string",
        description='Volume type of the current symbol. Possible values are: "base" for base currency, "quote" for quote currency, "tick" for the number of transactions, and "n/a" when there is no volume or its type is no',
    ),
    "ta.accdist": BuiltinVariable(
        name="ta.accdist",
        type="series float",
        description="Accumulation/distribution index.",
    ),
    "ta.iii": BuiltinVariable(
        name="ta.iii", type="series float", description="Intraday Intensity Index."
    ),
    "ta.nvi": BuiltinVariable(
        name="ta.nvi", type="series float", description="Negative Volume Index."
    ),
    "ta.obv": BuiltinVariable(
        name="ta.obv", type="series float", description="On Balance Volume."
    ),
    "ta.pvi": BuiltinVariable(
        name="ta.pvi", type="series float", description="Positive Volume Index."
    ),
    "ta.pvt": BuiltinVariable(
        name="ta.pvt", type="series float", description="Price-Volume Trend."
    ),
    "ta.tr": BuiltinVariable(
        name="ta.tr",
        type="series float",
        description="True range. Same as tr(false). It is max(high - low, abs(high - close[1]), abs(low - close[1]))",
    ),
    "ta.vwap": BuiltinVariable(
        name="ta.vwap",
        type="series float",
        description="Volume Weighted Average Price. It uses [hlc3](#var_hlc3) as its source series.",
    ),
    "ta.wad": BuiltinVariable(
        name="ta.wad",
        type="series float",
        description="Williams Accumulation/Distribution.",
    ),
    "ta.wvad": BuiltinVariable(
        name="ta.wvad",
        type="series float",
        description="Williams Variable Accumulation/Distribution.",
    ),
    "table.all": BuiltinVariable(
        name="table.all",
        type="table[]",
        description="Returns an array filled with all the current tables drawn by the script.",
    ),
    "text.align_bottom": BuiltinVariable(
        name="text.align_bottom",
        type="const string",
        description="Vertical text alignment for [box.new](#fun_box.new), [box.set_text_valign](#fun_box.set_text_valign), [table.cell](#fun_table.cell) and [table.cell_set_text_valign](#fun_table.cell_set_text_valign) fu",
    ),
    "text.align_center": BuiltinVariable(
        name="text.align_center",
        type="const string",
        description="Text alignment for [box.new](#fun_box.new), [box.set_text_halign](#fun_box.set_text_halign), [box.set_text_valign](#fun_box.set_text_valign), [label.new](#fun_label.new) and [label.set_textalign](#fun",
    ),
    "text.align_left": BuiltinVariable(
        name="text.align_left",
        type="const string",
        description="Horizontal text alignment for [box.new](#fun_box.new), [box.set_text_halign](#fun_box.set_text_halign), [label.new](#fun_label.new) and [label.set_textalign](#fun_label.set_textalign) functions.",
    ),
    "text.align_right": BuiltinVariable(
        name="text.align_right",
        type="const string",
        description="Horizontal text alignment for [box.new](#fun_box.new), [box.set_text_halign](#fun_box.set_text_halign), [label.new](#fun_label.new) and [label.set_textalign](#fun_label.set_textalign) functions.",
    ),
    "text.align_top": BuiltinVariable(
        name="text.align_top",
        type="const string",
        description="Vertical text alignment for [box.new](#fun_box.new), [box.set_text_valign](#fun_box.set_text_valign), [table.cell](#fun_table.cell) and [table.cell_set_text_valign](#fun_table.cell_set_text_valign) fu",
    ),
    "text.format_bold": BuiltinVariable(
        name="text.format_bold", type="const string", description="Bold format."
    ),
    "text.format_italic": BuiltinVariable(
        name="text.format_italic", type="const string", description="Italic format."
    ),
    "text.format_none": BuiltinVariable(
        name="text.format_none", type="const string", description="No format."
    ),
    "text.wrap_auto": BuiltinVariable(
        name="text.wrap_auto",
        type="const string",
        description="Automatic wrapping mode for [box.new](#fun_box.new) and [box.set_text_wrap](#fun_box.set_text_wrap) functions.",
    ),
    "text.wrap_none": BuiltinVariable(
        name="text.wrap_none",
        type="const string",
        description="Disabled wrapping mode for [box.new](#fun_box.new) and [box.set_text_wrap](#fun_box.set_text_wrap) functions.",
    ),
    "time": BuiltinVariable(
        name="time",
        type="series int",
        description="Current bar time in UNIX format. It is the number of milliseconds that have elapsed since 00:00:00 UTC, 1 January 1970.",
    ),
    "time_close": BuiltinVariable(
        name="time_close",
        type="series int",
        description="The time of the current bar\\`s close in UNIX format. It represents the number of milliseconds elapsed since 00:00:00 UTC, 1 January 1970.  ",
    ),
    "time_tradingday": BuiltinVariable(
        name="time_tradingday",
        type="series int",
        description="The beginning time of the trading day the current bar belongs to, in UNIX format (the number of milliseconds that have elapsed since 00:00:00 UTC, 1 January 1970).",
    ),
    "timeframe.isdaily": BuiltinVariable(
        name="timeframe.isdaily",
        type="simple bool",
        description="Returns true if current resolution is a daily resolution, false otherwise.",
    ),
    "timeframe.isdwm": BuiltinVariable(
        name="timeframe.isdwm",
        type="simple bool",
        description="Returns true if current resolution is a daily or weekly or monthly resolution, false otherwise.",
    ),
    "timeframe.isintraday": BuiltinVariable(
        name="timeframe.isintraday",
        type="simple bool",
        description="Returns true if current resolution is an intraday (minutes or seconds) resolution, false otherwise.",
    ),
    "timeframe.isminutes": BuiltinVariable(
        name="timeframe.isminutes",
        type="simple bool",
        description="Returns true if current resolution is a minutes resolution, false otherwise.",
    ),
    "timeframe.ismonthly": BuiltinVariable(
        name="timeframe.ismonthly",
        type="simple bool",
        description="Returns true if current resolution is a monthly resolution, false otherwise.",
    ),
    "timeframe.isseconds": BuiltinVariable(
        name="timeframe.isseconds",
        type="simple bool",
        description="Returns true if current resolution is a seconds resolution, false otherwise.",
    ),
    "timeframe.isticks": BuiltinVariable(
        name="timeframe.isticks", type="simple bool", description="Is ticks."
    ),
    "timeframe.isweekly": BuiltinVariable(
        name="timeframe.isweekly",
        type="simple bool",
        description="Returns true if current resolution is a weekly resolution, false otherwise.",
    ),
    "timeframe.main_period": BuiltinVariable(
        name="timeframe.main_period", type="simple string", description="Main period."
    ),
    "timeframe.multiplier": BuiltinVariable(
        name="timeframe.multiplier",
        type="simple int",
        description="Multiplier of resolution, e.g. '60' - 60, 'D' - 1, '5D' - 5, '12M' - 12.",
    ),
    "timeframe.period": BuiltinVariable(
        name="timeframe.period",
        type="simple string",
        description='A string representation of the chart\\`s timeframe. The returned string\\`s format is "[<quantity>][<units>]", where <quantity> and <units> are in some cases absent. <quantity> is the number of units, b',
    ),
    "timenow": BuiltinVariable(
        name="timenow",
        type="series int",
        description="Current time in UNIX format. It is the number of milliseconds that have elapsed since 00:00:00 UTC, 1 January 1970.",
    ),
    "volume": BuiltinVariable(
        name="volume", type="series float", description="Current bar volume."
    ),
    "weekofyear": BuiltinVariable(
        name="weekofyear",
        type="series int",
        description="Week number of current bar time in exchange timezone.",
    ),
    "xloc.bar_index": BuiltinVariable(
        name="xloc.bar_index",
        type="const string",
        description="A named constant that specifies the algorithm of interpretation of x-value in functions [line.new](#fun_line.new) and [label.new](#fun_label.new).  ",
    ),
    "xloc.bar_time": BuiltinVariable(
        name="xloc.bar_time",
        type="const string",
        description="A named constant that specifies the algorithm of interpretation of x-value in functions [line.new](#fun_line.new) and [label.new](#fun_label.new).  ",
    ),
    "year": BuiltinVariable(
        name="year",
        type="series int",
        description="Current bar year in exchange timezone.",
    ),
    "yloc.abovebar": BuiltinVariable(
        name="yloc.abovebar",
        type="const string",
        description="A named constant that specifies the algorithm of interpretation of y-value in function [label.new](#fun_label.new).",
    ),
    "yloc.belowbar": BuiltinVariable(
        name="yloc.belowbar",
        type="const string",
        description="A named constant that specifies the algorithm of interpretation of y-value in function [label.new](#fun_label.new).",
    ),
    "yloc.price": BuiltinVariable(
        name="yloc.price",
        type="const string",
        description="A named constant that specifies the algorithm of interpretation of y-value in function [label.new](#fun_label.new).",
    ),
}

PINE_KEYWORDS = [
    "and",
    "break",
    "by",
    "continue",
    "else",
    "export",
    "false",
    "for",
    "for...in",
    "if",
    "import",
    "in",
    "method",
    "not",
    "or",
    "switch",
    "to",
    "true",
    "type",
    "var",
    "varip",
    "while",
]
