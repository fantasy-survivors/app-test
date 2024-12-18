# App test

### install python with brew

```bash
brew update
brew upgrade
brew install python@3.11
echo 'export PATH="<python path>/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

### set up python environment

https://fastapi.tiangolo.com/virtual-environments/#upgrade-pip

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
source .venv/bin/activate
```

### start

```bash
chmod +x ./docker-up.sh  # only first time
./docker-up.sh
```

### stop

```bash
chmod +x ./docker-down.sh  # only first time
./docker-down.sh
```

### interact

```bash
docker exec -it <container id> bash
```
