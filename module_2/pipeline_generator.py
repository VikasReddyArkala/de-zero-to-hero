

def read_orders(filepath):
    """Stage 1: Read raw rows from CSV one at a time."""
    import csv
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row

def parse_amounts(records):
    """Stage 2: Convert amount from string to float. Recieves a generator, yields a generator."""
    for record in records:
        try:
            record['amount'] = float(record['amount'])
        except ValueError:
            record['amount'] = None
        yield record

def filter_completed(records):
    """Stage 3: Only pass through completed orders."""
    for record in records:
        if record['status'].lower() == 'completed':
            yield record

def flag_high_value(records, threshold = 400.0):
    """Stage 4: Add a 'high_value' flag for orders above a certain amount."""
    for record in records:
        # if record['amount'] is not None and record['amount'] > threshold:
        #     record['high_value'] = True
        # else:
        #     record['high_value'] = False

        record['high_value'] = True if record['amount'] is not None and record['amount'] > threshold else False
        yield record

def calculate_revenue(records):
    """Final stage: Comsume the generator and compute total revenue."""
    total = 0.0
    count = 0
    high_value_count = 0

    for record in records:
        if record['amount'] is not None:
            total += record['amount']
            count += 1

            if record['high_value'] == True:
                high_value_count += 1

    return total, count, high_value_count

raw = read_orders("orders_large.csv")
parsed = parse_amounts(raw)
completed = filter_completed(parsed)
flagged = flag_high_value(completed)

revenue, count, high_value_count = calculate_revenue(flagged)

print(f"Processed {count:,} completed orders")
print(f"Total revenue: ${revenue:,.2f}")
print(f"High-value orders: {high_value_count}")