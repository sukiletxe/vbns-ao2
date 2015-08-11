pushd ..
pandoc -f markdown_github -o readme.html -s readme.md
popd
