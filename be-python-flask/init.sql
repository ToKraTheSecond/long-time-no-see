CREATE TABLE encounters
(
    person_id SERIAL PRIMARY KEY,
    person VARCHAR(255),
    date_of_meeting VARCHAR(255),
    what_we_did VARCHAR(255)
);