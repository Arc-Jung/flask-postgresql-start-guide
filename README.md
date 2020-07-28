# flask-postgresql-start-guide

### ***Fisrt uploaded 2020-06-19 WooSung-Jung***

## 파이썬3로 가상환경 생성 / Make Python3 virtual environment
- Insert bash command in your bash shell
```bash
sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.6 2
update-alternatives --config python
python --version
alias python=python3
alias pip=pip3
python3 -m venv ./venv
source /home/ubuntu/environment/venv/bin/activate
```
## 깃허브 프로젝트 클론하기 / Clone project in Github

```bash
git clone https://github.com/WooSung-Jung/flask-postgresql-start-guide.git
sudo apt-get install libpq-dev python-dev
pip install records
pip install boto3
pip install -r requirements.txt
```

## 플라스크 가동 명령어 실행 / Flask run command

```bash
export FLASK_APP="app.py" 
export FLASK_DEBUG="True" 
export FLASK_ENV=development
flask run --host=0.0.0.0
```

## 생성한 플라스크 API를 로컬호스트로 확인하기 / Connect Flask API in localhost
- Create new bash shell in your OS
- Insert command at below
- confirm previous bash shell with new bash shell together

```bash
curl http://0.0.0.0:5000/check
```