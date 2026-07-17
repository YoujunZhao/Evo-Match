# Evo-Match GitHub Publication Design

## Goal

Publish the existing football forecasting skill as a clean, standalone GitHub repository named `Evo-Match` without changing its forecasting behavior.

## Repository Shape

The skill files live at the repository root so OpenClaw can install the Git repository directly. Generated Python caches and local forecast ledgers are excluded. MIT-0 matches the ClawHub publication license.

## Documentation

The repository uses separate English and Simplified Chinese README files with a language switcher. The presentation follows the information hierarchy of Vibe-Trading without copying its text or assets: centered project identity, concise value proposition, badges, section navigation, capability table, workflow diagram, installation, examples, safety, development, and license.

## Installation

The primary GitHub path is `openclaw skills install git:YoujunZhao/Evo-Match@main --global`. The README also documents the owner-qualified ClawHub path for the existing canonical skill slug.

## Verification

Local verification runs the complete standard-library unittest suite and an example multi-book forecast. GitHub Actions repeats these checks on Python 3.10 and 3.12.

## Security

No GitHub or ClawHub credentials are stored in the repository, command examples, commit messages, or generated files.
