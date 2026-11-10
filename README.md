# Fat Burner — Bonus Version (STARTING FILES)

These are **starting files** for the Monet+ Python **bonus** lesson.

In Google Classroom you will get short tasks to change this project until it
matches the **Bonus final version** (CML + skinfolds / age / body-fat stats).

Do **not** treat this folder as finished homework. Wire it step by step as instructed.

## What you are learning

Same architecture idea as the basic version, with richer user data:

1. **frontend** (`frontend_controller.py`) — screen / buttons  
2. **service** (`service.py`) — business rules (users, CML, fat estimates)  
3. **repository** (`repository.py`) — persistence beyond one program run  

Important rule:

- frontend talks to **service**
- service talks to **repository**
- frontend must **not** import repository

You do **not** need to invent guizero widgets today. The screen layout is already here.
Your job is mainly to **connect the layers** (and understand why).

## Files

| Layer | File | Role |
|---|---|---|
| Entry | `main.py` | starts the app |
| Frontend / controller | `frontend_controller.py` | UI; calls service functions |
| Service | `service.py` | users, CML, fat % / fat kg |
| Repository | `repository.py` | Google Sheets save details |

Bonus version scope:

- users: `name`, `weight`, `reference`, `skinfolds_sum`, `age_in_years`
- stats: CML + estimated body-fat balance  
- saved row: `date`, `weight`, `skinfolds_sum`, `bmr`, `cml`

## Setup (once)

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

For this lesson, use the **shared class Google Sheet / service account JSON**
already provided with the project (details in Classroom).

Later (not required today): you may create your own Google service account and sheet.

## Run

```bash
python main.py
```

## How to work

1. Open Classroom and follow the TODO / wiring steps there.  
2. Change only what Classroom asks (usually a few function calls).  
3. Test after each step: register → show stats → save → check the sheet.  
4. Keep layers clean: no repository imports in the frontend.

## Goal checklist (Bonus final)

- [ ] App opens and you can switch Existing user / Register  
- [ ] Register adds a user (name, weight, sex, skinfolds, age)  
- [ ] Show my stats prints CML and fat balance for the selected user  
- [ ] Save today writes a row through service → repository  
- [ ] Frontend does not talk to repository directly  

When Classroom says you are done, your project should match the Bonus final version.
