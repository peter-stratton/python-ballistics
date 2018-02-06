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
def testpypi(ctx):
    ctx.run('twine upload --repository-url https://test.pypi.org/legacy/ dist/* ')
