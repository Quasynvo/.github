# Quasynvo · organization home & community defaults

**Intelligence, in your orbit.**

This public `.github` repository provides the [Quasynvo organization profile](profile/README.md)
and shared community-health documents. The actual assistant lives in
[Quasynvo/Quasnooze](https://github.com/Quasynvo/Quasnooze).

## What is here?

- [`profile/README.md`](profile/README.md): the homepage shown at https://github.com/Quasynvo.
- [`profile/banner.png`](profile/banner.png): static-first organization banner using the approved orbital-Q logo.
- [`profile/banner.gif`](profile/banner.gif): optional decorative animated alternative.
- [`profile/orbit-background.jpg`](profile/orbit-background.jpg): AI-generated nebula backdrop used to build both banners.
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

The approved logo is reused, not redesigned; the nebula backdrop is AI-generated.
The GIF only animates decorative orbit markers; it is not product telemetry.
GitHub Markdown does not run JavaScript or custom reduced-motion CSS, so the
profile displays the static banner by default and links the animation separately.

The organization profile becomes current after normal PR review and merge into
this repository's default branch. No npm or product deployment is required.

## Local validation

```sh
python3 scripts/check-profile.py
```

The checks cover branding, links, local Markdown targets, the optional animated
banner, static-first rendering, SVG parsing and explicit product capability
boundaries. They require Pillow but no network or credentials. GitHub may render
the profile differently from a local preview; the live page changes only after
this branch is reviewed and merged.

The former contributor-queue link was broken in this repository; it now points to
the actual Quasnooze queue guide. Stale Growth wording is aligned with that guide.
No policy enforcement clauses are changed. The obsolete non-address contact
placeholder is removed, retaining the existing private-maintainer/advisory routes
without inventing a Quasynvo email address.
