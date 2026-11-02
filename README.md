# Quasynvo · organization home & community defaults

**Intelligence, in your orbit.**

This public `.github` repository provides the [Quasynvo organization profile](profile/README.md)
and shared community-health documents. The actual assistant lives in
[Quasynvo/Quasnooze](https://github.com/Quasynvo/Quasnooze).

## What is here?

- [`profile/README.md`](profile/README.md): the homepage shown at https://github.com/Quasynvo.
- [`profile/banner.gif`](profile/banner.gif): decorative organization banner using the approved orbital-Q logo.
- [`profile/banner.png`](profile/banner.png): static alternative.
- [`CONTRIBUTING.md`](CONTRIBUTING.md), [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md),
  [`SECURITY.md`](SECURITY.md) and issue/PR templates: existing community defaults,
  with current branding and links. Repositories can override eligible default files.

This update changes presentation and stale links, not review requirements, policy
clauses, collaborators, protections, private reporting settings or licensing.
Existing license/copyright provenance is preserved.

## Optional artwork rebuild

On a Linux development machine with Python 3, Pillow and DejaVu Sans:

```sh
python3 scripts/build-profile-art.py
```

The selected logo is reused, not redesigned. The GIF only animates decorative orbit
markers; it is not product telemetry. GitHub Markdown does not run JavaScript or
custom reduced-motion CSS, so the profile includes a direct static alternative.

The organization profile becomes current after normal PR review and merge into
this repository's default branch. No npm or product deployment is required.

## Local validation

```sh
python3 scripts/check-profile.py
```

Six checks cover current branding/links, local Markdown targets, a small animated
banner, static fallback/SVG parsing and explicit product capability boundaries.
They require Pillow but no network or credentials. The rendered offline preview
was also checked at 320, 390, 768 and 1440px; this is not a claim that GitHub itself
was browser-tested or that the profile has already been merged.

The former contributor-queue link was broken in this repository; it now points to
the actual Quasnooze queue guide. Stale Growth wording is aligned with that guide.
No policy enforcement clauses are changed. The obsolete non-address contact
placeholder is removed, retaining the existing private-maintainer/advisory routes
without inventing a Quasynvo email address.
