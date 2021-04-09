COMPILER=g++
FLAGS=-g -fopenmp -Wall -Werror --std=c++17
SOURCE=serial.cpp
PROGRAM=serial

all:
	${COMPILER} ${FLAGS} ${SOURCE} -o ${PROGRAM}

run: ${PROGRAM}
	./${PROGRAM}
