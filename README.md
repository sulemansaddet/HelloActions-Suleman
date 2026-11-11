# HelloActions-Suleman

## Part 5: Workflow Explanation

1. **What is the purpose of the `on` section?**
   The `on` section defines the triggers/events that determine when the workflow should execute (e.g., code pushes, pull requests, or manual triggers).

2. **What does `workflow_dispatch` do?**
   It enables manual execution of the workflow directly from the GitHub Actions tab interface.

3. **What does `runs-on` specify?**
   It specifies the type of virtual machine environment/runner (e.g., `ubuntu-latest`) provided by GitHub to execute the job.

4. **Why is `actions/checkout` needed?**
   It clones the repository files onto the GitHub runner virtual machine so that subsequent steps can access and execute the source code.

5. **What does the language setup action do?**
   It installs and configures the specified language runtime environment (and version) on the runner so the program can be compiled or executed.

6. **What is the difference between compiling and running the program?**
   Compiling translates source code into machine code/executable bytecode (necessary for compiled languages like Java or C++), whereas running executes the binary or script to perform its operations.

7. **Where can you see the program output?**
   Inside the GitHub Actions tab, under the specific workflow run and expanded job execution step logs.

8. **What is the difference between a workflow, a job, and a step?**
   - **Workflow:** The top-level automated process defined in a `.yml` file.
   - **Job:** A set of steps that execute sequentially on the same runner machine.
   - **Step:** An individual task or command run within a job.
