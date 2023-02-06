"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Funda Find."""


if __name__ == "__main__":
    main(prog_name="funda-find")  # pragma: no cover
