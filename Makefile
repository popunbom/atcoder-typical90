BREW_PKG_GCC = gcc@9
GCC_EXECS = gcc-9 g++-9

.PHONY: init
init:
	[[ $$(brew list $(BREW_PKG_GCC) 2>/dev/null) ]] && true || brew install $(BREW_PKG_GCC)
	which $(GCC_EXECS)

add:
	$(MAKE) -C ./tools add
