run:
	uvicorn main:app --reload

hello:
	echo "hello"

exporter:
	poetry export -f requirements.txt --output requirements.txt --without-hashes

build-run:
	sam build && sam local start-api

build-deploy:
	sam build
	sam deploy \
    --stack-name FastAPIOnLambda \
    --s3-bucket bucketalakon \
    --capabilities CAPABILITY_AUTO_EXPAND CAPABILITY_IAM
