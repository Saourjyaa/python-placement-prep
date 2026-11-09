# Practical Git exercise

Use the Week 1 temperature converter without pretending that the workflow has already happened:

```bash
git switch -c fix-temperature-input
# improve 03_temperature_converter.py and test it
git add Week-01-Python-Basics/exercises/03_temperature_converter.py
git commit -m "Fix invalid temperature input"
git push -u origin fix-temperature-input
```

Open a pull request on GitHub, request a review, merge it after approval, and delete the branch. Replace `origin` if your remote has another name.
