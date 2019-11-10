CC = g++
CFLAGS = -fsanitize=undefined -fno-sanitize-recover=undefined -std=c++14 -O2 -Wall 

default: abs

abs: abs.o 
	$(CC) -fsanitize=undefined -fno-sanitize-recover=undefined  -o abs abs.o

abs.o: abs.cpp 
	$(CC) $(CFLAGS) -c  abs.cpp

run: solution
	python3 Check.py ./abs

solution:
	mv $(filename) solution.txt || true

