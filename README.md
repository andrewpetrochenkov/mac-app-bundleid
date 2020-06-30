<!--
https://readme42.com
-->



[![](https://img.shields.io/badge/OS-Unix-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/v/mac-app-bundleid.svg?maxAge=3600)](https://pypi.org/project/mac-app-bundleid/)
[![](https://img.shields.io/npm/v/mac-app-bundleid.svg?maxAge=3600)](https://www.npmjs.com/package/mac-app-bundleid)[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/mac-app-bundleid/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/mac-app-bundleid/actions)

### Installation
```bash
$ [sudo] pip install mac-app-bundleid
```

```bash
$ [sudo] npm i -g mac-app-bundleid
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
    <a href="https://readme42.com/">readme42.com</a>
</p>