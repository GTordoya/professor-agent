bank = ["TX001", "TX001", "TX002", "TX003", "TX004", "TX005", "TX007"]
ledger = ["TX002", "TX003", "TX004", "TX005", "TX006","TX007"]

uniqBank = set()
uniqLedger = set()

for t in bank:
    if t in uniqBank:
        print("Duplicate bank value:",t)
    uniqBank.add(t)

for t in ledger:
    if t in uniqLedger:
        print("Duplicate ledger value:",t)
    uniqLedger.add(t)

for t in uniqBank:
    if t not in uniqLedger:
        print("Bank transaction not in ledger: ",t)

for t in uniqLedger:
    if t not in uniqBank:
        print("Ledger transaction not in bank: ",t)
