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


  Scenario: Adding one attribute
    Given a new element is created
    When i add an attribute
    Then this attribute is added to the class

  Scenario: Appending an attribute
    Given an element with class attribute
    When i add a class attribute
    Then the element has both attributes