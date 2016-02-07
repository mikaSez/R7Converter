Feature: Parametrize
  In order to have the same look and feel as in EAST
  I need most of the param to be converted to Reveal syntax

  Scenario: All enabled
    Given all params with oui as text
     When I init my param class
     Then my class anwer only truth

  Scenario: Comms are disabled
    Given Usually coms are not translated in EAST
     When I init my param class
     Then my class should have false in comms

