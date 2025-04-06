# Grocery Price Logger

This Python script allows users to input grocery items and their prices per pound, then saves the list to a formatted text file. It supports flexible input and displays the recorded prices.

## Features
- Input grocery name and price (as many as needed)
- Type `done` to stop input
- Saves the list to a file (`grocery_price.txt`)
- Formats prices to two decimal places
- Displays the contents of the file

## Getting Started

### Prerequisites
- Python 3.x

### Running the Program
```bash
python grocery_price_logger.py
```

### Sample Run
```
Enter grocery items and their prices per pound.
Enter grocery name (or 'done' to finish): Apples
Enter the price of Apples per pound: 3.25
Enter grocery name (or 'done' to finish): Flour
Enter the price of Flour per pound: 2.50
Enter grocery name (or 'done' to finish): done

--- Grocery Price List ---
Apples, Price: $3.25 per pound
Flour, Price: $2.50 per pound
```

## Files
- `grocery_price_logger.py`: Python script
- `grocery_price.txt`: Output file generated after running
- `README.md`: Documentation

## Future Improvements
- Support for CSV or JSON output
- Add total cost of all groceries
- GUI interface for user-friendly input

## Author
Nasim Bayati

---
A handy utility script to log and view grocery prices in a formatted text file!
