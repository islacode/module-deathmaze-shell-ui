# Project Instructions

## Environment Variables

Never read `.env` or `.env.*` files, except `.env*.example` templates.
Non-example files contain real secrets.

For environment variable definitions and expected values, reference
`.env*.example` files only (for example, `.env.example`, `.env.local.example`,
and `.env.production.example`).

The common secret-bearing filenames are denied in `.codex/config.toml`.
When adding a new secret-bearing dotenv filename, add it to the deny rules
in both `.codex/config.toml` and `.claude/settings.json`.
