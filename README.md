# cron-metal
Cron job that runs on deta.sh which queries metal-joke-api and sends the response as an email

## Setup

### (Optional) Copy git hooks to local .git/

From the project's root directory, run:
```bash
cp hooks/* .git/hooks/
```

## Testing

```bash
poetry run pytest
```
