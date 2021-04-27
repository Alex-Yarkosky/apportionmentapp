# Apportionment App

## About

Part of an undergraduate senior project on United States apportionment methods; used to do analysis for *Satisfactory Justification of the United States’ Apportionment* undergraduate senior thesis paper. The application can calculate apportionments for any appropriate house size and any Census from 1900 to 2010 with the following methods:

* Hamilton
* Jefferson
* Lowndes
* Adams
* Webster
* Dean
* Huntington-Hill

Apportionment can be done individually with results displayed in the terminal or they can be done en masse with results outputted in a CSV file. En masse apportionment can either be for a range of house sizes or be done for each Census from 1900 to 2010. En masse apportionment outputs the method name, census year, house size, and the average constituency size for the full apportionment on each line of the CSV file.

## Installation

Clone the repository by downloading the ZIP, using GitHub Desktop, or using the follow command in the terminal: `git clone https://github.com/Alex-Yarkosky/apportionmentapp.git`.

## Running

From a terminal based in the `src` folder, run the command `python apportionments.py` to run the program. Enter 0 anytime it prompts you to select a multiple choice option to exit the program.

### Running Test Suite

From a terminal based in the `test` folder, run the command `pytest` to run all of the tests in the `test_apportionment.py` file.
