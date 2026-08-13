# Marketing Ops Automation

## Introduction

This project is a lightweight automation toolkit designed to reduce repetitive tasks in digital marketing operations, including data cleaning, campaign QA, and performance reporting.

I work in digital marketing and data analytics, where I regularly handle data from platforms such as Google Ads, GA4, and other marketing systems. I created this project to turn common manual workflows into simple and reusable automation tools that can also be adapted by other marketers and analysts.

## Key Features

- Clean and validate CSV marketing datasets
- Check missing campaign or product information
- Calculate ROAS automatically
- Flag rows that may require manual review
- Export a clean QA result as CSV

## How to Use

1. Clone or download this repository.
2. Make sure Python 3.10+ is installed.
3. Run the script with the included sample file:

```bash
python campaign_qa.py examples/sample_data.csv
```

4. The script will create:

```text
examples/sample_data_qa_result.csv
```

## Example Checks

The current version flags:

- Missing campaign names
- Missing product/model names
- Spend greater than 0 with zero revenue
- Rows with zero spend
- Invalid numeric values
- ROAS calculation when spend is available

## Example Project Structure

```text
marketing-ops-automation/
├── README.md
├── LICENSE
├── requirements.txt
├── campaign_qa.py
└── examples/
    └── sample_data.csv
```

## Notes

This repository contains only fictional sample data. No client, company, credential, or proprietary information is included.

## License

MIT License
