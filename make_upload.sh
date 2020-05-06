rm upload.zip
rm -r upload/

unzip package/psycopg2-binary-2.8.4.zip -d package/

mkdir upload
mv package/psycopg2-binary-2.8.4/* upload/
cp app/lambda_function.py upload/
pip install -r app/requirements.txt -t upload/
cd upload/
zip -r ../upload.zip --exclude=__pycache__/* .
cd ../

rm -r package/psycopg2-binary-2.8.4/
rm -r package/__MACOSX/
rm -r upload/
