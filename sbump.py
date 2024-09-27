import click


@click.command()
def display():
    click.echo('0.0.42')


def run():
    # By default we display the current version as read from pyproject.toml
    display()


if __name__ == "__main__":
    run()
