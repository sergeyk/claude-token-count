# Claude Token Count

Simple way to use the Anthropic token counting endpoint [docs](https://docs.anthropic.com/en/docs/build-with-claude/token-counting).

Must have `ANTHROPIC_API_KEY` set in your environment.

```
> uvx claude-token-count "Hello, world"
{"input_tokens":10}
```

or

```
> echo "Hello, world" | uvx claude-token-count
{"input_tokens":10}
```

Have fun!
