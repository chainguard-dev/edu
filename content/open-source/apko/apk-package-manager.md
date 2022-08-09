---
title: "Why apk"
type: "article"
lead: "How apk-tools is different from other package managers"
date: 2022-07-06T08:49:31+00:00
lastmod: 2022-07-06T08:49:31+00:00
contributors: ["Ariadne Conill"]
draft: false
images: []
menu:
  docs:
    parent: "apko"
weight: 640
toc: true
---

[apko](/open-source/apko/getting-started-with-apko/) uses the [apk](https://wiki.alpinelinux.org/wiki/Package_management) package manager to compose container images based on declarative pipelines.
The apk format was introduced by [Alpine Linux](https://www.alpinelinux.org/) to address specific design requirements that could not be met by existing package managers such as `apt` and `dnf`. But what makes it different, and why does that matter in the context of apko?

## Manipulating the Desired State

In traditional package managers like `dnf` and `apt`, requesting the installation or removal of packages causes those packages to be directly installed or removed, after a consistency check.

In `apk`, when you run `apk add package1` to add a package or `apk del package2` to delete a package, `package1` and `package2` are added (or removed) as a dependency constraint in `/etc/apk/world`, which describes the desired system state. Package installation or removal is done as a side effect of modifying this system state. It is also possible to edit `/etc/apk/world` with the text editor of your choice and then use `apk fix` to synchronize the installed packages with the desired system state.

Because of this design, you can also add conflicts to the desired system state to prevent bringing in certain packages. For example, there was [a bug in Alpine in 2021](https://gitlab.alpinelinux.org/alpine/apk-tools/-/issues/10742) where `pipewire-pulse` was preferred over `pulseaudio` because the former had a simpler dependency graph. This did not prove to be a problem though, as users could add a conflict against `pipewire-pulse` by running `apk add !pipewire-pulse`, thus preventing the package from being brought in.

Another result of this design is that `apk` will never commit a change to the system that leaves it unbootable. If it cannot verify the correctness of the requested change, it will back out adding the constraint before attempting to change what packages are actually installed on the system. This allows the apk dependency solver to be rigid: there is no way to override or defeat the solver other than providing a scenario that results in a valid solution.

## Verification and Unpacking in Parallel to Package Fetching

Unlike other package managers, `apk` is completely driven by the package fetching I/O when installing or upgrading packages. When the package data is fetched, it is verified and unpacked on the fly. This allows package installations and upgrades to be extremely fast.

To make this safe, package contents are initially unpacked to temporary files and then atomically renamed once the verification steps are complete and the package is ready to be committed to disk.

## Constrained Solver

Lately, traditional package managers have promoted their advanced [SAT solvers](https://en.wikipedia.org/wiki/SAT_solver) for resolving complicated constraint issues automatically. For example, [aptitude is capable of solving Sudoku puzzles](https://web.archive.org/web/20080823224640/http://algebraicthunk.net/~dburrows/blog/entry/package-management-sudoku/). `apk`'s lack of these solvers can actually be considered a feature.

While it is true that `apk` does have a deductive dependency solver, it does not perform backtracking. The solver is also constrained: it is not allowed to make changes to the `/etc/apk/world` file. This ensures that the solver cannot propose a solution that will leave your system in an inconsistent state.

Trying to make a smart solver instead of appropriately constraining the problem can indicate a poor design choice. The fact that `apt`, `aptitude`, and `dnf` have all written code to constrain their SAT solvers in various ways proves this point.

## Fast and Safe Package Management

Package managers can be made to go fast — and can be safe while doing so — but require a careful design that is well-constrained. `apk` makes its own tradeoffs: a less powerful but easy to audit solver, trickier parallel execution instead of phase-based execution. These were the right decisions for `apk`, but may not be the right decisions for other distributions.

## Final Considerations

The reproducible nature of apk makes it the ideal solution for declarative pipelines, since it allows you to describe your desired system state without having to implement a series of individual steps that are not guaranteed to reach completion. When the apk dependency solver is unable to reach an installable set of packages, the build fails, without causing incomplete system changes.
This is the ideal behavior for automated pipelines since it eliminates the need for rollbacks, in addition to avoiding the risks of inconsistent environments.

_An earlier version of this article was published on [Ariadne Conill's Blog](https://ariadne.space/2021/04/25/why-apk-tools-is-different-than-other-package-managers/)._
