#!/usr/bin/env bash
{ set +x; } 2>/dev/null

( set -x; app-bundleid "Finder" ) || exit
( set -x; app-bundleid /System/Library/CoreServices/Finder.app ) || exit
