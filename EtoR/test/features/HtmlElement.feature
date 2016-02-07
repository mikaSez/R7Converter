Feature: Html element
  In order to generate the main content
  I need to have a class representing html elements
  This class is only needed for representation

  Scenario: Wrap all around
    Given a new element is created
    Then its name should wrap the content

  Scenario: Nested elements
    Given a new element is created
    When i insert another element
    Then second element is printed inside the first