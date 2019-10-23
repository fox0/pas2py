import re
import sys

from antlr4.InputStream import InputStream
from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.tree.Tree import ParseTreeWalker

from PascalLexer import PascalLexer
from PascalListener import PascalListener
from PascalParser import PascalParser

KEYWORDS = (
    'var', 'begin', 'end', 'readln', 'writeln', 'mod', 'div', 'if', 'then', 'else', 'while', 'do', 'integer', 'int64',
)


class Listener(PascalListener):
    def __init__(self):
        self.var_ls = {}
        self.spaces = -4

    def exitVariableDeclaration(self, ctx: PascalParser.VariableDeclarationContext):
        var_type = ctx.varType().getText()
        for i in ctx.identifierList().getText().split(','):
            self.var_ls[i] = var_type

    def enterBlock(self, ctx: PascalParser.BlockContext):
        self.spaces += 4

    def exitBlock(self, ctx: PascalParser.BlockContext):
        self.spaces -= 4

    def exitWritelnReadln(self, ctx: PascalParser.WritelnReadlnContext):
        var = ctx.ID().getText()
        const = ctx.CONST_STR().getText()
        self._print_input(var, const)

    def enterReadln(self, ctx: PascalParser.ReadlnContext):
        for i in ctx.identifierList().getText().split(','):
            self._print_input(i)

    def exitWriteln(self, ctx: PascalParser.WritelnContext):
        self._print('print({})'.format(ctx.expression().getText()))

    def exitAssignmentStatement(self, ctx: PascalParser.AssignmentStatementContext):
        var = ctx.ID().getText()
        expr = ctx.expression().getText()
        self._print('{var} = {expr}'.format(var=var, expr=expr))

    def enterIfStatement(self, ctx: PascalParser.IfStatementContext):
        self._print('if {}:'.format(ctx.expression().getText()))
        self.spaces += 4

    def exitIfStatement(self, ctx: PascalParser.IfStatementContext):
        self.spaces -= 4

    def enterElseStatement(self, ctx: PascalParser.ElseStatementContext):
        self.spaces -= 4
        self._print('else:')
        self.spaces += 4

    def exitElseStatement(self, ctx: PascalParser.ElseStatementContext):
        self.spaces -= 4

    def _print_input(self, var, const=None):
        const = const or ''
        var_type = self._get_var_type(var)
        if var_type:
            self._print('{var} = {var_type}(input({const}))'.format(var=var, var_type=var_type, const=const))
        else:
            raise NotImplementedError

    def _get_var_type(self, var):
        try:
            var_type = self.var_ls[var]
        except KeyError:
            raise ValueError('variable {} not defined'.format(var))
        if var_type in ('integer', 'int64'):
            return 'int'
        else:
            raise NotImplementedError(var_type)

    def _print(self, line):
        print(' ' * self.spaces, line, sep='')


def main(filename):
    with open(filename) as f:
        text = f.read()
    text = re.sub(r'\b({})\b'.format(r'|'.join(KEYWORDS)), lambda m: m.group().lower(), text, flags=re.IGNORECASE)
    text = text.replace('div', '//').replace('mod', '%')

    lexer = PascalLexer(InputStream(text))
    stream = CommonTokenStream(lexer)
    parser = PascalParser(stream)
    tree = parser.program()
    listener = Listener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        main('test1.pas')
