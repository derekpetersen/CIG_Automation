# CIG QA Test Automation


## Product Introduction

---

Careersingear.com offers one of the widest varieties in truck driving jobs in the industry. 
Companies like US Xpress, Averitt and Werner Enterprises post here to find yard jockeys and owner operators, 
student and experienced company drivers, and veterans looking to transition back into civilian life. 
Don't just find the trucking job you need; 
find the trucking driving job you want with the trucking company that wants you.


## Automation Test Overview

---

This automation suite primarily comprises blackbox UI-driven tests, encompassing both regression and end-to-end 
scenarios.


## Tools Used

---

1. Python 3.9
   - Selenium Webdriver
   - PyTest

## Testing Structure

---

The framework follows the Page Object Model (POM) structure, with tests organized by fixtures within the code (detailed 
information can be found in the Usage section). Web elements are systematically stored in their designated POM files, 
categorized by pages or specific element groups such as Navbar or Footer. Tests reside in the designated tests folder, 
further organized into API and UI test suites.

## Usage

---
### Prerequisites

Before running any tests, its necessary to have Python 3.9 installed. This can be obtained here:
>`https://www.python.org/downloads/`

Once you have the repository downloaded, you'll need to open/launch the venv. These activate scripts are located in
`venv/bin` For example, on Windows you will need to execute the `activate.ps1` file:
>`CIG\venv\bin\activate.ps1`

### Running Tests

Running tests via terminal is preferred. To run all tests, simply run:
>`pytest`

To run a test based on a specific flag, run:
>`pytest -m <INSERT FLAG HERE>`

Pytest markers
Naming convention
Design patterns
-POM
-Singleton for WebDriver

Future potential implementations:
- Facade
   - Group complex functionality in parametrized functions, classes, or interfaces
   - Ex. CIG search job by company and haul type
     - Search job facade could be a class that manipulates the page object (not for declaration, but functions)
- Fluent
  - Chain multiple actions in a single line of code.
- ISTQB requirements (methodology): For critical applications
- Rapid Software Testing (methodology): For not so critical apps

