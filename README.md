# ✨ Dani's Weather Project ✨

## Project Description
> Everyday we collect data about the weather in order to predict the forecast for the coming days. The problem is that this data is never in a human readable format, that’s where you come in! Your task is to process csv files containing data about the weather, and convert them into meaningful text-based summaries.

### Starter Code
> Some starter code has been provided to help you get started. Weather.py contains several functions, most of which are to be completed (by you!). To help you understand what each function is meant to do, they each contain something called a “docstring”.
Also provided is a run_tests.py file, and a tests directory. You won't actually be running the weather.py file, instead, the tests will run it for you. More on this later...

### Docstrings
> A docstring is a comment that describes exactly what the function does, including it’s arguments and what it should return.
Let’s look at this read_csv_file function as an example:

```
def read_csv_file(file_name):
      '''Reads a csv file and returns the data as a list.
      Args:
            file_name: a string representing the path and name of a csv file.
      Returns: a list.
      '''
      pass
```

> The first line in the docstring gives an overview of the function.
>> In this case, this function will read a csv file and return a list.
> “Args” are the arguments/parameters that the function accepts.
>> In this case, this function accepts only one argument called file_name, which is a string representing the path to a csv file, e.g. 'data/some_weather_data.csv'.
> “Returns” is what the function is meant to return when the function is complete.
>> In this case, it should return a list.
> So this docstring is telling us that this function should read a csv file, save the data to a list, and return that list.

### Tests
> More often than not, when working on a programming project you will be required to run your code against tests.
Tests help you to ensure that your code has the expected behavior and is correct for a variety of different inputs.
As mentioned above, the starter code includes a run_tests.py file, and a tests directory.
To test your code, run this run_tests.py file.
This will give a lot of output, and that’s not a bad thing and it’s nothing to worry about!
If you look in the tests directory, you’ll see a bunch of different files. Each of these files have a bunch of tests for a single function in weather.py. 
Since you are running this file for the first time, all of those tests are going to fail, because you haven’t written any code to make those functions work yet. As you complete more and more of the functions, less and less tests will fail, and that output will eventually be reduced to a few lines.
In the meantime, let’s understand how to read that output. Here’s a snippet of the output:

```
======================================================================
FAIL: test_convert_f_to_c (tests.test_convert_f_to_c.ConvertTempTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File
"/Users/hayley/Projects/she-codes/Python-content/Python_P.C.1/starter/tests/test_convert_f_to_c.py", line
15, in test_convert_f_to_c
       self.assertEqual(result, expected_result)
AssertionError: None != 32.2
```

The white lines are the ones we care about:
- FAIL:test_convert_f_to_c(tests.test_convert_f_to_c.ConvertTempTests)
  - This is the test that failed. If I wanted to see exactly what that test is doing, then I could look at the function called test_convert_f_to_c in the tests/test_convert_f_to_c.py file. From the file name and name of this test, I know that the function it tried to call in my weather.py file was the convert_f_to_c() function.
- AssertionError:None!=32.2
  - This is what the error was. In this case, it is telling me that when the test called my convert_f_to_c() function in the weather.py file, my function returned None but the test was expecting 32.2

To make this a little less daunting, you might prefer to only run a few tests at a time. You can do this by looking for the following lines in run_tests.py:

```
runner.run(unittest.TestSuite((unittest.makeSuite(ConvertDateTests))))
runner.run(unittest.TestSuite((unittest.makeSuite(ConvertTempTests))))
runner.run(unittest.TestSuite((unittest.makeSuite(CalculateMeanTests))))
runner.run(unittest.TestSuite((unittest.makeSuite(LoadCSVTests))))
runner.run(unittest.TestSuite((unittest.makeSuite(FindMinTests))))
runner.run(unittest.TestSuite((unittest.makeSuite(FindMaxTests))))
runner.run(unittest.TestSuite((unittest.makeSuite(GenerateSummaryTests))))
runner.run(unittest.TestSuite((unittest.makeSuite(GenerateDailySummaryTests))))
```

Each line corresponds to a function in weather.py, so if you wanted to just start with the function for
calculating means, you could comment out all the other tests to make the output shorter and easier to read:

```
# runner.run(unittest.TestSuite((unittest.makeSuite(ConvertDateTests))))
# runner.run(unittest.TestSuite((unittest.makeSuite(ConvertTempTests))))
runner.run(unittest.TestSuite((unittest.makeSuite(CalculateMeanTests))))
# runner.run(unittest.TestSuite((unittest.makeSuite(LoadCSVTests))))
# runner.run(unittest.TestSuite((unittest.makeSuite(FindMinTests))))
# runner.run(unittest.TestSuite((unittest.makeSuite(FindMaxTests))))
# runner.run(unittest.TestSuite((unittest.makeSuite(GenerateSummaryTests))))
# runner.run(unittest.TestSuite((unittest.makeSuite(GenerateDailySummaryTests))))
```

## Project Requirements
Your job is to make all of the tests pass!
Do not make any changes to anything in the tests directory or run_tests.py file (aside from commenting some tests while you are working). The contents of your weather.py file will be copied into a new directory and run against the original tests, so if you have changed any tests in your own repo, your code will likely fail upon submission.

### Submission
Please submit the following:
1. A text file containing a link to your project repository.
2. Include a screenshot of your code passing all of the tests in Terminal/Powershell.

