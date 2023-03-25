CXX        = g++-9
CXXFLAGS   = -std=gnu++17 -Wall -Wextra -O2
LDFLAGS    = 
ENTRYPOINT = main.cpp
EXECUTABLE = $(basename $(ENTRYPOINT))

$(EXECUTABLE): $(ENTRYPOINT)
	$(CXX) $(CXXFLAGS) $(LDFLAGS) -o $@ $^

all: clean build

.PHONY: clean
clean:
	rm -vf $(EXECUTABLE)

build: $(EXECUTABLE)

run: $(EXECUTABLE)
	./$(EXECUTABLE)

check: clean build
	$(MAKE) -C ../tools check PROJECT_DIR=$(PWD)

test: clean build
	$(MAKE) -C ../tools test PROJECT_DIR=$(PWD)
