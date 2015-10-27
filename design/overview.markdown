# Overall design hlnet #

hlnet will be centered around a test runner and three primary objects:

* **Environment**; which describes and specific numerical environment
* **Test**; which describes a single specific test
* **Test cases**; which describes how tests are executed in a specific environment

All tests are executed on a single core and each test should return 2 results,
for running the test once per environment startup and 100 times per environment
startup, to allow for adequate illuminations of the effects of jit
compilers. Besides that the tests should have switches for 32 and 64 bit floats.

## Environment ##

The environment should describe the following:

* The **path to the executable** that the test should be executed in or None for a
  compiled environment. The path should be detected and should have code paths
  for different operating systems
* **Compiler information** for a compiled environment


## Test ##

A test should contain:

* A **text description** of what is being tested
* Instances of **test cases** which describes how this test is executed in a
  specific environment
