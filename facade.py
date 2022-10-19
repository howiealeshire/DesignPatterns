class Scanner:
    stream = []
    def __init__(self,stream):
        self.stream = stream

class Parser:
    scanner = None
    program_node_builder = None
    def parse(self,scanner,program_node_builder):
        self.scanner = scanner
        self.program_node_builder = program_node_builder

class ProgramNode:
    line = 0
    index = 0
    # program node manipulation
    def get_source_position(self,line,index):
        self.line = line
        self.index = index
    # child manipulation
    def add(self,program_node):
        pass
    def remove(self,program_node):
        pass
    def traverse(self,code_generator):
        pass

class CodeGenerator:
    _output = None
    def __init__(self,bytecode_stream):
        self._output = bytecode_stream
    def visit(self,statement_node=None,expression_node=None):
        pass


class ProgramNodeBuilder:
    def make_new_variable(self,variable_name):
        return ProgramNode()
    def make_new_assignment(self,variable,expression):
        return ProgramNode()
    def make_new_return_statement(self, value):
        return ProgramNode()
    def make_new_condition(self, condition,true_part,false_part):
        return ProgramNode()
    def get_root_node(self):
        return ProgramNode()

def generator(bytecode_stream):
    return bytecode_stream

class Compiler:
    def Compile(self,input_char_stream,output_bytecode_stream):
        scanner = Scanner(input_char_stream)
        builder = ProgramNodeBuilder()
        parser = Parser()
        parser.parse(scanner,builder)
        risc_code_generator = generator(output_bytecode_stream)
        parse_tree = builder.get_root_node()
        parse_tree.traverse(risc_code_generator)

