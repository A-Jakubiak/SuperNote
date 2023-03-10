#!/bin/sh

# This script is meant to be run through MinGW
mv ../../configfile.py ../../configfile.py.old
cp configfile.py ../../
APP=SuperNote

echo "Setting up virtual environment..."

python3 -m venv --system-site-packages venv
. venv/bin/activate
python3 -m pip install --upgrade pip
PYINSTALLER_COMPILE_BOOTLOADER=1 PYI_STATIC_ZLIB=1 python3 -m pip install -r ../requirements.txt

echo "Running pyinstaller..."

python3 -OO -m PyInstaller $APP.spec

echo "Preparing app..."

cd dist/$APP
zip -r $APP.zip *
mv $APP.zip ../..
cd ../..
echo $(du -sk dist/$APP | cut -f 1) > INSTALLSIZE

echo "Running makensis..."

makensis $APP.nsi
for exe in $APP*.exe; do
    echo $(sha256sum $exe) > $exe.sha256
done

echo "Cleaning up..."

deactivate
mv $APP*.exe* ../..
rm $APP.zip
rm INSTALLSIZE
rm -r build
rm -r dist/*/*
rm -r dist
rm -r venv
mv ../../configfile.py.old ../../configfile.py
