---
name: container-test
description: Use to run a project's tests inside a container (Podman or Docker) to reproduce the runtime environment — before opening a PR, or when failures look environment-specific.
---

# Container Test

Running tests in a container reproduces the exact runtime (OS, language version, dependencies) and catches problems that don't appear on a developer machine. Prefer it as the final verification path.

## When to use

- Before opening a pull request.
- Debugging environment-specific failures (missing packages, architecture differences, graphics/headless issues).
- Verifying dependency files and the `Containerfile`/`Dockerfile` are correct.

## Prerequisites

- Podman (preferred) or Docker installed and reachable (`podman info` / `docker info`).
- A `Containerfile` or `Dockerfile` that builds.
- Test dependencies declared in the project's dependency file (e.g. `requirements.txt`).

## Workflow

1. **Discover the project's commands.** Check the `Makefile` (`make -qp | grep -E '^test|^build'` or read it), README, and CI config. Prefer existing targets such as `make build` and `make test-container`.
2. **Build the image**: `make build`, or `podman build -t <name> -f Containerfile .` (swap `docker` as needed).
3. **Run tests in the container**: `make test-container`. If no target exists, mount the source and run the project's test command, e.g. `podman run --rm -v "$PWD":/app:Z -w /app <name> pytest --cov --cov-report=term-missing`.
4. **Report** the exit status and any failures verbatim. A non-zero exit means tests failed.

Local runs (`make test`, `pytest`) are fine for fast iteration but do not replace the container run before a PR.

## Coverage

Aim for high coverage (around 80%+) on domain code, and don't reduce overall coverage with new code. Prefer behavior-driven tests over coverage-only tests.

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Image build fails | Check apt/pip steps in the Containerfile and that dependency files are valid. |
| `pytest` not found | Add it to the dependency file and rebuild the image. |
| Import errors | Ensure source is copied or mounted into the container and `PYTHONPATH`/working dir are correct. |
| Headless graphics errors | Containers have no display; use software rendering (e.g. `PYOPENGL_PLATFORM=osmesa`) or skip display-dependent tests. |
| Coverage file write error | Make sure the output path is writable by the container user (on SELinux, use the `:Z` mount flag). |
| Daemon unreachable | Start Docker, or use Podman rootless. |
