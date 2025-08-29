import os

import anthropic
import click


@click.command()
@click.argument("text", nargs=-1, required=False)
def main(text):
    # Raise error if no API key
    if not os.getenv("ANTHROPIC_API_KEY"):
        click.echo(
            "Error: Please set the ANTHROPIC_API_KEY environment variable.",
            err=True,
        )
        raise SystemExit(1)

    # Prefer positional args; if none, read from piped stdin
    text = " ".join(text or ())
    if not text:
        stdin = click.get_text_stream("stdin")
        text = stdin.read().strip()
    if not text:
        click.echo(
            'Usage: claude-token-count "text" or pipe input: cat file | claude-token-count',
            err=True,
        )
        raise SystemExit(1)

    client = anthropic.Anthropic()
    response = client.messages.count_tokens(
        model="claude-opus-4-1-20250805",
        messages=[
            {
                "role": "user",
                "content": text,
            }
        ],
    )
    print(response.json())


if __name__ == "__main__":
    main()
