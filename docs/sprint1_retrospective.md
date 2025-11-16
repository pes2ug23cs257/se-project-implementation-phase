## Sprint 1 Retrospective: Core Implementation

* **Sprint Goal:** To build the core, end-to-end functionality of the application. This included setting up the Flask backend, creating the frontend upload UI, and ensuring they could successfully communicate (upload image, receive mock prediction).
* **Final Status:** Completed.

### ✅ What Went Well?

* **Successful Integration:** We successfully connected the JavaScript `fetch` API on the frontend to the Flask `/predict` endpoint on the backend.
* **Problem-Solving:** We worked through and solved several critical, time-consuming bugs, including:
    * Fixing the `CORS` (Cross-Origin Resource Sharing) policy errors.
    * Correctly serving the frontend over HTTP (using `python -m http.server`) to allow `fetch` requests.
    * Resolving Git merge conflicts (`app.py`) and fixing broken `main` branches.
* **Project Setup:** We successfully set up the full project structure in Git, managed tasks in Jira, and practiced a PR-based workflow.

### ❌ What Didn't Go Well?

* **Wasted Time on Bugs:** We spent a significant amount of time (Days 2-4) debugging connection and Git issues instead of building features.
* **Git Workflow:** We accidentally merged failing PRs or pushed directly to `main`, which broke the pipeline for everyone else and required "hotfixes."
* **Initial CI Pipeline:** The CI pipeline in Sprint 1 was just a "stub" or placeholder. It didn't run any real tests or quality checks, which meant we didn't catch errors until late.

### 🚀 Action Items (Carried into Sprint 2)

1.  **Never Merge a Red Build (❌):** Establish a firm rule to **never** merge a Pull Request if the CI pipeline is failing.
2.  **Pull Before You Push:** All team members must run `git pull origin main` on their feature branch *before* pushing to get the latest fixes and avoid breaking the build.
3.  **Run Tests Locally:** Run `pytest` locally to catch errors *before* pushing to GitHub.
