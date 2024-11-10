build_and_publish:
	python3 -m build
	twine upload dist/*