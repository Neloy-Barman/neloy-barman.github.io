## Quick Start (One-time setup)

- Delete `portfolio.db`.
- python -m database.seed
- python -m build.build
- python -m watch
- python -m http.server 8000
- Check with `localhost:8000` in the browser
- All the data are being fetched from database/seed.py

## Development Workflow (Recommended)

### Terminal 1: Start the watch script

```
python -m watch
```

This will automatically rebuild the site whenever you modify files in `templates/` or `seed_data/`.

### Terminal 2: Start the local server

```
cd output
python -m http.server 8000
```

Then just:

- Edit any HTML template or seed data file
- Save the file
- The watch script automatically rebuilds everything
- Refresh `localhost:8000` to see your changes

**Note:** The watch script monitors `templates/` and `seed_data/` directories for changes and automatically:

1. Deletes the database
2. Reseeds it
3. Rebuilds the site
