CC = clang
SRC_DIR = .
SRCS = $(shell find $(SRC_DIR) -name '*.c')
LLVMS = $(SRCS:%.c=%.ll)

all: $(LLVMS)

%.ll : %.c
		$(CC) -S -emit-llvm $< -o $@

.PHONY: clean
clean:
	rm *.ll