# Programming Assignment 1: Hello Georgetown
## COSC 150 - Advanced Programming

- [Goals](#goals)
- [Description](#description)
- [Specification and requirements](#specification-and-requirements)
- [Grading rubric](#grading-rubric)

## Goals

In order to complete this assignment, you will need to:
- Create a working Java program on your computer
   - Install a Java 11 JDK (e.g., openjdk11)
   - Create and edit a .java source file (in a text editor or IDE)
   - Compile and run this program locally for testing
- Submit your program using the GitHub Classroom workflow
   - Install and configure git on your computer
   - Accept a GitHub Classroom assignment
   - Clone the resulting repository locally
   - Commit your source code to the local repository
   - Push to GitHub to trigger a Travis CI build

## Description

> The only way to learn a new programming language is by writing programs in it.
 The first program to write is the same for all languages: 
 Print the words `hello world`. 
 This is the big hurdle; 
 to leap over it you have to be able to create the program text somewhere, compile it successfully, load it, run it, and find out where your output went. 
 With these mechanical details mastered, everything else is comparatively easy.
- Brian Kernighan and Denis Ritchie, "The C Programming Language"

This assignment is designed to address the "toolchain" portion of Java programming:
- Creating, compiling, and running Java programs
- Working with GitHub Classroom and pushing commits to your repository

To accomplish this, we will write a variant of the "Hello world" program in Java.


*Note: The tools we use here (IDEs, git/GitHub, TravisCI) are specifically chosen because they are also used in large-scale commercial and FOSS development.

## Specification and requirements

To complete the assignment, you will need to accomplish the following tasks:

1. Write "Hello Georgetown" in Java

   You will write a simple "Hello world"-style program using Java. 
   Your work will consist of a single class, called `Hello` (implemented in the corresponding source code file `Hello.java`).
   This class should contain a single method (`main`) which prints the string `Hello Georgetown` to the console.
   
   *Note: This is a very short program (you may even find it verbatim in my lecture slides!). The goal is not to test your code-writing, but to verify that you know where your source code is created and saved, how to open, edit, compile, and run it.

2. Submit your program by pushing a commit to GitHub

   Once your program is ready to submit, you will need to submit it for grading.
   You will do this by
   1. Accepting the assignment from GitHub Classroom to create your personal repository for the assignment.
   2. Cloning the repository to your computer to work locally.
   3. Adding `Hello.java` to repository tracking, and creating a commit with the code included.
   4. Pushing your commits to GitHub and triggering a Travis CI build.

   If both of these steps are completed successfully, Travis will run our testing script using your latest commit as a code base.
   Upon completion, you will be able to see the test results in Travis' output.
   
   A build status of "Passed" indicates that every automated test has passed. 
   A build status of "Failed" indicates that one or more tests were unsuccessful.
   *This does not mean that you have earned zero points!*
   Instead, consult the Travis output to see which test have failed.

### Provided files

Upon accepting the assignment from GitHub Classroom, you will find your repository already contains several files:
- `README.md` which provides the assignment specification (you are reading this now!)
- `.gitignore` which specifies files git should NOT add to tracking (in particular, `*.class` files are not tracked as they can be compiled from source).
- `.travis.yml` which contains instructions for Travis to use while testing your code
- `travis` which contains test scripts for travis to use while testing.

You should not edit *any* of these files while working on your project; 
doing so may break Travis such that a test build does not run, or gives false/misleading feedback about the test cases your code passes.

## Grading rubric

Your score for this assignment is determined according to the following rubric.

*Note: The tests provided by TravisCI on this assignment are comprehensive; i.e., a passing build will receive full marks. On future assignments, there may be additional test cases and/or manual code reviews.*

Amazing Feat | Points Awarded | Tested by TravisCI?
---          | :---:          | ---:
You commit a file named `Hello.java` to your repository | 10 | Yes
The `Hello.java` in your repository compiles            | 10 | Yes
Your program runs and outputs "Hello Georgetown"        | 10 | Yes
**Total points**                                        | 30 |
