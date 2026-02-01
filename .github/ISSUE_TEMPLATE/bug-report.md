name: Bug Report
description: Report a bug or incorrect behavior in the wrapper
labels: bug
body:
  - type: markdown
    attributes:
      value: >
        Thanks for reporting a bug!
        Please make sure this is an issue with the wrapper itself and not the external API.

  - type: input
    attributes:
      label: Summary
      description: Briefly describe the bug
    validations:
      required: true

  - type: textarea
    attributes:
      label: Reproduction Steps
      description: Steps to reproduce the issue
    validations:
      required: true

  - type: textarea
    attributes:
      label: Minimal Code Example
      description: A short code snippet that demonstrates the bug
      render: python

  - type: textarea
    attributes:
      label: Expected Behavior
      description: What you expected to happen
    validations:
      required: true

  - type: textarea
    attributes:
      label: Actual Behavior
      description: What actually happened
    validations:
      required: true

  - type: input
    attributes:
      label: Wrapper Version
      description: Version of the wrapper you are using
    validations:
      required: true

  - type: input
    attributes:
      label: Python Version
      description: Output of `python --version`
    validations:
      required: true

  - type: checkboxes
    attributes:
      label: Checklist
      options:
        - label: I have searched for existing issues
          required: true
        - label: I am using the latest version of the wrapper
          required: true
        - label: I have removed any sensitive information (API keys, tokens, etc.)
          required: true

  - type: textarea
    attributes:
      label: Additional Context
      description: Anything else that might help