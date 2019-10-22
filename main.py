from antlr4.FileStream import FileStream
from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.tree.Tree import ParseTreeWalker

from PascalLexer import PascalLexer
from PascalListener import PascalListener
from PascalParser import PascalParser


class Listener(PascalListener):
    def __init__(self):
        self.var_ls = {}

    def exitVariableDeclaration(self, ctx):
        # identifierList COLON ('integer' | 'int64');
        # ctx.children[2]
        for i in ctx.children[0].children[::2]:
            self.var_ls[str(i)] = 'int'
        print('#', self.var_ls)


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
