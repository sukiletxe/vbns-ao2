pushd ..\src
python setup.py py2exe
rd /s /q build
ren dist vbns-ao2
7z a vbns-ao2-v1.0.zip vbns-ao2\ -r -tzip
rd /s /q vbns-ao2
popd
