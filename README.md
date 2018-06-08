# minimal sphinx auto-generated doc

## deps
```
apt-get install python-sphinx
pip install sphinx_rtd_theme
```

## cmds
```
user@host:~/git/sphinx-autodoc-example/proj/docs$ sphinx-quickstart
..interactive..
Refer to sphinx-quickstart.out.txt.

user@host:~/git/sphinx-autodoc-example/proj/docs$ sphinx-apidoc -f -o source ..
..generating *.rst files..
Refer to sphinx-apidoc.out.txt.

user@host:~/git/sphinx-autodoc-example/proj/docs$ sphinx-build -b html source build
..building html..
Refer to sphinx-build.out.txt.
```

Till this point, it's all set.

The html pages is generated under ~/git/sphinx-autodoc-example/proj/docs/build
