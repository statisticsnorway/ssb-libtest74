"""Command-line interface."""

import click


@click.command()
@click.version_option()
def main() -> None:
    """SSB Libtest74."""


if __name__ == "__main__":
    main(prog_name="ssb-libtest74")  # pragma: no cover
