# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with this repository.

## Repository Overview

**Name:** claude-test
**Purpose:** Test repository for Claude Code — used to evaluate and demonstrate Claude Code workflows, conventions, and capabilities.
**Owner:** mim1400

This is a minimal starter repository. Its primary role is to serve as a sandbox for experimenting with Claude Code features, establishing conventions, and validating AI-assisted development workflows.

## Repository Structure

```
claude-test/
├── README.md       # Project overview
└── CLAUDE.md       # This file — guidance for Claude Code
```

As the project grows, this structure should be updated to reflect new directories and files.

## Git Workflow

### Branches

- `main` — stable, production-ready code
- `claude/<description>-<session-id>` — feature branches created by Claude Code for individual tasks

### Branch Naming Convention

Claude Code branches follow this pattern:

```
claude/<short-task-description>-<session-id>
```

Example: `claude/claude-md-mm1202zyr8n1pe18-JcNLl`

### Development Flow

1. Always develop on the designated feature branch (never push directly to `main`)
2. Make focused, atomic commits with descriptive messages
3. Push to the feature branch when work is complete
4. Open a pull request to merge into `main`

### Git Push

Always push with upstream tracking:

```bash
git push -u origin <branch-name>
```

If a push fails due to network errors, retry up to 4 times with exponential backoff (2s, 4s, 8s, 16s).

### Commit Messages

Write clear, imperative commit messages describing *what* changed and *why*:

```
Add user authentication module

Implements JWT-based login and session management to support
multi-user access to the dashboard.
```

- First line: 50 chars or less, imperative mood ("Add", "Fix", "Update", not "Added")
- Blank line separator if a body is needed
- Body: explain motivation and context, not implementation details

## Development Conventions

### General Principles

- Prefer editing existing files over creating new ones
- Keep changes minimal and focused on the task at hand
- Do not add features, refactors, or "improvements" beyond what is explicitly requested
- Avoid over-engineering: build the minimum needed for the current requirement
- Delete unused code rather than commenting it out or adding backwards-compatibility shims

### Code Style

Until a language-specific stack is established in this repo, follow these defaults:

- Use consistent indentation (spaces preferred; match the existing file's style)
- Keep functions small and single-purpose
- Name variables and functions clearly — prefer readability over brevity
- Avoid abbreviations in identifiers unless they are universally understood (e.g., `id`, `url`)

### File Organization

- Group related files in directories by feature or concern, not by file type
- Keep the root directory clean; only config files and entry points belong there

### Security

- Never commit secrets, credentials, API keys, or tokens
- Do not introduce command injection, XSS, SQL injection, or other OWASP Top 10 vulnerabilities
- Validate input at system boundaries (user input, external APIs); trust internal code

## Testing

No test framework has been configured yet. When tests are added:

- Document the test command here (e.g., `npm test`, `pytest`, `go test ./...`)
- All tests must pass before merging to `main`
- New features should include corresponding tests

## Linting and Formatting

No linter or formatter is configured yet. When tooling is added:

- Document the lint/format commands here
- Run linting before committing
- Do not suppress linter warnings without justification

## Working with Claude Code

### What Claude Code Should Do

- Read and understand existing files before proposing changes
- Use the TodoWrite tool to plan and track multi-step tasks
- Prefer parallel tool calls where operations are independent
- Mark tasks complete immediately after finishing them — do not batch completions
- Ask for clarification when requirements are ambiguous before writing code

### What Claude Code Should Avoid

- Pushing to `main` or any branch other than the designated feature branch
- Creating files that are not necessary to complete the task
- Adding documentation (README, markdown files) unless explicitly requested
- Making assumptions about unstated requirements without asking

### Branch Discipline

Claude Code must only push to branches matching the pattern `claude/<...>`. Pushing to `main` directly will fail and is not permitted.

## Adding to This File

As the repository grows, update this file to reflect:

- New directories and their purpose
- The tech stack (language, frameworks, libraries)
- Build and run commands
- Test and lint commands
- Environment variable requirements
- Deployment process
- Any project-specific conventions that differ from the defaults above
