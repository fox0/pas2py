import io
import re
import sys

import black
from antlr4.InputStream import InputStream
from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.tree.Tree import ParseTreeWalker

from PascalLexer import PascalLexer
from PascalListener import PascalListener
from PascalParser import PascalParser

if sys.version_info < (3, 7):
    raise ValueError('version python < 3.7')

BANNER = '# generated by https://github.com/fox0/pas2py'

KEYWORDS = (
    'var', 'integer', 'int64', 'longint', 'real',
    'begin', 'end',
    'readln', 'writeln', 'read', 'write', 'inc',
    'mod', 'div', 'or', 'and',
    'if', 'then', 'else', 'while', 'do',
)
TYPES = {
    'byte': 'int',
    'longint': 'int',
    'integer': 'int',
    'int64': 'int',
    'real': 'float',
    'string': 'str',
    'boolean': 'bool',
}


# noinspection PyPep8Naming
class Listener(PascalListener):
    def __init__(self):
        self.var_ls: dict[str, str] = {}
        self.spaces = -4
        self.file = io.StringIO()
        self.file.writelines((BANNER, '\n'))

    def exitVariableDeclaration(self, ctx: PascalParser.VariableDeclarationContext):
        """identifierList COLON varType"""
        var_type: str = ctx.varType().getText()
        for i in ctx.identifierList().getText().split(','):
            self.var_ls[i] = var_type

    def enterBlockStatement(self, ctx: PascalParser.BlockStatementContext):
        self.spaces += 4

    def exitBlockStatement(self, ctx: PascalParser.BlockStatementContext):
        self.spaces -= 4

    def enterFakeblockStatement(self, ctx: PascalParser.FakeblockStatementContext):
        self.spaces += 4

    def exitFakeblockStatement(self, ctx: PascalParser.FakeblockStatementContext):
        self.spaces -= 4

    def exitAssignmentStatement(self, ctx: PascalParser.AssignmentStatementContext):
        """ID ASSIGN expression"""
        var: str = ctx.ID().getText()
        expr: str = ctx.expression().getText()
        self._print(f'{var} = {expr}')

    def enterWhileStatement(self, ctx: PascalParser.WhileStatementContext):
        """'while' expression 'do' blockOrFakeBlock"""
        expr: str = ctx.expression().getText()
        self._print(f'while {expr}:')

    def enterForStatement(self, ctx: PascalParser.ForStatementContext):
        """'for' ID ASSIGN expression 'to' expression 'do' blockOrFakeBlock"""
        var: str = ctx.ID().getText()
        exprs = ctx.expression()
        expr0: str = exprs[0].getText()
        expr1: str = exprs[1].getText()
        self._print(f'for {var} in range({expr0}, {expr1}):')

    def enterIfStatement(self, ctx: PascalParser.IfStatementContext):
        """'if' expression 'then' blockOrFakeBlock elseStatement?"""
        expr: str = ctx.expression().getText()
        self._print(f'if {expr}:')

    def enterElseStatement(self, ctx: PascalParser.ElseStatementContext):
        self._print('else:')

    def exitBreakStatement(self, ctx: PascalParser.BreakStatementContext):
        self._print('break')

    def exitWritelnReadln(self, ctx: PascalParser.WritelnReadlnContext):
        var: str = ctx.ID().getText()
        const: str = ctx.CONST_STR().getText()
        self._print_input(var, const)

    def enterReadln(self, ctx: PascalParser.ReadlnContext):
        for i in ctx.identifierList().getText().split(','):
            self._print_input(i)

    def exitWriteln(self, ctx: PascalParser.WritelnContext):
        expr: str = ctx.expressions().getText()
        self._print(f'print({expr})')

    def exitWrite(self, ctx: PascalParser.WritelnContext):
        expr: str = ctx.expressions().getText()
        self._print(f"print({expr}, end='')")

    def exitInc(self, ctx: PascalParser.IncContext):
        """'inc' LPAREN ID RPAREN"""
        var: str = ctx.ID().getText()
        self._print(f'{var} += 1')

    def _print_input(self, var: str, const: str = ''):
        var_type = self._get_var_type(var)
        if var_type == 'str':
            self._print(f'{var} = input({const})')
        else:
            self._print(f'{var} = {var_type}(input({const}))')

    def _print(self, line: str):
        print(' ' * self.spaces, line, sep='', file=self.file)

    def _get_var_type(self, var: str):
        try:
            var_type = self.var_ls[var]
        except KeyError:
            raise ValueError(f'variable {var} not defined')
        result = TYPES.get(var_type)
        if result is None:
            raise NotImplementedError(var_type)
        return result


def main(text: str) -> str:
    text = re.sub(r'\b({})\b'.format(r'|'.join(KEYWORDS)), lambda m: m.group().lower(), text, flags=re.IGNORECASE)
    text = text.replace('div', '//')
    text = text.replace('mod', '%')
    # text = text.replace('<>', '!=')
    # text = text.replace('=', '==')

    lexer = PascalLexer(InputStream(text))
    stream = CommonTokenStream(lexer)
    parser = PascalParser(stream)
    tree = parser.program()
    listener = Listener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    listener.file.seek(0)
    text = listener.file.read()
    try:
        return black.format_str(text, mode=black.Mode())
    except black.parsing.InvalidInput as e:
        return f'{text}\n# error: {e}'


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'example: {sys.argv[0]} tests/001.pas')
        exit(1)
    with open(sys.argv[1]) as f:
        print(main(text=f.read()))
