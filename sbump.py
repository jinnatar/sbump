import click
import tomllib
import semver


def get_from_pyproject():
    with open("pyproject.toml", "rb") as f:
        pyproject = tomllib.load(f)
    return semver.Version.parse(pyproject['project']['version'])


@click.command()
def display():
    version = get_from_pyproject()
    click.echo(version)


def run():
    # By default we display the current version as read from pyproject.toml
    display()


if __name__ == "__main__":
    run()
