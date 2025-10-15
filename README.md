# Python Projects Collection

This repository contains several small Python projects and challenge solutions grouped by topic. The goal of this README is to give you a clear, copy‑pasteable starting point so others (and future you) can run, test, and contribute to the code.

> **Overview**
>
> * `Client-Server/` — simple client/server examples (TCP/UDP, basic RPC patterns, toy protocols).
> * `Cryptohack/` — cryptography challenge solutions and experiments (CTF-style puzzles).
> * `Exercises/` — practice scripts, algorithms, and utility snippets.
> * `IEEExtreme/` — competition solutions and problem writeups for IEEEXtreme.

---

## Quick start

1. Install Python (recommended: **Python 3.10+**).
2. Create and activate a virtual environment:

```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies (if a `requirements.txt` exists at repo root):

```bash
pip install -r requirements.txt
```

If a folder has its own `requirements.txt`, `cd` into that folder and install from there.

---

## Project folders & how to run

> These sections provide generic run instructions. Replace the example filenames with the actual scripts present in each folder.

### `Client-Server/`

Typical contents: `server.py`, `client.py` (or subfolders per protocol).

Run the server in one terminal:

```bash
cd Client-Server
python server.py
```

Run a client in another terminal:

```bash
cd Client-Server
python client.py --host 127.0.0.1 --port 9000
```

If the folder contains multiple examples, prefer running each example file the same way (e.g. `server_tcp.py`, `client_tcp.py`) and check for help flags (`-h`, `--help`).

### `Cryptohack/`

Collection of cryptography challenge solves. Example usage:

```bash
cd Cryptohack
python solve_challenge_name.py
```

Note: some scripts require third-party crypto libraries (e.g. `pycryptodome`, `cryptography`) — see `requirements.txt` in this folder.

### `Exercises/`

Small scripts and algorithm practice. Run any script directly:

```bash
cd Exercises
python example_exercise.py
```

If there are multiple independent exercises, consider grouping them into subfolders and adding an index `README` inside `Exercises/` listing the filename → purpose.

### `IEEExtreme/`

Competition problem solutions. Typically each problem has a folder or a single file.

Run a solution like this:

```bash
cd IEEExtreme/problem_code
python solution.py < input.txt
```

Add short problem descriptions and expected input/output samples next to each solution to make it easy to reproduce.

---

## Testing

Add a `tests/` folder (or per-project tests) and run with `pytest`:

```bash
pip install pytest
pytest -q
```

If you already have tests, run `pytest` from the repo root.

---

## Linting & Formatting

Recommended tools:

* `black` for formatting
* `flake8` or `ruff` for linting

Install them into your virtual environment and run against the repo:

```bash
pip install black ruff
black .
ruff check .
```

---

## How to contribute

1. Fork the repo and create a feature branch: `git checkout -b fix/your-change`.
2. Make changes and add tests where appropriate.
3. Run linters and formatters.
4. Create a PR with a clear description of the change.

Add a `CONTRIBUTING.md` if you want project-specific rules.

---

## Recommended repository improvements (TODO)

* Add a root-level `requirements.txt` or per-folder `requirements.txt` files.
* Add `README.md` files inside each top-level folder describing contents and how to run specific examples.
* Add license file (e.g. `MIT` or other) if you want to allow reuse.
* Add CI (GitHub Actions) to run tests + linters on PRs.

---

## License

Specify a license by adding a `LICENSE` file. If unsure, `MIT` is a permissive default.

---

## Contact

If you want help running a specific script, paste the filename and the output you get — I'll help debug it.

---

*Generated README template — edit the example commands and filenames to match the actual scripts in your folders.*
