# flask-postgresql-start-guide

### ***Fisrt uploaded 2020-06-19 WooSung-Jung***

## Make Python3 virtual environment

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
## Make Python3 virtual environment

```bash
git clone https://github.com/WooSung-Jung/flask-postgresql-start-guide.git
sudo apt-get install libpq-dev python-dev
pip install records
pip install boto3
pip install -r requirements.txt
```

## Flask run

```bash
export FLASK_APP="app.py" 
export FLASK_DEBUG="True" 
export FLASK_ENV=development
flask run --host=0.0.0.0
```
## Connect Flask WEB in localhost
```
- Create new bash shell in your OS
- Insert command at below
- confirm previous bash shell with new bash shell together
```bash
curl http://0.0.0.0:5000/check
```