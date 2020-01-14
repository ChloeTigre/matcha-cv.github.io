all:
	./matcha-cv/rendercv.py

publish:
	cp -a _layouts _config.yml media public
	git subtree push --prefix public origin gh-pages
