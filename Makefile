SOURCE_DOCS := $(shell find src -type f -name "*.md")

HTML_FILES=$(SOURCE_DOCS:src/%.md=site/%.html)

all: generate_indexes html fix_links build_index
	miniserve site --index index.html

deploy: generate_indexes html fix_links build_index
	ntl deploy --prod

html: mkdirs $(HTML_FILES)

site/%.html: src/%.md templates/site.html
	pandoc -f markdown+fenced_divs -s $< -o $@ --table-of-contents --template templates/site.html

build_index: $(SOURCE_DOCS)
	pagefind --source site

fix_links: $(HTML_FILES)
	./bin/convert-html.sh

generate_indexes:
	./bin/generate-index-files.py

clean:
	rm -r site/**/*.html

.PHONY: mkdirs
mkdirs:
	rsync -a --include='*/' \
	--include="*.png" \
	--include="*.jpg" \
	--include="*.jpeg" \
	--exclude='*' src/ site/
