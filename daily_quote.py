import random

quotes = [
    "If you're going through hell, keep going.",
    "More is lost by indecision than wrong decision.",
    "Worrying is like paying interest on a debt you may never owe.",
    "Be the person your dog thinks you are."
]

print(random.choice(quotes))

name: Daily Motivation

on:
  schedule:
    - cron: '0 9 * * *'  # Runs every day at 9 AM UTC

jobs:
  run-quote:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v3
      
      - name: Run Quote Script
        run: python daily_quote.py
