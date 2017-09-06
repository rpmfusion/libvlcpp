#!/bin/bash

set -e

tmp=$(mktemp -d)

trap cleanup EXIT
cleanup() {
    set +e
    [ -z "$tmp" -o ! -d "$tmp" ] || rm -rf "$tmp"
}

unset CDPATH
pwd=$(pwd)
date=$(date +%Y%m%d)
package=libvlcpp

pushd "$tmp"
git clone https://code.videolan.org/videolan/libvlcpp.git
cd $package
git archive --prefix="${package}-${date}/" --format=tar master | xz > "$pwd"/${package}-${date}.tar.xz
popd
