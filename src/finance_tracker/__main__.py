"""Start the Streamlit shell on loopback, independently of local config files."""

from pathlib import Path
import subprocess
import sys


def main() -> int:
    if sys.version_info[:2] != (3, 14):
        print("Finance Tracker requires Python 3.14.x.", file=sys.stderr)
        return 1
    return subprocess.call(
        [
            sys.executable, "-m", "streamlit", "run",
            str(Path(__file__).with_name("app.py")),
            "--server.address=127.0.0.1",
            "--server.headless=true",
            "--browser.gatherUsageStats=false",
            "--server.enableCORS=true",
            "--server.enableXsrfProtection=true",
        ]
    )


if __name__ == "__main__":
    raise SystemExit(main())
