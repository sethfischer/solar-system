.PHONY: lint
lint: lint-python lint-shell

.PHONY: lint-python lint-shell
lint-python lint-shell:
	./$@.sh
