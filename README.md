# Marketing Ops Automation Toolkit

A lightweight open-source toolkit for automating repetitive **digital marketing operations, reporting, and campaign QA** tasks.

This project is based on workflows I encounter in my day-to-day work as a **Digital Analyst**, managing and analyzing paid media and e-commerce performance across multiple markets.

---

## About Me

I work in digital marketing analytics and performance operations, supporting campaigns across multiple markets.

My daily work involves handling data from platforms such as:

* Google Ads
* Search Ads 360
* Campaign Manager 360
* Google Analytics 4
* Excel / Power Query
* Various campaign, product, and e-commerce data sources

A large portion of this work involves repetitive processes such as combining datasets, checking campaign setups, validating product information, identifying inconsistencies, and preparing recurring reports.

I started building small automation workflows to reduce these manual tasks and make the process more reliable and reusable.

This repository is an attempt to organize those workflows into a simple toolkit that other digital marketers and analysts can also adapt to their own work.

---

## Why This Project Exists

Marketing operations often involve surprisingly manual work.

A typical workflow may require an analyst to:

1. Download data from several platforms
2. Combine files from different markets
3. Standardize campaign and product naming
4. Check missing or inconsistent values
5. Compare performance against predefined rules
6. Flag issues requiring manual review
7. Prepare the same reporting format every week

Each individual task is simple, but repeating the process across many campaigns, products, and markets takes significant time.

The goal of this project is to automate as much of that workflow as possible while keeping the output easy for non-developers to understand.

---

## What This Toolkit Automates

### 1. Marketing Data Cleaning

Standardizes common marketing datasets such as campaign, product, and performance reports.

Examples:

* Normalize column names
* Clean campaign naming
* Standardize country and market codes
* Handle missing values
* Remove duplicated rows
* Convert dates and numeric fields
* Merge multiple CSV or Excel exports

---

### 2. Campaign QA

Automatically checks campaign data against predefined rules and highlights potential issues.

Examples:

* Missing campaign names
* Missing landing page URLs
* Duplicate assets
* Inconsistent product names
* Invalid or missing model IDs
* Unexpected campaign status
* Missing performance data
* Naming convention violations

Instead of manually reviewing every row, the analyst can focus only on the records that require attention.

---

### 3. Performance Monitoring

Creates simple summaries from raw performance data.

Supported metrics can include:

* Spend
* Revenue
* Conversions
* CPC
* CVR
* CPA
* ROAS

The toolkit can also flag unusual changes such as:

* Sudden spend increases
* Significant ROAS decline
* Conversion drops
* Missing daily data
* Large differences between reporting sources

---

## Example Workflow

```text
Raw Marketing Data
        ↓
Data Cleaning
        ↓
Standardization
        ↓
Campaign / Product QA
        ↓
Performance Checks
        ↓
Issue Flags
        ↓
Automated Summary
```

Instead of reviewing the entire dataset manually, the user receives a smaller list of items that actually require investigation.

---

## Example

### Input

```csv
market,campaign,model,spend,revenue
MX,TV_AON,OLED65C5,1200,9600
MX,TV_AON,,800,2100
CO,REF_PROMO,GB41WGT,500,0
```

### Output

```text
Marketing QA Summary

[WARNING]
MX / TV_AON
Missing product model

[CHECK]
CO / REF_PROMO / GB41WGT
Revenue is 0 despite recorded media spend

[OK]
MX / TV_AON / OLED65C5
ROAS: 8.0
```

---

## Who This Is For

This project is designed primarily for:

* Digital marketers
* Performance marketers
* Marketing analysts
* E-commerce analysts
* Media agency teams
* Marketing operations teams

Especially those who spend too much time manually cleaning spreadsheets and checking campaign data.

The goal is not to replace marketing judgment.

The goal is to automate repetitive checks so analysts can spend more time on **analysis, problem solving, and decision making**.

---

## Project Principles

### Practical

The workflows should solve problems that actually occur in day-to-day marketing operations.

### Simple

Users should not need to be software engineers to understand or modify the workflow.

### Reusable

Rules and templates should be adaptable across different companies, markets, and campaign structures.

### Transparent

Automation should clearly explain why something was flagged instead of producing a black-box result.

---

## Planned Features

* [ ] CSV / Excel campaign data ingestion
* [ ] Automated data cleaning
* [ ] Campaign naming validation
* [ ] Product / model QA
* [ ] Landing page validation
* [ ] Performance anomaly detection
* [ ] ROAS / CPA monitoring
* [ ] Multi-market reporting
* [ ] Markdown summary generation
* [ ] Configurable QA rules
* [ ] AI-assisted issue summaries

---

## AI & Codex

I am not a full-time software engineer.

My background is in **digital marketing and analytics**, and most of the problems in this repository come directly from operational challenges I encounter in real marketing workflows.

AI coding tools such as OpenAI Codex make it possible for domain specialists to turn their knowledge of these problems into working automation tools.

I plan to use Codex to help:

* Develop reusable automation modules
* Improve code quality
* Write tests
* Refactor workflows
* Expand documentation
* Build additional marketing QA rules
* Make the toolkit easier for non-developers to use

I am particularly interested in exploring how AI-assisted development can help bridge the gap between **domain expertise and software development**.

---

## Open Source

The long-term goal of this repository is to build a collection of simple, reusable marketing operations automations.

Real company data, client information, credentials, and proprietary campaign information are **not included** in this repository.

All examples use fictional or anonymized data so the workflows can be safely shared and adapted by others.

Contributions, suggestions, and new workflow ideas are welcome.
