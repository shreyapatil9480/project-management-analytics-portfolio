.PHONY: train predict test

train:
	python src/train.py

predict:
	python src/predict.py --input data/sample_input.csv

test:
	pytest tests/
