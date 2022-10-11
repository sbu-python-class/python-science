# Testing

Testing is an integral part of the software development process.  We want to catch
mistakes early, before the go on to affect our results.

## Types of testing

There are a lot of different types of software testing that exist.
Most commonly, for scientific codes, we hear about:

* Unit testing : Tests that a single function does what it was designed to do

* Integration testing : Tests whether the individual pieces work together as intended.
  Sometimes done one piece at a time (iteratively)

* Regression testing : Checks whether changes have changed answers

* Verification & Validation (from the science perspective)

  * Verification: are we solving the equations correctly?

  * Validation: are we solving the correct equations?

## Automating testing

The best testing is automated.  Github provides a *continuous integration* service that can
be run on pull requests.  You write a short definition (a Github workflow) that tells Github
how to run your tests and then any time there is a change, the tests are run.

## Unit testing

* When to write tests?

  * Some people advocate writing a unit test for a specification
    before you write the functions they will test

    * This is called Test-driven development (TDD):
      https://en.wikipedia.org/wiki/Test-driven_development

  * This helps you understand the interface, return values,
    side-effects, etc. of what you intend to write

* Often we already have code, so we can start by writing tests to
  cover some core functionality

  * Add new tests when you encounter a bug, precisely to ensure that
    this bug doesn’t arise again

* Tests should be short

  * You want to be able to run them frequently



