![](https://img.shields.io/github/license/wh1isper/bedway)
![](https://img.shields.io/github/v/release/wh1isper/bedway)
![](https://img.shields.io/docker/image-size/wh1isper/bedway)
![](https://img.shields.io/pypi/dm/bedway)
![](https://img.shields.io/github/last-commit/wh1isper/bedway)
![](https://img.shields.io/pypi/pyversions/bedway)

# bedway

Self-host and maintained [bedrock-access-gateway](https://github.com/aws-samples/bedrock-access-gateway), which is under [MIT No Attribution License](https://github.com/aws-samples/bedrock-access-gateway/blob/093c6fa586be04964820baaf1e3dca431f1fe823/LICENSE)

## Install

`pip install bedway`

Or use docker image

`docker pull wh1isper/bedway`

## Usage

```bash
docker run --name bedway \
-p 9128:9128 \
-e "AWS_ACCESS_KEY_ID=<access_key_id>" \
-e "AWS_SECRET_ACCESS_KEY=<secret_access_key>" \
-e "API_KEY=<api_key_for_this_service>" \
wh1isper/bedway
```

## Develop

Install pre-commit before commit

```
pip install pre-commit
pre-commit install
```

Install package locally

```
pip install -e .[test]
```

Run unit-test before PR, **ensure that new features are covered by unit tests**

```
pytest -v
```
