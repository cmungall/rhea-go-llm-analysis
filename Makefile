MAKEFLAGS += --warn-undefined-variables
SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := help
.DELETE_ON_ERROR:
.SUFFIXES:
.SECONDARY:

RUN = poetry run
.PHONY: all clean

# note: "help" MUST be the first target in the file,
# when the user types "make" they should get help info
help: status
	@echo ""

