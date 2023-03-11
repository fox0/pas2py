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

KEYWORDS = (
    'var', 'integer', 'int64', 'real',
    'begin', 'end',
    'readln', 'writeln',
    'mod', 'div', 'or', 'and',
    'if', 'then', 'else', 'while', 'do',
)


# noinspection PyPep8Naming
class Listener(PascalListener):
    def __init__(self):
        self.var_ls: dict[str, str] = {}
        self.spaces = -4
        self.file = io.StringIO()

    def exitVariableDeclaration(self, ctx: PascalParser.VariableDeclarationContext):
        var_type: str = ctx.varType().getText()
        for i in ctx.identifierList().getText().split(','):
            self.var_ls[i] = var_type

    def exitWritelnReadln(self, ctx: PascalParser.WritelnReadlnContext):
        var: str = ctx.ID().getText()
        const: str = ctx.CONST_STR().getText()
        self._print_input(var, const)

    def enterReadln(self, ctx: PascalParser.ReadlnContext):
        for i in ctx.identifierList().getText().split(','):
            self._print_input(i)

    def exitWriteln(self, ctx: PascalParser.WritelnContext):
        self._print('print({})'.format(ctx.expressions().getText()))

    def exitAssignmentStatement(self, ctx: PascalParser.AssignmentStatementContext):
        var: str = ctx.ID().getText()
        expr: str = ctx.expression().getText()
        self._print('{var} = {expr}'.format(var=var, expr=expr))

    def enterWhileStatement(self, ctx: PascalParser.WhileStatementContext):
        self._print('while {}:'.format(ctx.expression().getText()))

    def enterIfStatement(self, ctx: PascalParser.IfStatementContext):
        self._print('if {}:'.format(ctx.expression().getText()))

    def enterElseStatement(self, ctx: PascalParser.ElseStatementContext):
        self._print('else:')

    def enterBlock(self, ctx: PascalParser.BlockContext):
        self.spaces += 4

    def exitBlock(self, ctx: PascalParser.BlockContext):
        self.spaces -= 4

    def enterBlockBody(self, ctx: PascalParser.BlockBodyContext):
        self.spaces += 4

    def exitBlockBody(self, ctx: PascalParser.BlockBodyContext):
        self.spaces -= 4

    def _print_input(self, var: str, const: str = None):
        const = const or ''
        var_type = self._get_var_type(var)
        if var_type:
            self._print('{var} = {var_type}(input({const}))'.format(var=var, var_type=var_type, const=const))
        else:
            raise NotImplementedError

    def _print(self, line: str):
        print(' ' * self.spaces, line, sep='', file=self.file)

    def _get_var_type(self, var: str):
        try:
            var_type = self.var_ls[var]
        except KeyError:
            raise ValueError('variable {} not defined'.format(var))
        result = {
            'integer': 'int',
            'int64': 'int',
            'real': 'float',
        }.get(var_type)
        if result is None:
            raise NotImplementedError(var_type)
        return result


def main(text: str) -> str:
    text = re.sub(r'\b({})\b'.format(r'|'.join(KEYWORDS)), lambda m: m.group().lower(), text, flags=re.IGNORECASE)
    text = text.replace('div', '//')
    text = text.replace('mod', '%')
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
    except black.parsing.InvalidInput:
        return text


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('example: {} tests/test1.pas'.format(sys.argv[0]))
        exit(1)
    with open(sys.argv[1]) as f:
        print(main(text=f.read()))
