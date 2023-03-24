CXX        = g++-9
CXXFLAGS   = -g
LDFLAGS    = 
ENTRYPOINT = main.cpp
EXECUTABLE = $(basename $(ENTRYPOINT))

all: clean build

.PHONY: clean
clean:
	rm -vf $(EXECUTABLE)

build: $(EXECUTABLE)

run: $(EXECUTABLE)
	./$(EXECUTABLE)

$(EXECUTABLE): $(ENTRYPOINT)
	$(CXX) $(CXXFLAGS) $(LDFLAGS) -o $@ $^

test:
	$(MAKE) -C ../tools test PROJECT_DIR=$(PWD)
