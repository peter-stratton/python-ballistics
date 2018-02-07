from invoke import task


@task
def clean(ctx, docs=False, bytecode=False, extra=''):
    patterns = ['build']
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
    ctx.run('python setup.py sdist bdist_wheel')
    if docs:
        ctx.run('sphinx-build docs docs/_build')


@task
def runtests(ctx, html=False):
    if html:
        ctx.run('pytest -v --cov-report html --cov=ballistics tests/')
    else:
        ctx.run('pytest -v --cov=ballistics tests/')


@task
def testpypi(ctx):
    ctx.run('twine upload --repository-url https://test.pypi.org/legacy/ dist/* ')


@task
def genreq(ctx):
    """
    Generates a requirements.txt file
    """
    ctx.run('pipenv lock --requirements --dev > requirements.txt')
