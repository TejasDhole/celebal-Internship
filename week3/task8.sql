/* Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters 
in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.
*/
/*
    Enter your query here and follow these instructions:
    1. Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
    2. The AS keyword causes errors, so follow this convention: "Select t.Field From table1 t" instead of "select t.Field From table1 AS t"
    3. Type your code immediately after comment. Don't leave any blank line.
*/
(SELECT CITY, LENGTH(CITY) AS name_length FROM STATION ORDER BY LENGTH(CITY) ASC, CITY ASC LIMIT 1) UNION (SELECT CITY, LENGTH(CITY) AS name_length FROM STATION ORDER BY LENGTH(CITY) DESC, CITY ASC LIMIT 1);
