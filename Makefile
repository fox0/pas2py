all: PascalParser.py

PascalParser.py: Pascal.g4
	antlr4 -Dlanguage=Python3 $<

clean:
	rm -f *.interp *.tokens Pascal*.py
