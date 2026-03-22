import os
import sys
import subprocess
import time
from pathlib import Path
from datetime import datetime

WATCH_DIRS = [
    "templates",
    "seed_data",
    "developer_data",
    "build",
]
DB_PATH = "database/portfolio.db"


def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")


def clean_and_rebuild():
    try:
        log("🔄 Change detected. Rebuilding...")

        # Delete database
        if os.path.exists(DB_PATH):
            os.remove(DB_PATH)
            log("✅ Deleted portfolio.db")

        # Seed database
        subprocess.run([sys.executable, "-m", "database.seed"], check=True)
        log("✅ Seeded database")

        # Build site
        subprocess.run([sys.executable, "-m", "build.build"], check=True)
        log("✅ Built site")

        log("🎉 Ready! Check localhost:8000")
    except Exception as e:
        log(f"❌ Error: {e}")


def get_file_times():
    """Get modification times of watched files"""
    times = {}
    for dir_name in WATCH_DIRS:
        if os.path.exists(dir_name):
            for root, dirs, files in os.walk(dir_name):
                for file in files:
                    filepath = os.path.join(root, file)
                    times[filepath] = os.path.getmtime(filepath)
    return times


def main():
    log("👀 Watching templates/ and seed_data/ for changes...")
    file_times = get_file_times()

    try:
        while True:
            time.sleep(1)
            current_times = get_file_times()

            # Check for new/modified files
            for filepath, mtime in current_times.items():
                if filepath not in file_times or file_times[filepath] != mtime:
                    clean_and_rebuild()
                    file_times = current_times
                    break
    except KeyboardInterrupt:
        log("\n👋 Watch mode stopped")


if __name__ == "__main__":
    main()
