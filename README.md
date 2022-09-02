<div align="center">
<img src="./docs/static/img/logo_app.png" alt="drawing" width="400"/>
<a href="https://richionline-portfolio.nw.r.appspot.com"><img src="https://falken-home.herokuapp.com/static/home_project/img/falken_logo.png" width=50 alt="Personal Portfolio web"></a>

![Version](https://img.shields.io/badge/version-1.0.0-blue) ![GitHub language count](https://img.shields.io/github/languages/count/falken20/pomodoro) ![GitHub Top languaje](https://img.shields.io/github/languages/top/falken20/pomodoro) ![Test coverage](https://img.shields.io/badge/test%20coverage-0%25-green) ![GitHub License](https://img.shields.io/github/license/falken20/pomodoro)


[![Richi web](https://img.shields.io/badge/web-richionline-blue)](https://richionline-portfolio.nw.r.appspot.com) [![Twitter](https://img.shields.io/twitter/follow/richionline?style=social)](https://twitter.com/richionline)

</div>


---
App for helping to apply the pomodoro technic.


##### Setup

```bash
pip install -r requirements.txt
```

##### Running the app

```bash
python ./src/pomodoro.py
```

##### Script check project

```bash
./scripts/check_project.sh
```

##### Setup tests

```bash
pip install -r requirements-test.txt
```

##### Running the tests with pytest and coverage

```bash
./scripts/coverage.sh
```
or
```bash
coverage run -m pytest -v && coverage html --omit=*/venv/*,*/tests/*
```
---

##### Versions

1.0.0 First version
