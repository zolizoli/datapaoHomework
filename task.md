# Homework @DATAPAO

DATAPAO wants to acquire a commercial real estate company as a new customer.

The company is building a new smart office containing many IoT devices, but before they sign the contract for our services, they want to see how robust our solutions are.

For this reason, they would like to see some simple analytics for one of their existing offices about people coming and leaving the office.

They provided data for 2023 February for the 25 people working there (everyone gave their consent for the collection of this data)

You can download the file from here:

[datapao_homework_2023.csv](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5140b45c-2852-400b-bb65-8b1194ff8d98/new_homework_(1).csv)

There are two parts to this exercise:

1. For each person, calculate the amount of time and the number of days spent in the office during the month and write it to a CSV file containing (user_id, time, days, average_per_day, rank)

user_id - id of the user

time - net hours spent in the office (IN 8, OUT 12, IN 13, OUT 18) → this is 4 + 5 = 9 hours

days - the number of calendar days the user was present in the office

average_per_day - time/days

rank - order the employees based on the average_per_day (using Ordinal ranking)

2. Calculate who had the longest work session this month and write it to a CSV file containing (user_id, session_length)

user_id - id of the user

session_length - a work session is a time between coming to the office and leaving to go home (an office exit with no re-entry for two hours counts as going home, thus marking the end of a work session). Breaks shorter than two hours count as part of the session.

e.g. IN 8, OUT 12, IN 13, OUT 18, (IN next day)

→ this counts as one session from 8 to 18

eg. IN 8, OUT 12, IN 15, OUT 18, (IN next day) 

→ these count as two sessions from 8 to 12 and from 15 to 18

1. (optional) You have the data. Please show us your ideas. It’s an opportunity to propose an insight you think would be valuable.

Implement the assignment considering the following:

- **Language:** Python - if your skills are rusty, don't worry; just let us know. It is okay to take extra time to catch up on things before handing in your solution. After all, we want to see the best of you. 🙂
- **Libraries:** only Python Standard Library can be used (https://docs.python.org/3/library/)
- Unit Tests
- Please include the exercise outputs in your repository:
    - /output/first.csv | Header: (user_id, time, days, average_per_day, rank)
    - /output/second.csv | Header: (user_id, session_length)
- Provide detailed instructions on how to run your solution in a separate markdown file.

### How are we going to evaluate your work? ✨

For such a task, one can evaluate many things - this time, the things that we care about the most are:

- Following programming best practices (e.g., naming conventions, commenting, etc.)
- Completeness: are all requirements met? are all tests passing?
- Correctness: is the code written in a sensible, thought-out way?
- Maintainability: is it written in a clean, supportable way?

### **Code Submission**

Please create a repository on a git provider of your own choice. Then organize, design, test, and document your code as if it were going into production - then push your changes to the main branch. Please, either make the repository publicly available or share it with

- andras.fulop@datapao.com
- kornel.kovacs@datapao.com
- gergely.bokor@datapao.com
- dominik.gulacsy@datapao.com
- andras.csillag@datapao.com

and our recruiter, lilla.persik@datapao.com.

Happy coding! 🙂

The DATAPAO Team