<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/badge/OS-macOS-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/v/mac-app-bundleid.svg?maxAge=3600)](https://pypi.org/project/mac-app-bundleid/)
[![](https://img.shields.io/npm/v/mac-app-bundleid.svg?maxAge=3600)](https://www.npmjs.com/package/mac-app-bundleid)
[![Travis](https://api.travis-ci.org/looking-for-a-job/mac-app-bundleid.svg?branch=master)](https://travis-ci.org/looking-for-a-job/mac-app-bundleid/)

#### Installation
```bash
$ [sudo] npm i -g mac-app-bundleid
```
```bash
$ [sudo] pip install mac-app-bundleid
```

#### Scripts usage
```bash
usage: app-bundleid app [value]
```

#### Examples
```bash
$ app-bundleid "Finder"
com.apple.finder
$ app-bundleid /System/Library/CoreServices/Finder.app
com.apple.finder
```

```bash
$ app-bundleid path/to/my-app.app "me.my-app.app"
$ app-bundleid path/to/my-app.app
me.my-app.app
```

<p align="center">
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>