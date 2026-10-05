# CSPC - Computer Science for Physics and Chemistry
My coursework repository. Each practical is under PW<n>/Lab <X>/.

## Setup
Create the environment for a given lab:

    conda env create -f PW<n>/Lab\ <X>/environment.yml
    conda activate cspc

---

## PW1 - Lab A: Reproducible Foundations

**What I built:**
- Repository CSPC with Git and GitHub, a conda environment, a radioactive decay simulation, pytest tests and a speed comparison.

**Speed comparison (loop vs NumPy):**
- loop : 2.9477 s
- numpy : 0.000395 s
- speed-up: 7460 x faster

**Tests:** all passing? yes

**Conclusion:**
- In this lab I built my CSPC repository, set up a conda environment, wrote tests with pytest and pushed everything to GitHub. The NumPy simulation was about 7460 times faster than the pure-Python loop (0.000395 s vs 2.9477 s).
- The hardest part was the first push: it failed because I had accidentally committed the 188 MB Miniconda installer (GitHub's limit is 100 MB), and my remote URL was also wrong. I removed the file from the history and fixed the URL.
- I learned that GitHub needs a personal access token instead of a password, that .gitignore and `git status` should be checked before `git add .`, and that vectorised code is much faster than loops.


Branch and merge practised in Lab A.


## PW1 --- Lab B: Data, Plotting, and Automation

**Data comparison:**
The observed decay data from `decay_observed.csv` matches the analytical exponential decay law: N(t) = N0 * e^(-0.3 * t).

**Automation with Snakemake:**
The Snakemake rule automates generating `figure.png` from `decay_observed.csv` using `plot.py`.



## PW2 --- Lab A: Motion from Tracking Data

**Results:**
- **Mean acceleration:** -8.58 m/s² (shows the object is falling under gravity).
- **Standard deviation:** 28.72 m/s² (shows the acceleration jumps around a lot).
- **Why acceleration is noisy:** Finding derivatives compares nearby points, which makes tiny errors in position look huge in acceleration.
- **Integration recovery:** Integrating adds values together, which cancels out random errors. It restored the position with less than 0.8 m difference.