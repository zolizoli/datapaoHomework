# Homework @DATAPAO

## Assumptions about the input
We DON'T test most of our assumptions, we posit that
we get consistent and relatively well-formed data.
We used `assert` where we wanted to check data
integrity.

+ The schema of the csv file is fixed
+ We don't deal with other months right now
+ `GATE_IN` & `GATE_OUT` has been written to the file
in consecutive order for `user_id`

## Assumptions about the task
+ Input csv can grow without any limit, we
have to be able to process very big files
+ We are building a prototype, we don't
want to deploy the code right now. Probably
a junior colleague will continue our work.

## Notes
+ Made with `Python 3.11.2`
+ Dev dependencies: `black` & `isort`
+ Feel free to run it as it is since it has no
any external dependency
+ Run: ```python src/csv_magic.py```
+ Test: ```python -m unittest  discover tests/```

## Final remarks
+ Project started at 2023-05-25, 12:00
+ Project finished at 2023-05-25, 21:22
 (except for final editing)
+ Number of distractions: 4
+ Time spent on distractions and breaks: 3:37