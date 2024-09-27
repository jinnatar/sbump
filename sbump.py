import click
import tomlkit
from tomlkit.toml_file import TOMLFile
import semver

PYPROJECT: TOMLFile = TOMLFile("pyproject.toml")


def get_from_pyproject() -> semver.Version:
    pyproject: tomlkit.TOMLDocument = PYPROJECT.read()
    version: str = str(pyproject["project"]["version"])  # pyright: ignore
    return semver.Version.parse(version)


def update_pyproject(new_version: semver.Version):
    pyproject: tomlkit.TOMLDocument = PYPROJECT.read()
    pyproject["project"]["version"] = str(new_version)  # pyright: ignore
    PYPROJECT.write(pyproject)


@click.group(invoke_without_command=True)
@click.pass_context
@click.option(
    "--dry_run/--no_dry_run",
    default=False,
    help="Don't write changes to pyproject.toml",
)
def cli(ctx, dry_run: bool):
    ctx.ensure_object(dict)
    ctx.obj['dry_run'] = dry_run
    if not ctx.invoked_subcommand:
        display()


@cli.command()  # pyright: ignore
def display():
    version = get_from_pyproject()
    click.echo(version)


@cli.command()  # pyright: ignore
@click.pass_context
def major(ctx):
    version = get_from_pyproject()
    new_version = version.bump_major()
    click.echo(new_version)
    if not ctx.obj['dry_run']:
        update_pyproject(new_version)


@cli.command()  # pyright: ignore
@click.pass_context
def minor(ctx):
    version = get_from_pyproject()
    new_version = version.bump_minor()
    click.echo(new_version)
    if not ctx.obj['dry_run']:
        update_pyproject(new_version)


@cli.command()  # pyright: ignore
@click.pass_context
def patch(ctx):
    version = get_from_pyproject()
    new_version = version.bump_patch()
    click.echo(new_version)
    if not ctx.obj['dry_run']:
        update_pyproject(new_version)
