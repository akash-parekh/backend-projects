# 📦 GitHub User Activity CLI

A simple TypeScript-based command-line tool that fetches and displays recent GitHub user activity using the public GitHub Events API.

This project is built as part of the **roadmap.sh GitHub User Activity** [challenge](https://roadmap.sh/projects/github-user-activity).

---

## 🚀 Features

-   Fetches recent GitHub events for any username
-   Parses GitHub event types into clean, readable messages
-   Uses **built-in Node.js fetch** (no external HTTP libraries)
-   Supports major event types:

    -   PushEvent
    -   WatchEvent
    -   IssuesEvent
    -   PullRequestEvent
    -   ForkEvent
    -   CreateEvent
    -   DeleteEvent

---

## 🗂️ Project Structure

```
src/
  index.ts     → CLI entry point
  api.ts       → Fetch GitHub events
  parser.ts    → Convert raw events to readable output

dist/          → Compiled JavaScript output
```

---

## 📥 Installation

Clone the repository:

```
git clone <your-repo-url>
cd github-activity-cli
```

Install dependencies:

```
npm install
```

Build the project:

```
npm run build
```

---

## ▶️ Usage

Run the CLI:

```
node dist/index.js <github-username>
```

Example:

```
node dist/index.js octocat
```

Or run with ts-node during development:

```
npx ts-node src/index.ts <github-username>
```

---

## 🛠️ Technologies Used

-   **TypeScript**
-   **Node.js**
-   `fetch()` (built-in to Node 18+)
-   No external HTTP libraries (as required by the challenge)

---

## 📡 API Used

This project uses the public GitHub Events API:

```
https://api.github.com/users/<username>/events
```

---

## 📄 License

This project is open-source and available under the MIT License.

---
