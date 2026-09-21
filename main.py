"""Telegram bot service entry point."""
from pathlib import Path
import runpy

runpy.run_path(str(Path(__file__).with_name("bot.py")), run_name="__main__")
