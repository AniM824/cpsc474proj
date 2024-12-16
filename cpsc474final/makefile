SHELL := /bin/bash

.PHONY: all project_info results baseline_small baseline_large strat1_small strat1_large strat2_small strat2_large

all: project_info results baseline_small baseline_large strat1_small strat1_large strat2_small strat2_large

project_info:
	@echo "CPSC 474 Final Project: Aniketh Malyala and Thomas Luong"
	@echo "In this final project, we will be exploring various minimax strategies to solve a variant of NYT's Wordle, Dordle (solving two Wordle board simultaneously)"
	@echo "This script should take approximately 2 minutes to run."

baseline_small:
	@echo "Running random baseline agent, small vocabulary size..."
	@python3 dordle_baseline.py
	@echo ""

baseline_large:
	@echo "Running random baseline agent, large vocabulary size..."
	@python3 dordle_baseline.py --large
	@echo ""

strat1_small:
	@echo "Running Strategy 1 (dual board focus strategy), small vocabulary size..."
	@python3 dordle_stratone.py
	@echo ""

strat1_large:
	@echo "Running Strategy 1 (dual board focus strategy), large vocabulary size..."
	@python3 dordle_stratone.py --large
	@echo ""

strat2_small:
	@echo "Running Strategy 2 (single board focus strategy), small vocabulary size..."
	@python3 dordle_strattwo.py
	@echo ""

strat2_large:
	@echo "Running Strategy 2 (single board focus strategy), large vocabulary size..."
	@python3 dordle_strattwo.py --large
	@echo ""

results:
	@echo ""
	@echo "Expected Number of Turns to Complete Board over Numerous Trials:"
	@echo "Baseline small vocab: 6.738 (1000 trials)"
	@echo "Baseline large vocab: 8.907 (1000 trials)"
	@echo ""
	@echo "Strategy 1 small vocab: 5.53 (100 trials)"
	@echo "Strategy 1 large vocab:  7.51 (100 trials)"
	@echo ""
	@echo "Strategy 2 small vocab: 5.81 (100 trials)"
	@echo "Strategy 2 large vocab:  7.5 (100 trials)"
	@echo ""
