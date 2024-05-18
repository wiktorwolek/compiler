GRAMMAR=Expr.g4
START=prog
TEST=tests/real_divide.x

ifeq ($(OS),Windows_NT)
	EXT=a.exe
else
	EXT=a.out
endif

antlr:
	antlr4 -Dlanguage=Python3 $(GRAMMAR)

compile:
	python3 compiler.py $(TEST)

llvm:
	clang $(START).ll

run: 
	./$(EXT)

interpret:
	python3 interpreter.py

clean:
	rm $(START).ll