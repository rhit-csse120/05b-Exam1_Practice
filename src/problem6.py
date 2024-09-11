"""
PRACTICE Exam 1, problem 6.

Authors: David Mutchler, Rachel Krohn, Dave Fisher, Shawn Bohner, Sriram Mohan,
         Amanda Stouder, Vibha Alangar, Mark Hays, Dave Henthorn, Matt Boutell,
         Scott McClellan, Yiji Zhang, Mohammed Noureddine, Steve Chenoweth,
         Claude Anderson, Michael Wollowski, Chandan Rupakheti,
         Derek Whitley, Curt Clifton, Valerie Galluzzi, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

"""
Academic Integrity: I got help on this module from:
         PUT_HERE_THE_NAMES_OF_PEOPLE_WHO_HELPED_YOU_ON_THIS_MODULE_(IF_ANY).
"""  # TODO: If you got help from anyone on this module, list their names here.

###############################################################################
# Students:
#
# These problems have DIFFICULTY and TIME ratings:
#  DIFFICULTY rating:  1 to 10, where:
#     1 is very easy
#     3 is an "easy" Test 1 question.
#     5 is a "typical" Test 1 question.
#     7 is a "hard" Test 1 question.
#    10 is an EXTREMELY hard problem (too hard for a Test 1 question)
#
#  TIME ratings: A ROUGH estimate of the number of minutes that we
#     would expect a well-prepared student to take on the problem.
#
#  IMPORTANT: For ALL the problems in this module,
#    if you reach the time estimate and are NOT close to a solution,
#    STOP working on that problem and ASK YOUR INSTRUCTOR FOR HELP
#    on it, in class or via Piazza.
###############################################################################
import testing_helper
import time


def main():
    """Calls the   TEST   functions in this module."""
    run_test_problem6()


def run_test_problem6():
    """Tests the   problem6   function."""
    print()
    print("--------------------------------------------------")
    print("Testing the   problem6  function:")
    print("--------------------------------------------------")

    format_string = "    problem6( {}, {}, {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = (4 / 3) + (5 / 6) + (6 / 9) + (7 / 12)
    # which is approximately 3.4166666666666665
    print_expected_result_of_test(
        [3, 1, 4], expected, test_results, format_string, suffix="  (approximately)"
    )
    actual = problem6(3, 1, 4)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results, precision=8)

    # Test 2:
    expected = 1.9999999999999998  # approximately
    print_expected_result_of_test(
        [3, 10, 6], expected, test_results, format_string, suffix="  (approximately)"
    )
    actual = problem6(3, 10, 6)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results, precision=8)

    # Test 3:
    expected = 0.5150565563468789  # approximately
    print_expected_result_of_test(
        [1, 20, 4], expected, test_results, format_string, suffix="  (approximately)"
    )
    actual = problem6(1, 20, 4)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results, precision=8)

    # Test 4:
    expected = 3.7822668072668075  # approximately
    print_expected_result_of_test(
        [4, 10, 10], expected, test_results, format_string, suffix="  (approximately)"
    )
    actual = problem6(4, 10, 10)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results, precision=8)

    # Test 5:
    expected = 16.430727605727608  # approximately
    print_expected_result_of_test(
        [30, 10, 11], expected, test_results, format_string, suffix="  (approximately)"
    )
    actual = problem6(30, 10, 11)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results, precision=8)

    # Test 6:
    expected = 63.02261904761905  # approximately
    print_expected_result_of_test(
        [100, 4, 8], expected, test_results, format_string, suffix="  (approximately)"
    )
    actual = problem6(100, 4, 8)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results, precision=8)

    # Test 7:
    expected = 62.41296296296296  # approximately
    print_expected_result_of_test(
        [99, 4, 8], expected, test_results, format_string, suffix="  (approximately)"
    )
    actual = problem6(99, 4, 8)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results, precision=8)

    # Test 8:
    expected = 63.63227513227513  # approximately
    print_expected_result_of_test(
        [101, 4, 8], expected, test_results, format_string, suffix="  (approximately)"
    )
    actual = problem6(101, 4, 8)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results, precision=8)

    # Test 9:
    expected = 54.196512303485996  # approximately
    print_expected_result_of_test(
        [101, 5, 7], expected, test_results, format_string, suffix="  (approximately)"
    )
    actual = problem6(101, 5, 7)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results, precision=8)

    # Test 10:
    expected = 33.666666666666664  # approximately
    print_expected_result_of_test(
        [100, 1, 1], expected, test_results, format_string, suffix="  (approximately)"
    )
    actual = problem6(100, 1, 1)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results, precision=8)

    # Test 11:
    expected = 34.0
    print_expected_result_of_test(
        [101, 1, 1], expected, test_results, format_string, suffix="  (approximately)"
    )
    actual = problem6(101, 1, 1)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results, precision=8)

    # Test 12:
    expected = 34.333333333333336  # approximately
    print_expected_result_of_test(
        [102, 1, 1], expected, test_results, format_string, suffix="  (approximately)"
    )
    actual = problem6(102, 1, 1)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results, precision=8)

    # Test 13:
    expected = 820.9158391822649  # approximately
    print_expected_result_of_test(
        [1000, 6, 23], expected, test_results, format_string, suffix="  (approximately)"
    )
    actual = problem6(1000, 6, 23)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results, precision=8)

    # Test 14:
    expected = 39.69125934089201  # approximately
    print_expected_result_of_test(
        [999, 600, 25],
        expected,
        test_results,
        format_string,
        suffix="  (approximately)",
    )
    actual = problem6(999, 600, 25)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results, precision=8)

    # Test 15:
    expected = 614.6541445559384  # approximately
    print_expected_result_of_test(
        [2999, 10000, 2001],
        expected,
        test_results,
        format_string,
        suffix="  (approximately)",
    )
    actual = problem6(2999, 10000, 2001)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results, precision=8)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def problem6(r, s, t):
    """
    What comes in:  Positive integers r, s and t.
    What goes out:
      -- Returns the sum of the series
           ((r + 1) / (s + 2))
                +  ((r + 2) / (s + 5))
                +  ((r + 3) / (s + 8)
                +  ((r + 4) / (s + 11))
                +  ...
                +  ((r + t) / ((s - 1) + (3 * t)))
    Side effects:   None.
    Examples:
      -- problem6(3, 1, 4) returns
             (4 / 3)  +  (5 / 6)  +  (6 / 9)  +  (7 / 12),
           which is approximately 3.4166666666666665
    """
    ###########################################################################
    # TODO: 2. DEBUG this function -- our code with ERRORS appears below.
    #          Use the Debugger (or PRINT statements, but the Debugger is easy)
    #          to do the debugging.
    #          Tests have been written for you (above).
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      6
    #    TIME ESTIMATE:   7 to 12 minutes.
    ###########################################################################
    total = 0
    for k in range(t + 1):
        numerator = r + k
        denominator = (s + 2) + (4 * k)
        total = total + (numerator / denominator)
        return total


###############################################################################
# Our tests use the following to print error messages in red.
# Do NOT change it.  You do NOT have to do anything with it.
###############################################################################


def print_expected_result_of_test(
    arguments, expected, test_results, format_string, suffix=""
):
    testing_helper.print_expected_result_of_test(
        arguments, expected, test_results, format_string, suffix
    )


def print_actual_result_of_test(expected, actual, test_results, precision=None):
    testing_helper.print_actual_result_of_test(
        expected, actual, test_results, precision
    )


def print_summary_of_test_results(test_results):
    testing_helper.print_summary_of_test_results(test_results)


# To allow color-coding the output to the console:
USE_COLORING = True  # Change to False to revert to OLD style coloring

testing_helper.USE_COLORING = USE_COLORING
if USE_COLORING:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_colored
else:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_uncolored

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# The   try .. except   prevents error messages on the console from being
# intermingled with ordinary output to the console.
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    try:
        main()
    except Exception:
        print("ERROR - While running this test,", color="red")
        print("your code raised the following exception:", color="red")
        print()
        time.sleep(1)
        raise
