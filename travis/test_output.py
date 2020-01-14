# *****
# Test case template:
# 1. Define test_case object
# 2. Define do_test( test_data, test_case, skip_remaining_tests )
# 3. Call ( test_data, skip_remaining) = library.run_before_test( test_case )
# 4. Perform test
# 5. Calll library.run_after_test( test_case, skip_remaining_tests )

import library

# *****
# 1. Define test_case object
# - Required fields:
# - - name
# - - description
# - - points_possible
# - - points_earned (initialize to zero)
# - - test_ran (initialize to False)
# - - test_passed (initialize to False)
# *****

test_case = {
  'name' : 'Output Test',
  'description' : 'Your program runs and outputs "Hello Georgetown"',
  'points_possible' : 10,
  'points_earned' : 0,
  'test_ran' : False,
  'test_passed' : False,
  'feedback' : '',
}

# *****
# 2. Define do_test
# Inputs:
# - test_case : Defined above; update fields within do_test
# - skip_remaining_tests : Update within do_test
# Outputs:
# - test_case : Updated test case data
# - skip_remaining_tests : Updated skip flag
# *****

def do_test( test_case, skip_remaining_tests ):
  
  # Short-circuit if skipping
  if ( skip_remaining_tests ):
    print('Skipping due to an earlier error...')
    return ( test_case, skip_remaining_tests )
  else:
    test_case['test_ran'] = True
  
  
  from subprocess import Popen, PIPE, STDOUT
  import re
  import tempfile
  
  hello_output = tempfile.NamedTemporaryFile()
  
  test_timeout = False
  print('Running "java Hello"...')
  proc_hello = Popen( ['java', 'Hello'],
                      stdout=hello_output,
                      stderr=STDOUT,
                      text=True )
  
  try:
    proc_hello.wait(timeout=60)
  except TimeoutError:
    proc_hello.kill()
    test_timeout = True
  
  # Timeout failure
  if ( test_timeout ):
    print('Timeout error: your program took longer than 60 seconds to run.')
    test_case['feedback'] = 'Test timed out; took longer than 60 seconds to run'
    skip_remaining_tests = True
  # test returned
  else:
    proc_hello.poll()
    # Run-time error
    if ( proc_hello.returncode != 0 ):
      print('Run-time error: java return code non-zero')
      print('Command-line output:')
      print('-' * 10)
      with open( hello_output.name, 'r') as output:
        for line in output:
          print(line.rstrip())
      print('-' * 10)
      print('Review the java output above to diagnose run-time error')
      
      test_case['feedback'] = 'Run-time error on your program'
      skip_remaining_tests = True
    # Ran successfully; search output
    else:
      # Award points for running program
      test_case['points_earned'] = test_case['points_possible'] // 2
      print('Program ran successfully; command-line output:')
      print( '-' * 10)
      with open( hello_output.name, 'r') as output:
        for line in output:
          print(line.rstrip())
      print ('-' * 10)
      print('Searching output above for "Hello Georgetown"...')
      
      rx = re.compile('hello georgetown', re.I) # case insensitive
      result = False
      with open( hello_output.name, 'r' ) as output:
        for line in output:
          result = result or bool( rx.search(line) )
      # Result is now true if the pattern appears in at least one line
      if ( not result ):
        print('Your program did not print "Hello Georgetown"')
      else:
        print('Your program printed "Hello Georgetown"')
        test_case['points_earned'] = 10
        test_case['test_passed'] = True
    #
  #
    
  return test_case, skip_remaining_tests       

# *****
# 3. Call run_before_test
# *****
( test_data, skip_remaining_tests ) = library.run_before_test( test_case )

# *****
# 4. Perform test
# *****

(test_case, skip_remaining_tests) = do_test( test_case, skip_remaining_tests )

# *****
# 5. Call run_after_test
# *****
library.run_after_test( test_data, test_case, skip_remaining_tests )