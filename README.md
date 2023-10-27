# PythonSelenium-Automation-Sample

This is a simple Automation Sample using Gherkin (Behave), Selenium and Python. The Code is unusable as it is but it is provided like that to present the thought process behind class, step, page and function creation and usage in a test.

We are breaking up each component by Page, Feature Files and Step Files while saving the data in separate files and creating functions to be used in each one of the page. We first create the Feature File Scenarios and then initialize the steps.py file steps. 
Also, we are creating the methods needed for each step in the respective page file and call them in steps. Assertions are primarily created in the step level (but some of them could be also created in page files).

This README provides an overview of a generic sample project that demonstrates the use of Python, Behave, and Selenium for automated testing. This project serves as a template and guide for creating and running BDD (Behavior-Driven Development) tests with Selenium in a Python environment.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Writing Feature Files](#writing-feature-files)
- [Writing Step Definitions](#writing-step-definitions)
- [Running Tests](#running-tests)
- [Customization](#customization)
- [CI/CD Integration](#cicd-integration)
- [Best Practices](#best-practices)



## Prerequisites

Before getting started with this sample project, make sure you have the following prerequisites installed:

- [Python](https://www.python.org/) (Python 3.x recommended)
- [pip](https://pip.pypa.io/en/stable/installation/) (Python package manager)
- [Selenium](https://selenium-python.readthedocs.io/installation.html) (Python Selenium package)
- [Behave](https://behave.readthedocs.io/en/latest/install.html) (Python BDD framework)
- [Webdriver](https://www.selenium.dev/documentation/en/webdriver/driver_requirements/) (e.g., ChromeDriver) for your browser of choice
- A text editor or integrated development environment (IDE) of your choice

## Project Structure

The project structure is organized as follows:

```
generic-project-structure/
├── features/
| ├── sample.feature
├── step_definitions/
| ├── sample_steps.py
├── utils/
| ├── webdriver.py
├── .gitignore
├── pip_requirements.txt
├── README.md
```

- `features/`: This directory contains your Behave feature files (written in Gherkin syntax).
- `step_definitions/`: Place your Python step definition files.
- `utils/`: Store utility files, such as webdriver setup and configuration.
- `.gitignore`: List of files and directories to ignore when using version control with Git.
- `requirements.txt`: Python package requirements for your project.
- `README.md`: The document you are currently reading.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/behave-sample-project.git
   ```
2. Navigate to the project directory:

  ```bash
  cd generic-project-structure
  ```

3. Install project dependencies using pip:
  
  ```bash
  pip install -r pip_requirements.txt
  ```

## Writing Feature Files
Feature files are written in Gherkin syntax and reside in the features/ directory. To create a new feature file:

1. Create a new .feature file (e.g., sample.feature) in the features/ directory.

2. Write your feature scenarios using Gherkin syntax. Example:

```gherkin
Feature: Sample Feature
  Scenario: Verify a web page title
    Given I open the website
    Then the page title should contain "Sample Page"
```

## Writing Step Definitions
Step definition files are written in Python and reside in the step_definitions/ directory. To create step definitions for your feature files:

1. Create a Python file (e.g., sample_steps.py) in the step_definitions/ directory.
2. Write Python code to implement the steps defined in your feature file.

## Running Tests
To run the sample tests, use the following command:

  ```bash
  behave
  ```

Behave will execute the feature scenarios and display the results in the console.

## Customization
You can customize the behavior of the project by modifying the utils/webdriver.py file for webdriver configuration, and by adding more features and step definitions for your specific testing needs.

## CI/CD Integration
To integrate this project into our CI/CD pipeline, we can use Behave for our automated testing. Ensure that our CI/CD environment supports the necessary dependencies and webdriver setup.

## Best Practices
- Keep our feature files focused, readable, and easy to understand.
- Write clear and concise step definitions that map to our feature scenarios.
- Organize our project structure for maintainability and reusability.
- Regularly update dependencies for the latest features and security patches.
