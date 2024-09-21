# peak
Peak Calculator

## Requirements

Ensure you have python >= 3.10 installed. This will likely work on older python versions,
but this has only been tested on python 3.10+.

This project is set up with the poetry package manager:
```bash
$ sudo apt install python3-poetry
```

Start the poetry shell and install the required packages:
```bash
$ poetry shell
$ poetry install
```

## Testing

To test the underlying application code:

```bash
$ pytest
```

To run the peak calculation tool:

```bash
$ peak-cli get-hours <year> <month>
# year in YYYY format: 2024
# month in m format: 2
```
