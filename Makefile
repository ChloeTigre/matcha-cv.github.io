.PHONY = all write publish
all: write publish

write:
	mkdir -p public
	./matcha-cv/rendercv.py

publish:
	cp -r _layouts _config.yml media public/
	git add public
	git commit -m "publishing pages"
	git subtree push --prefix public/ origin gh-pages
