from antlr4.FileStream import FileStream
from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.tree.Tree import ParseTreeWalker

from PascalLexer import PascalLexer
from PascalListener import PascalListener
from PascalParser import PascalParser


class Listener(PascalListener):
    def __init__(self):
        self.var_ls = {}
        self.spaces = -4

    def exitVariableDeclaration(self, ctx: PascalParser.VariableDeclarationContext):
        # var_type = ctx.varType()
        for i in ctx.identifierList().children[::2]:  # todo replace children
            self.var_ls[str(i)] = 'int'
        print(' ' * self.spaces, '# ', self.var_ls, sep='')

    def enterBlock(self, ctx: PascalParser.BlockContext):
        self.spaces += 4

    def exitBlock(self, ctx: PascalParser.BlockContext):
        self.spaces -= 4

    def exitCallFunction(self, ctx: PascalParser.CallFunctionContext):
        func = str(ctx.ID())
        ls = []
        for i in ctx.parameterList().children[::2]:  # todo bug
            ls.append(str(i))

        if func == 'readln':
            for i in ls:
                var_type = self.var_ls[i]
                if var_type == 'int':
                    print(' ' * self.spaces, '%s = int(input())' % i, sep='')
                else:
                    raise NotImplementedError(var_type)
        elif func == 'writeln':
            print(' ' * self.spaces, 'print(%s)' % ', '.join(ls), sep='')
        else:
            raise NotImplementedError(func)

    def exitAssignmentStatement(self, ctx: PascalParser.AssignmentStatementContext):
        var = ctx.ID()
        ls = ctx.expression()  # todo
        print(' ' * self.spaces, '%s = %s' % (var, ls), sep='')


def main(filename):
    lexer = PascalLexer(FileStream(filename))
    stream = CommonTokenStream(lexer)
    parser = PascalParser(stream)
    tree = parser.program()
    listener = Listener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)


if __name__ == '__main__':
    # todo replace '\bVAR\b' -> 'var'
    main('test1.pas')
