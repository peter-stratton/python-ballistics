from invoke import task


@task
def clean(ctx, docs=False, bytecode=False, extra=''):
    patterns = ['build', 'src/*.egg-info']
    if docs:
        patterns.append('docs/_build')
    if bytecode:
        patterns.append('**/*.pyc')
    if extra:
        patterns.append(extra)
    for pattern in patterns:
        ctx.run("rm -rf {}".format(pattern))


@task
def build(ctx, docs=False):
    ctx.run('python setup.py clean --all sdist bdist_wheel')
    if docs:
        ctx.run('sphinx-build docs docs/_build')


@task
def runtests(ctx, html=False):
    if html:
        ctx.run('pytest -v --cov-report html --cov=ballistics tests/')
    else:
        ctx.run('pytest -v --cov=ballistics tests/')


@task
def deploy(ctx, testserver=False):
    if testserver:
        ctx.run('twine upload --repository-url https://test.pypi.org/legacy/ --skip-existing dist/*.whl dist/*.gz')
    else:
        ctx.run('twine upload --skip-existing dist/*.whl dist/*.gz')


@task
def genreq(ctx):
    """
    Generates a requirements.txt file
    """
    ctx.run('pipenv lock --requirements --dev > requirements.txt')
