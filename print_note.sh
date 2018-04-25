#!/bin/sh
cat testdata_cantilever.pc | grep ^NODE | awk '{print $4, $5, $6}' > node.dat
cat testdata_cantilever.pc | grep ^SHELL | awk '{print $4, $5, $6, $7, $8}' > shell.dat
#cat testdata_cantilever.pc | grep ^\$# > comment.dat
