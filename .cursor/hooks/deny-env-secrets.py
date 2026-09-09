#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path

DENY_MESSAGE = (
    "Blocked access to a secret dotenv file. Use an .env*.example template instead."
)

EXAMPLE_NAME = re.compile(r"^\.env.*\.example$")
SECRET_NAME = re.compile(r"^\.env(?:\..+)?$")
PATH_TOKEN = re.compile(r"""(?<![A-Za-z0-9._-])((?:~|\.{1,2})?(?:/?[\w.-]+)+)""")


def is_secret_dotenv(name: str) -> bool:
    if EXAMPLE_NAME.match(name):
        return False
    return SECRET_NAME.match(name) is not None


def deny() -> dict:
    return {
        "permission": "deny",
        "user_message": DENY_MESSAGE,
        "agent_message": DENY_MESSAGE,
    }


def allow() -> dict:
    return {"permission": "allow"}


def command_targets_secret(command: str) -> bool:
    for raw in PATH_TOKEN.findall(command or ""):
        name = Path(raw).name
        if is_secret_dotenv(name):
            return True
    return False


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        json.dump(deny(), sys.stdout)
        return 0

    file_path = payload.get("file_path")
    if file_path:
        result = deny() if is_secret_dotenv(Path(file_path).name) else allow()
        json.dump(result, sys.stdout)
        return 0

    command = payload.get("command")
    if command is not None:
        result = deny() if command_targets_secret(command) else allow()
        json.dump(result, sys.stdout)
        return 0

    json.dump(allow(), sys.stdout)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
