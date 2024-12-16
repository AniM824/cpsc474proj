SHELL := /bin/bash

.PHONY: all results baseline_small baseline_large strat1_small strat1_large strat2_small strat2_large

all: results baseline_small baseline_large strat1_small strat1_large strat2_small strat2_large

baseline_small:
	@echo "Running random agent, small vocabulary size..."
	@python3 dordle_baseline.py

baseline_large:
	@echo "Running random agent, large vocabulary size..."
	@python3 dordle_baseline.py --large

strat1_small:
	@echo "Running strat 1 (dual board focus strategy), small vocabulary size..."
	@python3 dordle_stratone.py

strat1_large:
	@echo "Running strat 1 (dual board focus strategy), large vocabulary size..."
	@python3 dordle_stratone.py --large

strat2_small:
	@echo "Running strat 2 (single board focus strategy), small vocabulary size..."
	@python3 dordle_strattwo.py

strat2_large:
	@echo "Running strat 2 (single board focus strategy), large vocabulary size..."
	@python3 dordle_strattwo.py --large

results:
	@echo "\nExpected Results over Numerous Trials:"
	@echo "Baseline small vocab: 6.738 (1k trials)"
	@echo "Baseline large vocab: 8.907 (1k trials)"
	@echo "\nstrat1 small vocab: 5.53 (100 trials)"
	@echo "strat1 large vocab:  7.51 (100 trials)"
	@echo "\nstrat2 small vocab: 5.81 (100 trials)"
	@echo "strat2 large vocab:  7.5 (100 trials)"
