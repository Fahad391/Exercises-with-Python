# Car Tracker

A small command-line app to log a car collection to disk, built as a Python practice project. Focus areas: OOP, exception handling, and using NumPy/Pandas together in one cohesive system rather than in isolation.

## What it does

- Add cars (Brand + Model) to a persistent collection
- View the full collection
- Get fleet stats: total car count and number of unique brands

## Project structure

```
car_record_practice/
├── main.py              # CLI interface — user interaction loop
├── Car_Analytics.py     # Car_Tracker class — data logic
└── Car_List.csv         # persisted data (created on first run)
```

## How it's built

**`Car_Analytics.py`** — `Car_Tracker` class
- `__init__` — ensures the storage directory exists (`os`) and loads existing data
- `_load_data()` — reads the CSV; returns an empty DataFrame if the file is missing or empty (handled via `try/except`)
- `save_data()` — writes the current DataFrame back to CSV
- `add_car(brand, model)` — appends a new row via `pd.concat`
- `show_all_cars()` — returns the DataFrame for display
- `get_total_count()` — uses `np.shape()` on the DataFrame's underlying array to count rows
- `analyze()` — uses `np.unique()` on the Brand column to compute unique brand count and list

**`main.py`**
- Instantiates `Car_Tracker`
- `manage_add_cars()` — loop for entering one or more cars, with empty-input validation, saves on exit
- `manage_show_cars()` — prints all cars row by row, then prints the NumPy-derived stats
- Top-level `while True` loop drives a simple numbered menu (Add / Show / Exit)

## What each library is doing

| Library | Role |
|---|---|
| `os` | Creates the folder the CSV lives in, so the app doesn't crash on first run |
| `pandas` | Loads, saves, appends, and displays car records as a DataFrame |
| `numpy` | Computes total car count and unique-brand analysis from the DataFrame's array form |

## Run it

```bash
python main.py
```

## Known limitations (practice-stage, not production)

- `file_path` is a relative path — the app must be run from the correct working directory, or it will look for / create the CSV in the wrong place
- No duplicate detection — the same Brand/Model can be added repeatedly
- Brand matching in `analyze()` is case-sensitive (`"Tesla"` and `"tesla"` count as different brands)
- `analyze()` computes brand counts internally but doesn't currently expose them — only the unique brand list and total are shown

## Credits

- **Design & structure:** decided independently — what to build, what tools to use, and why
- **Code:** written with Gemini, which handled most of the implementation
- **Debugging:** self + Gemini
