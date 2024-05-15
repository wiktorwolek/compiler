GRAMMAR=Expr.g4
START=prog
TEST=tests/int_divide.x

antlr:
	antlr4 -Dlanguage=Python3 $(GRAMMAR)

compile:
	python3 compiler.py $(TEST)

run:
	clang $(START).ll

interpret:
	python3 interpreter.py

clean:
	rm $(START).ll