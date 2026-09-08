# Project Instructions

## Environment Variables

Never read `.env` or `.env.*` files — they contain real secrets.

For environment variable definitions and expected values, always reference `.env*.example` files instead (e.g. `.env.example`, `.env.local.example`, `.env.production.example`).

The common secret-bearing filenames are denied in `.claude/settings.json`. That list is an allowlist-by-omission: a new dotenv file under a name not on it is readable by default, so add it there when you create one.