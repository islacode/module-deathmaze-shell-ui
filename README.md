# module-deathmaze-shell-ui

## Environment Variables

AI agents in this repo cannot read `.env`/`.env.*` files (denied by agent config); use `.env*.example` files as the reference for variable definitions and expected values.

If a new `.env*` file is added under a name not already covered by that deny list, the agent config files (`.claude/settings.json`, `.agents/settings.json`, `.codex/config.toml`, `.cursor/cli.json`) must be updated to include it.