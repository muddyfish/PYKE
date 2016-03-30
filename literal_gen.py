from node.create_list import List
from node.numeric_literal import NumericLiteral
from node.string_literal import StringLiteral
from node.string_single import StringSingle

nodes = {int: NumericLiteral,
         float: NumericLiteral,
         str: StringLiteral,
         list: List,
         tuple: List}

def int_literal(number):
    if number == 0:
        return "0"
    abs_num = abs(number)
    is_neg = number<0
    return str(abs_num)+"_"*is_neg

def float_literal(number):
    if number == 0:
        return ".0"
    abs_num = abs(number)
    is_neg = number<0
    less_one = abs_num < 1
    return str(abs_num)[less_one:]+"_"*is_neg

def string_literal(string):
    if len(string) == 1:
        return "\\"+string
    return '"'+string+'"'

def list_literal(seq):
    end = List.char
    if len(seq) != List.default_arg:
        end += int_literal(len(seq))
    return stack_literal(seq)+end

def tuple_literal(seq):
    return list_literal(seq)

def set_literal(seq): return NotImplementedError()
def dict_literal(dic): return NotImplementedError()

parsers = {int: int_literal,
           float: float_literal,
           str: string_literal,
           list: list_literal,
           tuple: tuple_literal,
           set: set_literal,
           dict: dict_literal}

def parse_item(item):
    return parsers[type(item)](item)

def stack_literal(stack):
    node_list = list(map(parse_item, stack))
    rtn = ""
    for i in range(len(node_list)-1):
        rtn += node_list[i]
        node_type = nodes[type(stack[i])]
        node_type_next = nodes[type(stack[i+1])]
        assert(node_type.accepts(node_list[i]))
        code, node = node_type.accepts(node_list[i]+node_list[i+1])
        if code == "" or code is None or code == "_":
            rtn += " "
        elif node_type is List and node_type_next is NumericLiteral:
            rtn += " "
        is_list = node_type_next is List
        if is_list:
            next_test_parsed = node_list[i+1]
            next_test_str = stack[i+1]
            while node_type_next is List:
                next_test_parsed = next_test_parsed[0]
                next_test_str = next_test_str[0]
                node_type_next = nodes[type(next_test_str)]
            code, node = node_type.accepts(node_list[i]+next_test_parsed)
            if code == "":
                rtn += " "
            elif node_type is List and node_type_next is NumericLiteral:
                rtn += " "
    if node_list:
        rtn += node_list[-1]
    return rtn