CXX        = g++-9
CXXFLAGS   = -g
LDFLAGS    = 
ENTRYPOINT = main.cpp
EXECUTABLE = $(basename $(ENTRYPOINT))

all: clean build run

.PHONY: clean
clean:
	rm -vf $(EXECUTABLE)

build: $(EXECUTABLE)

run: $(EXECUTABLE)
	./$(EXECUTABLE)

$(EXECUTABLE): $(ENTRYPOINT)
	$(CXX) $(CXXFLAGS) $(LDFLAGS) -o $@ $^
