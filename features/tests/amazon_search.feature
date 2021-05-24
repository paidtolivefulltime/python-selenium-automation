# Created by rleft at 5/24/2021
  #Enter feature name here
Feature: Test Amazon Search
  # Enter feature description here

   # Enter scenario name here
  Scenario: User can search for a product
    # Enter steps here
   Given Open Amazon page
    When Input Table in search field
    And Click on Amazon search icon
    Then Verify search worked