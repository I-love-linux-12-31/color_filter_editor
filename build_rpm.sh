#!/bin/bash
VERSION="1.2.6"
SOURCES_ARH="color-filter-editor-$VERSION.tar.gz"

sed -i "s/^Version:.*$/Version:        $VERSION/" color-filter-editor.spec

if [ -d "./rpmbuild" ]; then
    rm -rf ./rpmbuild
fi

rpmdev-setuptree
cp ~/rpmbuild/ -r ./

tar -czf $SOURCES_ARH ./cfe ./cfe/* ./cfe.desktop ./LICENSE.md ./README* ./run_cfe.sh
cp color-filter-editor.spec rpmbuild/SPECS/
cp $SOURCES_ARH rpmbuild/SOURCES/

rpmbuild -ba rpmbuild/SPECS/color-filter-editor.spec && echo -e "You can find .rpm file at \033[32m./rpmbuild/RPMS/noarch/\033[0m"

rm $SOURCES_ARH

cp ./rpmbuild/RPMS/noarch/color-filter-editor* ./
