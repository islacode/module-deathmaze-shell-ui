# Project Instructions

## Environment Variables

Never read `.env` or `.env.*` files, except `.env*.example` templates.
Non-example files contain real secrets.

For environment variable definitions and expected values, reference
`.env*.example` files only (for example, `.env.example`, `.env.local.example`,
and `.env.production.example`).

The common secret-bearing filenames are denied in `.agents/settings.json`.
When adding a new secret-bearing dotenv filename, add it to the deny rules
in `.agents/settings.json`, `.claude/settings.json`, `.codex/config.toml`,
and `.cursor/cli.json`.
