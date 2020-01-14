.PHONY = all write publish
all: write publish

write:
	mkdir -p public
	./matcha-cv/rendercv.py

publish:
	cp -a _layouts _config.yml media public/
	git subtree push --prefix public/ origin gh-pages
