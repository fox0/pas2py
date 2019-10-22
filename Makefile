all: HelloParser.py

HelloParser.py: Hello.g4
	antlr4 -Dlanguage=Python3 $<

clean:
	rm -f *.interp *.tokens HelloLexer.py HelloListener.py HelloParser.py
